"""Offline source-contract checks. Never an agent/host behavior test."""

from pathlib import Path, PurePosixPath
import posixpath
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
BUNDLE = ROOT / "pvnw"
REFERENCES = (
    "decision-gates.md",
    "routes-and-lifecycle.md",
    "project-system.md",
    "note-modeling.md",
    "safe-inbox.md",
    "provenance-and-permissions.md",
    "acceptance-cases.md",
)
DOCS = (
    ROOT / "README.md",
    ROOT / "AGENTS.md",
    ROOT / "CONTRIBUTING.md",
    ROOT / "CHANGELOG.md",
    BUNDLE / "SKILL.md",
    *(BUNDLE / "references" / name for name in REFERENCES),
)
LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
FRONTMATTER = re.compile(r"\A---\n(?P<fields>.*?)\n---\n", re.DOTALL)


def unsafe_bold_lines(text):
    """Flag risky source syntax; not a Markdown parser or host-rendering test."""
    text = re.sub(r"(?ms)^\s*```.*?^\s*```[^\n]*$", "", text)
    text = re.sub(r"`+[^`\n]*`+", "", text)
    problems = []
    for number, line in enumerate(text.splitlines(), 1):
        if len(re.findall(r"(?<!\\)\*\*", line)) % 2:
            problems.append((number, "unpaired double stars"))
        for match in re.finditer(r"(?<!\\)\*\*([^*\n]+)\*\*", line):
            if match.group(1)[-1] in "：，。；！？" and match.end() < len(line) and not line[match.end()].isspace():
                problems.append((number, "punctuation inside bold next to prose"))
    return problems


def frontmatter(text):
    match = FRONTMATTER.match(text)
    if not match:
        raise ValueError("SKILL.md requires YAML frontmatter")
    fields = {}
    for line in match.group("fields").splitlines():
        if ":" not in line:
            raise ValueError("Only simple one-line frontmatter is supported here")
        key, value = line.split(":", 1)
        if key in fields or not key or not value.strip():
            raise ValueError("Duplicate/empty metadata field: " + key)
        fields[key] = value.strip()
    return fields


def local_links(source, text):
    """Resolve conventional Markdown links inside this repository."""
    # Fenced synthetic examples are templates, not source-repository links.
    text = re.sub(r"(?ms)^\s*```.*?^\s*```[^\n]*$", "", text)
    for target in LINK.findall(text):
        if re.match(r"^[a-z][a-z0-9+.-]*:", target, re.IGNORECASE) or target.startswith("#"):
            continue
        path = (source.parent / target.split("#", 1)[0]).resolve()
        try:
            path.relative_to(ROOT.resolve())
        except ValueError as exc:
            raise ValueError(f"Escaping link: {source.name} -> {target}") from exc
        if not path.exists():
            raise ValueError(f"Missing link: {source.name} -> {target}")


