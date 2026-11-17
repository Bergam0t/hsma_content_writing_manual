"""Zip the rendered book so it can be shared and browsed offline.

Runs as a Quarto post-render step. It only runs after a full render of the
book (not for `quarto preview` or single-file renders, and not for the
standalone profile).

Output: _book/HSMA-Content-Writing-Manual.zip, with everything inside a
top-level HSMA-Content-Writing-Manual/ folder. Unzip it and open index.html.
"""

import os
import sys
import zipfile
from pathlib import Path

ZIP_NAME = "HSMA-Content-Writing-Manual"

if not os.environ.get("QUARTO_PROJECT_RENDER_ALL"):
    sys.exit(0)
if "standalone" in os.environ.get("QUARTO_PROFILE", ""):
    sys.exit(0)

out_dir = Path(os.environ.get("QUARTO_PROJECT_OUTPUT_DIR", "_book"))
zip_path = out_dir / f"{ZIP_NAME}.zip"
zip_path.unlink(missing_ok=True)

with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
    for path in sorted(out_dir.rglob("*")):
        if path.is_file() and path != zip_path:
            zf.write(path, Path(ZIP_NAME) / path.relative_to(out_dir))

print(f"Zipped book to {zip_path}")
