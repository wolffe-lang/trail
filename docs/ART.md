# The soil and silhouettes

The view is a soil floor, not a forest. Every ground cell has a seeded mark;
there are no invisible background bands. Lair's noise channel 17 modulates
the earth tones, while its cell hash scatters large rocks (3%), smaller
clods (6%), flecks (25%) and fine grit. The seed is normalised before it
reaches the engine's hash, including for signed 64-bit seed extremes.

## Wolves

An original north-facing five-by-five pixel mask contains seventeen solid
pixels. The head is the three-pixel cap, the central mass is the body,
the four corners on rows one and three are legs, and the last pixel is the
tail. Every other heading is a rotation of that same mask, not another
body shape. Two vertical pixels pack into a terminal half-block pair:
upper, lower or full block. The footprint stays five columns by three
rows in every heading, on both tiers.

The leader's coat is brighter and bold; followers are grey; a running
newcomer is gold. The plain sprite replaces each occupied half-block cell
with `#`, with a directional head marker (`^`, `v`, `<`, `>`). Its occupancy
mask and footprint exactly match rich. The brighter cap and four legs are
visible in the study; no sprite is copied from another game.

## Meat, eagle and shadow

Meat is two full red blocks, `##` in the plain tier. The eagle is a
seven-by-three spread-wing silhouette, pale against the dark earth so the
telegraph remains readable. Its dim five-by-three diamond shadow slides
from an edge towards the tail for a full second. Both tiers use the same
positions and masks. A miss continues beyond the opposite edge; a hit
shortens the pack before the eagle exits. The title and death cards share
the floor's palette, with different original text.

## Study and goldens

`target/trail --art-study --dump target/study` writes four sheets: rich
and plain at 80x24 and 200x60. Each shows leader, follower and newcomer
across all headings, plus meat, eagle and shadow. The engine's golden gate
holds these and every game-frame scene to text, styles and pure state.
Unit tests independently check the rotations, four legs, tier occupancy,
plain colour range, solid meat, leader contrast and visible soil scatter.