class SourceContract(unittest.TestCase):
    def test_eight_file_bundle(self):
        self.assertEqual(
            {path.name for path in BUNDLE.joinpath("references").iterdir()},
            set(REFERENCES),
        )
        self.assertEqual({path.name for path in BUNDLE.iterdir()}, {"SKILL.md", "references", "LICENSE"})
        self.assertEqual((BUNDLE / "LICENSE").read_bytes(), (ROOT / "LICENSE").read_bytes())
        self.assertTrue(all(path.is_file() for path in DOCS))

    def test_entry_metadata_and_reference_paths(self):
        text = (BUNDLE / "SKILL.md").read_text(encoding="utf-8")
        metadata = frontmatter(text)
        self.assertEqual(metadata["name"], BUNDLE.name)
        self.assertRegex(metadata["name"], r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
        self.assertLessEqual(len(metadata["name"]), 64)
        self.assertLessEqual(len(metadata["description"]), 1024)
        self.assertIn("task", metadata["description"].lower())
        self.assertLess(len(text.splitlines()), 500)
        for name in REFERENCES:
            with self.subTest(name=name):
                self.assertIn(f"references/{name}", text)

    def test_links_and_text_hygiene(self):
        for source in DOCS:
            with self.subTest(source=source.name):
                text = source.read_text(encoding="utf-8")
                self.assertTrue(text.endswith("\n") and not text.endswith("\n\n"))
                self.assertFalse(any(line != line.rstrip() for line in text.splitlines()))
                self.assertNotIn("/Users/", text)
                self.assertNotIn("/home/", text)
                self.assertNotIn("-----BEGIN " + "PRIVATE KEY-----", text)
                local_links(source, text)

    def test_bold_source_boundary_not_renderer(self):
        """Catch known risky syntax in source, without claiming host compatibility."""
        self.assertEqual(unsafe_bold_lines("1. **标签**：正文\n1. `**标签：**正文`\n```md\n1. **标签：**正文\n```"), [])
        self.assertEqual(unsafe_bold_lines("1. **标签：**正文\n2. **未闭合\n3. **一句。**后续"), [
            (1, "punctuation inside bold next to prose"),
            (2, "unpaired double stars"),
            (3, "punctuation inside bold next to prose"),
        ])
        for source in DOCS:
            with self.subTest(source=source.name):
                self.assertEqual(unsafe_bold_lines(source.read_text(encoding="utf-8")), [])

    def test_git_closeout_written_contract_not_host_behavior(self):
        entry = (BUNDLE / "SKILL.md").read_text(encoding="utf-8")
        permissions = (BUNDLE / "references" / "provenance-and-permissions.md").read_text(encoding="utf-8")
        note = (BUNDLE / "references" / "note-modeling.md").read_text(encoding="utf-8")
        cases = (BUNDLE / "references" / "acceptance-cases.md").read_text(encoding="utf-8")
        for phrase in ("WBS 状态", "里程碑节点推进", "无本地提交授权就请人确认", "明确禁止 commit 才不提交", "仅禁止 push 不挡获权本地 commit"):
            self.assertIn(phrase, entry)
        for phrase in ("工作包完成不等于节点通过", "不逐行／逐文件提交", "已有暂存", "拟提交快照", "任务结束", "当前任务明确“不提交”", "仅明确“不推送”", "不替人清空暂存"):
            self.assertIn(phrase, permissions)
        self.assertIn("`**标签**：正文`", note)
        self.assertIn("目标阅读器", note)
        for label in ("AM", "AN", "AO", "AP", "AQ", "AR", "AS"):
            self.assertIn(f"| {label} |", cases)

    def test_existing_topic_continuation_written_contract_not_host_behavior(self):
        """Source wording and in-memory cases; not real model authorization or writes."""
        entry = (BUNDLE / "SKILL.md").read_text(encoding="utf-8")
        gates = (BUNDLE / "references" / "decision-gates.md").read_text(encoding="utf-8")
        routes = (BUNDLE / "references" / "routes-and-lifecycle.md").read_text(encoding="utf-8")
        permissions = (BUNDLE / "references" / "provenance-and-permissions.md").read_text(encoding="utf-8")
        cases = (BUNDLE / "references" / "acceptance-cases.md").read_text(encoding="utf-8")
        for phrase in ("先核已有专题", "里程碑结论", "持续维护或托管建系权", "一次建系同意不自动延续"):
            self.assertIn(phrase, entry)
        for phrase in ("助手在回答问题时自己验证", "状态不变也可有进展", "仅因提到专题名不造记录"):
            self.assertIn(phrase, gates)
        for phrase in ("里程碑结论不变", "现有工作包篇", "进展／入口"):
            self.assertIn(phrase, routes)
        for phrase in ("旧会话助手的自称", "跨会话宿主未呈现旧决定", "一次性建系许可"):
            self.assertIn(phrase, permissions)
        for label in ("AT", "AU", "AV", "AW"):
            self.assertIn(f"| {label} |", cases)

        def expected_route(*, existing, new_evidence, standing_write, current_opt_out):
            if current_opt_out or not new_evidence:
                return "answer only"
            if existing and standing_write:
                return "answer + append process + sync summary"
            return "answer + ask for scoped write permission"

        self.assertEqual(expected_route(existing=True, new_evidence=True, standing_write=True, current_opt_out=False),
                         "answer + append process + sync summary")
        self.assertEqual(expected_route(existing=True, new_evidence=True, standing_write=False, current_opt_out=False),
                         "answer + ask for scoped write permission")
        self.assertEqual(expected_route(existing=True, new_evidence=False, standing_write=True, current_opt_out=False),
                         "answer only")
        self.assertEqual(expected_route(existing=True, new_evidence=True, standing_write=True, current_opt_out=True),
                         "answer only")

    def test_managed_research_written_contract_not_host_activation(self):
        """Assert policy wording and paper cases; never infer actual host dispatch."""
        entry = (BUNDLE / "SKILL.md").read_text(encoding="utf-8")
        gates = (BUNDLE / "references" / "decision-gates.md").read_text(encoding="utf-8")
        routes = (BUNDLE / "references" / "routes-and-lifecycle.md").read_text(encoding="utf-8")
        project = (BUNDLE / "references" / "project-system.md").read_text(encoding="utf-8")
        permissions = (BUNDLE / "references" / "provenance-and-permissions.md").read_text(encoding="utf-8")
        cases = (BUNDLE / "references" / "acceptance-cases.md").read_text(encoding="utf-8")
        for phrase in ("原任务搜索／执行前", "需查证、比较、分解", "先建", "每个安全、可观察的步骤", "不默认创建 `.obsidian`", "不自动 git init"):
            with self.subTest(entry=phrase):
                self.assertIn(phrase, entry)
        for phrase in ("可靠地直接回答", "需查证／比较／分解", "唯一建档位置", "无权时仍尽可能完成原题"):
            with self.subTest(gates=phrase):
                self.assertIn(phrase, gates)
        for phrase in ("先建获权根→摘要→当前包篇", "已有获权 Vault 不另造", "不强制虚构 micro"):
            with self.subTest(routes=phrase):
                self.assertIn(phrase, routes)
        for phrase in ("未执行", "每次搜索", "人确认启动"):
            self.assertIn(phrase, project)
        for phrase in ("托管策略", "不自动 git init", "不逐步／逐行提交", "工作包完成不等于节点通过"):
            self.assertIn(phrase, permissions)
        for label in ("AX", "AY", "AZ", "BA", "BB", "BC"):
            with self.subTest(case=label):
                self.assertIn(f"| {label}.", cases)
        for negative in ("不自建默认 Vault", "不建 `.obsidian`", "不逐动作 commit", "摘要无权"):
            self.assertIn(negative, cases)

    def test_static_safety_and_synthetic_cases(self):
        """Assertions on written policy/fixtures, NOT proof of model compliance."""
        entry = (BUNDLE / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("不自动写", entry)
        self.assertIn("原问题", entry)
        self.assertIn("未验证", entry)
        cases = (BUNDLE / "references" / "acceptance-cases.md").read_text(encoding="utf-8")
        for label in "ABCDEFGHIJKLMNOP":
            with self.subTest(case=label):
                self.assertIn(f"| {label}.", cases)
        for signal in ("无写授权", "唯一获授权", "必须不写", "未验证默认启动"):
            self.assertIn(signal, cases)

    def test_three_view_written_contract_not_runtime_behavior(self):
        """Written guidance and synthetic examples only; not model compliance."""
        entry = (BUNDLE / "SKILL.md").read_text(encoding="utf-8")
        routes = (BUNDLE / "references" / "routes-and-lifecycle.md").read_text(encoding="utf-8")
        modeling = (BUNDLE / "references" / "note-modeling.md").read_text(encoding="utf-8")
        permissions = (BUNDLE / "references" / "provenance-and-permissions.md").read_text(encoding="utf-8")
        cases = (BUNDLE / "references" / "acceptance-cases.md").read_text(encoding="utf-8")
        for text in (entry, routes, modeling):
            with self.subTest(guide=text[:35]):
                for level in ("微观", "中观", "宏观"):
                    self.assertIn(level, text)
        self.assertIn("不是每项任务强制创建三份文件", entry)
        self.assertIn("每次工作包篇变更", routes)
        self.assertIn("进展或入口", routes)
        self.assertIn("状态／关系／导航实变", routes)
        self.assertIn("不强制先造 micro 文件", routes)
        self.assertIn("分别核查", routes)
        self.assertIn("不同于", routes)  # terminated exploration vs invalidated freeze
        self.assertIn("获授权的既有材料", modeling)
        self.assertIn("授权改其中一层不连带", permissions)
        for label in "IJKLMNOP":
            with self.subTest(scenario=label):
                self.assertIn(f"| {label}.", cases)
        self.assertIn("根地图未获写授权", cases)
        self.assertIn("回收号", cases)

    def test_authorized_build_reorganization_written_contract(self):
        """Policy text and synthetic cases only; no agent execution occurs."""
        entry = (BUNDLE / "SKILL.md").read_text(encoding="utf-8")
        routes = (BUNDLE / "references" / "routes-and-lifecycle.md").read_text(encoding="utf-8")
        gates = (BUNDLE / "references" / "decision-gates.md").read_text(encoding="utf-8")
        modeling = (BUNDLE / "references" / "note-modeling.md").read_text(encoding="utf-8")
        permission = (BUNDLE / "references" / "provenance-and-permissions.md").read_text(encoding="utf-8")
        inbox = (BUNDLE / "references" / "safe-inbox.md").read_text(encoding="utf-8")
        cases = (BUNDLE / "references" / "acceptance-cases.md").read_text(encoding="utf-8")
        for phrase in ("托管建系", "重构", "逐级", "不自动写", "人的冻结", "相对链接"):
            with self.subTest(entry=phrase):
                self.assertIn(phrase, entry)
        for phrase in ("空白建系", "旧库重构", "先只读", "旧路径／入口→拟建", "回滚", "评估节点", "不自动冻结", "普通 Markdown", ".obsidian"):
            with self.subTest(routes=phrase):
                self.assertIn(phrase, routes)
        self.assertIn("明确要求且授权实际建系时应执行", gates)
        for phrase in ("宏观", "中观", "微观", "原始安全条目", "来源标识", "纠偏前后", "<br>", "反向返回"):
            with self.subTest(modeling=phrase):
                self.assertIn(phrase, modeling)
        for phrase in ("备份", "旧入口", "拟提交快照", "被明确批准的批次", "凭据"):
            with self.subTest(permission=phrase):
                self.assertIn(phrase, permission)
        self.assertIn("不是旧库重构的备份／搬移暂存区", inbox)
        for label in "QRSTUVWXYZ":
            with self.subTest(scenario=label):
                self.assertIn(f"| {label}.", cases)
        for phrase in ("只授权读取", "纯 Markdown", "坏锚", "密钥", "拟提交快照"):
            self.assertIn(phrase, cases)

    def test_project_management_written_contract_not_runtime_behavior(self):
        """Checks the published written contract, not agent adherence or approvals."""
        entry = (BUNDLE / "SKILL.md").read_text(encoding="utf-8")
        guide = (BUNDLE / "references" / "project-system.md").read_text(encoding="utf-8")
        routes = (BUNDLE / "references" / "routes-and-lifecycle.md").read_text(encoding="utf-8")
        cases = (BUNDLE / "references" / "acceptance-cases.md").read_text(encoding="utf-8")
        self.assertIn("project-system.md", entry)
        self.assertIn("有权者选定的唯一授权位置", entry)
        self.assertIn("micro WBS 工作包", entry)
        for phrase in (
            "0_<name>.md", "N_<dir name>/", "N.0_<name>.md", "N.1_<短名>.md",
            "未编号候选", "不回收", "已选普通 Markdown", "Unicode", "碰撞",
            "旧→新路径／ID 映射", "不能按数字批量替换", "工作包完成不等于节点通过",
            "每次工作包篇更新", "同一逻辑变更", "逆操作", "拟提交快照",
            "四空格", "单元格", "整个 Skill bundle",
        ):
            with self.subTest(policy=phrase):
                self.assertIn(phrase, guide)
        self.assertIn("项目级目录／命名", routes)
        for label in ("AA", "AB", "AC", "AD", "AE", "AF", "AG", "AH", "AI", "AJ", "AK", "AL"):
            with self.subTest(scenario=label):
                self.assertIn(f"| {label}.", cases)
        self.assertIn("from six to seven references", (ROOT / "CHANGELOG.md").read_text(encoding="utf-8"))
        self.assertIn("七份", (ROOT / "README.md").read_text(encoding="utf-8"))

    def test_pre_research_plan_and_stepwise_history_fixture(self):
        """An in-memory plan is valid before observations; a claimed result needs provenance."""
        root = "0_研究.md"
        summary = "1_核验/1.0_当前判断.md"
        package = "1_核验/1.1_核验来源.md"
        planned = {
            root: "# 研究\n1. **目标**：[核验](1_核验/1.0_当前判断.md)",
            summary: "# 当前判断\n1. **根**：[研究](../0_研究.md)\n"
                     "2. **节点**：预期：来源可核查；实得：未验证；人的冻结：无\n"
                     "3. **包**：[1.1 核验来源](1.1_核验来源.md)；进展：未执行",
            package: "# 1.1 核验来源\n1. **目标**：核实来源；[返回摘要](1.0_当前判断.md)\n"
                     "    1. **计划**：读取权威版本说明。\n    2. **状态**：未执行。",
        }

        def issues(snapshot, *, claims_result=False):
            problems = set()
            for source, text in snapshot.items():
                for target in LINK.findall(text):
                    resolved = posixpath.normpath(str(PurePosixPath(source).parent / target))
                    if resolved not in snapshot:
                        problems.add("broken link")
            process = snapshot.get(package, "")
            if not all(phrase in process for phrase in ("**目标**", "**计划**", "[返回摘要]")):
                problems.add("empty plan")
            if claims_result and not all(phrase in process for phrase in ("**动作**", "**来源**", "**观察**")):
                problems.add("unsupported claim")
            return problems

        self.assertEqual(issues(planned), set())
        self.assertIn("empty plan", issues({**planned, package: "# 1.1 核验来源"}))
        self.assertIn("broken link", issues({root: planned[root], summary: planned[summary]}))
        self.assertIn("unsupported claim", issues(planned, claims_result=True))
        observed = {**planned, package: planned[package] +
                    "\n    3. **动作**：读取合成来源 v1。\n    4. **来源**：合成来源 v1。"
                    "\n    5. **观察**：发现其范围仅覆盖版本 A。"}
        self.assertEqual(issues(observed, claims_result=True), set())

    def test_synthetic_wbs_links_and_gates_reject_incomplete_snapshot(self):
        """In-memory new-model fixture; no agent/host runtime or filesystem writes."""
        root = "0_项目总览.md"
        summary = "1_恢复演练/1.0_当前判断.md"
        first = "1_恢复演练/1.1_样本校验.md"
        second = "1_恢复演练/1.2_隔离恢复.md"
        baseline = {
            root: "# 项目\n1. **目标**：[恢复演练](1_恢复演练/1.0_当前判断.md)",
            summary: "# 当前\n1. **根**：[项目](../0_项目总览.md)\n"
                     "2. **节点**：隔离恢复可复现；判据：隔离演练成功；结果：未通过；人的冻结：无\n"
                     "3. **工作包**：[1.1 样本校验](1.1_样本校验.md)，依赖已获权样本；"
                     "[1.2 隔离恢复](1.2_隔离恢复.md)，依赖 1.1，缺：隔离观察",
            first: "# 1.1 样本校验\n1. **目标**：校验样本；[返回目标](1.0_当前判断.md)\n"
                   "    1. **来源**：合成演练 v1。\n    2. **计划**：比对校验和。\n"
                   "    3. **观察**：校验失败。\n    4. **纠偏**：待复验。",
            second: "# 1.2 隔离恢复\n1. **目标**：隔离恢复；依赖 1.1；"
                    "[返回目标](1.0_当前判断.md)\n"
                    "    1. **计划**：等待样本校验。\n    2. **未验证**：尚无隔离观察。",
        }

        def inspect(snapshot):
            problems = set()
            for source, text in snapshot.items():
                for target in LINK.findall(text):
                    path = posixpath.normpath(str(PurePosixPath(source).parent / target.split("#", 1)[0]))
                    if path not in snapshot:
                        problems.add("missing link")
            if summary not in snapshot or not all(f"[{id_} " in snapshot[summary] for id_ in ("1.1", "1.2")):
                problems.add("missing work items")
            for path, id_ in ((first, "1.1"), (second, "1.2")):
                text = snapshot.get(path, "")
                if not text.startswith(f"# {id_} ") or not all(
                    re.search(r"^    \d+\. \*\*" + re.escape(field) + r"\*\*：", text, re.MULTILINE)
                    for field in (("来源", "计划", "观察", "纠偏") if path == first else ("计划", "未验证"))
                ):
                    problems.add("missing ordered execution history")
                if "[返回目标](1.0_当前判断.md)" not in text:
                    problems.add("missing return route")
            if summary in snapshot and "依赖 1.1，缺：隔离观察" not in snapshot[summary]:
                problems.add("missing dependency or gap")
            if summary in snapshot and not all(
                phrase in snapshot[summary]
                for phrase in ("**节点**：隔离恢复可复现", "判据：隔离演练成功", "结果：未通过", "人的冻结：无")
            ):
                problems.add("checkpoint conflated with task completion")
            return problems

        self.assertEqual(inspect(baseline), set())
        self.assertIn("missing link", inspect({root: baseline[root], summary: baseline[summary]}))
        self.assertIn("missing work items", inspect({**baseline, summary: baseline[summary].replace("[1.2 ", "[X ")}))
        self.assertIn("missing dependency or gap", inspect({**baseline, summary: baseline[summary].replace("缺：隔离观察", "完成")}))
        self.assertIn("missing ordered execution history", inspect({**baseline, first: baseline[first].replace("    3. **观察**：", "观察：")}))
        self.assertIn("missing return route", inspect({**baseline, second: baseline[second].replace("[返回目标](1.0_当前判断.md)", "无回链")}))
        self.assertIn("checkpoint conflated with task completion", inspect({**baseline, summary: baseline[summary].replace("结果：未通过", "结果：任务完成即通过")}))

    def test_skill_list_note_scope_and_migration_counterexamples(self):
        """Written instructions and synthetic scenarios, not formatting/rendering proof."""
        entry = (BUNDLE / "SKILL.md").read_text(encoding="utf-8")
        modeling = (BUNDLE / "references" / "note-modeling.md").read_text(encoding="utf-8")
        cases = (BUNDLE / "references" / "acceptance-cases.md").read_text(encoding="utf-8")
        for phrase in ("整个 Skill", "四空格", "同格", "1. …<br>2. …"):
            self.assertIn(phrase, entry)
        for phrase in ("全部 Skill Markdown", "每层四空格", "不默认放到表外", "视觉编号"):
            self.assertIn(phrase, modeling)
        for phrase in ("| AK.", "| AL.", "Tab 缩进", "批量改成 `N.1`"):
            self.assertIn(phrase, cases)

    def test_bundle_markdown_uses_list_note_mainline(self):
        """Static syntax guard; not renderer, accessibility or agent-behavior proof."""
        for path in [BUNDLE / "SKILL.md", *(BUNDLE / "references").glob("*.md")]:
            text = path.read_text(encoding="utf-8")
            if path.name == "SKILL.md":
                text = text.split("---", 2)[-1]
            in_code = False
            for line in text.splitlines():
                if line.lstrip().startswith("```"):
                    in_code = not in_code
                    continue
                if in_code or not line.strip() or line.startswith(("#", "|", ">", "    ")):
                    continue
                with self.subTest(path=path.name, line=line[:50]):
                    self.assertRegex(line, r"^\d+\. ", "Bundle prose must use ordered list notes")
                self.assertNotIn("\t", line)

    def test_synthetic_navigation_rejects_incomplete_snapshots(self):
        """Pure in-memory fixture graph; not agent output, Git index or host behavior."""
        overview = "0_项目总览.md"
        summary = "1_恢复演练/1.0_当前判断.md"
        process = "1_恢复演练/1.1_隔离恢复.md"
        files = {
            overview: "# project\n1. **目标**：[当前目标](1_恢复演练/1.0_当前判断.md#checkpoint)",
            summary: "# checkpoint\n1. **根**：[根](../0_项目总览.md#project) [演练](1.1_隔离恢复.md#observation)",
            process: "# observation\n1. **目标**：[目标](1.0_当前判断.md#checkpoint)\n来源：合成演练 v1\n观察：隔离恢复失败",
        }

        def flaws(snapshot):
            issues = []
            edges = set()
            for source, text in snapshot.items():
                for target in LINK.findall(text):
                    path, _, anchor = target.partition("#")
                    if "://" in path:
                        continue
                    normalized = posixpath.normpath(str(PurePosixPath(source).parent / path)) if path else source
                    edges.add((source, normalized))
                    if normalized not in snapshot:
                        issues.append("missing path")
                    elif anchor and f"# {anchor}" not in snapshot[normalized].splitlines():
                        issues.append("broken anchor")
            for edge in ((overview, summary), (summary, overview), (summary, process), (process, summary)):
                if edge not in edges:
                    issues.append("missing reciprocal route")
            if process not in snapshot or not all(word in snapshot[process] for word in ("来源：", "观察：")):
                issues.append("missing evidence")
            return set(issues)

        self.assertEqual(flaws(files), set())
        self.assertEqual(flaws({overview: files[overview], summary: files[summary]}),
                         {"missing path", "missing reciprocal route", "missing evidence"})
        self.assertEqual(flaws({**files, summary: files[summary].replace("#observation", "#missing")}),
                         {"broken anchor"})
        self.assertEqual(flaws({**files, process: files[process].replace("[目标](1.0_当前判断.md#checkpoint)", "无反向入口")}),
                         {"missing reciprocal route"})
        self.assertEqual(flaws({**files, process: "# observation\n1. **目标**：[目标](1.0_当前判断.md#checkpoint)"}),
                         {"missing evidence"})

    def test_validation_rejects_bad_metadata_and_link(self):
        with self.assertRaises(ValueError):
            frontmatter("name: pvnw\n")
        with self.assertRaises(ValueError):
            frontmatter("---\nname: pvnw\nname: again\n---\n")
        with self.assertRaises(ValueError):
            local_links(ROOT / "README.md", "[missing](missing-fixture.md)")


if __name__ == "__main__":
    unittest.main()
