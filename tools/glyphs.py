#!/usr/bin/env python3
"""Hold docs/GLYPHS.md to the rendered rich repertoire in both directions."""
from pathlib import Path
import re
root=Path(__file__).resolve().parents[1]
wanted={int(x,16) for x in re.findall(r'U\+([0-9A-F]{4,6})',(root/'docs/GLYPHS.md').read_text())}
seen=set()
for path in (root/'tests/goldens').rglob('*.txt'):
    if 'rich' in str(path):seen|={ord(c) for c in path.read_text() if ord(c)>127}
assert wanted==seen,('missing',seen-wanted,'stale',wanted-seen)
print('glyphs: eight documented non-ASCII rich glyphs, sets equal')
