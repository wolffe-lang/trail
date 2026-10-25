# The soil and silhouettes

The view is a soil floor, not a forest. Every ground cell has a seeded mark;
there are no invisible background bands. Lair's noise channel 17 modulates
the earth tones, while its cell hash scatters large rocks (3%), smaller
clods (6%), flecks (25%) and fine grit. The seed is normalised before it
reaches the engine's hash, including for signed 64-bit seed extremes.

## Wolves

2026-10-25 play revision: a long, low solid torso, a forward snout and ears,
four moving feet and a trailing tail. Pack's own sheet and distance-driven
trot were studied as the collection's proportions/timing reference; these
masks and sheets are original trail work, not copied pack files.

One north-facing semantic pixel mask is rotated as a whole for all four
headings: torso, head, ears, feet and tail never come from unrelated body
shapes. Two vertical pixels pack into an upper, lower or full block. The
existing **five-column by three-row footprint is unchanged**, as are the
logical board, movement, wrap and hit rules. The narrow torso has a longer
axis than its width; the four contact points swing around it instead of
forming the old square block.

Each wolf owns a travelled-cell counter. Every accepted cell movement
advances its four-contact leg cycle by one; ticks without movement do not.
The phases are reach, contact, gather and push-off. The tail changes side
between consecutive four-contact strides: one complete sway per stride
pair (eight travelled cells). Pausing freezes position, contact phase and
tail, including newcomers. A newcomer uses the very same sprite/gait from
its accumulated approach distance in 1/256-cell units, not its animation
age; that travelled distance is retained when it joins the pack. Its path
uses Manhattan distance for the contact counter.

The leader remains bright and bold, followers grey, and a newcomer gold.
Plain has the same occupancy mask, footprint, four leg frames and tail
period. It uses directional heads, solid `#` torso cells, four contact
marks and a `~` tail. Every pose is checked on both tiers and every heading.

## Meat, eagle and shadow

Meat is two full red blocks, `##` in the plain tier. The eagle is a
seven-by-three spread-wing silhouette, pale against the dark earth so the
telegraph remains readable. Its dim five-by-three diamond shadow slides
from an edge towards the tail for a full second. Both tiers use the same
positions and masks. A miss continues beyond the opposite edge; a hit
shortens the pack before the eagle exits. The title and death cards share
the floor's palette, with different original text.

## Study and goldens

`target/trail --art-study --dump target/study` writes a wolf-contact sheet
and a props companion for each tier at 80x24 and 200x60: eight sheets total.
The wolf sheet crosses all four headings with all four contact phases,
shows leader/follower/newcomer coats, and includes the opposite tail sway.
The props companion retains meat, eagle and sliding shadow.

The ordinary-key `stride-{up,down,left,right}-{80,200}` goldens each move
one logical cell, pinning contact phase one in every heading and both
tiers. All original scene goldens are regenerated for the new wolves.
Unit rows check distance rather than tick-driven phase, pause freeze,
newcomer continuity, four distinct frames on each tier, exact rotations,
four separate feet and the tail's stride pair.
