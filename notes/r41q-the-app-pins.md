# r41q — trail to lair `df11d213` (wolf 0.2.36 / lupin 0.1.58)

_trail's part of r41q (the apps, the games and the docs to the published pair), after the engine's (lair#26)._

## Prediction

Written before the first change (2026-11-01, base trunk at `lair.pin` `57870143`).

- `lair.pin` moves `57870143` to **`df11d213`** (lair trunk, read twice): 32 engine commits, lr03's held
  keys, lr04's strict keyboard-control grammar and r41q's toolchain pin. trail opts into neither input mode
  (lair's README: a pin bump alone does not switch a game's input), so no frame moves.
- The engine's own toolchain file at `df11d213` names wolf 0.2.36 / lupin 0.1.58 / std `78b9d3cb` (lair#26,
  r41q's engine half): `.lair/tools/fetch-toolchain` accepts the linux x86-64 archives by digest and
  `.lair/tools/lib-toolchain.sh` accepts `wolf 0.2.36 (wolfgang, pin 5adf3d9)`, `lupin 0.1.58 (wolf-interp,
  reference interpreter at pin a5378e3)` and `STD-REV` `78b9d3cb`. No source here declares the names 0.2.36
  adds to the prelude (`VaList`, the four `va_*`, `env_arg0`, `env_args_bytes`), so `--deny-warnings` sees
  no W0304.
- `tier pr` stays green: **92 tests** (trunk's 77 plus the **15** engine tests lr03 and lr04 add to the ten
  modules trail links), zero SKIPs, both builds, **166 golden lines ok, zero DIFFERS** (byte for byte),
  **13 pty rows ok**, the gameplay and glyph checks.
- `tier full` adds the macOS leg (the goldens and rows on the second host) and the perf gate; the
  orchestrator labels and watches it.
- The README's "77 checked unit tests including the pinned engine" moves to 92 (a README-only commit).

## Forbidden

No merge, label, tag, release, issue filed or closed; no attribution trailer. No build on the Mac; local
runs on hasu block B alone, both lock names held per run; kasumi not touched. No other implementation's
source read. No source, test, golden, tool or workflow of trail changed: `lair.pin` and the README's test count, this note and nothing else.

## Inputs verified

- Base: trail trunk `59050227`, as the contract read it on 2026-10-31; trunk's last nightly (41194756172)
  green at the old pin with 77 tests (30 trail's, 47 the engine's), 166 golden lines, 13 pty rows.
- The engine between `57870143` and `df11d213`: 32 commits, lr03's held keys and lr04's strict
  keyboard-control grammar in `src/` (8 files), plus r41q's toolchain pin. trail opts into neither input
  mode, so no frame should move; the gauntlet and `tier pr` hold every golden to it.
- What waits for this pin: nothing in trail's notes or README names 0.2.36 or the next pin; its two open
  issues (#7, #8, the glyph inventory) do not wait on it.
- README read: "77 checked unit tests including the pinned engine" moves to **92** (30 trail's, 62 the
  engine's), a README-only commit; its 83 golden directories and thirteen pty rows do not move.
- lair trunk read twice before the pin was written (`git ls-remote` at 00:55:19Z and 00:55:21Z, and the
  commits API): `df11d213785f7694bdf3f3572299abc550d8b903`, lair#26's merge (r41q's engine half). The
  digests behind it are lair#26's: the release API read twice, every pinned archive hashed twice, the
  identities read from the archives; this repo's gauntlet holds the staged `.lair/wolf-toolchain.toml` to
  the same two API passes by script (`engine-pin`).
- 0.2.36's prelude names (`VaList`, the four `va_*`, `env_arg0`, `env_args_bytes`): declared in no `.lu`
  file here, so no W0304 under `--deny-warnings`.

## Evidence index

- `af51bb6` Predict lair.pin at df11d213 moves no frame
- `ca22bd4` lair.pin: the engine at df11d213 (wolf 0.2.36 / lupin 0.1.58)
- `973d12e` README: 92 checked unit tests with the engine at df11d213 (README only)
- The gauntlet at the final head, on hasu block B (`/home/mfwolffe/lanes/r41q/bin/gauntlet-game.sh trail
  <sha>`, its log under `/home/mfwolffe/lanes/r41q/logs/`): the head asserted, `lair.pin` against lair's
  trunk read live, `tools/fetch-lair` (the
  staged `LAIR-REV` asserted), the staged engine's toolchain file proved against the API passes, the
  planner's tests, the image `localhost/r41q-pack-ci:fbee7e864f7dbee6`, `.lair/tools/fetch-toolchain`, then
  `tools/check-linux` in the container on CPUs 6-11, and the count (every test ok, zero FAILED, zero SKIP,
  the game's and the engine's split by path). Every step prints `END <step> exit=N`; the wrapper stops at
  the first nonzero one. The END lines and the counts are in the PR body.

## Done-when

The PR is open at its final head with `tier pr` green there, `Footprint: cross-cutting` (a pin), the audit
run once and passing but for the labelled `tier full`, which the orchestrator labels and watches (the
second host's goldens). Nothing to close or file here.
