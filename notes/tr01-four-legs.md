Current head: `e658f5b26c2385eb2a3ff965cc16847749e0b906`. Complete note for materialisation as `notes/tr01-four-legs.md`; the wrapper prohibits Markdown report files.

## Prediction

Committed before implementation in `4a4ced3`: four separated leg columns need seven columns; expected exactly four visible feet in every phase, floor cells between them, straight body top/belly, alternating diagonal pairs, and 200x60 plain render+diff below 1 ms. All measured bars pass locally. The initially predicted raised/shortened contacts were deliberately replaced with full-height fore/aft sweeps: four legs remain obvious in every phase. The hit roll remains 3403/10000 (34.03%).

**Recommendations implemented, not lane decisions:**
- **R-tr01-1:** use a **7x3 east/west sheet**, mirrored for west, and the same construction literally quarter-turned to **3x7 north/south**. Reserve a **7x7 logical collision envelope** so perpendicular neighbouring wolves cannot overlap. A 7x3 logical envelope cannot contain its own quarter-turn; compressing it would lose separated feet again.
- **R-tr01-2:** minimum **40x16**, retaining at least two seven-row logical cells plus HUD/controls. The former 40x12 cannot contain two quarter-turned wolves. 80x24 is now 11x3 logical cells; 200x60 is 28x8. The four wrap/self-collision rules are unchanged, but seeded placement and old-geometry replay scores necessarily change.

## Forbidden

Original game sheets and draw code; no external game code/assets. No engine/pin/workflow/planning/configuration edits, packages, labels, merges, tags, releases or issue actions; no attribution trailers. Module plants ran locally only, not in CI. Builds/tests on kasumi CPUs 8–11, taskset and `/home/mfwolffe/lanes/kasumi-cores-8-11.lock`, inside the staged engine container. Exactly one Mac release play build, behind scripted vm_stat floor (15.81 GiB >= 8 GiB); no Mac tests, golden generation or pty loops. All processes waited for, no kills or maintainer-server changes.

## Inputs verified

Base trunk `0c740f8` is merged game `6dbe253` plus the materialised tr00 note. Engine remains `57870143ebbb4806b8bee40379e8c6e781f50842`, unchanged, with the same verified complete wolf 0.2.35/lupin 0.1.56 archive pairs and std `2386522eb059cca5a84108562c2c0a0e72345d34`.

The play finding is the oracle: no central body line and only two noticeable legs. The replacement has a five-cell solid horizontal body bar, a forward head block with quarter-cell ear notch, a rear one-cell tail stroke, and four full-height half-cell legs at columns 0/2/4/6. Three whole floor cells separate them in **every** phase; none is hidden or reduced to a quarter-height stub. Front-left/back-right move together, then the other diagonal. Four distinct phases remain tied to travelled distance; tail sway, newcomers and pause freeze retain tr00's distance model. Plain uses the same occupancy/orientation with #, | and . contacts.

## Evidence index

- `83ba2e0`: original body/leg construction, quadrant turns, 7x7 geometry and independent tests; extended font inventory (17 reachable non-ASCII glyphs).
- `b4620fe`: all oriented sheets, rare-state and ordinary-key goldens; refreshed pty recordings and executable-level expected geometry.
- `3a5bf01`: geometry recommendations, frame data and local red/green evidence; `e658f5b`: README-only refresh, read/current.
- Locked Linux complete source gate: `notes/tr01-evidence/final-source-linux.log`. **67 checked tests**, 0 failed/rejected/unsupported/SKIP; native/release and binary selftest; **31 cases x two tiers plus art = 63 golden directories, 424 files**; twelve pty rows, including the new 40x16 minimum and both title-start keys; both-backend gameplay and 17-glyph inventory. Slack-1 plain 200x60: **144 us average, 177 us p99, 325 us max**, gate 4000 us. Exact final head `e658f5b26c2385eb2a3ff965cc16847749e0b906` was fetched and staged-tree-compared on kasumi, then complete `tools/check-linux` plus slack-1 perf passed, direct exit 0. Logs `/Users/mfwolffe/lanes/tr01/logs/final-head-linux.log` and matching `.exit`, also `/home/mfwolffe/lanes/tr01/final-head-linux.log`. Final-head plain 200x60: **156 us average, 230 us p99, 350 us max**. Immediate one-time CI read returned `[]`; the required audit subsequently observed **40245217270**, completed success, **tier pr**. Module footprint, all paths, CI jobs/steps/annotations, sections, shas, ancestry and orphan checks passed. Direct audit exit 1; last line **`AUDIT FAIL (footprint: module)`**. The sole failure is the intentionally retained play worktree. Log `/Users/mfwolffe/lanes/tr01/logs/audit.log`. No CI wait or label.
- Regenerated recordings use seeds **9** (80x24 rich) and **206** (200x60 plain), each score **100**, one meal and an arrived follower. New ordinary-key 200x60 witness: **728 ticks, 12 meals, longest pack 12, first eagle roll 3, score 1200**. Old-geometry replays are not claimed to preserve scores. `notes/tr01-evidence/witnesses-linux.log` retains the real recorder output.
- Art study: 16 heading/tier/size sheets plus four props companions. `tools/sprite-frames.py` extracts the literal committed sheet cells below. `notes/tr01-evidence/frames.txt` is the retained raw extraction, not a hand transcription.

