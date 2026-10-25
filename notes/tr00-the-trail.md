This body carries the complete note for materialisation as `notes/tr00-the-trail.md`: the wrapper prohibits Markdown report files. Current implementation head: `6dbe253fad3c73225c547a036aa8ec786abd91dc`. The initial implementation evidence below is retained, followed by the card-start correction.

## Prediction

Committed before implementation in `6a93a35`: expected 34.5–35.5% hits over 10,000 seeded strikes (required 33.5–36.5%); 200x60 plain render+diff below 3 ms; engine noise would need game-side soil scatter.

Measured **3403/10000 = 34.03%**: outside the narrow prediction, inside the required band. The final-head kasumi plain 200x60 budget is **159 us average, 252 us p99, 400 us max**, against a 4,000 us gate and 33,333 us tick. Original hash-scattered clods and rocks over engine noise supply the soil floor.

## Forbidden

Only cub's tooling/CI scaffolding and the pinned lair modules were reused. Simulation, sprites, art, cards and game text are original; no snake implementation or third-party game assets were read. The explicitly permitted pack path drawing was read for the house ground-texture shape, not copied.

No engine, planning-repo or user-configuration edits; no packages, labels, merges, tags, releases or issue actions; no attribution trailers. No maintainer server was touched. All tests/builds except the initial and expressly requested card-fix/gait Mac play builds ran on kasumi CPUs 8–11 under `/home/mfwolffe/lanes/kasumi-cores-8-11.lock`, taskset and the staged engine container. Every process was waited for; no process was killed. The initial Mac release build passed the scripted 8 GiB floor at 10.19 GiB; the requested card-fix rebuild passed at 12.24 GiB. No Mac tests, goldens or pty loops ran.

## Inputs verified

- Base `c353dfc3`; engine trunk **`57870143ebbb4806b8bee40379e8c6e781f50842`**, read twice, unchanged in `lair.pin`.
- wolf 0.2.35 `cf0c13d38479f444b69bb8356ad5709d07eff323`; lupin 0.1.56; std `2386522eb059cca5a84108562c2c0a0e72345d34`. Both host archive pairs' release digests read twice and independently verified by the fetchers; complete archives staged, including runtime libraries. The engine build's `WOLF_MIDEND=0` workaround is retained.
- Contract, revised soil premise and trail/pack/cub campaigns; engine/replay docs; cub scaffold and coast note; house design/art/glyph/palette/key docs; pack path drawing; lane rules and wolf guide.
- Campaign R-TR-1/2 ruled A; R-TR-3/4/5 implemented as recommended, not newly decided.

New recommendations, implemented pending review (none is a lane decision):
- **R-tr00-1 A:** keep the initial logical board across SIGWINCH and re-centre the layout only. Avoid remapping collisions or changing the seeded rules because a window moved. `--size` keeps a fixed layout.
- **R-tr00-2 A:** show the latest sixteen rolls and total strike/survival counts on the death card; reconstruct the full history from seed and replay. Bound long-run HUD storage.
- **R-tr00-3 A:** use explicitly labelled numeric scene fixtures for rare-state goldens, plus an independent ordinary-key long witness and real pty recordings. Never describe fixtures as recordings.
- **R-tr00-4 A:** use CI's macOS full-tier leg as the second-host pty/golden evidence. The host grant forbids local Mac test loops; only its final play build was run. This evidence is still owed until the coordinator runs/watches that leg.
- **R-tr00-5 A:** use a five-column/three-row logical cell, rotating a single five-by-five pixel wolf before half-block packing. Four legs and a head fit the 40x12 minimum with identical rich/plain footprints.
- **R-tr00-6 A:** score 100 per meal, 25 per missed eagle, no passive time score. Values are documented for tuning by play.

Engine workaround: `term.open` and `term.resize` hard-code 80x24. Trail validates 40x12 using std, constructs the engine's public terminal state and reads layout resizes game-side. Engine enter/leave, signals and runtime restore remain unchanged. A configurable-minimum engine API is a possible follow-on, not a blocker or an engine edit here.

## Evidence index

Implementation chunks:
- `6a93a35`: prediction before code; `e935c12`, `4f2e071`: scaffold and its five pty rows.
- `cdef4d9`: pure seeded simulation, bounded ring deque and rule tests.
- `96168be`: original rotated solid-block wolves, soil, sprites/cards and art tests.
- `924bafc`: clock, held keys, live/headless, recording/replay, perf; `550cd14` removes accidentally staged compiler cache outputs and ignores them.
- `de279a9`: always-visible odds and extreme soil seeds; `428d8f0`: goldens, pty rows, two recordings and ordinary-key witness.
- `2fabc41`: bounded negative-test searches; `49718ea`: complete docs and both-way rendered glyph inventory; `aeca5ac`: README-only refresh.
- `2ded66e`: hold latching after same-tick arrows, with a next-tick regression assertion; `9aca470`: single Mac play-build identity.

