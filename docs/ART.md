# The soil and silhouettes

The view is a soil floor, not a forest. Every ground cell has a seeded mark;
there are no invisible background bands. Lair's noise channel 17 modulates
the earth tones, while its cell hash scatters large rocks (3%), smaller
clods (6%), flecks (25%) and fine grit. The seed is normalised before it
reaches the engine's hash, including for signed 64-bit seed extremes.

## North and south

North is the supplied 5x7 top-down rectangle: ear corners and head above,
a one-cell neck, a three-cell-wide solid torso, two legs on each side and
the tail below. Phases are pair A forward, level, pair B forward, level;
level deliberately repeats. South is generated from north by reversing
row order and vertically reflecting each cell's quadrant bits. No second
south drawing is stored. The head becomes `▜█▛` at the bottom; the tail's
exact reflected phases are `▖` and `▗` at the top.

East/west retain the previous 7x3 profile and separated leg columns.
All headings remain centred in the same 7x7 collision cell; minimum 40x16
and field capacities are unchanged. Leader bright/bold, followers grey
and newcomers gold remain distinct. Gait advances per cell moved; pause
freezes it. Plain north uses # torso, ^ head, | level legs and apostrophe/
comma forward/back legs; south mirrors the construction with a v head.

## Eagles and the floor shadow

The supplied 7x3 eagle has a central body column, a head above the body,
and wings up, level, down, level. Four indexed flap phases make one cycle
per cell flown, using quarter-cell distance, not time. Level intentionally
repeats. Plain keeps the footprint with diagonal wing strokes, - level
wings and | body. The dim floor diamond is unchanged. Shadows draw below
wolves, the flying eagle above them; a taken wolf hangs below the eagle.
Meat stays two solid red cells.

## Study and motion scenes

The study includes every wolf heading/phase on both tiers at both sizes,
props companions, and an eagle-flap sheet for each tier/size. It uses simple
marked soil patches so limbs and wings can be counted; the live field
retains the full seeded soil scatter.

`tools/sprite-frames.py` extracts these literal cells from the committed
sheets. Middle dots below are floor. Mirror, side-leg/head, literal-sheet
and flap-distance tests are independent of golden bytes. Goldens also
show middle scatter/carry-away, the delayed card, an actual positional
dodge and a caught strike. Fixture launches are disclosed; their impacts
are decided by the normal simulation.

### Rich contact sheets

```
NORTH  phase 0 / phase 1 / phase 2 / phase 3
·▟█▙·   ·▟█▙·   ·▟█▙·   ·▟█▙·
··█··   ··█··   ··█··   ··█··
▘███▖   ▌███▐   ▖███▘   ▌███▐
·███·   ·███·   ·███·   ·███·
▖███▘   ▌███▐   ▘███▖   ▌███▐
·███·   ·███·   ·███·   ·███·
··▘··   ··▝··   ··▘··   ··▝··

SOUTH  phase 0 / phase 1 / phase 2 / phase 3
··▖··   ··▗··   ··▖··   ··▗··
·███·   ·███·   ·███·   ·███·
▘███▖   ▌███▐   ▖███▘   ▌███▐
·███·   ·███·   ·███·   ·███·
▖███▘   ▌███▐   ▘███▖   ▌███▐
··█··   ··█··   ··█··   ··█··
·▜█▛·   ·▜█▛·   ·▜█▛·   ·▜█▛·

EAGLE up / level / down / level
▖·····▗   ·······   ·······   ·······
·▙·█·▟·   ▄▄▄█▄▄▄   ·▛·█·▜·   ▄▄▄█▄▄▄
··▀█▀··   ···█···   ▘··█··▝   ···█···

```