Local module plants, all direct exit 1 (no CI dispatch or negative PR):
- Leg columns moved onto the intervening floor: `test_wolf_body_bar_and_four_separated_leg_columns ... FAILED (trap(assert))`, `notes/tr01-evidence/plant-legs-linux.log`.
- Collision envelope reverted to five: `test_oriented_sprite_envelope_matches_collision_cell ... FAILED (trap(assert))`, `notes/tr01-evidence/plant-envelope-linux.log`.
- All legs assigned one pair: `test_four_contact_frames_move_diagonal_pairs_without_hiding_feet ... FAILED (trap(assert))`, `notes/tr01-evidence/plant-diagonal-linux.log`.

### Literal sheet frames

Columns are phases 0 / 1 / 2 / 3. Middle dots are floor, not parts of the wolf.

```
RICH
EAST  phase 0 / phase 1 / phase 2 / phase 3
▖·····▟   ▖·····▟   ▖·····▟   ▖·····▟
▐██████   ▐██████   ▐██████   ▐██████
▐·▌·▌·▐   ▐·▐·▐·▐   ▌·▐·▐·▌   ▌·▌·▌·▌

WEST  phase 0 / phase 1 / phase 2 / phase 3
▙·····▗   ▙·····▗   ▙·····▗   ▙·····▗
██████▌   ██████▌   ██████▌   ██████▌
▌·▐·▐·▌   ▌·▌·▌·▌   ▐·▌·▌·▐   ▐·▐·▐·▐

NORTH  phase 0 / phase 1 / phase 2 / phase 3
▜█▀   ▜█▀   ▜█▄   ▜█▄
·█·   ·█·   ·█·   ·█·
·█▄   ·█▀   ·█▀   ·█▄
·█·   ·█·   ·█·   ·█·
·█▄   ·█▀   ·█▀   ·█▄
·█·   ·█·   ·█·   ·█·
▗▀▀   ▗▀▀   ▗▀▄   ▗▀▄

SOUTH  phase 0 / phase 1 / phase 2 / phase 3
▄▄▘   ▄▄▘   ▀▄▘   ▀▄▘
·█·   ·█·   ·█·   ·█·
▀█·   ▄█·   ▄█·   ▀█·
·█·   ·█·   ·█·   ·█·
▀█·   ▄█·   ▄█·   ▀█·
·█·   ·█·   ·█·   ·█·
▄█▙   ▄█▙   ▀█▙   ▀█▙

PLAIN
EAST  phase 0 / phase 1 / phase 2 / phase 3
......#   ......#   ......#   ......#
#######   #######   #######   #######
#.|.|.#   #.#.#.#   |.#.#.|   |.|.|.|

WEST  phase 0 / phase 1 / phase 2 / phase 3
#......   #......   #......   #......
#######   #######   #######   #######
#.|.|.#   #.#.#.#   |.#.#.|   |.|.|.|

NORTH  phase 0 / phase 1 / phase 2 / phase 3
###   ###   ##|   ##|
.#.   .#.   .#.   .#.
.#|   .##   .##   .#|
.#.   .#.   .#.   .#.
.#|   .##   .##   .#|
.#.   .#.   .#.   .#.
.##   .##   .#|   .#|

SOUTH  phase 0 / phase 1 / phase 2 / phase 3
##.   ##.   |#.   |#.
.#.   .#.   .#.   .#.
|#.   ##.   ##.   |#.
.#.   .#.   .#.   .#.
|#.   ##.   ##.   |#.
.#.   .#.   .#.   .#.
###   ###   |##   |##

```

## Done-when

- [x] Clear body bar/head notch/tail, four separated full-height legs in all phases; same construction mirrored/quarter-turned for all headings.
- [x] Collision geometry and minimum follow the recommended sheet; all four-heading mid-stride and both-tier art studies regenerated.
- [x] Locked Linux fmt, 67 tests, both builds, goldens, twelve pty rows, gameplay, glyph inventory and slack-1 performance green; three named local plants red.
- [x] Docs and README current; one memory-gated Mac play build at this head.
- [x] Final-head module PR tier green, run 40245217270.
- [ ] Coordinator reviews R-tr01-1/2 and frames, accepts play and materialises the note. No label required for this module PR.

Mac binary: `/Users/mfwolffe/lanes/tr01/trail/target/trail`, SHA256 **`59a969212a01f32ef2477449684f8a5fcd24a8eff86c25d36b6faabe03890746`**. Play `/Users/mfwolffe/lanes/tr01/trail/target/trail --seed 206 --size 200x60` (for an 80x24 terminal, `--seed 9 --size 80x24`). Build log `/Users/mfwolffe/lanes/tr01/logs/mac-build.log`.

No engine issue added here: CSI-u key mapping and configurable minimum remain the earlier lair follow-ups. New glyph widths/physical terminal/font qualification remain owed. After play/merge cleanup candidates are `/Users/mfwolffe/lanes/tr01/` and `/home/mfwolffe/lanes/tr01/` only; keep the play worktree for now. Prior tr00 worktree untouched for comparison. No job running.

Pruned only tr01 regenerated Linux target/{goldens,gameplay,natural-route,record-witnesses}; committed evidence, toolchains, binaries and pty captures retained.

