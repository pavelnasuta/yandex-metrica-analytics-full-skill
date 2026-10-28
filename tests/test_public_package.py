"""Offline contract tests for the public Yandex Metrica Analytics skill."""

from pathlib import Path
import subprocess
import unittest


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "yandex-metrica-analytics-full" / "SKILL.md"
ADAPTERS = (
    ROOT / "agents" / "hermes" / "SKILL.md",
    ROOT / "agents" / "claude-code" / "SKILL.md",
    ROOT / "agents" / "codex" / "AGENTS.md",
    ROOT / "agents" / "agents-md" / "AGENTS.md",
)


class PublicPackageTests(unittest.TestCase):
    def test_portable_package_has_one_canonical_read_only_workflow(self):
        skill = SKILL.read_text(encoding="utf-8")
        self.assertIn("metrika:read", skill)
        self.assertIn("analytics-brief.md", skill)
        self.assertIn("analytics-operating-model.md", skill)
        self.assertNotIn("metrika:write", skill)
        for adapter in ADAPTERS:
            self.assertTrue(adapter.is_file(), adapter)
            self.assertIn("skills/yandex-metrica-analytics-full/SKILL.md", adapter.read_text(encoding="utf-8"))

    def test_support_files_are_packaged_and_the_helper_is_safe(self):
        root = SKILL.parent
        for relative in (
            "scripts/metrica_read.py",
            "references/analytics-operating-model.md",
            "references/role-playbooks.md",
            "templates/analytics-brief.md",
            "templates/weekly-digest.md",
        ):
            self.assertTrue((root / relative).is_file(), relative)
        result = subprocess.run(
            ["python3", str(root / "scripts/metrica_read.py"), "report", "--counter", "1", "--dimensions", "ym:s:clientID"],
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 2)
        self.assertIn("unsafe", result.stderr.lower())

    def test_public_files_have_no_credentials_or_machine_local_paths(self):
        public_text = "\n".join(
            path.read_text(encoding="utf-8", errors="ignore")
            for path in ROOT.rglob("*")
            if path.is_file() and ".git" not in path.parts and "tests" not in path.parts and path.suffix != ".pyc"
        )
        for marker in ("/root/", "/home/", "YANDEX_METRICA_TOKEN=", "access_token="):
            self.assertNotIn(marker, public_text)
        self.assertIn("MIT License", (ROOT / "LICENSE").read_text(encoding="utf-8"))

    def test_readme_documents_installation_boundaries_and_support(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        for text in (
            "hermes skills tap add",
            "hermes skills install",
            "metrika:read",
            "Limitations",
            "GitHub Issues",
        ):
            self.assertIn(text, readme)


if __name__ == "__main__":
    unittest.main()
