# PVNW repository instructions for contributing agents

This file governs work **in this repository**. It is not the runtime Skill entry, not an installation recipe, and not permission to change a user's files. Runtime instructions start at `pvnw/SKILL.md`; six on-demand references live at `pvnw/references/`.

## Authority and scope

1. Respect the user's instruction, applicable host policy, and the target project's own rules. For *this repo*, the Skill bundle owns user-facing behavior; README explains distribution and limitations; CONTRIBUTING owns PR and commit rules; CHANGELOG owns release history. Resolve contradictions rather than silently treating implementation as specification.
2. Keep PVNW portable: do not depend on any local project paths, a particular host, private notebooks, model secrets, or external packages. Do not install or modify host discovery configurations as a side effect of editing this repo.
3. Treat the root `AGENTS.md` as contributor guidance, **not** a guarantee that a host loads `SKILL.md`. Never claim static success proves actual activation or meaningful answers.

## Editing boundary

- Maintain `pvnw/SKILL.md` as a concise entry point. It must name `pvnw`, describe *when* to use the skill and link to the six references with relative paths. Do not merge all references into the entry or add a seventh reference without explicitly documenting the compatibility decision.
- Preserve critical distinctions: every-task **judgment** versus not-every-task **writing**; first-time no authorized location versus unique authorized target; current-task default opt-out versus unsupported persistent opt-out; planning an inbox versus creating one; human-confirmed freeze versus AI proposal; recorded source versus actual host test.
- Connect each suggestion, model and action to the user's original question and observable exit. Preserve corrections and attribution; do not retroactively rewrite a human decision as an agent design choice.
- Never add real conversations, credentials, private file paths, personal IDs, or sensitive summaries to source, fixtures, issues, commits, or releases. `.gitignore` is only a guardrail; inspect actual staged content and history before publishing.

## Validation and changes

Run `python3 -m unittest discover -s tests -v` and `git diff --check`; for staged edits also run `git diff --cached --check`. The tests are offline static assertions, **not** agent-behavior or host-loading tests. If format tooling is already available, optionally run `skills-ref validate ./pvnw` and report whether it actually ran. Describe failures or unverified behavior honestly.

Follow [CONTRIBUTING.md](CONTRIBUTING.md) for Conventional Commits, small PRs, AI disclosure and SemVer. Do not publish a release, copy a bundle into a host, or commit another user's worktree changes without specific authorization. All examples must be synthetic and safe to make public.
