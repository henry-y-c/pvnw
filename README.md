# PVNW — Progressive Vibe Notes Writing

[中文](#用法与边界) · [English summary](#english-summary)

PVNW 是一个可移植的**项目管理文档** [Agent Skill](https://agentskills.io/)：帮助 AI 在**每项任务开始时判断是否值得留痕**，但不默认落盘。明确委托且获授权时，它管理项目顶层范围／目标地图、可独立确认或终止的里程碑、里程碑内的 micro WBS 工作包（同篇保存整个执行过程）；可以从零建系或只读盘点后安全重构旧资料。**宏观→中观→微观是阅读与更新职责**，不是每项任务必建三个目录或四种路由；WBS 不是强制第四层。人已选的授权 Markdown 目录与 Vault 一样有效。最终记录必须帮助回答原问题，并标明实际证据与未验证边界。

> **重要：**开源的是 Skill 源码，不是宿主自动启用机制。仓库存在、格式检查通过、有人手动读取，均不证明任何客户端会逐任务自动触发或保证记录效果。

## 用法与边界

1. 阅读 [pvnw/SKILL.md](pvnw/SKILL.md)，需要时再打开其指向的七份 [references](pvnw/references/)；不要把整份仓库复制进任务上下文。单独分发 `pvnw/` bundle 时保留随附的 [bundle LICENSE](pvnw/LICENSE)，不得仅复制 SKILL.md 丢失版权／许可声明。
2. 若你有兼容 Agent Skills 的客户端，可**自行**按该客户端文档将完整 `pvnw/` bundle 安装或提供给它。不同客户端的发现路径、调用时机和权限不同；本仓库不替你修改宿主设置，尚未验证任何客户端的默认加载。安装后的逐任务判断需要在目标宿主用真实任务手工确认。
3. 任务里可以直接提出：“先按 PVNW 判断是否留痕；优先回答我的原问题，本任务不允许写入。”也可以在**明确路径和操作授权**下委托：“请在这个已有 Vault／这个普通 Markdown 目录，从零建立项目总览、一个真实里程碑及可回查过程。”或“先只读盘点旧文档、画旧→新映射；获准改动后才分批重构”。若没有获授权写入目标，只答可答问题并说明未持久化，而不是自建工作区。
4. 无脚本运行依赖，也不需要 API Key；只有开发时的离线静态测试需要 Python 3 标准库。建系以 `.md`、相对 Markdown 链接和实际项目约定为基线，不要求安装 Obsidian 插件／Git、配置 `.obsidian` 或先造空过程篇才能有目标摘要；节点是可评估门槛，按实际证据复评而非按耗时任务分号。micro 工作包篇更新且项目采用 micro→摘要链，须跟进 `N.0` 的进展／入口；每包按 Markdown 清单体在同篇连续记交付计划、依赖、真实动作、观察、纠偏、行动者、状态和未验证项，根导航只在项目范围／全局风险或待决策、目标状态／跨目标关系／入口实变时改。建系默认的命名、目录、编号、WBS 及生命周期决策见 [project-system](pvnw/references/project-system.md)：目标项目已有约定优先，不强制迁库。真实写入、跨目录重构、Git 与公开各取决于独立授权、宿主工具权限及目标项目规则。

### 一个合成场景（不是模型实测）

> 输入：“解释一段命令对文件的影响；这是一次性咨询，不要记录。”
>
> 预期：“解释文件影响和风险；当前任务不建立笔记、目录或 Git commit，说明未持久化。”

若新证据需要长期回查，但用户未指定获授权位置：先尽可能回答原问题，请有权者选择**获准的已有 Vault 或普通文档目录**；未选择前不新建。明确获准建系且已有安全过程材料时，即便只有一个目标，也交付并逐跳验证宏总览→中目标／节点→micro 工作包全过程／依据；缺证据／权限要报告链路未闭合，不靠空模板凑数。重构旧库先只读盘点、标明人工决定、旧入口与回退条件，移动／删除／备份及失败时逆操作另需许可；无可验证恢复点不做破坏性迁移。更多反例见 [acceptance-cases](pvnw/references/acceptance-cases.md)。

### 可阅读的最小项目模型（合成规划，非运行结果）

```text
<已选且获权的文档根>/
  0_项目总览.md                 # macro 项目范围、目标状态/依赖与入口
  1_恢复演练/
    1.0_当前判断.md             # meso 目标、下一节点、micro 包入口/依赖
    1.1_样本校验.md             # micro 工作包 1.1 的整个执行过程
    1.2_隔离恢复.md             # micro 工作包 1.2 的整个执行过程
```

1. **宏观与中观：**根写“恢复演练：进行中，隔离恢复未通过”并链接 `1.0`；摘要写节点判据“隔离恢复可复现”，索引工作包 `1.1` 校验样本（进行中）、`1.2` 隔离恢复（受阻，依赖 `1.1`），标证据或缺口与可达入口。
2. **微观全过程：**每个 `N.1_<name>.md` 本身就是该 WBS 工作包记录，不再把 `N.W1` 计划 ID 与 `N-1` 问题日志分离。用有序 Markdown 清单依次写原问题、安全来源、计划、真实动作、观察、纠偏及复验；从篇内回链 `N.0`。一维内容四空格嵌套，多对象 × 稳定字段才用局部 Markdown 管道表，格内多项就地编号 `1. …<br>2. …`（仅视觉编号，渲染未验证）。**整个 Skill 的 Markdown 正文也遵循这套清单体写法**，章节标题／必要短提示／代码样本作为辅助，不让表格或空栏目取代主干。
3. **边界：**工作包完成不自动表示节点通过或人的冻结；既有项目文件名、WBS 系统优先，不自动迁移。旧 `N.W1`／`N-1` 与新 `N.1` 不能按数字一对一批量映射；改名需另授权，先核旧→新路径／ID 映射、人工编辑、入链及恢复点。没有真实工作包就不建空篇。

## 源码与权限

```text
pvnw/                       # 独立仓库根
├── pvnw/
│   ├── SKILL.md            # 唯一技能入口；name 与 bundle 目录同名
│   ├── references/         # 七份按需读取；新增 project-system.md 管项目模型
│   └── LICENSE             # 随 bundle 分发的 MIT 声明，不是第八份行为引用
├── tests/                  # 仅项目离线静态检查，不属于 Skill bundle
├── .github/workflows/      # 仓库 CI，不控制目标客户端
├── AGENTS.md               # 贡献者代理协作规则，不是 Skill 入口
├── CONTRIBUTING.md
├── CHANGELOG.md
└── LICENSE                 # MIT 授权，复制 bundle 时也应保留许可告知
```

1. **默认判断≠默认写入。** 首次无授权位置先问；独立一次性咨询可以不留记录；含身份、凭据或原始敏感聊天的内容不得进入公开仓库。
2. 收件线索只在**唯一已授权且安全可写的目标**下考虑，并须另有相应目录和操作权限。仓库绝非任务收件箱。
3. micro 工作包篇、meso 目标摘要、macro 地图、建目录、已有文件搬移／删除、备份、Git 提交、远端公开和宿主安装都是各自独立的操作授权；Skill 指令不能自行授予这些权限。无权更新上层时说明未同步；项目要求原子同步却无法获权时暂缓写入；不得以迁移或收件箱绕过。
4. 公开讨论/Issues/PR 也不能附个人数据、真实客户材料或凭据。如遇疑似秘密泄露，不要贴完整值；按 GitHub 私下安全渠道联系维护者并及时撤销相关凭据。

## 验证、发布与限制

```sh
python3 -m unittest discover -s tests -v
```

本地和 CI 运行上述**静态仓库测试**：检查结构、链接、frontmatter、合成的目录／WBS 导航反例与安全边界，包括授权建系／重构的**文字契约**。它不会调用模型，不测试宿主是否发现、每项任务是否启动、是否正确创建或迁移目录、Obsidian 渲染和是否恰当回答真实问题。可在隔离的合成目录按 [验收场景](pvnw/references/acceptance-cases.md) 进行**单独记录的人工宿主实测**；未执行不可宣称通过。可选地在**已有** `skills-ref` 的环境运行 `skills-ref validate ./pvnw` 核查官方格式；本项目不自动安装依赖，也不把外部工具通过当成行为验收。

版本用 [SemVer 2.0.0](https://semver.org/spec/v2.0.0.html) 的 `v0.x.y` 起步；公开契约是技能入口、bundle 布局、必要引用和写入前安全判断，详见 [CHANGELOG.md](CHANGELOG.md)。本阶段不承诺任何目标客户端或跨会话退出机制兼容。协作方式见 [CONTRIBUTING.md](CONTRIBUTING.md)；开发代理的约定见 [AGENTS.md](AGENTS.md)。

## English summary

PVNW is a portable project-management documentation Agent Skill: it **judges whether an AI task merits persistent notes without writing by default**. With explicit authorization it can bootstrap or safely reorganize project overviews, independently assessable milestones, optional milestone-local WBS deliverables/work packages, and evidence-backed execution histories in an existing Obsidian vault or Markdown directory. For new authorized projects, `0_<name>.md` links `N_<name>/N.0_<name>.md` and micro WBS files `N.1_<name>.md` etc.; each work-package file contains its entire execution history in ordered Markdown list-note form. Existing project IDs and filenames remain in place unless migration is separately authorized. Completing tasks does not prove a checkpoint or authorize a human freeze. These are reading and maintenance roles, not mandatory folders or a second project-management system; existing project conventions take precedence. It does **not** grant file/Git permissions or install itself in any host. Read [the skill entry](pvnw/SKILL.md) and its seven on-demand references, including [the project-system contract](pvnw/references/project-system.md). Source validation is static only; host activation and real-world effectiveness remain unverified. The docs and skill instructions are currently written in Chinese; contributions and safe, synthetic feedback are welcome under [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT; see [LICENSE](LICENSE). Third-party repositories linked for research are not included or relicensed here.
