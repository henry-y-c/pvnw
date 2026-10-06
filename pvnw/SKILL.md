---
name: pvnw
description: Progressive Vibe Notes Writing (PVNW). When explicitly invoked or enabled by a host, assess each visible AI task at its start for process-note value; answer the original question first and never write by default. 宿主启用后逐任务判断，而非默认建档。
license: MIT
---

# PVNW — Progressive Vibe Notes Writing

PVNW 是**原任务的判断层**，不是要求把每次对话写成笔记的任务生成器。宿主需要自行发现或启用本 Skill；此文件**不能**使任一客户端自动加载、跨会话记住退出、获得写权限或保证实际效果。

## 每项任务先判断，不自动写

1. **先辨认出口：**用户原本要解决什么、怎样算回答了？先做原任务；不要让建档流程抢占它。只需在任务开始时做轻量 PVNW 判断；细则见 [decision-gates](references/decision-gates.md)。
2. **尊重退出：**用户明确“不启动／不记录”时，按指定范围退出；未指明范围仅限当前独立任务，不为退出单独造记录。跨会话、长期退出若无可验证的宿主记忆，不能承诺持续有效。
3. **决定是否值得留痕：**有影响后续决策的证据、纠偏、人的取舍或可维护的模型才考虑记录。一次无后续价值的独立咨询，合法结果是只回答并说明未持久化。不要为了形成笔记而发明第二个问题。
4. **定位与权限分开：**若值得记录，区分新专题、已获授权专题的新里程碑、维护既有笔记或暂不写；位置、创建目录、修改现有文件、创建收件区、Git 提交与宿主安装各需各自适用的授权。首次没有获授权目标，先完成可独立回答的原问题，再就确有记录价值的内容请求有权者选位置；不擅建目录。路由见 [routes-and-lifecycle](references/routes-and-lifecycle.md)。
5. **安全先行：**每次实际写入前检查内容、文件名、相对链接和 Git 扩散风险。仅有唯一获授权、安全可写目标且归属暂未定时，才**考虑**目标内最小安全收件线索；不是自动授权。见 [safe-inbox](references/safe-inbox.md) 与 [provenance-and-permissions](references/provenance-and-permissions.md)。
6. **边做边记，仅在该记时：**在记录的任务中，先保存当前问题和可回查的决定／证据／反例，后续纠偏按时间追加；同层摘要跟进实质变化，跨专题导航只在关系改变时改。笔记应帮助回答或改进原问题，而不是制造完成感。写法见 [note-modeling](references/note-modeling.md)。
7. **最后回到出口：**先回答原问题，明确做了什么、没做什么、哪些是人的决定、AI 推断、实际验证与未验证；若未落盘就直说，不宣称跨宿主已经触发。用 [acceptance-cases](references/acceptance-cases.md) 核查纸面反例。

## 原则是推理，不是打勾

- **实事求是：**区分材料、人的决定、AI 推断与本机实测；不足以回答原问题时说不确定，不把“字段齐全”当真相。
- **解放思想：**对问题的隐含假设给出有依据的替代模型，并用反例检查；不把现成模板或宿主习惯当天然正确。
- **知行合一：**提出能回应原问题的下一步、实际执行与观察结果；不能执行或验证时标清边界，而不是只报告流程通过。

> [!NOTE]
> 本仓库提供的是可移植的指令，不携带自动触发器、宿主配置或隐式文件写入。项目开发者的 `AGENTS.md` 不是本 Skill 的启动入口。