The initial implementation Linux checkout was fetched, staged tree-compared to `9aca470e14d4bb5598519dbd128580244e4c0595`, and tested with no working-tree diff. Direct exit 0 is retained at `/home/mfwolffe/lanes/tr00/final-head-linux.exit` and `/Users/mfwolffe/lanes/tr00/logs/final-head-linux.exit`; full logs at the matching `.log` paths. Earlier source/scaffold/plant logs are committed under `notes/tr00-evidence/`. Mac build identity is `notes/tr00-evidence/mac-play-build.txt`.

| gate | final-head Linux, locked 8–11 container | macOS |
|---|---|---|
| fmt / checked tests | 62 pass, 0 failed/rejected/unsupported/SKIP | CI full leg owed |
| native + release / binary selftest | green | one release play build succeeds; tests owed in CI |
| goldens | 23 scripts x 2 tiers + art = 47 directories, 332 files; both backends identical | CI full leg owed |
| pty rows | ten pass: quit, ctrl-c, trap, agree-rich/plain, title-pause, 40x12, Escape, resize, record-roundtrip | CI full leg owed |
| black-box gameplay / glyph inventory | both backends green | CI full leg owed |
| 80x24 rich/plain average | 31 / 33 us | not measured locally |
| 200x60 rich/plain average | 163 / 159 us | not measured locally |
| input median / p90 | 26.2 / 32.3 ms, repeat 26.7 / 33.2 ms | not measured locally |
| idle / 10 seconds | 301, repeat 300 voluntary switches | not measured locally |

Final performance uses slack **1**. Golden SHA256, sorted relative paths + NUL + bytes: `4b1745012dba5e66872e194e989208f50107565a30fd5d4cd29d51d455e8853e`.

The two actual pty recordings are `tests/replays/recorded-80-rich.pk` (seed 52, score 100, one meal, arrived follower, right-edge wrap) and `recorded-200-plain.pk` (seed 552, score 100, one meal, arrived follower, turn south). Their scores are recomputed, never trusted as comments. `tests/cases/natural-80.pk` has ordinary keys only: 561 ticks, 25 meals, longest trail 23, first eagle hit on roll 3, score 2500. Rare scene fixtures are disclosed separately in `docs/REPLAY.md` and the case comments.

Negative draft PRs, left open and never labelled; named local reds are in the committed logs:
- **#2 wrap:** head `9951acd23d265e26f0d82069d077946b2d6ee06a`, run **40239656143**, expected `test_wrap_all_four_edges_both_axes ... FAILED (trap(assert))`; local 61 pass / 1 fail, exit 1, `notes/tr00-evidence/plant-wrap-linux.log`.
- **#3 always hit:** head `ed402731ce7fecf9152741f48a71fbff50996bcf`, run **40239660507**, expected `test_d20_distribution_10000_seeded_strikes ... FAILED (trap(assert))` (pack-of-one miss also fails); local 60 pass / 2 fail, exit 1, `notes/tr00-evidence/plant-roll-linux.log`.
- **#4 newcomer reapable:** head `deeca048ecf821c2c70541008c1606e8f94de9ce`, immediate one-time run listing returned `[]`; expected `test_running_newcomer_is_immune_to_eagle ... FAILED (trap(assert))`; local 61 pass / 1 fail, exit 1, `notes/tr00-evidence/plant-immunity-linux.log`. Coordinator must obtain its run id and observe all three named CI reds; the lane did not wait or poll.

The initial-head immediate one-time CI read returned `[]`. The required audit subsequently identified **40240364449**, completed success at the exact final head, **tier pr**. No CI wait, poll or label occurred in this lane.

The initial required audit ran once at head 9aca470, direct exit 1, retained at `/Users/mfwolffe/lanes/tr00/logs/audit.log`. Its last line is **`AUDIT FAIL (footprint: cross-cutting)`**. Ancestry, attribution, footprint, sections, cited shas, PR head, all PR-tier jobs/steps/annotations and orphan checks passed. The two failures are the still-owed **tier full** run (macOS and perf) and the deliberately retained play worktree. The coordinator owns the label/watch; do not remove the play tree before play is accepted.


### Card-start correction, 2026-10-25

