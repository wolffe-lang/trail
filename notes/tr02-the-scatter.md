Head `68b90f7e34a9d8db954fd6f3d950fa549ef8786e`. Complete note for materialisation as `notes/tr02-the-scatter.md`; the wrapper prohibits Markdown report files.

## Prediction

Committed before implementation in `24099a8`: the supplied 5x7 north should read at 80x24; all north/south/eagle-bearing image directories and all state dumps should change. Both existing short recordings have no eagle opportunities, so predicted unchanged replay rate is **0/0**, not a percentage. The old longer witness should end during the slower approach instead of its former strike.

Measured: both short recordings still score 100, zero attempts/dodges/catches. The unchanged 728-tick long witness still scores 1200, zero attempts, eagle age 29: approach still in progress. Refreshed ordinary-key witness reaches a genuine **certain dodge**, no roll, at tick 785; final 786 ticks, 14 meals, longest pack 14, score **1425**. All 63 pre-existing golden directories move, 20 added; 83 regenerated in total.

## Forbidden

Supplied sheets reproduced as instructed; game code original. No engine, pin, workflow, planning or configuration edits; no packages, labels, merges, tags, releases or issue actions; no attribution trailers. Three module plants ran locally in the lane gauntlet only, never in CI. All builds/tests used kasumi CPUs 8–11, taskset, `/home/mfwolffe/lanes/kasumi-cores-8-11.lock` and the staged engine container, except one final-head Mac play build. Its scripted vm_stat floor passed at **16.05 GiB >= 8 GiB**; no Mac tests, goldens or pty loops. All jobs waited for; no kills or maintainer-server changes.

## Inputs verified

Contract read first and whole; tr01 code, its materialised note, campaign/rules and guide. Base `2284d57` is merged game `e658f5b` plus the tr01 note. Engine unchanged at `57870143ebbb4806b8bee40379e8c6e781f50842`; complete verified archive pairs wolf 0.2.35/lupin 0.1.56 and std `2386522eb059cca5a84108562c2c0a0e72345d34`.

R-tr02-1/2/3 A implemented as recommended, not decided: **60% current leader speed**, a visible approach >=2 seconds, certain positional dodge before the RNG, caught-only d20 hit 1–7 (35%), and a 30-tick death animation.

Additional recommendations, implemented pending review:
- **R-tr02-4:** a twelve-cell approach, visibly starting on the nearest seeded edge, using a moving boundary out-and-back lead-in before the final line. At the capped leader pace this is exactly two seconds; a short field otherwise cannot contain a sufficiently long straight visible approach. Aim is frozen at launch, projected by a private copy of the pure pack movement, including seeded meat, arrivals and pace changes if the current heading continues. Flight speed still updates to 60% of the actual current pace every tick. No hover or hidden offscreen warning time.
- **R-tr02-5:** scattered wolves take a cardinal direction away from the collision point, seed-breaking equal choices, at seeded 4–7 cells/s; stop at field bounds instead of wrapping. Their leg distance advances only while moving. The leader participates. Last-wolf carry continues toward the far edge at the same slow speed for the full second, then the card; it is not teleported offscreen.

North/south geometry is now 5x7 inside the unchanged 7x7 cell. East/west, minimum 40x16 and collision capacity are unchanged. South is an actual vertical reflection of north, including quadrant bits. Consequently its tail is `▖` in phases 0/2 and `▗` in level phases 1/3; the latter is the south-tail example in the brief. No second south sheet is drawn.

## Evidence index

- `66175d7`: supplied top-down north and generated south, mirror/legs/head tests and sheets.
- `03468a5`: pure seeded scatter/carry, middle/end scenes and actual-pty delayed-card witness.
- `32e0f66`: predictive moving approaches, certain dodges and caught-only RNG, timing/scripted tests.
- `fa88f8f`: supplied eagle wings, four distance phases per flown cell (up/level/down/level), plain counterpart.
- `431bdbc`: native/release integration, caught/dodge/scatter/carry goldens, counters/layering; `8103e9d`: docs and named local evidence; `68b90f7`: README-only refresh, read/current.

Complete source gauntlet: `notes/tr02-evidence/final-source-linux.log`, direct exit 0, locked container. **77 checked tests**, zero failed/rejected/unsupported/SKIP; both compiled backends/selftest; **41 cases x two tiers + art = 83 directories / 558 files**; **13 pty rows** including `scatter-before-card`; both-backend gameplay; 18-glyph inventory; slack-1 performance. Source 200x60 plain avg/p99/max **165/300/514 us**, against a 4000 us gate. Exact final head `68b90f7e34a9d8db954fd6f3d950fa549ef8786e` was fetched and staged-tree-compared on kasumi; complete check-linux plus slack-1 perf passed, direct exit **0**, `/Users/mfwolffe/lanes/tr02/logs/final-head-linux.log` and matching `.exit` (also `/home/mfwolffe/lanes/tr02/final-head-linux.log`). Final-head plain 200x60 avg/p99/max **149/208/323 us**. Immediate one-time CI listing returned `[]`; the required audit subsequently observed **40249740671**, completed success, **tier pr**. Module/path checks, every CI job/step/annotation, ancestry, sections, shas and orphan checks passed. Direct audit exit 1; last line **`AUDIT FAIL (footprint: module)`**. Sole failure: the intentionally retained play worktree. Log `/Users/mfwolffe/lanes/tr02/logs/audit.log`. No CI wait, polling or label.

