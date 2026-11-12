import importlib.util
from pathlib import Path
import tempfile
import unittest

spec = importlib.util.spec_from_file_location("assemble_pages", Path(__file__).parents[1] / "doc/assemble_pages.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class PublishTests(unittest.TestCase):
    def test_replaces_dev_and_retains_cached_releases(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            previous = root / "previous"
            fresh = root / "fresh"
            for path in ("dev/jp/07_support/issues/OLD.html", "26.10/jp/index.html", "CNAME"):
                target = previous / path
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text("preserved")
            for language in ("en", "jp"):
                target = fresh / "dev" / language
                (target / "07_support/issues").mkdir(parents=True)
                (target / "index.html").write_text("new")
                (target / "07_support/issues/index.html").write_text("lookup")
            destination = root / "publish"
            module.assemble(previous, fresh, destination)
            self.assertFalse((destination / "dev/jp/07_support/issues/OLD.html").exists())
            self.assertEqual((destination / "26.10/jp/index.html").read_text(), "preserved")
            self.assertEqual((destination / "CNAME").read_text(), "preserved")
            self.assertEqual((destination / "dev/en/index.html").read_text(), "new")

    def test_incomplete_build_cannot_replace_previous_pages(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            with self.assertRaises(ValueError):
                module.assemble(root / "previous", root / "fresh", root / "publish")
            self.assertFalse((root / "publish").exists())
