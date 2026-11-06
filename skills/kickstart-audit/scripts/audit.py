#!/usr/bin/env python3
"""kickstart audit: measure a repository's production readiness and report numbers.

Usage:
    python3 audit.py --repo . --out .kickstart/audit [--json-only] [--quiet]

Writes <out>/latest.json, <out>/latest.md, <out>/history.jsonl and a dated copy.
Standard library only. Runs external scanners when present, skips them when not.
Exit code is always 0; the score is the signal.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

VERSION = "0.1.1"

EXCLUDED_DIRS = {
    ".git", "node_modules", "vendor", "dist", "build", "out", ".next", ".nuxt", ".svelte-kit",
    ".venv", "venv", "env", "__pycache__", ".mypy_cache", ".pytest_cache", ".ruff_cache",
    "target", "bin", "obj", ".gradle", ".idea", ".vscode", "coverage", ".turbo", ".cache",
    "Pods", ".dart_tool", "_build", "deps", ".terraform", ".kickstart",
    # Agent skill/config folders: installed third-party skills, not the project's code.
    ".agents", ".claude", ".cursor", ".codex", ".windsurf", ".cline", ".gemini", ".opencode",
    ".amp", ".kilocode", ".roo", ".zed", ".warp", ".continue", ".aider",
}

LANG_EXT = {
    ".ts": "TypeScript", ".tsx": "TypeScript", ".js": "JavaScript", ".jsx": "JavaScript", ".mjs": "JavaScript",
    ".cjs": "JavaScript", ".py": "Python", ".go": "Go", ".rs": "Rust", ".rb": "Ruby", ".php": "PHP",
    ".java": "Java", ".kt": "Kotlin", ".cs": "C#", ".swift": "Swift", ".dart": "Dart", ".ex": "Elixir",
    ".exs": "Elixir", ".scala": "Scala", ".vue": "Vue", ".svelte": "Svelte", ".c": "C", ".cpp": "C++",
    ".h": "C/C++", ".sql": "SQL", ".sh": "Shell", ".tf": "Terraform", ".yml": "YAML", ".yaml": "YAML",
}

MANIFESTS = {
    "package.json": "npm", "pnpm-lock.yaml": "npm", "yarn.lock": "npm", "package-lock.json": "npm", "bun.lockb": "npm",
    "pyproject.toml": "python", "requirements.txt": "python", "Pipfile": "python", "setup.py": "python", "uv.lock": "python",
    "poetry.lock": "python",
    "go.mod": "go", "Cargo.toml": "rust", "Gemfile": "ruby", "composer.json": "php",
    "pom.xml": "java", "build.gradle": "java", "build.gradle.kts": "java",
    "pubspec.yaml": "dart", "mix.exs": "elixir",
}

LOCKFILES = [
    "package-lock.json", "pnpm-lock.yaml", "yarn.lock", "bun.lockb", "poetry.lock", "uv.lock", "Pipfile.lock",
    "go.sum", "Cargo.lock", "Gemfile.lock", "composer.lock", "packages.lock.json", "pubspec.lock", "mix.lock",
    "gradle.lockfile",
]

SECRET_FILE_NAMES = re.compile(r"^(\.env(\..*)?|.*\.(pem|key|p12|pfx|jks|keystore)|id_rsa.*|id_ed25519.*|credentials\.json|service-account.*\.json)$")
SECRET_FILE_ALLOW = {".env.example", ".env.sample", ".env.template", ".env.test.example"}

# (name, regex, severity, note)
UNSAFE_PATTERNS = [
    ("string-built SQL", re.compile(r"""(execute|query|raw|exec)\s*\(\s*(f["']|["'].*%s|["'].*\+\s*\w|`[^`]*\$\{)""", re.I), "high", "Use parameterised queries"),
    ("eval()", re.compile(r"\beval\s*\("), "high", "Avoid eval on any input"),
    ("pickle.load", re.compile(r"\bpickle\.loads?\s*\("), "high", "Unsafe deserialisation"),
    ("yaml.load without Loader", re.compile(r"\byaml\.load\s*\([^)]*\)(?![^\n]*Loader)"), "medium", "Use yaml.safe_load"),
    ("shell=True", re.compile(r"shell\s*=\s*True"), "medium", "Avoid shell=True with variables"),
    ("child_process exec with template", re.compile(r"\bexec(Sync)?\s*\(\s*`[^`]*\$\{"), "high", "Use execFile with args"),
    ("dangerouslySetInnerHTML", re.compile(r"dangerouslySetInnerHTML"), "medium", "Sanitise or avoid"),
    ("innerHTML assignment", re.compile(r"\.innerHTML\s*="), "medium", "Use textContent or sanitise"),
    ("MD5/SHA1 for password", re.compile(r"(md5|sha1)\s*\([^)]*pass", re.I), "high", "Use bcrypt/argon2"),
    ("CORS wildcard", re.compile(r"""(Access-Control-Allow-Origin["']?\s*[:=,]\s*["']\*|origin:\s*["']\*["']|cors\(\s*\))"""), "medium", "Allow-list origins"),
    ("URL with credentials", re.compile(r"[a-z]+://[^/\s:@]+:[^/\s@]+@[^\s]+", re.I), "high", "Credentials embedded in URL"),
    ("debug true", re.compile(r"^\s*DEBUG\s*=\s*True\s*$", re.M), "medium", "Wire DEBUG to environment"),
]

