# Trail rules

A run is a seed and a sequence of tick-stamped keys. The simulation reads
neither a terminal nor a clock. The loop uses lair's fixed 30 Hz clock;
late frames drop renders, never simulation ticks.

## The field and the pack

One logical cell occupies five terminal columns and three rows. The first
and last terminal rows are the HUD and controls. An 80x24 field therefore
has 16x7 logical cells; 200x60 has 40x19. The minimum is 40x12 (8x3).
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

## Eagles

The first eagle is scheduled when the third wolf joins. Its delay is
`max(6, 12 + seeded(0..8) - length/3)` seconds. Every subsequent strike
schedules the next with the current length, even if it has fallen below
three. The shadow approaches the current tail over 30 ticks, tracking its
position. At tick 30 the eagle rolls; it exits over another 18 ticks.

The independent Park–Miller strike stream uses seed modulo 2147483646,
plus one, multiplier 48271 and modulus 2147483647. Rejection of the top six
outcomes gives an unbiased d20. **1–7 hits: fixed 35%.** Neither length nor
score changes those odds. A hit removes only the deque's tail. Removing
the only wolf ends the run, even if a newcomer is still approaching. A
miss is one eagle survived and 25 points. The HUD displays the last roll,
threshold and fixed odds, including at the minimum size.

The death card gives the cause, score, longest pack, survived/strike counts
and the most recent sixteen rolls. The complete history is reproducible
from the replay. Enter, Space, an arrow or `r` dismisses either card; arrows also choose
the first heading and Space does not pause on dismissal. Quit and interrupt
leave without starting. A death-card key retries the original seed and initial board, retaining
the replay's monotonically increasing tick count.

## Window changes and terminal lifecycle

Without `--size`, a valid SIGWINCH re-centres the original logical board
in the new terminal and records the layout dimensions. The board itself
never grows, remaps wolves or changes the RNG because of a resize. Small
windows clip it; enlarge the terminal to recover the view. With `--size`,
the field stays fixed. Replay resizes reproduce the layout changes.

Trail validates its 40x12 minimum before constructing the engine's public
terminal state: lair's opener currently fixes 80x24. The engine still owns
enter/leave, raw mode, signal listening and the registered runtime restore.
Quit, Escape, typed Ctrl-C, normal replay/tick exit, I/O returns and a trap
all use that restore. SIGKILL and machine loss cannot restore a terminal.

## Tests and tuning

The rich/plain simulation is identical. Unit tests cover every rule;
black-box tests check the built executables' state, not just golden bytes.
Rare visual states use explicit `scene` replay fixtures. A separate,
ordinary-key 561-tick run collects 25 meals, reaches 23 wolves, receives
the first eagle hit and verifies score 2500. Two actual pty recordings
each verify score 100. Fixture files are not recordings.

These are the initial values from 2026-10-25. Pace, meat count and cadence
are proposed tuning values; self-collision and the fixed strike odds are
settled rules. Play can tune the former without quietly changing the latter.

## Distance-driven gait (2026-10-25 play revision)

The five-by-three footprint and every collision rule stay unchanged. Each
pack member has a separate travelled-cell counter incremented only after
a successful cell move, including a seam crossing. Its leg phase is
distance modulo four; its tail phase is floor(distance / four) modulo
two. Newcomers accumulate actual approach distance in 1/256-cell units
and retain its whole-cell component when they join. Pause advances none
of these counters or approach positions. The body uses the same original
turned mask in every heading, with long torso, forward head/ears and tail.
