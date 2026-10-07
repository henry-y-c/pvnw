# Contributing to PVNW

欢迎安全、可复核的改进。**先描述原问题、预期出口和最可能失败的反例**，再讨论文件形式或模板。文档与示例当前主要使用中文；英语贡献可先附最小中文摘要，以便审阅者看清行为变化。

## 报告与讨论

- 明确的文案错误、断链、离线校验失败：提 Issue，给当前版本、最小**合成**复现及预期/实际。新行为、跨宿主安装或有破坏性的权限建议：先开 Discussion/Issue 说明范围、反例与迁移，不要把一个客户端的加载机制升格为通用承诺。
- 安全问题请避免在公开 Issue/PR 粘贴真实密钥、用户内容、原始聊天、个人信息或客户文件；若误泄露，应立即撤销相关凭据并按 GitHub 私下渠道报告，不能指望删一次提交解决历史泄露。
- 欢迎补充纸面场景和宿主实测，但务必区分“我读过源码”“静态检查通过”“在某版本客户端触发成功”“对原任务有帮助”；未运行就写未验证。

## 小范围 PR

1. 阅读 [AGENTS.md](AGENTS.md) 与 [SKILL.md](pvnw/SKILL.md)，说明是改入口、某份引用、README 还是版本/测试。不要未经讨论改动基本安全关口或将私有笔记和本项目绑定。
2. PR 写明目标问题、为何目前不够、修改前/后合成输入及预期出口、权限和隐私影响；涉及行为兼容要附迁移方案和 CHANGELOG 提案。修改项目命名、里程碑／WBS 身份或状态迁移时，核对 [project-system.md](pvnw/references/project-system.md) 与四路由、旧项目约定优先、编号不复用及其他六份引用；旧 `N.W1`／`N-1` 不可按数字批量改成 `N.1`。Skill 本身的 Markdown 与合成示例也用清单体（一维四空格嵌套有序列表，必要的局部管道表与格内编号），勿用增加文件层级或空表替代可回查证据。
3. 运行 `python3 -m unittest discover -s tests -v`、`git diff --check`，有暂存改动时也运行 `git diff --cached --check`；可选 `skills-ref validate ./pvnw`（仅工具已存在时）。报告**实际运行**和未运行的测试；若做了宿主冒烟，附客户端名称/版本、手工发现与逐任务行为记录，不上传真实用户输入。
4. 如使用 AI 辅助，PR 中披露使用范围、人工审阅过的关键风险点以及测试实况；贡献者对版权来源、安全和正确性负责。不要照搬第三方 Skill 正文或受限样例。
5. 保持一次 PR 一类主题，不改写别人尚未授权的历史稿，不为消除测试错误而删除安全反例。

## 提交与版本

采用 [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/)：`feat: 增加受控判断`、`fix: 修正未授权写入风险`、`docs: 澄清宿主边界`、`test: 扩充静态场景`、`chore: 更新协作流程`；破坏性改动另附 `BREAKING CHANGE:` 与迁移说明。subject 简短，body 说明**为何**；分主题提交，拒绝凭据和真实用户内容。

以 [SemVer 2.0.0](https://semver.org/spec/v2.0.0.html) 表示**公开契约**变化：兼容纠错 → patch；兼容的能力扩展 → minor；不兼容的入口、路径、安全语义变化 → major（0.x 初期可调整，但同样在 CHANGELOG 明示迁移）。标记 `vX.Y.Z`，发布时将已验证和未验证分开写在 [CHANGELOG.md](CHANGELOG.md) 与 GitHub Release；遵循 [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) 的人工分类，不以 `git log` 自动替代。

MIT 许可见 [LICENSE](LICENSE)。提交者必须有权许可其原创贡献；第三方库的公开可读不代表其内容可重新授权为 MIT。