Approach times, pinned from the first visible launch state (age/credit zero), with unchanged length:

| length | leader cells/s | eagle cells/s | approach ticks / seconds |
|---|---|---|---|
| 1 | 4 | 2.4 | 150 / **5.0** |
| 8 | 5.75 | 3.45 | 105 / **3.5** |
| 16 | 7.75 | 4.65 | 78 / **2.6** |
| 25+ | 10 | 6 | 60 / **2.0** |

A turn two cells before impact dodges with roll stream unchanged. A continued heading rolls; a separate row verifies prediction across seeded meals and arrivals. The 10,000 caught-only roll-gate sample is **3403 hits (34.03%)**, within 35% ±1.5. A separate 10,000-dodge stream consumes zero rolls. Both actual binary backends run caught/dodge cases at both sizes.

The pty scatter row observes actual rendered trace phases and the final terminal-model card: phase 3 first, no card until scatter age 30. Middle/end goldens independently distinguish the HUD from the modal. Scatter/carry cannot be skipped with ordinary gameplay keys; quit/interrupt still restore the terminal.

Three local module plants, all gauntlet exit 1, each named row observed red:
- South cells reversed without quadrant reflection: `test_south_is_generated_vertical_mirror_of_north ... FAILED (trap(assert))`, `notes/tr02-evidence/plant-south-linux.log`.
- Zero-tick scatter: `test_scatter_is_seeded_and_card_waits_thirty_ticks ... FAILED (trap(assert))`, `notes/tr02-evidence/plant-zero-linux.log`.
- Dodge consumes a hidden d20: `test_turn_two_cells_before_impact_dodges_without_rng ... FAILED (trap(assert))`, `notes/tr02-evidence/plant-dodge-linux.log` (long no-roll stream also fails).

Goldens named completely by these expansions: `{carry,caught,death,dodge,hit,miss,one,scatter,scatter-end,stride-{up,down,left,right},summons,telegraph,title,wrap-{up,down,left,right}}-{80,200}-{rich,plain}`, `natural-200-{rich,plain}`, and `art`. Full explicit 83-directory listing: `notes/tr02-evidence/golden-directories.txt`. E/W-only contact-sheet cells stay unchanged; every pre-existing state directory changes for the new counters. Recordings were genuinely recaptured: their bytes/scores stayed 100/100 because they never reach an eagle. `unchanged-replays-linux.log` and `refresh-linux.log` retain both measurements.

### Literal supplied-sheet frames

Extracted by `tools/sprite-frames.py` from committed sheets; not hand transcription. Dots are floor. The four indexed phases deliberately repeat level.

```
RICH
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

PLAIN
NORTH  phase 0 / phase 1 / phase 2 / phase 3
.#^#.   .#^#.   .#^#.   .#^#.
..#..   ..#..   ..#..   ..#..
'###,   |###|   ,###'   |###|
.###.   .###.   .###.   .###.
,###'   |###|   '###,   |###|
.###.   .###.   .###.   .###.
.....   .....   .....   .....

SOUTH  phase 0 / phase 1 / phase 2 / phase 3
.....   .....   .....   .....
.###.   .###.   .###.   .###.
'###,   |###|   ,###'   |###|
.###.   .###.   .###.   .###.
,###'   |###|   '###,   |###|
..#..   ..#..   ..#..   ..#..
.#v#.   .#v#.   .#v#.   .#v#.

EAGLE up / level / down / level
\...../   .......   .......   .......
.\.|./.   ---|---   ./.|.\.   ---|---
..-|-..   ...|...   /..|..\   ...|...

```

## Done-when

- [x] Exact supplied north, generated south mirror and supplied eagle wings on both tiers; same collision envelope.
- [x] Real seeded 30-tick scatter and last-wolf carry before the modal, mid-animation goldens and pty card timing.
- [x] Slow visible approaches, seeded predictive locked aim, certain dodges and caught-only 35% d20, distance-based flaps.
- [x] Complete locked Linux source gate, 77 tests, both backends, 83 golden directories, 13 pty rows; three local plants red by name.
- [x] Docs/README current, refreshed recordings and natural dodge proof, one final-head Mac release play build.
- [x] Final-head module PR tier green: 40249740671.
- [ ] Coordinator accepts play, reviews recommendations and materialises this note. No label required.

Play binary `/Users/mfwolffe/lanes/tr02/trail/target/trail`, SHA256 **`169533e8a44b4008b301b538f39264459a4ac0d436da1ffd3889c08975cf1271`**.
Command: `/Users/mfwolffe/lanes/tr02/trail/target/trail --seed 206 --size 200x60` (80x24 alternative: seed 9). Build log `/Users/mfwolffe/lanes/tr02/logs/mac-build.log`. Actual play binary built at this head, pid 46414 exited; no Mac test loops.

No engine change or new issue action: lair#13 remains filed; physical keyboard/font qualification remains owed. Planning clarification only: an exact vertical reflection turns north `▘/▝` into south `▖/▗`; the implementation/test keeps that mirror literal. Planning and memory files untouched.

After play/merge cleanup candidates: `/Users/mfwolffe/lanes/tr02/` and `/home/mfwolffe/lanes/tr02/` only. Keep the play tree/evidence for now. No running job; no prior lane tree touched.

Pruned only generated tr02 Linux target/{goldens,gameplay,natural-route,record-witnesses,baseline-80,baseline-200,baseline-natural}. Committed goldens, logs, binaries, toolchains and pty captures retained. Prior lane trees untouched.

