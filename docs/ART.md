# The soil and silhouettes

The view is a soil floor, not a forest. Every ground cell has a seeded mark;
there are no invisible background bands. Lair's noise channel 17 modulates
the earth tones, while its cell hash scatters large rocks (3%), smaller
clods (6%), flecks (25%) and fine grit. The seed is normalised before it
reaches the engine's hash, including for signed 64-bit seed extremes.

## Wolves

The rich east-facing construction is seven columns by three rows. Its
central five-cell body is a solid horizontal bar with a straight back and
belly. A head block projects at the front with a missing upper quadrant
for an ear notch; the tail is one quarter-block stroke behind the body.
The four legs are **separate full-height half-cell columns** at columns
0, 2, 4 and 6, with a complete floor cell between each. No contact pose
hides or merges two of them. A narrow hip joins the rear leg to the bar.

West mirrors the complete east sheet. North and south quarter-turn the
same cells and each cell's quadrants, producing a three-column by seven-row
sheet; they are not squashed versions or unrelated poses. Every heading
is centred in a **7x7 logical collision cell**. This prevents overlap when
neighbours turn perpendicular to one another. The former 5x3 footprint
cannot hold four separated columns, and a 7x3 envelope cannot contain its
own literal quarter-turn. This geometry requires a 40x16 minimum to retain
two logical board rows; 80x24 and 200x60 remain supported.

Four contact phases alternate the diagonal pairs: front-left with
back-right, then front-right with back-left. Each foot sweeps between the
left and right half of its own column, retaining the full-height stem
throughout. Both diagonal-pair and four-distinct-frame assertions are
independent of the golden bytes. Distance, not ticks, advances each wolf's
phase. The tail changes side once per pair of strides; pausing freezes
all contact/tail phases and the newcomer's approach. Arriving wolves use
the same construction and retain their distance-driven phase on joining.

The leader stays bright/bold, followers grey and arrivals gold. Plain has
exactly the same cell occupancy, orientation and four phases: `#` for the
body and planted contact, `|` for the other contact, `.` for the tail.
Separate foreground/background styles keep its tail distinct from soil.
All sheets and drawing code are original work.

## Meat, eagle and shadow

Meat is two full red blocks, `##` in the plain tier. The eagle is a
seven-by-three spread-wing silhouette, pale against the dark earth so the
telegraph remains readable. Its dim five-by-three diamond shadow slides
from an edge towards the tail for a full second. Both tiers use the same
positions and masks. A miss continues beyond the opposite edge; a hit
shortens the pack before the eagle exits. The title and death cards share
the floor's palette, with different original text.

## Study and goldens

`target/trail --art-study --dump target/study` writes one contact sheet
per heading, tier and field size (16 sheets), plus four props companions.
Each contact sheet shows the four phases across one row and the opposite
tail sway below. A simple marked soil patch, rather than scattered rocks,
lets the eye count all four legs. The game still uses the full soil floor.

`tools/sprite-frames.py` extracts the actual rich/plain contact cells from
the committed sheets for review, not a hand-drawn approximation. Mid-stride
goldens cover every heading at both sizes and tiers. Geometry tests pin the
straight body bar, four separated leg columns, head notch, tail, diagonal
pairs, exact tier occupancy and the quarter-turned collision envelope.
