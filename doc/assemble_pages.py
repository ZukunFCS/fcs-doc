"""Replace rebuilt manuals while retaining cached historical Pages content."""
from __future__ import annotations

import argparse
from pathlib import Path
import shutil
import subprocess
import tarfile
import tempfile


def assemble(previous: Path, fresh: Path, destination: Path) -> None:
    # Require both complete dev manuals before deleting any prior output.
    for language in ("en", "jp"):
        if not (fresh / "dev" / language / "index.html").is_file():
            raise ValueError(f"Missing rebuilt dev manual: {language}")
        if not (fresh / "dev" / language / "07_support/issues/index.html").is_file():
            raise ValueError(f"Missing rebuilt issue lookup: {language}")
    shutil.copytree(previous, destination)
    shutil.rmtree(destination / "dev", ignore_errors=True)
    shutil.copytree(fresh, destination, dirs_exist_ok=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("fresh", type=Path)
    parser.add_argument("destination", type=Path)
    args = parser.parse_args()
    with tempfile.TemporaryDirectory(prefix="fcs-pages-") as temporary:
        root = Path(temporary)
        archive = root / "pages.tar"
        subprocess.run(["git", "archive", "--format=tar", "-o", str(archive), "origin/gh-pages"], check=True)
        previous = root / "previous"
        previous.mkdir()
        with tarfile.open(archive) as content:
            content.extractall(previous, filter="data")
        assemble(previous, args.fresh, args.destination)


if __name__ == "__main__":
    main()
