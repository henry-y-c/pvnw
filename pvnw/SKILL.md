---
name: pvnw
description: Progressive Vibe Notes Writing (PVNW), a project-management documentation skill. When invoked or enabled by a host, assess each visible AI task without writing by default; answer the original question first. For authorized work, create or maintain portable project overviews, assessable milestones, WBS work packages, and evidence-backed execution history in Obsidian or Markdown, or safely reorganize old docs. 宿主启用后逐任务判断；获权管理项目文档，不默认落盘。
license: MIT
---

# PVNW — Progressive Vibe Notes Writing

1. **定位**：PVNW 是原任务的判断层，不是要求把每次对话写成笔记的任务生成器。
2. **宿主边界**：客户端须自行发现或启用本 Skill；此文件不能让任一客户端自动加载、跨会话记住退出、获得写权限或保证实际效果。

## 每项任务先判断，不自动写

1. **先辨认出口**：用户原本要解决什么、怎样算回答了？先做原任务；不要让建档流程抢占它。只需在任务开始时做轻量 PVNW 判断；细则见 [decision-gates](references/decision-gates.md)。
2. **尊重退出**：用户明确“不启动／不记录”时，按指定范围退出；未指明范围仅限当前独立任务，不为退出单独造记录。跨会话、长期退出若无可验证的宿主记忆，不能承诺持续有效。
3. **先核已有专题的增量，再判一次性咨询**：当前问题明确属于获权的既有工作包时，比较本轮可核实的新观察、纠偏或人的取舍与已落盘证据；即使结论／里程碑状态未变，只要会影响后续判断，就按既有维护路由续记过程并同步必要摘要，不因用户只问“怎么办”而漏写。没有新事实或后续价值的独立咨询，只回答并说明未持久化；不要为留痕发明第二个问题。先核写权，价值不等于许可。
4. **明确建立或重组项目文档体系要交付项目管理结构**：按 [routes-and-lifecycle](references/routes-and-lifecycle.md) 的新专题／既有维护分支操作；优先使用**有权者选定的唯一授权位置**，无位置或有冲突则先确认，绝不因本机有 Vault 覆盖用户已选的普通 Markdown 目录。以 `.md` 和相对链接为基线。明确授权完整建系且有真实目标及可安全引用的过程／既有依据时，即便单目标也交付根导航→目标现状→可回查证据；缺权限或依据就报告不完整，不造空篇。旧库重构先只读盘点、旧→新映射和可验证恢复点，获准后分批验证及回滚；创建、各层修改、移动／删除、Git、公开与安装各自核权。项目文档的命名／目录／WBS／生命周期合同见 [project-system](references/project-system.md)。
5. **安全与持续授权**：每次实际写入前检查内容、文件名、相对链接和 Git 扩散风险。持续维护权须有当前明确指令或可核实的适用项目规则，限定专题、现有文件及可做的非破坏性动作；一次建系同意不自动延续为跨任务写权，也不授权新文件、搬删、Git 或安装。无权时说明拟续记范围并请人确认；本任务禁止记录优先。仅有唯一获授权、安全可写目标且归属暂未定时，才**考虑**目标内最小安全收件线索；不是自动授权。见 [safe-inbox](references/safe-inbox.md) 与 [provenance-and-permissions](references/provenance-and-permissions.md)。
6. **项目管理三层与统一写法**：获权新建时宏观 macro 根 `0_<name>.md` 管项目导航；中观 meso 里程碑 `N_<dir name>/N.0_<name>.md` 管目标／节点／工作包入口；同目录 `N.1_<name>.md`、`N.2_<name>.md`… 各为一个微观 micro WBS 工作包，**篇内按真实先后记录该包整个执行过程**。不再用 v0.4.0 的 `N.W1` 与 `N-1` 分离模型；已有项目不自动改名。整个 Skill 的 Markdown 和获权新笔记都按**清单体笔记**组织：一维用四空格缩进的嵌套有序列表；多对象×稳定字段才用局部管道表格，同格多项就地以 `1. …<br>2. …` 视觉编号；不强套表格或空栏目。加粗标签用 `**标签**：正文`，交付前检查受影响 Markdown 的裸露星号；能访问目标阅读器则抽查显示，否则标渲染未验证，不把标点包进加粗后紧贴汉字。工作包完成不等于节点通过，AI 判断不等于人的冻结。采用 micro→摘要链时，每次工作包篇变更都在同一逻辑变更跟进摘要进展或入口；根仅在项目范围／全局风险或待决策、目标状态／关系或导航实变时更新。写前预检各层独立授权，逐级核根→目标→工作包／安全证据及反向入口。**不是每项任务强制创建三份文件**。见 [project-system](references/project-system.md) 与 [note-modeling](references/note-modeling.md)。
7. **Git 收尾**：获授权的文档进度批次完成后，主动判断本地提交：WBS 状态／证据／依赖实变须连同摘要同步，里程碑节点推进／复评须连同获权上层入口核验；小修正并入本轮逻辑批次，不逐行提交。仅在项目规则或本次指令明确授权本地 commit、且没有当前禁令时，核拟提交快照、安全与既有暂存后限范围提交；无本地提交授权就请人确认，明确禁止 commit 才不提交；仅禁止 push 不挡获权本地 commit，始终不自动 push。细则见 [provenance-and-permissions](references/provenance-and-permissions.md)。
8. **最后回到出口**：先回答原问题，明确做了什么、没做什么、哪些是人的决定、AI 推断、实际验证与未验证；若未落盘就直说，涉及 Git 再报告提交与剩余改动，不宣称跨宿主已经触发。用 [acceptance-cases](references/acceptance-cases.md) 核查纸面反例。

## 原则是推理，不是打勾

1. **实事求是**：区分材料、人的决定、AI 推断与本机实测；不足以回答原问题时说不确定，不把“字段齐全”当真相。
2. **解放思想**：对问题的隐含假设给出有依据的替代模型，并用反例检查；不把现成模板或宿主习惯当天然正确。
3. **知行合一**：提出能回应原问题的下一步、实际执行与观察结果；不能执行或验证时标清边界，而不是只报告流程通过。

> [!NOTE]
> 本仓库提供的是可移植的指令，不携带自动触发器、宿主配置或隐式文件写入。项目开发者的 `AGENTS.md` 不是本 Skill 的启动入口。