SECRET_VALUE_PATTERNS = [
    ("AWS access key", re.compile(r"\b(AKIA|ASIA)[0-9A-Z]{16}\b")),
    ("GitHub token", re.compile(r"\b(ghp_[A-Za-z0-9]{36}|github_pat_[A-Za-z0-9_]{22,})\b")),
    ("Slack token", re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{10,}\b")),
    ("OpenAI/Stripe-style key", re.compile(r"\b(sk-[A-Za-z0-9_-]{20,}|sk_live_[A-Za-z0-9]{20,}|rk_live_[A-Za-z0-9]{20,})\b")),
    ("Razorpay live key", re.compile(r"\brzp_live_[A-Za-z0-9]{10,}\b")),
    ("Google API key", re.compile(r"\bAIza[0-9A-Za-z_-]{35}\b")),
    ("Private key block", re.compile(r"-----BEGIN (RSA |EC |OPENSSH |DSA |PGP )?PRIVATE KEY-----")),
    ("Generic assigned secret", re.compile(r"""(?i)\b(password|passwd|secret|api[_-]?key|access[_-]?token|auth[_-]?token)\b\s*[:=]\s*["'][^"'\s]{12,}["']""")),
]

HEADER_HINTS = re.compile(r"(helmet|secureHeaders|secure_headers|SecurityMiddleware|Strict-Transport-Security|Content-Security-Policy|django-csp|NetEscapades|tower_http::set_header|unrolled/secure|X-Frame-Options|frame-ancestors)", re.I)
RATE_LIMIT_HINTS = re.compile(r"(ratelimit|rate_limit|rate-limit|throttle|Throttler|rack-attack|slowapi|bucket4j|express-rate-limit|@upstash/ratelimit|limiter)", re.I)
VALIDATION_HINTS = re.compile(r"(\bzod\b|\byup\b|\bjoi\b|pydantic|class-validator|FormRequest|validates|go-playground/validator|FluentValidation|jakarta\.validation|@Valid\b|valibot|ajv)", re.I)
LOGGING_HINTS = re.compile(r"(\bpino\b|winston|structlog|python-json-logger|lograge|log/slog|serilog|logback|zerolog|zap\.New|tracing_subscriber|bunyan)", re.I)
ERROR_TRACKING_HINTS = re.compile(r"(sentry|bugsnag|rollbar|honeybadger|datadog|new_relic|newrelic|appsignal)", re.I)
HEALTH_HINTS = re.compile(r"""(["'/](health|healthz|readyz|livez|_health|actuator/health)["'/]?)""", re.I)
MIGRATION_HINTS = ["migrations", "migrate", "alembic", "prisma/migrations", "db/migrate", "drizzle", "flyway", "liquibase", "goose", "Migrations"]
AUTH_HINTS = re.compile(r"(next-auth|@auth/|@clerk/|supabase.*auth|passport|django\.contrib\.auth|allauth|devise|has_secure_password|spring-boot-starter-security|Microsoft\.AspNetCore\.Identity|lucia|authlib|fastapi-users|go-oidc|jsonwebtoken|jose)", re.I)
TEST_FILE = re.compile(r"(^|/)(tests?|__tests__|spec|e2e|specs)(/|$)|(\.|_)(test|spec)\.[a-z]+$|_test\.go$|Tests?\.(cs|java|kt)$|test_.*\.py$|.*_spec\.rb$")
SECURITY_TEST_HINTS = re.compile(r"(401|403|unauthori[sz]ed|forbidden|rate.?limit|too many requests|429|csp|strict-transport|x-content-type|cannot access|other user|another user)", re.I)
CI_PATHS = [".github/workflows", ".gitlab-ci.yml", ".circleci/config.yml", "bitbucket-pipelines.yml", "azure-pipelines.yml", "Jenkinsfile", ".buildkite", ".drone.yml", ".woodpecker.yml"]
DEPLOY_FILES = ["Dockerfile", "docker-compose.yml", "compose.yml", "fly.toml", "vercel.json", "netlify.toml", "railway.json", "railway.toml", "render.yaml", "app.yaml", "serverless.yml", "wrangler.toml", "wrangler.jsonc", "Procfile", "config/deploy.yml", "k8s", "kubernetes", "helm", "terraform", "infra", "cdk.json", "Pulumi.yaml"]
DOC_FILES = {
    "readme": ["README.md", "README.rst", "README.txt", "README", "readme.md"],
    "license": ["LICENSE", "LICENSE.md", "LICENSE.txt", "COPYING"],
    "changelog": ["CHANGELOG.md", "CHANGES.md", "HISTORY.md"],
    "contributing": ["CONTRIBUTING.md"],
    "security_policy": ["SECURITY.md", ".github/SECURITY.md"],
    "env_example": [".env.example", ".env.sample", ".env.template"],
    "architecture": ["docs/architecture.md", "ARCHITECTURE.md", "docs/ARCHITECTURE.md"],
    "runbook": ["docs/runbook.md", "RUNBOOK.md", "docs/operations.md"],
    "privacy": ["PRIVACY.md", "docs/privacy.md"],
}
LINT_CONFIGS = [".eslintrc", ".eslintrc.js", ".eslintrc.cjs", ".eslintrc.json", "eslint.config.js", "eslint.config.mjs", "eslint.config.ts", "biome.json", "biome.jsonc", ".prettierrc", "ruff.toml", ".ruff.toml", "setup.cfg", "tox.ini", ".flake8", "mypy.ini", ".golangci.yml", ".golangci.yaml", "rustfmt.toml", "clippy.toml", ".rubocop.yml", "phpstan.neon", ".php-cs-fixer.php", "pint.json", ".editorconfig", "analysis_options.yaml", ".swiftlint.yml", "detekt.yml", "checkstyle.xml"]
DEP_AUTOMATION = [".github/dependabot.yml", ".github/dependabot.yaml", "renovate.json", "renovate.json5", ".renovaterc", ".renovaterc.json", ".github/renovate.json"]
PII_HINTS = re.compile(r"\b(email|phone|date_of_birth|dob|ssn|aadhaar|pan_number|passport|address|national_id)\b", re.I)
DELETION_HINTS = re.compile(r"(delete[_-]?account|deleteAccount|erase|gdpr|dpdp|right.?to.?be.?forgotten|data[_-]?deletion|anonymi[sz]e)", re.I)

WEIGHTS = {"security": 25, "dependencies": 20, "tests": 15, "ci": 15, "docs": 10, "operability": 10, "compliance": 5}


def run(cmd: list[str], cwd: Path, timeout: int = 180) -> tuple[int, str, str]:
    try:
        p = subprocess.run(cmd, cwd=str(cwd), capture_output=True, text=True, timeout=timeout)
        return p.returncode, p.stdout, p.stderr
    except (OSError, subprocess.TimeoutExpired) as e:
        return 127, "", str(e)


def have(tool: str) -> bool:
    return shutil.which(tool) is not None


def clamp(v: float, lo: float = 0, hi: float = 100) -> int:
    return int(max(lo, min(hi, round(v))))


class Audit:
    def __init__(self, repo: Path, quiet: bool = False):
        self.repo = repo
        self.quiet = quiet
        self.findings: list[dict] = []
        self.skipped: list[str] = []
        self.numbers: dict = {}
        self.files: list[Path] = []
        self.text_cache: dict[Path, str] = {}

    def log(self, msg: str) -> None:
        if not self.quiet:
            print(msg, file=sys.stderr)

    def add(self, category: str, severity: str, finding: str, path: str = "", line: int | None = None, rec: str = "") -> None:
        self.findings.append({"category": category, "severity": severity, "finding": finding, "path": path, "line": line, "recommendation": rec})

    # ---------- discovery ----------
    def walk(self) -> None:
        for root, dirs, files in os.walk(self.repo):
            dirs[:] = [d for d in dirs if d not in EXCLUDED_DIRS and not d.startswith(".git")]
            for f in files:
                p = Path(root) / f
                try:
                    if p.stat().st_size > 2_000_000:
                        continue
                except OSError:
                    continue
                self.files.append(p)

    def rel(self, p: Path) -> str:
        return str(p.relative_to(self.repo))

    def text(self, p: Path) -> str:
        if p in self.text_cache:
            return self.text_cache[p]
        try:
            t = p.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            t = ""
        self.text_cache[p] = t
        return t

    def exists(self, *names: str) -> str | None:
        for n in names:
            if (self.repo / n).exists():
                return n
        return None

    def source_files(self) -> list[Path]:
        return [p for p in self.files if p.suffix in LANG_EXT and p.suffix not in {".yml", ".yaml", ".sql", ".sh", ".tf"}]

    def inventory(self) -> None:
        langs: dict[str, int] = {}
        loc = 0
        for p in self.files:
            lang = LANG_EXT.get(p.suffix)
            if not lang:
                continue
            n = self.text(p).count("\n") + 1
            loc += n
            langs[lang] = langs.get(lang, 0) + n
        top = sorted(langs.items(), key=lambda kv: -kv[1])[:5]
        ecosystems = sorted({MANIFESTS[p.name] for p in self.files if p.name in MANIFESTS and p.parent == self.repo} |
                            {MANIFESTS[p.name] for p in self.files if p.name in MANIFESTS})
        self.numbers.update({
            "files": len(self.files), "loc": loc,
            "languages": [{"name": k, "loc": v} for k, v in top],
            "ecosystems": ecosystems,
        })

    # ---------- security ----------
    def security(self) -> int:
        score = 100
        # committed secret-like files
        for p in self.files:
            if SECRET_FILE_NAMES.match(p.name) and p.name not in SECRET_FILE_ALLOW:
                tracked = self.git_tracked(p)
                if tracked:
                    self.add("security", "critical", f"secret-like file committed: {p.name}", self.rel(p), rec="Remove from git, add to .gitignore, rotate contents")
                    score -= 25
        # secret values: external scanner first
        secrets_found = 0
        if have("gitleaks") and (self.repo / ".git").exists():
            rc, out, err = run(["gitleaks", "git", "--no-banner", "--redact", "--exit-code", "1", "--report-format", "json", "--report-path", "/dev/stdout", "."], self.repo, 600)
            if rc == 127 or "unknown command" in err:
                rc, out, err = run(["gitleaks", "detect", "--no-banner", "--redact", "--exit-code", "1", "--report-format", "json", "--report-path", "/dev/stdout"], self.repo, 600)
            try:
                items = json.loads(out) if out.strip().startswith("[") else []
            except json.JSONDecodeError:
                items = []
            secrets_found = len(items)
            for it in items[:50]:
                self.add("security", "critical", f"secret in history: {it.get('RuleID', 'secret')}", it.get("File", ""), it.get("StartLine"), rec="Rotate the secret, purge history with git filter-repo")
            self.numbers["secret_scanner"] = "gitleaks"
        else:
            self.skipped.append("gitleaks (secret scan of git history)")
            self.numbers["secret_scanner"] = "regex-fallback"
            for p in self.files:
                if p.suffix in {".lock", ".min.js", ".map", ".svg", ".png", ".jpg"} or p.name in LOCKFILES:
                    continue
                t = self.text(p)
                if not t:
                    continue
                for name, rx in SECRET_VALUE_PATTERNS:
                    for m in rx.finditer(t):
                        line = t.count("\n", 0, m.start()) + 1
                        if "example" in p.name.lower() or "test" in self.rel(p).lower() and name == "Generic assigned secret":
                            continue
                        secrets_found += 1
                        self.add("security", "critical", f"possible secret: {name}", self.rel(p), line, rec="Move to environment/secret manager and rotate")
                        if secrets_found > 50:
                            break
        self.numbers["secrets_found"] = secrets_found
        score -= min(60, secrets_found * 15)

        # unsafe code patterns
        unsafe = 0
        for p in self.source_files():
            t = self.text(p)
            if not t or TEST_FILE.search(self.rel(p)):
                continue
            for name, rx, sev, rec in UNSAFE_PATTERNS:
                for m in rx.finditer(t):
                    line = t.count("\n", 0, m.start()) + 1
                    unsafe += 1
                    self.add("security", sev, f"unsafe pattern: {name}", self.rel(p), line, rec=rec)
                    break  # one per file per pattern keeps the report readable
        self.numbers["unsafe_patterns"] = unsafe
        score -= min(25, unsafe * 3)

        # presence of protective patterns
        src_blob = "\n".join(self.text(p) for p in self.source_files()[:3000])
        manifests_blob = "\n".join(self.text(self.repo / n) for n in ("package.json", "pyproject.toml", "requirements.txt", "Gemfile", "composer.json", "go.mod", "Cargo.toml", "pom.xml", "build.gradle") if (self.repo / n).exists())
        blob = src_blob + "\n" + manifests_blob
        checks = {
            "security_headers": bool(HEADER_HINTS.search(blob)),
            "rate_limiting": bool(RATE_LIMIT_HINTS.search(blob)),
            "input_validation": bool(VALIDATION_HINTS.search(blob)),
            "auth_library": bool(AUTH_HINTS.search(blob)),
        }
        self.numbers.update(checks)
        is_app = bool(self.numbers.get("ecosystems"))
        if is_app:
            if not checks["security_headers"]:
                self.add("security", "medium", "no security headers middleware detected", rec="Add helmet/secure_headers/SecurityMiddleware equivalent"); score -= 8
            if not checks["rate_limiting"]:
                self.add("security", "medium", "no rate limiting detected", rec="Rate-limit auth and expensive routes"); score -= 5
            if not checks["input_validation"]:
                self.add("security", "medium", "no input validation library detected", rec="Validate request bodies with a schema"); score -= 5
        # gitignore covers .env
        gi = self.text(self.repo / ".gitignore") if (self.repo / ".gitignore").exists() else ""
        if not re.search(r"^\s*\.env(\s|$|\.)", gi, re.M) and not re.search(r"^\s*\*\.env", gi, re.M):
            self.add("security", "low", ".gitignore does not exclude .env", ".gitignore", rec="Add .env and .env.* (keep .env.example)"); score -= 3
        return clamp(score)

    def git_tracked(self, p: Path) -> bool:
        if not (self.repo / ".git").exists():
            return True
        rc, out, _ = run(["git", "ls-files", "--error-unmatch", self.rel(p)], self.repo, 30)
        return rc == 0

    # ---------- dependencies ----------
    def dependencies(self) -> int:
        score = 100
        eco = set(self.numbers.get("ecosystems", []))
        lock = self.exists(*LOCKFILES)
        self.numbers["lockfile"] = lock
        if eco and not lock:
            self.add("dependencies", "high", "no lockfile found", rec="Commit a lockfile and install with frozen flag in CI"); score -= 20
        vulns = {"critical": 0, "high": 0, "medium": 0, "low": 0}
        ran = []

        def bump(sev: str, n: int = 1) -> None:
            sev = sev.lower()
            if sev in vulns:
                vulns[sev] += n

        if "npm" in eco and (self.repo / "package.json").exists():
            pm = "pnpm" if (self.repo / "pnpm-lock.yaml").exists() and have("pnpm") else "yarn" if (self.repo / "yarn.lock").exists() and have("yarn") else "npm" if have("npm") else None
            if pm and (self.repo / "node_modules").exists() or pm == "npm" and (self.repo / "package-lock.json").exists():
                rc, out, _ = run([pm, "audit", "--json"] if pm != "yarn" else ["yarn", "npm", "audit", "--json"], self.repo, 300)
                try:
                    data = json.loads(out.strip().splitlines()[0] if pm == "yarn" else out)
                    meta = data.get("metadata", {}).get("vulnerabilities", {})
                    for k in vulns:
                        bump(k, int(meta.get(k, 0)))
                    ran.append(f"{pm} audit")
                except (json.JSONDecodeError, IndexError, ValueError):
                    self.skipped.append(f"{pm} audit (could not parse output)")
            else:
                self.skipped.append("npm audit (install dependencies first)")
        if "python" in eco:
            if have("pip-audit"):
                args = ["pip-audit", "-f", "json", "--progress-spinner", "off"]
                if (self.repo / "requirements.txt").exists():
                    args += ["-r", "requirements.txt"]
                rc, out, _ = run(args, self.repo, 300)
                try:
                    data = json.loads(out)
                    deps = data.get("dependencies", data if isinstance(data, list) else [])
                    for d in deps:
                        for v in d.get("vulns", []):
                            bump("high")  # pip-audit lacks severity without extra flags; treat as high
                    ran.append("pip-audit")
                except json.JSONDecodeError:
                    self.skipped.append("pip-audit (could not parse output)")
            else:
                self.skipped.append("pip-audit")
        if "go" in eco:
            if have("govulncheck"):
                rc, out, _ = run(["govulncheck", "-json", "./..."], self.repo, 600)
                n = sum(1 for line in out.splitlines() if '"finding"' in line and '"trace"' in line)
                bump("high", n); ran.append("govulncheck")
            else:
                self.skipped.append("govulncheck")
        if "rust" in eco:
            if have("cargo-audit") or have("cargo"):
                rc, out, _ = run(["cargo", "audit", "--json"], self.repo, 300)
                try:
                    data = json.loads(out)
                    n = data.get("vulnerabilities", {}).get("count", 0)
                    bump("high", n); ran.append("cargo audit")
                except json.JSONDecodeError:
                    self.skipped.append("cargo audit")
            else:
                self.skipped.append("cargo audit")
        if "ruby" in eco:
            if have("bundle-audit") or have("bundler-audit"):
                tool = "bundle-audit" if have("bundle-audit") else "bundler-audit"
                rc, out, _ = run([tool, "check", "--update", "--format", "json"], self.repo, 300)
                try:
                    data = json.loads(out)
                    for r in data.get("results", []):
                        bump(str(r.get("advisory", {}).get("criticality", "high")))
                    ran.append(tool)
                except json.JSONDecodeError:
                    self.skipped.append(tool)
            else:
                self.skipped.append("bundler-audit")
        if "php" in eco:
            if have("composer"):
                rc, out, _ = run(["composer", "audit", "--format=json", "--no-interaction"], self.repo, 300)
                try:
                    data = json.loads(out)
                    for pkg, advs in data.get("advisories", {}).items():
                        bump("high", len(advs))
                    ran.append("composer audit")
                except json.JSONDecodeError:
                    self.skipped.append("composer audit")
            else:
                self.skipped.append("composer audit")
        if not ran and have("osv-scanner"):
            rc, out, _ = run(["osv-scanner", "--format", "json", "--recursive", "--skip-git", "."], self.repo, 600)
            try:
                data = json.loads(out)
                for r in data.get("results", []):
                    for pkg in r.get("packages", []):
                        for v in pkg.get("vulnerabilities", []):
                            sev = "high"
                            for s in v.get("severity", []) or []:
                                if s.get("type") == "CVSS_V3":
                                    try:
                                        sc = float(s.get("score", "").split("/")[0].split(":")[-1]) if ":" in s.get("score", "") else 0
                                    except ValueError:
                                        sc = 0
                                    sev = "critical" if sc >= 9 else "high" if sc >= 7 else "medium" if sc >= 4 else "low"
                            bump(sev)
                ran.append("osv-scanner")
            except json.JSONDecodeError:
                self.skipped.append("osv-scanner")
        elif not ran and eco:
            self.skipped.append("osv-scanner (universal dependency scan)")
        self.numbers["vulnerabilities"] = vulns
        self.numbers["dependency_scanners_run"] = ran
        if vulns["critical"]:
            self.add("dependencies", "critical", f"{vulns['critical']} critical dependency vulnerabilities", rec="Upgrade affected packages now")
        if vulns["high"]:
            self.add("dependencies", "high", f"{vulns['high']} high dependency vulnerabilities", rec="Upgrade within 30 days")
        score -= min(60, vulns["critical"] * 15 + vulns["high"] * 5 + vulns["medium"] * 1)

        # outdated (npm only, cheap)
        outdated_major = None
        if "npm" in eco and have("npm") and (self.repo / "node_modules").exists():
            rc, out, _ = run(["npm", "outdated", "--json"], self.repo, 120)
            try:
                data = json.loads(out or "{}")
                outdated_major = sum(1 for k, v in data.items() if str(v.get("current", "0")).split(".")[0] != str(v.get("latest", "0")).split(".")[0])
                self.numbers["outdated_total"] = len(data)
            except json.JSONDecodeError:
                pass
        self.numbers["outdated_major"] = outdated_major
        if outdated_major:
            score -= min(10, outdated_major)

        auto = self.exists(*DEP_AUTOMATION)
        self.numbers["dependency_automation"] = auto
        if eco and not auto:
            self.add("dependencies", "low", "no Dependabot/Renovate config", rec="Add weekly grouped updates"); score -= 10
        return clamp(score)

    # ---------- tests ----------
    def tests(self) -> int:
        test_files = [p for p in self.files if TEST_FILE.search(self.rel(p)) and p.suffix in LANG_EXT]
        n = len(test_files)
        self.numbers["test_files"] = n
        score = 0
        if n:
            score += 40
            score += min(20, n)  # up to 20 for breadth
        else:
            self.add("tests", "high", "no test files found", rec="Add a test runner and the six baseline security tests")
        cov = self.coverage()
        self.numbers["coverage_percent"] = cov
        if cov is not None:
            score += cov * 0.3
        sec_tests = sum(1 for p in test_files if SECURITY_TEST_HINTS.search(self.text(p)))
        self.numbers["security_tests"] = sec_tests
        if sec_tests:
            score += min(10, sec_tests * 3)
        elif n:
            self.add("tests", "medium", "no security-focused tests found", rec="Add tests for 401/403, cross-user access, bad input, rate limit, headers")
        return clamp(score)

    def coverage(self) -> float | None:
        for name in ("coverage/coverage-summary.json", "coverage-summary.json"):
            p = self.repo / name
            if p.exists():
                try:
                    d = json.loads(self.text(p))
                    return float(d["total"]["lines"]["pct"])
                except (KeyError, ValueError, json.JSONDecodeError):
                    pass
        for name in ("coverage/lcov.info", "lcov.info"):
            p = self.repo / name
            if p.exists():
                t = self.text(p)
                lf = sum(int(x) for x in re.findall(r"^LF:(\d+)", t, re.M))
                lh = sum(int(x) for x in re.findall(r"^LH:(\d+)", t, re.M))
                if lf:
                    return round(100 * lh / lf, 1)
        for name in ("coverage.xml", "coverage/cobertura-coverage.xml"):
            p = self.repo / name
            if p.exists():
                m = re.search(r'line-rate="([0-9.]+)"', self.text(p))
                if m:
                    return round(100 * float(m.group(1)), 1)
        return None

    # ---------- ci ----------
    def ci(self) -> int:
        score = 0
        ci_path = self.exists(*CI_PATHS)
        self.numbers["ci"] = ci_path
        if not ci_path:
            self.add("ci", "high", "no CI configuration found", rec="Add a workflow running lint, tests, scans and build")
        else:
            score += 40
            blob = ""
            p = self.repo / ci_path
            if p.is_dir():
                for f in p.iterdir():
                    if f.suffix in {".yml", ".yaml"}:
                        blob += self.text(f)
            else:
                blob = self.text(p)
            steps = {
                "lint": bool(re.search(r"(lint|eslint|ruff|golangci|rubocop|phpstan|clippy|dotnet format|biome)", blob, re.I)),
                "test": bool(re.search(r"(\btest\b|pytest|vitest|jest|go test|rspec|phpunit|cargo test|dotnet test|gradle test|mvn test)", blob, re.I)),
                "secret_scan": bool(re.search(r"(gitleaks|trufflehog|secret.?scan)", blob, re.I)),
                "dependency_scan": bool(re.search(r"(npm audit|pnpm audit|pip-audit|cargo audit|govulncheck|osv-scanner|bundler-audit|composer audit|dependency-check|snyk|trivy|--vulnerable)", blob, re.I)),
                "build": bool(re.search(r"(\bbuild\b|docker build)", blob, re.I)),
                "pinned_actions": bool(re.search(r"uses:\s*\S+@[0-9a-f]{40}", blob)) or ("uses:" not in blob),
            }
            self.numbers["ci_steps"] = steps
            score += 10 if steps["lint"] else 0
            score += 15 if steps["test"] else 0
            score += 10 if steps["secret_scan"] else 0
            score += 10 if steps["dependency_scan"] else 0
            score += 5 if steps["build"] else 0
            score += 5 if steps["pinned_actions"] else 0
            for k, v in steps.items():
                if not v and k != "pinned_actions":
                    self.add("ci", "medium", f"CI does not run {k.replace('_', ' ')}", ci_path, rec="Add the step")
            if not steps["pinned_actions"]:
                self.add("ci", "low", "actions not pinned to a digest", ci_path, rec="Pin third-party actions to a commit SHA")
        deploy = [d for d in DEPLOY_FILES if (self.repo / d).exists()]
        self.numbers["deploy_config"] = deploy
        if deploy:
            score += 5
        return clamp(score)

    # ---------- docs ----------
    def docs(self) -> int:
        score = 0
        present = {}
        for key, names in DOC_FILES.items():
            present[key] = self.exists(*names)
        self.numbers["docs"] = present
        readme = present["readme"]
        if readme:
            t = self.text(self.repo / readme)
            score += 20
            if re.search(r"(npm (install|run|start)|pnpm|yarn|pip install|uv |poetry|go run|cargo run|bundle|composer|dotnet run|docker|make |just )", t, re.I):
                score += 15
            else:
                self.add("docs", "medium", "README has no run instructions", readme, rec="Add install, run and test commands")
            if re.search(r"(env|environment variable|\.env)", t, re.I):
                score += 5
        else:
            self.add("docs", "high", "no README", rec="Write a README with what, run, env, deploy")
        weights = {"license": 10, "changelog": 10, "contributing": 5, "security_policy": 5, "env_example": 15, "architecture": 10, "runbook": 10}
        for k, w in weights.items():
            if present[k]:
                score += w
            elif k in ("env_example", "architecture", "runbook", "license"):
                self.add("docs", "low", f"missing {k.replace('_', ' ')}", rec=f"Add {DOC_FILES[k][0]}")
        return clamp(score)

    # ---------- operability ----------
    def operability(self) -> int:
        score = 0
        blob = "\n".join(self.text(p) for p in self.source_files()[:3000])
        manifests = "\n".join(self.text(self.repo / n) for n in ("package.json", "pyproject.toml", "requirements.txt", "Gemfile", "composer.json", "go.mod", "Cargo.toml", "pom.xml", "build.gradle", "mix.exs", "pubspec.yaml") if (self.repo / n).exists())
        ops = {
            "health_endpoint": bool(HEALTH_HINTS.search(blob)),
            "structured_logging": bool(LOGGING_HINTS.search(blob + manifests)),
            "error_tracking": bool(ERROR_TRACKING_HINTS.search(blob + manifests)),
            "migrations": any((self.repo / m).exists() or any(m in self.rel(p) for p in self.files[:5000]) for m in MIGRATION_HINTS),
            "containerised": bool(self.exists("Dockerfile", "docker-compose.yml", "compose.yml")),
            "lint_config": bool(self.exists(*LINT_CONFIGS)),
        }
        self.numbers["operability"] = ops
        for k, w in {"health_endpoint": 15, "structured_logging": 20, "error_tracking": 20, "migrations": 15, "containerised": 15, "lint_config": 15}.items():
            if ops[k]:
                score += w
            else:
                self.add("operability", "low", f"missing {k.replace('_', ' ')}", rec="See kickstart-scaffold phase 3/5")
        return clamp(score)

    # ---------- compliance ----------
    def compliance(self) -> int:
        score = 0
        cm = self.repo / ".kickstart" / "compliance.md"
        self.numbers["compliance_checklist"] = cm.exists()
        implemented = planned = 0
        if cm.exists():
            score += 40
            t = cm.read_text(encoding="utf-8", errors="ignore")
            implemented = len(re.findall(r"\|\s*implemented\s*\|", t))
            planned = len(re.findall(r"\|\s*planned\s*\|", t))
            total = implemented + planned
            if total:
                score += 40 * implemented / total
        else:
            self.add("compliance", "medium", "no .kickstart/compliance.md", rec="Run kickstart-compliance (OWASP Top 10 at minimum)")
        self.numbers["controls_implemented"] = implemented
        self.numbers["controls_planned"] = planned
        blob = "\n".join(self.text(p) for p in self.source_files()[:3000])
        handles_pii = bool(PII_HINTS.search(blob))
        self.numbers["handles_personal_data"] = handles_pii
        if handles_pii:
            if DELETION_HINTS.search(blob):
                score += 10
            else:
                self.add("compliance", "medium", "personal data fields found but no deletion/erasure path detected", rec="Add account deletion and data export")
            if self.numbers.get("docs", {}).get("privacy") or any("privacy" in self.rel(p).lower() for p in self.files):
                score += 10
            else:
                self.add("compliance", "low", "no privacy notice found", rec="Add a privacy page")
        else:
            score += 20
        return clamp(score)

    # ---------- orchestration ----------
    def run_all(self) -> dict:
        self.log("kickstart audit: scanning…")
        self.walk()
        self.inventory()
        cats = {
            "security": self.security(),
            "dependencies": self.dependencies(),
            "tests": self.tests(),
            "ci": self.ci(),
            "docs": self.docs(),
            "operability": self.operability(),
            "compliance": self.compliance(),
        }
        overall = clamp(sum(cats[k] * WEIGHTS[k] for k in cats) / 100)
        band = "production-grade" if overall >= 85 else "nearly there" if overall >= 70 else "needs work" if overall >= 50 else "at risk"
        sev_order = {"critical": 0, "high": 1, "medium": 2, "low": 3}
        self.findings.sort(key=lambda f: (sev_order.get(f["severity"], 9), f["category"]))
        return {
            "version": VERSION,
            "repo": self.repo.name,
            "date": dt.date.today().isoformat(),
            "score": overall,
            "band": band,
            "confidence": "full" if not self.skipped else f"partial: {len(self.skipped)} checks skipped",
            "categories": cats,
            "weights": WEIGHTS,
            "numbers": self.numbers,
            "skipped": self.skipped,
            "findings": self.findings,
            "proposals": self.proposals(cats),
        }

    def proposals(self, cats: dict) -> list[dict]:
        n = self.numbers
        out = []

        def p(title, cat, gain, effort, risk, what):
            before = cats[cat]
            after = clamp(before + gain)
            out.append({"title": title, "category": cat, "before": before, "after": after, "overall_gain": round((after - before) * WEIGHTS[cat] / 100, 1), "effort": effort, "risk": risk, "what": what})

        if n.get("secrets_found"):
            p("Rotate and purge committed secrets", "security", 15 * min(4, n["secrets_found"]), "M 1–2h each", "history rewrite", "Rotate in provider, git filter-repo, force push, add scanning")
        v = n.get("vulnerabilities", {})
        if v.get("critical") or v.get("high"):
            p("Upgrade vulnerable dependencies", "dependencies", v.get("critical", 0) * 15 + v.get("high", 0) * 5, "M 1–4h", "possible breaking majors", "Upgrade affected packages, run tests between groups")
        if not n.get("lockfile") and n.get("ecosystems"):
            p("Commit a lockfile", "dependencies", 20, "S 15m", "none", "Generate and commit; use frozen install in CI")
        if not n.get("ci"):
            p("Add CI workflow (lint, test, scan, build)", "ci", 70, "M 1h", "none", "Add .github/workflows/ci.yml from kickstart-guardrails template")
        else:
            steps = n.get("ci_steps", {})
            if not steps.get("secret_scan"):
                p("Add secret scanning to CI", "ci", 10, "S 15m", "none", "gitleaks job")
            if not steps.get("dependency_scan"):
                p("Add dependency scanning to CI", "ci", 10, "S 20m", "none", "osv-scanner or ecosystem audit job")
            if not steps.get("test"):
                p("Run tests in CI", "ci", 15, "S 20m", "none", "Add test step")
        if not n.get("test_files"):
            p("Add test runner and baseline security tests", "tests", 55, "M 1–2h", "none", "Runner config, one unit test, six OWASP baseline tests")
        elif not n.get("security_tests"):
            p("Add the six baseline security tests", "tests", 10, "M 1–2h", "none", "401/403, cross-user, bad input, rate limit, headers, fail closed")
        if n.get("ecosystems") and not n.get("security_headers"):
            p("Add security headers middleware", "security", 8, "S 30m–1h", "CSP may need tuning", "helmet / secure_headers / SecurityMiddleware")
        if n.get("ecosystems") and not n.get("rate_limiting"):
            p("Rate-limit auth and expensive routes", "security", 5, "M 1h", "none", "Middleware on login, signup, reset, search")
        if n.get("unsafe_patterns"):
            p("Fix unsafe code patterns", "security", min(25, n["unsafe_patterns"] * 3), "M 1–4h", "low", "See findings: parameterise SQL, remove eval/pickle, sanitise HTML")
        ops = n.get("operability", {})
        if not ops.get("structured_logging"):
            p("Add structured logging with request id", "operability", 20, "M 1h", "none", "pino/structlog/slog JSON logger")
        if not ops.get("error_tracking"):
            p("Add error tracking", "operability", 20, "S 30m", "none", "Sentry or equivalent, DSN from env")
        if not ops.get("health_endpoint"):
            p("Add /health endpoint", "operability", 15, "S 15m", "none", "Returns version and DB check")
        if not ops.get("containerised"):
            p("Add Dockerfile (multi-stage, non-root)", "operability", 15, "M 1h", "none", "From kickstart-scaffold template")
        docs = n.get("docs", {})
        if not docs.get("readme"):
            p("Write README with run instructions", "docs", 40, "S 30m", "none", "What, run, env, test, deploy")
        if not docs.get("env_example"):
            p("Add .env.example", "docs", 15, "S 15m", "none", "Every variable documented, no values")
        if not docs.get("runbook") or not docs.get("architecture"):
            p("Write architecture note and runbook", "docs", 20, "M 2h", "none", "docs/architecture.md, docs/runbook.md")
        if not n.get("dependency_automation") and n.get("ecosystems"):
            p("Add Dependabot/Renovate", "dependencies", 10, "S 15m", "none", "Weekly grouped updates")
        if not n.get("compliance_checklist"):
            p("Create compliance checklist (OWASP Top 10 minimum)", "compliance", 40, "M 1h", "none", "Run kickstart-compliance")
        if any("deletion" in f["finding"] for f in self.findings if f["category"] == "compliance"):
            p("Add account deletion and data export", "compliance", 10, "M 2–4h", "none", "Required by GDPR, DPDPA, CCPA and most privacy laws")
        out.sort(key=lambda x: -x["overall_gain"])
        return out


def effort_hours(proposals: list[dict]) -> float:
    total = 0.0
    for p in proposals:
        e = p["effort"]
        total += 0.5 if e.startswith("S") else 2.5 if e.startswith("M") else 12
    return round(total, 1)


def render_md(r: dict) -> str:
    n = r["numbers"]
    c = r["categories"]
    crit = [f for f in r["findings"] if f["severity"] == "critical"]
    v = n.get("vulnerabilities", {})
    lines = []
    lines.append(f"# Kickstart audit: {r['repo']}  ({r['date']})\n")
    lines.append(f"**Score: {r['score']}/100 ({r['band']})**   Confidence: {r['confidence']}\n")
    if "delta" in r:
        lines.append(f"Change since {r['delta']['date']}: {r['delta']['score']:+d}\n")
    lines.append("## Critical (fix this week)")
    if crit:
        seen = set()
        for f in crit:
            key = f["finding"].split(":")[0]
            if key in seen:
                continue
            seen.add(key)
            count = sum(1 for x in crit if x["finding"].split(":")[0] == key)
            lines.append(f"- {count}× {key}  → {f['recommendation']}")
    else:
        lines.append("- none")
    lines.append("")
    lines.append("## Category scores")
    lines.append("| Security | Dependencies | Tests | CI/CD | Docs | Operability | Compliance |")
    lines.append("|---|---|---|---|---|---|---|")
    lines.append(f"| {c['security']} | {c['dependencies']} | {c['tests']} | {c['ci']} | {c['docs']} | {c['operability']} | {c['compliance']} |\n")
    lines.append("## Numbers that matter")
    langs = ", ".join(f"{l['name']} ({l['loc']:,})" for l in n.get("languages", []))
    lines.append(f"- {n.get('files', 0):,} files, {n.get('loc', 0):,} lines: {langs or 'no source detected'}")
    lines.append(f"- Ecosystems: {', '.join(n.get('ecosystems', [])) or 'none'}; lockfile: {n.get('lockfile') or 'no'}; automated updates: {n.get('dependency_automation') or 'no'}")
    lines.append(f"- Vulnerabilities: {v.get('critical', 0)} critical / {v.get('high', 0)} high / {v.get('medium', 0)} medium  (scanners: {', '.join(n.get('dependency_scanners_run', [])) or 'none ran'})")
    lines.append(f"- Secrets: {n.get('secrets_found', 0)} found ({n.get('secret_scanner')}); unsafe patterns: {n.get('unsafe_patterns', 0)}")
    cov = n.get("coverage_percent")
    lines.append(f"- Tests: {n.get('test_files', 0)} test files, coverage {str(cov) + '%' if cov is not None else 'unknown'}, security tests: {n.get('security_tests', 0)}")
    steps = n.get("ci_steps", {})
    lines.append(f"- CI: {n.get('ci') or 'none'}; runs: " + (", ".join(k for k, ok in steps.items() if ok and k != 'pinned_actions') or "n/a"))
    ops = n.get("operability", {})
    lines.append(f"- Operability: " + ", ".join(f"{k.replace('_', ' ')}={'yes' if ok else 'no'}" for k, ok in ops.items()))
    lines.append(f"- Compliance checklist: {'yes' if n.get('compliance_checklist') else 'no'}; controls implemented {n.get('controls_implemented', 0)} / planned {n.get('controls_planned', 0)}; personal data detected: {'yes' if n.get('handles_personal_data') else 'no'}")
    lines.append("")
    lines.append(f"**Estimated effort to reach 85: ~{effort_hours(r['proposals'])}h across {len(r['proposals'])} changes**\n")
    lines.append("## Proposed changes (ranked by score gain)")
    for i, p in enumerate(r["proposals"], 1):
        lines.append(f"{i}. **{p['title']}**  \n   {p['category']}: {p['before']} → {p['after']} (overall +{p['overall_gain']})  ·  Effort {p['effort']}  ·  Risk: {p['risk']}  \n   {p['what']}")
    lines.append("")
    if r["skipped"]:
        lines.append("## Not checked (tool unavailable)")
        for s in r["skipped"]:
            lines.append(f"- {s}")
        lines.append("")
    lines.append("## Details")
    for cat in WEIGHTS:
        fs = [f for f in r["findings"] if f["category"] == cat]
        if not fs:
            continue
        lines.append(f"### {cat.title()} ({c[cat]}/100)")
        lines.append("| severity | location | finding | recommendation |")
        lines.append("|---|---|---|---|")
        for f in fs:
            loc = f["path"] + (f":{f['line']}" if f.get("line") else "")
            lines.append(f"| {f['severity']} | {loc} | {f['finding']} | {f['recommendation']} |")
        lines.append("")
    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--repo", default=".")
    ap.add_argument("--out", default=".kickstart/audit")
    ap.add_argument("--json-only", action="store_true")
    ap.add_argument("--quiet", action="store_true")
    a = ap.parse_args()
    repo = Path(a.repo).resolve()
    out = Path(a.out) if Path(a.out).is_absolute() else repo / a.out
    out.mkdir(parents=True, exist_ok=True)

    audit = Audit(repo, a.quiet)
    report = audit.run_all()

    hist = out / "history.jsonl"
    if hist.exists():
        try:
            last = json.loads(hist.read_text().strip().splitlines()[-1])
            report["delta"] = {"date": last["date"], "score": report["score"] - last["score"]}
        except (json.JSONDecodeError, IndexError, KeyError):
            pass
    with hist.open("a") as f:
        f.write(json.dumps({"date": report["date"], "score": report["score"], "categories": report["categories"]}) + "\n")

    (out / "latest.json").write_text(json.dumps(report, indent=2))
    (out / f"{report['date']}.json").write_text(json.dumps(report, indent=2))
    if not a.json_only:
        md = render_md(report)
        (out / "latest.md").write_text(md)
        print(md)
    else:
        print(json.dumps(report, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
