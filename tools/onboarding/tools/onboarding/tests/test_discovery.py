import tempfile
import unittest
from pathlib import Path

from tools.onboarding.discovery import discover_repository


def _write(root: Path, name: str, content: str) -> None:
    (root / name).write_text(content, encoding="utf-8")


class TestDiscovery(unittest.TestCase):
    def test_detects_rust_cpp_llvm_qnx(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            _write(
                root,
                "MODULE.bazel",
                'bazel_dep(name = "rules_rust", version = "0.70.0")\n'
                'bazel_dep(name = "rules_cc", version = "0.2.18")\n'
                'bazel_dep(name = "toolchains_llvm", version = "1.7.0")\n'
                "# target: qnx8\n",
            )
            _write(root, "project_config.bzl", 'PROJECT_CONFIG = {\n    "asil_level": "QM",\n    "source_code": ["rust"],\n}\n')
            _write(root, "README.md", "Docs built with Sphinx.\n")
            (root / "docs").mkdir()
            _write(root / "docs", "conf.py", "# sphinx conf\n")

            repository = discover_repository(root, name="module_template")

            self.assertEqual(repository.name, "module_template")
            self.assertEqual(repository.asil, "QM")
            self.assertIn("rust", repository.languages)
            self.assertIn("cpp", repository.languages)
            self.assertIn("llvm", repository.toolchains)
            self.assertIn("qnx", repository.toolchains)
            self.assertEqual(repository.build_system, "Bazel")
            self.assertEqual(repository.docs_system, "Sphinx")

    def test_defaults_when_files_missing(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            repository = discover_repository(root, name="empty_repo")
            self.assertEqual(repository.asil, "QM")
            self.assertEqual(repository.languages, [])
            self.assertEqual(repository.build_system, "Unknown")
            self.assertEqual(repository.docs_system, "Unknown")


if __name__ == "__main__":
    unittest.main()
