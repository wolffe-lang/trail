#!/usr/bin/env python3
"""Extract the actual committed contact-sheet cells, not a hand transcription."""
from pathlib import Path
root=Path(__file__).resolve().parents[1]
for tier in ('rich','plain'):
    print(tier.upper())
    for heading,name in [(1,'NORTH'),(2,'SOUTH')]:
        rows=(root/f'tests/goldens/art/heading-{heading}-80-{tier}.txt').read_text().splitlines()
        w,h=(5,7) if heading<=2 else (7,3)
        top=3+(7-h)//2
        print(name+'  phase 0 / phase 1 / phase 2 / phase 3')
        for y in range(h):
            print('   '.join(rows[top+y][3+f*18+(7-w)//2:3+f*18+(7-w)//2+w] for f in range(4)))
        print()
    rows=(root/f'tests/goldens/art/eagle-80-{tier}.txt').read_text().splitlines()
    print('EAGLE up / level / down / level')
    for y in range(3):print('   '.join(rows[6+y][3+f*18:3+f*18+7] for f in range(4)))
    print()
