---
name: pvnw
description: Progressive Vibe Notes Writing (PVNW). When invoked or enabled by a host, assess each visible AI task; answer the original question first, never write by default. For an authorized request, build or safely reorganize a project documentation system in Obsidian or portable Markdown, with macro navigation, meso milestone evolution and micro evidence-backed notes. 宿主启用后逐任务判断；获授权时建系或重构，而非默认落盘。
license: MIT
---

# PVNW — Progressive Vibe Notes Writing

PVNW 是**原任务的判断层**，不是要求把每次对话写成笔记的任务生成器。宿主需要自行发现或启用本 Skill；此文件**不能**使任一客户端自动加载、跨会话记住退出、获得写权限或保证实际效果。

## 每项任务先判断，不自动写

1. **先辨认出口：**用户原本要解决什么、怎样算回答了？先做原任务；不要让建档流程抢占它。只需在任务开始时做轻量 PVNW 判断；细则见 [decision-gates](references/decision-gates.md)。
2. **尊重退出：**用户明确“不启动／不记录”时，按指定范围退出；未指明范围仅限当前独立任务，不为退出单独造记录。跨会话、长期退出若无可验证的宿主记忆，不能承诺持续有效。
3. **决定是否值得留痕：**有影响后续决策的证据、纠偏、人的取舍、单目标现状或跨目标关系才考虑记录。一次无后续价值的独立咨询，合法结果是只回答并说明未持久化。不要为了形成笔记而发明第二个问题。
4. **明确建系／重构要交付结构，而非只谈职责：**若原任务是建立或重组项目文档体系，按 [routes-and-lifecycle](references/routes-and-lifecycle.md) 的新专题／既有维护分支，先确定唯一获授权的项目位置：可用且获授权的 Obsidian Vault 优先，否则选获授权的普通 Markdown 文件夹；只用可移植 `.md` 与相对链接作基线。完整建系且有真实目标／安全过程材料时，即便单目标也交付宏观导航→里程碑中观摘要→可回查微观问题篇／节；缺材料或权限报告链未闭合，不造空篇。旧库先只读盘点、旧→新映射及可验证恢复点，再按独立许可分批重构、验链接与失败时回滚。首次无已授权目标、位置冲突或仅请求口头方案，不擅建目录／配置 Vault。目录、各层文件、移动／删除、Git、远端公开与宿主安装仍各自核授权。
5. **安全先行：**每次实际写入前检查内容、文件名、相对链接和 Git 扩散风险。仅有唯一获授权、安全可写目标且归属暂未定时，才**考虑**目标内最小安全收件线索；不是自动授权。见 [safe-inbox](references/safe-inbox.md) 与 [provenance-and-permissions](references/provenance-and-permissions.md)。
6. **让三层逐级可读、随节点演化：**获权建立完整体系时，从宏观当前目标状态／依赖及入口，进入中观可独立确认或终止的目标、当前阶段与下一可评估节点，再追到微观原始安全条目、证据、失败／纠偏和回查动作；每跳验证相对链接。关键节点是可判定的门槛，不是耗时任务；按原点假设／目标倒拆／探索正推与失败复盘选下一节点，不以 AI 判定替代人的冻结。它们是可组合的阅读职责，**不是每项任务强制创建三份文件**。采用过程篇／目标摘要结构时，每次过程篇变更要跟进同层摘要的进展或入口，仅判断／边界实变才改结论；宏观在状态、关系或导航实变时才更新。各层创建／修改权限独立核查。见 [routes-and-lifecycle](references/routes-and-lifecycle.md) 与 [note-modeling](references/note-modeling.md)。
7. **最后回到出口：**先回答原问题，明确做了什么、没做什么、哪些是人的决定、AI 推断、实际验证与未验证；若未落盘就直说，不宣称跨宿主已经触发。用 [acceptance-cases](references/acceptance-cases.md) 核查纸面反例。

## 原则是推理，不是打勾

- **实事求是：**区分材料、人的决定、AI 推断与本机实测；不足以回答原问题时说不确定，不把“字段齐全”当真相。
- **解放思想：**对问题的隐含假设给出有依据的替代模型，并用反例检查；不把现成模板或宿主习惯当天然正确。
- **知行合一：**提出能回应原问题的下一步、实际执行与观察结果；不能执行或验证时标清边界，而不是只报告流程通过。

> [!NOTE]
> 本仓库提供的是可移植的指令，不携带自动触发器、宿主配置或隐式文件写入。项目开发者的 `AGENTS.md` 不是本 Skill 的启动入口。
