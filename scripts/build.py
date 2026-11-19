"""Build index.html from src/template.html with an embedded stroke-count table.

The stroke counts come from the Unicode Unihan database (kTotalStrokes), read
from the SQLite file shipped in the @mandel59/mojidata npm package.

Usage:
    npm pack @mandel59/mojidata && tar xzf mandel59-mojidata-*.tgz
    python3 scripts/build.py package/dist/moji.db

The table covers the CJK Unified Ideographs block (U+4E00-U+9FFF). Each code
point is stored as one character: chr(0x30 + strokes), or "0" when unknown.
"""

import json
import sqlite3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FIRST, LAST = 0x4E00, 0x9FFF


def load_strokes(db_path: str) -> dict[int, int]:
    conn = sqlite3.connect(f"file:{db_path}?mode=ro", uri=True)
    strokes = {}
    for ucs, value in conn.execute("SELECT UCS, value FROM unihan_kTotalStrokes"):
        if len(ucs) == 1 and FIRST <= ord(ucs) <= LAST:
            strokes[ord(ucs)] = int(value.split()[0])
    conn.close()
    return strokes


def main() -> None:
    if len(sys.argv) != 2:
        sys.exit("usage: python3 scripts/build.py path/to/moji.db")
    strokes = load_strokes(sys.argv[1])
    table = "".join(chr(0x30 + strokes.get(cp, 0)) for cp in range(FIRST, LAST + 1))
    template = (ROOT / "src" / "template.html").read_text(encoding="utf-8")
    if "__STROKES__" not in template:
        sys.exit("src/template.html is missing the __STROKES__ placeholder")
    html = template.replace("__STROKES__", json.dumps(table))
    (ROOT / "index.html").write_text(html, encoding="utf-8")
    print(f"index.html written: {len(strokes)} characters with stroke data")


if __name__ == "__main__":
    main()