- `6edc6da`: both title and death card dismiss on any mapped non-quit key (Enter, Space, all four arrows, r). A starting arrow chooses the first heading, including west; Space dismisses without pausing. Quit/interrupt never start a run. Both cards now say **Enter or any key**.
- `7639b8b`: controls docs, engine gap and README counts refreshed; README read, current (63 tests, twelve pty rows).
- Before fix, `notes/tr00-evidence/card-before-linux.log` records `test_card_start_keys_enter_gameplay_without_pausing ... FAILED (trap(assert))`, unit exit 1, and `pty: title-space FAILED`, exit 1; CR already passed. After fix, `notes/tr00-evidence/card-after-linux.log` records all green. The unit row crosses title/death phases with every starting key plus quit/interrupt exceptions. Separate `title-cr` and `title-space` rows inject actual bytes without --no-title and assert the first gameplay HUD/controls, no title, no pause, and a carrying frame.
- Exact current head `7639b8b508bf3d1fe8f14f64413345503a4ea10f` fetched/tree-compared on kasumi: complete `tools/check-linux` direct exit 0. 63 tests; both backends; 47 golden directories; twelve pty rows; two score-100 recordings and the score-2500 ordinary-key witness still verify. Logs: `/Users/mfwolffe/lanes/tr00/logs/card-final-head-linux.log` and matching `.exit`, also `/home/mfwolffe/lanes/tr00/card-final-head-linux.log`. Only the eight title/death golden directories changed; death visual fixtures no longer inject a start key which would immediately dismiss them.
- One expressly requested Mac release rebuild at this exact head, vm_stat conditional 12.24 GiB >= 8 GiB. No Mac tests or pty loops. Binary `/Users/mfwolffe/lanes/tr00/trail/target/trail`, SHA256 `fe6ca9c1875c3f262128530f7c41f533ca529f9349b875dc63ebab40b30b1a9a`. Build log `/Users/mfwolffe/lanes/tr00/logs/card-mac-build.log`.
- **Engine issue for the coordinator to file on lair:** decode CSI-u Enter/arrows/Escape/Space to the same keys as their legacy forms instead of recognising and ignoring them. Ghostty CSI-u Enter `ESC [ 13 u` still cannot start this pinned decoder; this patch does not claim enhanced-protocol support or alter lair. Include lair term.open/resize's hard-coded **80x24** minimum in the engine follow-up; trail's game-side minimum remains 40x12.
- Pushed with `git push origin HEAD:tr00`. Immediate one-time new-head CI listing returned `[]`; the required new-head audit identified run **40241573729**, in progress. Audit direct exit 1; last line **`AUDIT FAIL (footprint: cross-cutting)`**. Its only failures were the still-running head run and the intentionally retained play worktree; ancestry, sections, shas, attribution and orphan checks passed. Log: `/Users/mfwolffe/lanes/tr00/logs/card-audit.log`. No label or CI wait by the lane.


### Wolf gait revision, 2026-10-25

