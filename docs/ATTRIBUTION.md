# Attribution

## GitHub Spec Kit

The spec-driven workflow in `kickstart-feature`, the project constitution in `kickstart-constitution`, and the three-step bug process in `kickstart-bugfix` are adapted from [GitHub Spec Kit](https://github.com/github/spec-kit). Kickstart's adaptation is based on the repository as of commit `3ca735b` (2026-11-05).

What was adapted:

- The stage sequence: constitution, specify, clarify, plan, tasks, analyze, implement, converge, and the optional requirements checklist.
- The spec structure: prioritised user stories, Given/When/Then acceptance scenarios, `FR-###` requirements, `SC-###` success criteria, and at most three `[NEEDS CLARIFICATION]` markers.
- The clarification method: a coverage scan by category and at most five targeted questions, written back into the spec.
- The consistency check: detection passes and severity levels across spec, plan and tasks, with constitution conflicts treated as critical.
- The convergence loop: append-only gap tasks classified as missing, partial, contradicts or unrequested.
- Constitution versioning (MAJOR, MINOR, PATCH) and the Sync Impact Report.
- The bug process of assess, fix and test, ending in a verified, partial or failed verdict.

What kickstart changes:

- Tests are mandatory and written first. In Spec Kit they are optional.
- The constitution is seeded from kickstart's stack, scale, enforcement and compliance decisions.
- Plans include a compliance-controls table, and the consistency check has a compliance pass.
- Facts follow kickstart's freshness rule: 24 hours for tech stack facts, 60 days for compliance records.
- Pet projects get a shorter path through the same stages.

Spec Kit is distributed under the MIT License:

```
MIT License

Copyright GitHub, Inc.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
