---
name: pvnw
description: Progressive Vibe Notes Writing (PVNW), a project-management documentation skill. When invoked or enabled by a host, assess each visible AI task without writing by default; answer the original question first. For authorized work, create or maintain portable project overviews, assessable milestones, WBS work packages, and evidence-backed execution history in Obsidian or Markdown, or safely reorganize old docs. 宿主启用后逐任务判断；获权管理项目文档，不默认落盘。
license: MIT
---

# PVNW — Progressive Vibe Notes Writing

PVNW 是**原任务的判断层**，不是要求把每次对话写成笔记的任务生成器。宿主需要自行发现或启用本 Skill；此文件**不能**使任一客户端自动加载、跨会话记住退出、获得写权限或保证实际效果。

## 每项任务先判断，不自动写

1. **先辨认出口：**用户原本要解决什么、怎样算回答了？先做原任务；不要让建档流程抢占它。只需在任务开始时做轻量 PVNW 判断；细则见 [decision-gates](references/decision-gates.md)。
2. **尊重退出：**用户明确“不启动／不记录”时，按指定范围退出；未指明范围仅限当前独立任务，不为退出单独造记录。跨会话、长期退出若无可验证的宿主记忆，不能承诺持续有效。
3. **决定是否值得留痕：**有影响后续决策的证据、纠偏、人的取舍、单目标现状或跨目标关系才考虑记录。一次无后续价值的独立咨询，合法结果是只回答并说明未持久化。不要为了形成笔记而发明第二个问题。
4. **明确建立或重组项目文档体系要交付项目管理结构：**按 [routes-and-lifecycle](references/routes-and-lifecycle.md) 的新专题／既有维护分支操作；优先使用**有权者选定的唯一授权位置**，无位置或有冲突则先确认，绝不因本机有 Vault 覆盖用户已选的普通 Markdown 目录。以 `.md` 和相对链接为基线。明确授权完整建系且有真实目标及可安全引用的过程／既有依据时，即便单目标也交付根导航→目标现状→可回查证据；缺权限或依据就报告不完整，不造空篇。旧库重构先只读盘点、旧→新映射和可验证恢复点，获准后分批验证及回滚；创建、各层修改、移动／删除、Git、公开与安装各自核权。项目文档的命名／目录／WBS／生命周期合同见 [project-system](references/project-system.md)。
5. **安全先行：**每次实际写入前检查内容、文件名、相对链接和 Git 扩散风险。仅有唯一获授权、安全可写目标且归属暂未定时，才**考虑**目标内最小安全收件线索；不是自动授权。见 [safe-inbox](references/safe-inbox.md) 与 [provenance-and-permissions](references/provenance-and-permissions.md)。
6. **项目管理对象不同，逐级可读：**宏观根管项目范围、目标状态／依赖及导航；中观 `N-0` 管可独立终止的目标、阶段、节点判据及 WBS 工作分解；微观 `N-1…` 管独立问题的安全来源、执行观察与纠偏。`N.W1` 工作项不是 `N-1` 文件、可评估节点或新目标。WBS 只在有管理价值且获权时建立，完成任务不等于节点通过，AI 的判断不等于人的冻结。采用过程篇→摘要链时，过程篇每次变更都在同一逻辑变更跟进摘要进展或入口；WBS 行交付计划／依赖／行动者／状态／证据等实变才更新它，根仅在项目范围／全局风险或待决策、目标状态／关系或导航实变时更新。各层授权独立核查，写前预检项目要求同步的层级；逐跳验证根→目标→WBS／安全证据及反向入口。**不是每项任务强制创建三份文件。**见 [note-modeling](references/note-modeling.md)。
7. **最后回到出口：**先回答原问题，明确做了什么、没做什么、哪些是人的决定、AI 推断、实际验证与未验证；若未落盘就直说，不宣称跨宿主已经触发。用 [acceptance-cases](references/acceptance-cases.md) 核查纸面反例。

## 原则是推理，不是打勾

- **实事求是：**区分材料、人的决定、AI 推断与本机实测；不足以回答原问题时说不确定，不把“字段齐全”当真相。
- **解放思想：**对问题的隐含假设给出有依据的替代模型，并用反例检查；不把现成模板或宿主习惯当天然正确。
- **知行合一：**提出能回应原问题的下一步、实际执行与观察结果；不能执行或验证时标清边界，而不是只报告流程通过。

> [!NOTE]
> 本仓库提供的是可移植的指令，不携带自动触发器、宿主配置或隐式文件写入。项目开发者的 `AGENTS.md` 不是本 Skill 的启动入口。
