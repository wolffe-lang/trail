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
