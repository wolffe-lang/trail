# Trail rules

A run is a seed and a sequence of tick-stamped keys. The simulation reads
neither a terminal nor a clock. The loop uses lair's fixed 30 Hz clock;
late frames drop renders, never simulation ticks.

## The field and the pack

One logical cell occupies seven terminal columns and seven rows. The first
and last terminal rows are the HUD and controls. An 80x24 field therefore
has 11x3 logical cells; 200x60 has 28x8. The minimum is 40x16 (5x2).
Dimensions above 400x120 are refused. Unused margins carry the same soil.

The pack begins with one wolf at the centre, heading east. Arrows turn it;
a reverse is refused, even for the first wolf. At most one corner is
accepted before the next movement: two quick turns cannot reverse into
the second wolf. Wolves follow a bounded ring deque, retaining their
individual headings through corners and all four wrapping seams. Entering
the departing tail cell is legal unless a newcomer grows into that cell
on the same movement. Entering any other occupied cell scatters the pack.

Speed is four logical cells/second, plus 0.25 per additional wolf, capped
at ten. Integer movement credit adds 16 + length - 1 (capped at 40) each
tick; a cell costs 120 credits. Space pauses gameplay time, including the
eagle and newcomers, but not input/replay ticks.

## Meat and newcomers

One piece is present below eight wolves, two from eight onward, except
when the board has no free cells. A seeded starting cell and bounded scan
place each piece away from the pack and other meat. A meal is 100 points.
It summons one newcomer from beyond a seeded edge at a seeded coordinate.
The sprite approaches the moving tail over 24 ticks, then waits for the
next cell movement to occupy the departing tail's cell. It is not a deque
member and cannot be reaped while approaching or waiting. Runner storage
is bounded by the board area; a saturated runner queue drops a further
summon rather than allocating without limit.

## Slower, dodgeable eagles

The first eagle is scheduled when the third wolf joins. Its delay remains
`max(6, 12 + seeded(0..8) - length/3)` seconds. A new attempt waits until
the previous eagle has exited as well as its cadence deadline.

An approach flies at **60% of the leader's current speed**, updated every
tick. If pace is q quarter-cells/second, a leader moves q/120 cells/tick;
the eagle moves q/200. Its complete approach is twelve cells long, so even
the maximum pace needs **60 ticks after the first visible launch frame**.
The launch cell is visibly on the nearest seeded edge, not offscreen.
A boundary out-and-back lead-in supplies the extra distance before the
final line to the target; it is moving, not hovering. This makes the full
two-second warning possible even on a short field.

At launch a scratch copy of the pure simulation projects the last wolf's
position if the current heading continues. It uses the same movement helper,
seeded meat placement, pending arrivals and pace changes, not a guessed
constant-length extrapolation. The visible aim is then locked. At impact:
- Tail outside that logical strike cell: **certain dodge, no d20 drawn**,
  HUD `eagle: dodged`, one survival and 25 points.
- Tail in that cell: a fair seeded d20; **1–7 hits, fixed 35%**, unchanged
  by length or score. A caught miss earns one survival and 25 points.

The independent Park–Miller stream uses normalised seed plus one,
multiplier 48271, modulus 2147483647 and rejection of its six unused
outcomes. Dodges consume none of that roll stream or roll history. The
10,000 caught-roll witness measures 3403 hits (34.03%). A scripted turn
two cells before impact dodges without advancing the stream; an unchanged
heading is caught, including seeded growth during the approach.

| fixed trail length | leader speed | eagle speed | visible approach |
|---|---|---|---|
| 1 | 4 cells/s | 2.4 cells/s | 150 ticks / 5.0 s |
| 8 | 5.75 cells/s | 3.45 cells/s | 105 ticks / 3.5 s |
| 16 | 7.75 cells/s | 4.65 cells/s | 78 ticks / 2.6 s |
| 25+ | 10 cells/s | 6 cells/s | 60 ticks / 2.0 s |

The exit continues at 60% pace toward the opposite edge. A hit carries the
taken wolf; if it was the only wolf, its departure is shown for the same
one-second death animation before the card, without teleporting it away.

## A real scatter before the card

Self-collision starts a **30-tick** scatter, not an immediate modal. Every
wolf, including the leader, chooses a direction away from the collision
point with seeded tie-breaking and a seeded 4–7 cells/s speed. They stop
at the field bound instead of wrapping; gait follows actual distance.
The HUD says `the pack scatters`. Only after all 30 ticks does the death
card appear. The last-wolf eagle death uses a moving carry-away instead.

During either death animation only quit/interrupt is acted on; a start,
arrow, r or Space cannot skip it. The card gives the cause, score, longest
pack, attempts/survivals, dodged/caught counts and latest sixteen caught
rolls. Enter, Space, an arrow or r retries the same seed after the card.
The replay tick counter remains monotonic. Space still pauses normal
play, including eagle flight and newcomer approach.

## Window changes and terminal lifecycle

Without `--size`, a valid SIGWINCH re-centres the original logical board
in the new terminal and records the layout dimensions. The board itself
never grows, remaps wolves or changes the RNG because of a resize. Small
windows clip it; enlarge the terminal to recover the view. With `--size`,
the field stays fixed. Replay resizes reproduce the layout changes.

Trail validates its 40x16 minimum before constructing the engine's public
terminal state: lair's opener currently fixes 80x24. The engine still owns
enter/leave, raw mode, signal listening and the registered runtime restore.
Quit, Escape, typed Ctrl-C, normal replay/tick exit, I/O returns and a trap
all use that restore. SIGKILL and machine loss cannot restore a terminal.

## Tests and tuning

The rich/plain simulation is identical. Unit tests cover every rule;
black-box tests check the built executables' state, not just golden bytes.
Rare visual states use explicit `scene` replay fixtures. A separate,
ordinary-key 786-tick run collects 14 meals, reaches 14 wolves, dodges
the first eagle without a roll and verifies score 1425. Two actual pty recordings
each verify score 100. Fixture files are not recordings.

These are the initial values from 2026-10-25. Pace, meat count and cadence
are proposed tuning values; self-collision and the fixed strike odds are
settled rules. Play can tune the former without quietly changing the latter.

## Distance-driven gait (2026-10-25 play revision)

The sprite occupies a 7x3 east/west or 5x7 north/south sheet inside a 7x7 logical
collision envelope; the rule remains one occupied logical cell per wolf. Each
pack member has a separate travelled-cell counter incremented only after
a successful cell move, including a seam crossing. Its leg phase is
distance modulo four. East/west tails sway over a stride pair; the supplied
north tail alternates its two quarter-cell positions with the contact phase. Newcomers accumulate actual approach distance in 1/256-cell units
and retain its whole-cell component when they join. Pause advances none
of these counters or approach positions. East/west keep the profile; north is top-down with legs on both sides,
and south is generated by vertically mirroring north.

## Four-leg geometry revision, 2026-10-25

Four separated one-cell leg columns require seven columns, since three
whole floor cells separate them. East/west therefore use a 7x3 sheet;
north/south now use the supplied 5x7 top-down construction. Every logical
cell reserves 7x7, so a perpendicular neighbour cannot overlap it. This
changes field capacity and seeded meat placement, not self-collision, wrap
or eagle odds. The 40x16 minimum holds two such rows plus the HUD/control
rows. Earlier geometry replays should not be expected to preserve their
scores; fresh ordinary-key witnesses are pinned for this revision.
