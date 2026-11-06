#!/usr/bin/env node
// Installs the kickstart skills via the `skills` CLI, then prints next steps
// (the `skills` CLI has no post-install hook, so this wrapper supplies one).
// Usage: npx github:iponnam/kickstart-skills [skills add flags, e.g. -g, -a claude-code]
"use strict";
const { spawnSync } = require("node:child_process");
const { existsSync } = require("node:fs");
const { join } = require("node:path");
const { homedir } = require("node:os");

const REPO = "iponnam/kickstart-skills";
const B = "\x1b[1m", D = "\x1b[2m", C = "\x1b[36m", G = "\x1b[32m", Y = "\x1b[33m", N = "\x1b[0m";

const result = spawnSync("npx", ["skills", "add", REPO, ...process.argv.slice(2)], {
  stdio: "inherit",
  shell: process.platform === "win32",
});

if (result.error) {
  console.error(`\nCould not run the skills CLI: ${result.error.message}`);
  console.error(`Install manually: npx skills add ${REPO}`);
  process.exit(1);
}
if (result.status !== 0) process.exit(result.status ?? 1);

// Agents people most often expect and most often forget to tick in the 79-agent picker.
const AGENTS = [
  { name: "Claude Code", flag: "claude-code", dir: ".claude/skills" },
  { name: "Cursor", flag: "cursor", dir: ".cursor/skills" },
  { name: "Codex", flag: "codex", dir: ".codex/skills" },
];
const global = process.argv.includes("-g") || process.argv.includes("--global");
const root = global ? homedir() : process.cwd();
const has = (a) => existsSync(join(root, a.dir, "kickstart"));
const installed = AGENTS.filter(has).map((a) => a.name);
const missing = AGENTS.filter((a) => !has(a));

const lines = [
  `${B}Next steps${N}`,
  ``,
  `1. Open this project in the agent you selected above.`,
  installed.length
    ? `   ${G}✓${N} Ready for: ${installed.join(", ")}`
    : `   ${Y}!${N} Not installed for Claude Code, Cursor or Codex. Skills only go to the agents you ticked.`,
  ...missing.map((a) => `   ${D}Need ${a.name}? Re-run with:${N} npx github:${REPO} -a ${a.flag}${global ? " -g" : ""}`),
  `2. Type:`,
  ``,
  `     ${C}${B}/kickstart${N}`,
  ``,
  `   Empty folder  → asks what you're building, recommends a stack with costs, scaffolds it.`,
  `   Existing repo → audits it: 0–100 score, critical findings, fixes with before/after numbers.`,
  `   ${D}Not recognised? Say "set up this project" or "audit this repo" in plain words.${N}`,
  ``,
  `${B}Day to day${N} ${D}(/kickstart routes to these for you)${N}`,
  `  ${C}/kickstart-assess${N}    "I have an idea"        → go / clarify / kill verdict`,
  `  ${C}/kickstart-feature${N}   "add a feature"         → spec, plan, tasks, tests first, converge`,
  `  ${C}/kickstart-bugfix${N}    "this crashes"          → root cause, regression test, verified fix`,
  `  ${C}/kickstart-release${N}   "ship it"               → pre-release checklist`,
  `  ${C}/kickstart-refresh${N}   monthly                 → dependency + vulnerability refresh`,
  ``,
  `${D}Docs: https://github.com/${REPO}${N}`,
];
const width = Math.max(...lines.map((l) => l.replace(/\x1b\[[0-9;]*m/g, "").length)) + 4;
const pad = (l) => l + " ".repeat(width - 2 - l.replace(/\x1b\[[0-9;]*m/g, "").length);
console.log(`\n${G}╭${"─".repeat(width - 2)}╮${N}`);
for (const l of lines) console.log(`${G}│${N} ${pad(l)}${G}│${N}`);
console.log(`${G}╰${"─".repeat(width - 2)}╯${N}\n`);
