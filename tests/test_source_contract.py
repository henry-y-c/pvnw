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
    def test_seven_file_bundle(self):
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
        self.assertIn("每次过程篇变更", routes)
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
        for phrase in ("建立或重组", "重构", "逐级", "不自动写", "人的冻结", "相对链接"):
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

    def test_synthetic_navigation_rejects_incomplete_snapshots(self):
        """Pure in-memory fixture graph; not agent output, Git index or host behavior."""
        overview = "0-项目总览.md"
        summary = "1-恢复演练/1-0-当前判断.md"
        process = "1-恢复演练/1-1-演练证据.md"
        files = {
            overview: "# project\n[当前目标](1-恢复演练/1-0-当前判断.md#checkpoint)",
            summary: "# checkpoint\n[根](../0-项目总览.md#project) [演练](1-1-演练证据.md#observation)",
            process: "# observation\n[目标](1-0-当前判断.md#checkpoint)\n来源：合成演练 v1\n观察：隔离恢复失败",
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
        self.assertEqual(flaws({**files, process: files[process].replace("[目标](1-0-当前判断.md#checkpoint)", "无反向入口")}),
                         {"missing reciprocal route"})
        self.assertEqual(flaws({**files, process: "# observation\n[目标](1-0-当前判断.md#checkpoint)"}),
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
