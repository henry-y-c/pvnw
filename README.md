# PVNW — Progressive Vibe Notes Writing

[中文](#用法与边界) · [English summary](#english-summary)

PVNW 是一个可移植的 [Agent Skill](https://agentskills.io/)，帮助 AI 在**每项任务开始时判断是否值得维护过程笔记**，但不会把每项任务默认写入。它要求过程记录最终服务于用户原来的问题：实事求是地辨认证据与未验证点，跳出不合适的模板重新建模，并将判断落实到可观察的回答或行动。

> **重要：**开源的是 Skill 源码，不是宿主自动启用机制。仓库存在、格式检查通过、有人手动读取，均不证明任何客户端会逐任务自动触发或保证记录效果。

## 用法与边界

1. 阅读 [pvnw/SKILL.md](pvnw/SKILL.md)，需要时再打开其指向的六份 [references](pvnw/references/)；不要把整份仓库复制进任务上下文。单独分发 `pvnw/` bundle 时保留随附的 [bundle LICENSE](pvnw/LICENSE)，不得仅复制 SKILL.md 丢失版权／许可声明。
2. 若你有兼容 Agent Skills 的客户端，可**自行**按该客户端文档将完整 `pvnw/` bundle 安装或提供给它。不同客户端的发现路径、调用时机和权限不同；本仓库不替你修改宿主设置，尚未验证任何客户端的默认加载。安装后的逐任务判断需要在目标宿主用真实任务手工确认。
3. 任务里可以直接提出：“先按 PVNW 判断是否留痕；优先回答我的原问题，本任务不允许写入。”若没有获授权的写入目标，应该只答问题并说明未持久化，而不是自建工作区。
4. 当前发行版无脚本运行依赖，也不需要 API Key；只有开发时的离线静态测试需要 Python 3 标准库。真实写入取决于用户授权、宿主工具权限与目标仓库规则。

### 一个合成场景（不是模型实测）

> 输入：“解释一段命令对文件的影响；这是一次性咨询，不要记录。”
>
> 预期：“解释文件影响和风险；当前任务不建立笔记、目录或 Git commit，说明未持久化。”

若新证据需要长期回查，但用户未指定获授权位置：先尽可能回答原问题，请有权者选择 Vault 或普通文档目录；未选择前不新建。更多反例见 [acceptance-cases](pvnw/references/acceptance-cases.md)。

## 源码与权限

```text
pvnw/                       # 独立仓库根
├── pvnw/
│   ├── SKILL.md            # 唯一技能入口；name 与 bundle 目录同名
│   ├── references/         # 六份按需读取的判断与验收资料
│   └── LICENSE             # 随 bundle 分发的 MIT 声明，不是第七份行为引用
├── tests/                  # 仅项目离线静态检查，不属于 Skill bundle
├── .github/workflows/      # 仓库 CI，不控制目标客户端
├── AGENTS.md               # 贡献者代理协作规则，不是 Skill 入口
├── CONTRIBUTING.md
├── CHANGELOG.md
└── LICENSE                 # MIT 授权，复制 bundle 时也应保留许可告知
```

- **默认判断≠默认写入。** 首次无授权位置先问；独立一次性咨询可以不留记录；含身份、凭据或原始敏感聊天的内容不得进入公开仓库。
- 收件线索只在**唯一已授权且安全可写的目标**下考虑，并须另有相应目录和操作权限。仓库绝非任务收件箱。
- Git 提交、远端公开和宿主安装都是独立操作授权；Skill 指令不能自行授予这些权限。
- 公开讨论/Issues/PR 也不能附个人数据、真实客户材料或凭据。如遇疑似秘密泄露，不要贴完整值；按 GitHub 私下安全渠道联系维护者并及时撤销相关凭据。

## 验证、发布与限制

```sh
python3 -m unittest discover -s tests -v
```

本地和 CI 运行上述**静态仓库测试**：检查结构、链接、frontmatter 与合成反例中的安全边界。它不会调用模型，不测试宿主是否发现、每项任务是否启动、是否恰当回答真实问题。可选地在**已有** `skills-ref` 的环境运行 `skills-ref validate ./pvnw` 核查官方格式；本项目不自动安装依赖，也不把外部工具通过当成行为验收。

版本用 [SemVer 2.0.0](https://semver.org/spec/v2.0.0.html) 的 `v0.x.y` 起步；公开契约是技能入口、bundle 布局、必要引用和写入前安全判断，详见 [CHANGELOG.md](CHANGELOG.md)。本阶段不承诺任何目标客户端或跨会话退出机制兼容。协作方式见 [CONTRIBUTING.md](CONTRIBUTING.md)；开发代理的约定见 [AGENTS.md](AGENTS.md)。

## English summary

PVNW is a portable Agent Skill for **deciding whether process notes are worth keeping at the start of an AI task**, while prioritizing the user's original objective. It does **not** write by default, grant file/Git permissions, or install itself in any host. Read [the skill entry](pvnw/SKILL.md) and its six on-demand references. Source validation is static only; host activation and real-world effectiveness remain unverified. The docs and skill instructions are currently written in Chinese; contributions and safe, synthetic feedback are welcome under [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT; see [LICENSE](LICENSE). Third-party repositories linked for research are not included or relicensed here.
