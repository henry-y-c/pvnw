# Changelog

Changes to the portable PVNW Skill are documented here. Format inspired by [Keep a Changelog](https://keepachangelog.com/en/1.1.0/); versioning follows [Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html). The public contract covers the `pvnw/` bundle layout, entry metadata, six referenced decision/safety guides, and explicitly documented behavior and permission boundaries. It does **not** cover unspecified host auto-activation.

## [Unreleased]

### Notes

- Host installation, default activation and real-task answer quality require separate end-to-end observation; no compatibility claims have been verified.

## [0.1.0] - 2026-10-07

### Added

- `pvnw/SKILL.md` plus six on-demand references for decision gates, task routing, note modeling, safe inbox boundaries, provenance/permissions and synthetic acceptance cases.
- Project README, contributor instructions, MIT license, offline repository validation and CI.
- Source-only release; no client installation or persistent opt-out mechanism is bundled.

### Security

- Writing, inbox creation, Git commit and public distribution remain separately authorized operations; first-time unknown storage targets do not trigger automatic file creation.

[Unreleased]: https://github.com/henry-y-c/pvnw/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/henry-y-c/pvnw/releases/tag/v0.1.0
