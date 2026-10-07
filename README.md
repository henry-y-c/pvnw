# PVNW — Progressive Vibe Notes Writing

[中文](#用法与边界) · [English summary](#english-summary)

PVNW 是一个可移植的**项目管理文档** [Agent Skill](https://agentskills.io/)：目标是宿主在**每项任务开始、搜索／执行前调用**，先区分可靠直接可答的简单问题与需查证、比较、分解或多步行动的思考型任务；后者原则上值得留痕，但未经授权不落盘。获当前指令或工作空间可见托管策略授权时，它管理项目顶层范围／目标地图、可独立确认或终止的里程碑、里程碑内的 micro WBS 工作包（同篇边做边记整个过程）；可以从零建系或只读盘点后安全重构旧资料。**宏观→中观→微观是阅读与更新职责**，不是每项任务必建三个目录或四种路由；WBS 不是强制第四层。人已选的授权 Markdown 目录与 Vault 一样有效。最终记录必须帮助回答原问题，并标明实际证据与未验证边界。

> **重要**：开源的是 Skill 源码，不是宿主自动启用机制。仓库存在、格式检查通过、有人手动读取，均不证明任何客户端会逐任务自动触发或保证记录效果。

## 用法与边界

1. 阅读 [pvnw/SKILL.md](pvnw/SKILL.md)，需要时再打开其指向的七份 [references](pvnw/references/)；不要把整份仓库复制进任务上下文。单独分发 `pvnw/` bundle 时保留随附的 [bundle LICENSE](pvnw/LICENSE)，不得仅复制 SKILL.md 丢失版权／许可声明。
2. **宿主入口是独立实现**：为每个真实用户任务在搜索／执行前可靠注入 Skill 全文，需要目标宿主显式配置和逐任务实测。仓库里的描述或模型可选的 Skill 目录不能保证它会调用；不同客户端机制不同，本 bundle 不自行改宿主、不保证已安装版本自动启用。
3. 可对工作空间作限定授权：“先核本空间已有获权 Vault；无 Vault 时在指定位置建 Obsidian 兼容 Markdown 文件夹。允许创建专题根、当前目标摘要和工作包篇并持续更新；是否允许本地 commit 单独声明。”研究前先写真实问题、计划和未执行状态，执行中逐步追加结果。也可以委托仅只读盘点旧文档；若没有唯一获授权目标、托管策略或写入权，仍尽可能回答原题并报告未持久化。
4. 无脚本运行依赖，也不需要 API Key；只有开发时的离线静态测试需要 Python 3 标准库。Vault 的兼容基线是文件夹中的 `.md` 与相对 Markdown 链接；不要求安装 Obsidian 插件／Git、配置 `.obsidian`，也不自动 git init。获得托管建系权且有真实当前工作包时先建计划篇再研究；只有既有安全依据而无确需跟踪工作包时，不造空过程篇。节点是可评估门槛，不按耗时任务分号。micro 工作包篇更新且项目采用 micro→摘要链，须跟进 `N.0` 的进展／入口；每包按 Markdown 清单体在同篇连续记交付计划、依赖、真实动作、观察、纠偏、行动者、状态和未验证项，根导航只在项目范围／全局风险或待决策、目标状态／跨目标关系／入口实变时改。建系默认的命名、目录、编号、WBS 及生命周期决策见 [project-system](pvnw/references/project-system.md)：目标项目已有约定优先，不强制迁库。真实写入、跨目录重构、Git 与公开各取决于独立授权、宿主工具权限及目标项目规则。

### 一个合成场景（不是模型实测）

> 输入：“解释一段命令对文件的影响；这是一次性咨询，不要记录。”
>
> 预期：“解释文件影响和风险；当前任务不建立笔记、目录或 Git commit，说明未持久化。”

思考型研究先只读定位适用的既有专题和获权 Vault；无 Vault 但当前工作空间已有明确托管策略，指定唯一位置并授权目录／分层文件写入时才在此处建 Obsidian 兼容文件夹；既有获权 Vault 不另造。无授权位置则请有权者选择，未选择前不新建，仍尽可能答原题。获准且有真实可检验目标与首包交付时，先建有问题、计划和未执行状态的宏总览→中目标／节点→micro 工作包入口，研究中追加可观察结果；缺证据／权限要报告链路未闭合，不靠空模板凑数。重构旧库先只读盘点、标明人工决定、旧入口与回退条件，移动／删除／备份及失败时逆操作另需许可；无可验证恢复点不做破坏性迁移。更多反例见 [acceptance-cases](pvnw/references/acceptance-cases.md)。

### 可阅读的最小项目模型（合成规划，非运行结果）

```text
<已选且获权的文档根>/
  0_项目总览.md                 # macro 项目范围、目标状态/依赖与入口
  1_恢复演练/
    1.0_当前判断.md             # meso 目标、下一节点、micro 包入口/依赖
    1.1_样本校验.md             # micro 工作包 1.1 的整个执行过程
    1.2_隔离恢复.md             # micro 工作包 1.2 的整个执行过程
```

1. **宏观与中观**：根写“恢复演练：进行中，隔离恢复未通过”并链接 `1.0`；摘要写节点判据“隔离恢复可复现”，索引工作包 `1.1` 校验样本（进行中）、`1.2` 隔离恢复（受阻，依赖 `1.1`），标证据或缺口与可达入口。
2. **微观全过程**：每个 `N.1_<name>.md` 本身就是该 WBS 工作包记录，不再把 `N.W1` 计划 ID 与 `N-1` 问题日志分离。用有序 Markdown 清单依次写原问题、安全来源、计划、真实动作、观察、纠偏及复验；从篇内回链 `N.0`。一维内容四空格嵌套，多对象 × 稳定字段才用局部 Markdown 管道表，格内多项就地编号 `1. …<br>2. …`（仅视觉编号，渲染未验证）。**整个 Skill 的 Markdown 正文也遵循这套清单体写法**，章节标题／必要短提示／代码样本作为辅助，不让表格或空栏目取代主干。
3. **边界**：工作包完成不自动表示节点通过或人的冻结；既有项目文件名、WBS 系统优先，不自动迁移。旧 `N.W1`／`N-1` 与新 `N.1` 不能按数字一对一批量映射；改名需另授权，先核旧→新路径／ID 映射、人工编辑、入链及恢复点。没有真实工作包就不建空篇。

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

1. **默认判断≠默认写入。** 宿主应在每项用户任务前调用 PVNW；直接可答的简单咨询可只答，需思考的查证／比较任务原则上先核留痕位置。明确关联已获维护授权的既有工作包时，先对照记录，执行中每个安全可观察动作依次记入原篇并同步必要摘要，即使结论未变。首次值得留痕却无授权位置或可见托管策略时才询问位置／写权，简单咨询不为建档提问；一次建系同意不等于跨任务持续写权，明确托管策略须限定位置、创建／维护范围，可撤销且本任务不记录优先。仅复述已知或未执行的新建议不造过程；含身份、凭据或原始敏感聊天的内容不得进入公开仓库。
2. 收件线索只在**唯一已授权且安全可写的目标**下考虑，并须另有相应目录和操作权限。仓库绝非任务收件箱。
3. micro 工作包篇、meso 目标摘要、macro 地图、建目录、已有文件搬移／删除、备份、Git 提交、远端公开和宿主安装都是各自独立的操作授权；Skill 指令不能自行授予这些权限。无权更新上层时说明未同步；项目要求原子同步却无法获权时暂缓写入；不得以迁移或收件箱绕过。每完成一个有可核验证据或受阻出口的 WBS，若已有 Git 且获本地提交授权，先核过程／摘要和拟提交快照再限范围做一次本地 commit；研究中的各动作要记在同一包，但不逐动作 commit。里程碑节点推进／复评连同必要上层入口另成完整批次；小修正按任务批次合并，不逐行提交。无提交授权则问，当前任务明令不提交则停；仅禁止 push 不挡已获权本地提交，但始终不自动 push；详见 [provenance-and-permissions](pvnw/references/provenance-and-permissions.md)。
4. 新写／修改的 Markdown 加粗标签用 `**标签**：正文`，不要把中文标点放在加粗内部后紧贴正文；交付前检查受影响稿的裸露星号；能访问目标阅读器时抽查，否则标渲染未验证。仅规则及源码静态测试不能保证已安装的任何客户端渲染正确；旧文档无改写权时不批量修复。见 [note-modeling](pvnw/references/note-modeling.md)。
5. 公开讨论/Issues/PR 也不能附个人数据、真实客户材料或凭据。如遇疑似秘密泄露，不要贴完整值；按 GitHub 私下安全渠道联系维护者并及时撤销相关凭据。

## 验证、发布与限制

```sh
python3 -m unittest discover -s tests -v
```

本地和 CI 运行上述**静态仓库测试**：检查结构、链接、frontmatter、合成的目录／WBS 导航反例与安全边界，包括研究前计划、托管建 Vault 和逐包 Git 的**文字契约**。它不会调用模型，不测试宿主是否发现、每项任务是否启动、是否正确创建或迁移目录、Obsidian 渲染和是否恰当回答真实问题。可在隔离的合成目录按 [验收场景](pvnw/references/acceptance-cases.md) 进行**单独记录的人工宿主实测**；未执行不可宣称通过。可选地在**已有** `skills-ref` 的环境运行 `skills-ref validate ./pvnw` 核查官方格式；本项目不自动安装依赖，也不把外部工具通过当成行为验收。

版本用 [SemVer 2.0.0](https://semver.org/spec/v2.0.0.html) 的 `v0.x.y` 起步；公开契约是技能入口、bundle 布局、必要引用和写入前安全判断，详见 [CHANGELOG.md](CHANGELOG.md)。本阶段不承诺任何目标客户端或跨会话退出机制兼容。协作方式见 [CONTRIBUTING.md](CONTRIBUTING.md)；开发代理的约定见 [AGENTS.md](AGENTS.md)。

## English summary

PVNW is a portable project-management documentation Agent Skill. Host integration should invoke it before each user task; directly answerable questions may need no note, while questions requiring research, comparison or multi-step reasoning generally merit one, **without implicit write permission**. Under explicit, scoped workspace authorization it can reuse an existing authorized vault or create an Obsidian-compatible Markdown folder at an agreed unique location, then bootstrap or safely reorganize project overviews, independently assessable milestones, milestone-local WBS deliverables/work packages, and evidence-backed execution histories. For new authorized projects, `0_<name>.md` links `N_<name>/N.0_<name>.md` and micro WBS files `N.1_<name>.md` etc.; each work-package file contains its entire execution history in ordered Markdown list-note form. Existing project IDs and filenames remain in place unless migration is separately authorized. An authorized research project writes an actual problem, plan and unexecuted state before substantive work, logs safe observable actions as they happen, and considers one locally authorized Git commit at each completed or blocked WBS package; no Git initialization or push is implied. Completing tasks does not prove a milestone checkpoint or authorize a human freeze. These are reading and maintenance roles, not mandatory folders for simple questions or a second project-management system; existing project conventions take precedence. It does **not** grant file/Git permissions or install itself in any host. Read [the skill entry](pvnw/SKILL.md) and its seven on-demand references, including [the project-system contract](pvnw/references/project-system.md). Source validation is static only; host activation and real-world effectiveness remain unverified. The docs and skill instructions are currently written in Chinese; contributions and safe, synthetic feedback are welcome under [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT; see [LICENSE](LICENSE). Third-party repositories linked for research are not included or relicensed here.
