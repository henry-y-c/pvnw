"""Offline source-contract checks. Never an agent/host behavior test."""

from pathlib import Path
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

    def test_validation_rejects_bad_metadata_and_link(self):
        with self.assertRaises(ValueError):
            frontmatter("name: pvnw\n")
        with self.assertRaises(ValueError):
            frontmatter("---\nname: pvnw\nname: again\n---\n")
        with self.assertRaises(ValueError):
            local_links(ROOT / "README.md", "[missing](missing-fixture.md)")


if __name__ == "__main__":
    unittest.main()
