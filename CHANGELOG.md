# Changelog

Changes to the portable PVNW Skill are documented here. Format inspired by [Keep a Changelog](https://keepachangelog.com/en/1.1.0/); versioning follows [Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html). The public contract covers the `pvnw/` bundle layout, entry metadata, six referenced decision/safety guides, and explicitly documented behavior and permission boundaries. It does **not** cover unspecified host auto-activation.

## [Unreleased]

### Notes

- Host installation, default activation and real-task answer quality require separate end-to-end observation; no compatibility claims have been verified.

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

[Unreleased]: https://github.com/henry-y-c/pvnw/compare/v0.3.0...HEAD
[0.3.0]: https://github.com/henry-y-c/pvnw/releases/tag/v0.3.0
[0.2.0]: https://github.com/henry-y-c/pvnw/releases/tag/v0.2.0
[0.1.0]: https://github.com/henry-y-c/pvnw/releases/tag/v0.1.0