- Read pack's own `src/sprites/sprites.lu`, `docs/ART.md`, art draw path and `sim.trot_frame` at pack trunk `278480955f7c088b40b9f2cdd57565ece8f4a865`: four leg frames tied to travelled distance, and tail variants. No pack files or masks copied. Trail's new original mask has a long solid torso, a forward snout, ears, four separately swinging feet and a tail; every semantic part is turned together for four headings.
- **Footprint stays 5x3**, with the same logical board, wrapping, self-collision and strike tests. No footprint ruling or collision adjustment was needed. Leader bright/bold, followers grey, newcomers gold remain distinct.
- Every wolf has its own travelled-cell counter: one contact-phase advance per accepted cell movement, including wrap. Four distinct contact frames on both rich/plain, exact occupancy parity and rotation tests. The tail changes side between consecutive four-contact strides: one full sway per stride pair (eight travelled cells). Newcomers use the same gait from accumulated approach distance in 1/256-cell units; the final approach segment is counted and its contact phase is retained on joining. Pause freezes pack gait, approach position, runner gait and tail; idle ticks never advance them.
- `acde458` implements the original mask/gait, distance accounting and tests; `fe4ec02` pins all-heading contact goldens and the negative witness; `7218d6a` documents the trot; `6dbe253` is the README-only refresh. README read and current: **66 tests, 31 cases x two tiers plus art = 63 directories / 436 files**, twelve pty rows. Art study now has a four-heading/four-contact sheet plus the opposite tail sway and a separate props companion, on both tiers at both sizes. Eight ordinary-key stride cases pin contact phase one after one cell in every heading/size; no scene injection in those cases.
- The locally planted tick-driven gait failed **`test_leg_phase_tracks_cells_not_ticks_and_pause_freezes_run_in`**, direct exit 1, `notes/tr00-evidence/gait-tick-plant-linux.log`. Corrected unit, native/release builds, binary selftest, goldens, pty and gameplay pass in `gait-full-linux.log` / `gait-nose-linux.log`. The arrival-phase row checks the newcomer's final half-cell segment, not merely a nonzero phase.
- Exact final head **`6dbe253fad3c73225c547a036aa8ec786abd91dc`** fetched and staged-tree-compared on kasumi; `tools/check-linux` plus slack-1 performance direct exit **0**, `/Users/mfwolffe/lanes/tr00/logs/gait-final-head-linux.log` and matching `.exit` (also `/home/mfwolffe/lanes/tr00/gait-final-head-linux.log`). 66 checked tests, zero failed/rejected/unsupported/SKIP; both-backend 63-directory goldens and gameplay; all twelve pty rows including title CR and Space. Recorded scores 100/100 and the ordinary-key score 2500 remain unchanged. Final plain 200x60 render+diff: **147 us average, 176 us p99, 305 us max**; rich average 161 us, against the 4000 us frame gate.
- One expressly requested Mac release build at this final head: scripted memory gate **17.71 GiB >= 8 GiB**, build pid 86813 exited, no Mac test loop. `/Users/mfwolffe/lanes/tr00/trail/target/trail`, SHA256 **`349609ab20279892ff6e532bde35381370e078907167b2d1b2861d1b4ea9bf71`**. Build log `/Users/mfwolffe/lanes/tr00/logs/gait-mac-build.log`. Play `/Users/mfwolffe/lanes/tr00/trail/target/trail --seed 52 --size 80x24`; add --plain for the other tier. The earlier Mac identities above are historical revisions, not this binary.
- Pushed `HEAD:tr00`. Immediate one-time new-head CI listing returned `[]`; the required final-head audit subsequently observed **40242634284**, completed success, **tier full: 4 of 4 jobs**, including macOS goldens/pty and performance. Every job/step and annotations check passed. Audit direct exit 1, last line **`AUDIT FAIL (footprint: cross-cutting)`**: its sole failure is the intentionally retained play worktree. Log `/Users/mfwolffe/lanes/tr00/logs/gait-audit.log`. No label, CI wait or polling by the lane. The CSI-u Enter/arrows/Escape/Space mapping gap and engine's hard-coded 80x24 minimum remain explicitly owed to lair; no engine change was made.

## Done-when

- [x] Original playable game on the pinned engine, rich/plain, 40x12 minimum, seeded replay/recording, all specified rules and art.
- [x] Current-head Linux fmt, 66 checked tests, both builds/selftest, both-backend 63-directory goldens, twelve pty rows and gameplay.
- [x] Two recorded replays with pinned scores; ordinary-key first-eagle witness; three locally named red drafts left open.
- [x] Docs complete, README read and current; one memory-gated Mac play build retained.
- [x] Final-head PR tier green: audit observed run 40240364449.
- [x] Final gait head full-tier CI green, including macOS and perf: 40242634284.
- [ ] Coordinator confirms/closes the original three negative drafts and accepts play.
- [ ] Coordinator materialises this note, applies any required full-matrix label at the final head, watches CI, closes the three negative drafts unmerged and merges only on green.

Play: `/Users/mfwolffe/lanes/tr00/trail/target/trail --seed 52 --size 80x24` (add `--plain` for the other tier). Enter starts; arrows turn; Space pauses; q/Escape quits. Current binary SHA256 `349609ab20279892ff6e532bde35381370e078907167b2d1b2861d1b4ea9bf71`.

Pruned now: exact clean Mac plant worktrees `/Users/mfwolffe/lanes/tr00/plant-{wrap,roll,immunity}` individually, without force; Linux regenerated `trail/target/{goldens,gameplay,natural-route,record-witnesses}` only. Committed evidence, logs, toolchains, binaries and pty captures remain. After play/merge, cleanup candidates are `/Users/mfwolffe/lanes/tr00/` and `/home/mfwolffe/lanes/tr00/` only; keep the play worktree until accepted. No job remains running.

To file/correct, without issue actions by this lane: lair configurable terminal minimum if desired; trail's physical font/keyboard measurements and PAX installer are follow-ons. The planning campaign's sprite paragraph still says forest/trunks despite its revised premise; R-TR-2's option text says “1-in-3” beside 1–7/20. Soil and exactly 35% were implemented. No planning or memory file was changed.



