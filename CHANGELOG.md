# Changelog

1. **Scope:** the public contract covers the portable `pvnw/` bundle layout, entry metadata, seven on-demand guides, and documented behavior/permission boundaries—not unspecified host auto-activation.
2. **Versioning:** format inspired by [Keep a Changelog](https://keepachangelog.com/en/1.1.0/); versions follow [Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.6.1] - 2026-10-07

1. Made the existing eight-step Skill procedure an explicit conditional Workflow: for work worth recording, locate the uniquely authorized vault or chosen Markdown directory and check directory/file scope before substantive research; ask for missing location or permission before that work, not after drafting an answer. Directly answerable tasks and explicit opt-outs do not prompt for a vault. Filesystem writability is not authorization; reuse an applicable authorized vault and create a compatible `.md` folder only at an approved unique location when none applies.
2. Added synthetic timing/permission counterexamples and an offline written-contract test. Existing project structures need no migration; host installation, pre-task invocation and real note creation still require separate host integration and runtime validation. No Git, push, release or `.obsidian` permission follows from this update.

### Verification

1. Before publication, 19 offline source-contract tests passed locally; Ruby Psych parsed the actual Skill frontmatter, and changed-file Markdown links and Git diff whitespace checks passed. Remote CI for the exact release commit must pass before tagging; these checks do not establish host pre-task invocation, Obsidian rendering or real-task behavior.

## [0.6.0] - 2026-10-07

1. Shifted the entry decision toward reasoning-intensive questions: an authorized research task records a real question, testable first milestone, current WBS plan and unexecuted status before substantive research; safe observable actions then append to the same package and sync its summary. Directly answerable questions and explicit opt-outs may still leave no note. Existing identities and human-only freeze are unchanged.
2. Added a scoped managed-workspace branch: if no suitable authorized vault exists and visible policy specifies one destination plus directory/file creation and later maintenance rights, create an Obsidian-compatible Markdown vault there without requiring Obsidian or `.obsidian`; otherwise keep the existing no-write/ask boundary and honor user-chosen ordinary Markdown directories.
3. Clarified one Git checkpoint per verifiably delivered or blocked WBS package, not per research action, with existing Git, explicit local commit permission, staged-snapshot verification and no automatic git init/push; host pre-task activation still requires independent host implementation and runtime validation.
4. Added synthetic AX–BC acceptance cases for pre-task dispatch, managed vault bootstrap, research-before-write sequencing, stepwise logs and conditional per-package commits; offline contract tests do not prove host behavior.
5. Defined a permission-gated local Git closeout at complete WBS progress, milestone movement/reassessment, and task-batch boundaries; no per-line commits, no implicit write-to-commit permission, no automatic push, and explicit task prohibitions still prevail.
6. Normalized Chinese bold-label punctuation outside emphasis across the portable bundle and added a source check for risky emphasis boundaries. New authorized notes should receive a Markdown check and, where possible, a target-reader spot check; existing user documents are not migrated.
7. Clarified existing-work-package continuation: check newly verified evidence before classifying a question as throwaway; with explicit scoped continuing maintenance permission, append to the original process and sync the necessary summary even when the milestone conclusion is unchanged. One-time bootstrap permission does not imply continuing write access.
8. Offline synthetic checks cover written commit gates, risky bold syntax and continuation boundaries, not real agent/host execution. Host installation, default activation, renderer behavior and real-task quality require separate observation; no such claims have been verified.

### Fixed

1. Quoted the colon-containing `description` YAML scalar in `SKILL.md`: previously valid-looking source failed actual YAML parsing and could be excluded from a host's skill catalog. The Python source test now rejects this unquoted-colon regression; CI parses actual metadata and the broken fixture with Ruby Psych, without changing bundle dependencies.

### Verification

1. Before release, 18 offline source-contract tests passed locally; Ruby Psych accepted the corrected frontmatter and rejected the unquoted-colon fixture; `git diff --check` passed. Remote CI for the release commit is a separate gate to check before tagging. Metadata parsing does not prove host discovery, automatic pre-task invocation or a real task result.

## [0.5.0] - 2026-10-07

### Changed

1. **New-project identities:** macro `0_<name>.md` → meso `N_<dir name>/N.0_<name>.md` → micro WBS package `N.1_<name>.md`, `N.2_<name>.md` etc. Each package is a file containing its whole evidence-backed execution process, not a `N.W1` planning row plus independent `N-1` issue note. Completing a package does not prove a milestone checkpoint.
2. **Markdown writing:** the Skill entry and all seven references use ordered list-note bodies, four-space nested lists for one-dimensional reasoning, and local comparison tables only when multiple objects share stable fields; multiple points inside a cell receive visual `1. …<br>2. …` numbering. Rendering, accessibility, and semantic HTML behavior are not claimed verified.
3. **Compatibility and safety:** prior v0.4.0 identities remain valid in existing projects; no automatic migration, filename rewrite or one-to-one numeric mapping. Existing project conventions, per-operation permission gates, human freeze and conditional micro→meso→macro sync remain. Synthetic AA–AL cases and offline tests cover new/old identity collisions and incomplete work-package histories; they do not prove agent behavior.

### Verification

1. Before release, 12 offline source-contract and in-memory fixture tests passed; source-link resolution and `git diff --check` passed. Staged-snapshot and publication/CI checks require separate verification of this version's exact commit SHA. `skills-ref` and host activation have not been verified.

## [0.4.0] - 2026-10-07

### Added

- Seventh on-demand reference `project-system.md`: a concrete, opt-in project-management contract for project overview, independently assessable milestone, milestone-local WBS deliverables/work packages and evidence-backed problem history. Document stable naming, collision checks, distinct `N` / `N.W…` / `N-1` identities, parent-child work breakdown, dependencies, acceptance evidence and human-only freeze. Existing conventions take precedence; work items and directories are not mandatory for ordinary tasks.
- Event-by-event update/lifecycle guidance and synthetic counterexamples for changing state, a failed work package, renamed paths, an incomplete newly added index and incomplete permissions. Root updates remain conditional; micro changes require meso follow-up when the target project uses that chain.

### Changed

- The on-demand bundle grows from six to seven references as a **documented compatible additive change**: the prior six reference paths and four task routes remain; clients distributing the complete bundle must include the new reference, while existing project files do not require renaming or WBS migration. The short `SKILL.md` now links the new contract and describes project-management scope; README, contributor guidance and source tests follow it. Treat this as a 0.x minor capability extension; no automatic per-task writing or expanded permissions.
- A user-selected authorized Markdown directory takes precedence over an unrelated usable Vault; creation, old-file renaming, link repair, rollback, Git and publication each require applicable permission.

### Verification

- Before the release commit, 10 offline source-contract/fixture checks passed (`PYTHONDONTWRITEBYTECODE=1 python3 -B -m unittest discover -s tests -v`), including source-relative links; `git diff --check` and `git diff --cached --check` passed. All 11 intended files including the new reference were staged; staged Markdown paths resolved, added lines had no private absolute paths, emails or credential-shaped strings (heuristic, not exhaustive). Remote publication/CI is a separate gate. `skills-ref` was unavailable and not run. Static checks cannot demonstrate host discovery, agent compliance, safe migration on real projects, Obsidian rendering or user benefit.

## [0.3.0] - 2026-10-07

### Added

- Explicitly authorized project-documentation bootstrap in an existing Obsidian vault or ordinary portable Markdown folder, including macro goal navigation → meso assessable milestone and phase evidence → micro source-backed original list and correction, with relative-link walk-through. No mandatory three files for ordinary tasks or new fifth route.
- Read-only inventory and old→new migration map before authorized, incremental reorganization of an existing document collection; restore/old-link checks and stop conditions. Assessable checkpoint review handles small wins, risk, failure and replanning without equating a time-consuming task with a milestone or AI judgment with human freeze.
- Synthetic positive/negative written scenarios for both storage choices, limited permissions, safe original notes, broken navigation and proposed staged-snapshot consistency. Offline tests assert policy text and an in-memory fixture graph (missing path/anchor/reciprocal entry/evidence); they do **not** inspect a real project's files or Git index.

### Security

- Keep separate permissions for project location, directory/file creation, old-file moves/deletion, backups, Git commit, remote publication and host installation. A writable root is not blanket permission for `.obsidian`, migration, inbox or release; original sensitive material is never copied merely to preserve verbatim history.

### Verification

- Before the release commit, 8 offline source-contract checks passed, bundle-relative links resolved, `git diff --check` and `git diff --cached --check` passed, and staged additions were screened for private paths, emails and credential-shaped strings (heuristic, not an exhaustive security audit). This validates written source/fixtures, not model behavior, host loading, Obsidian rendering, real migration or reader benefit. `skills-ref` was unavailable and not run.

## [0.2.0] - 2026-10-07

### Added

- Optional micro-level question history, meso-level current goal summaries and macro-level cross-goal status/navigation, with evidence links and conditional update triggers. No mandatory three-file vault layout, new route or extra reference.
- Synthetic counterexamples for unavailable storage, partial layer permissions, terminated exploration and invalidated frozen judgments; an additional offline written-contract test.

### Security

- Explicit independent authorization for writing each view and creating directories; report an unsynchronized upper layer, or defer when the target project requires atomic synchronization. Existing no-write default, separate Git/publication/installation gates and human-only freeze remain intact.

### Verification

- Six local offline static repository tests passed before release. Host discovery, task activation, model behavior, rendering and real-world benefit remain unverified; optional `skills-ref` validation did not run (tool unavailable).

## [0.1.0] - 2026-10-07

### Added

- `pvnw/SKILL.md` plus six on-demand references for decision gates, task routing, note modeling, safe inbox boundaries, provenance/permissions and synthetic acceptance cases.
- Project README, contributor instructions, MIT license, offline repository validation and CI.
- Source-only release; no client installation or persistent opt-out mechanism is bundled.

### Security

- Writing, inbox creation, Git commit and public distribution remain separately authorized operations; first-time unknown storage targets do not trigger automatic file creation.

[Unreleased]: https://github.com/henry-y-c/pvnw/compare/v0.6.1...HEAD
[0.6.1]: https://github.com/henry-y-c/pvnw/releases/tag/v0.6.1
[0.6.0]: https://github.com/henry-y-c/pvnw/releases/tag/v0.6.0
[0.5.0]: https://github.com/henry-y-c/pvnw/releases/tag/v0.5.0
[0.4.0]: https://github.com/henry-y-c/pvnw/releases/tag/v0.4.0
[0.3.0]: https://github.com/henry-y-c/pvnw/releases/tag/v0.3.0
[0.2.0]: https://github.com/henry-y-c/pvnw/releases/tag/v0.2.0
[0.1.0]: https://github.com/henry-y-c/pvnw/releases/tag/v0.1.0
