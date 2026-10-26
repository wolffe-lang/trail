# trail

| machine | current build |
|---|---|
| macOS arm64 | play binary; rich/plain terminal renderer |
| Linux x86-64 | container correctness, pty and performance gates |
| PAX | not yet installed or font-qualified; plain uses Latin-1 and sixteen colours |

One wolf on a soil floor, and meat in the open. Eat, and another wolf runs
in from beyond the edge to fall in behind you; the pack is a single trail
that grows with every meal. Eagles come for the last wolf in the line,
and whether they take it is a fair roll you can see. Leave by one edge of
the screen and you arrive from the other, still running. The third game of
the lair, the wolf games collection, on the collection's shared engine
[`lair`](https://github.com/wolffe-lang/lair); the others are `pack` and `cub`.

The game includes all four wrapping seams, arriving wolves, one or two
pieces of meat, the eagle's moving shadow, fixed 35% seeded d20 strikes,
self-collision, title/death cards, pause, replay and recording. Ground is
textured soil with scattered rocks, never a forest or flat fill. Wolves
have a top-down north/south torso with legs on both sides, profile east/west
bodies, moving legs, forward heads/ears and swaying tails. Gait follows distance moved and freezes when paused, also
for arriving wolves. Both tiers keep the same seven-by-seven collision cell, containing a 7x3 or 5x7 sheet.

## Build and play

From this checkout, with git, Python 3 and the host's normal linker tools:

```
tools/fetch-lair
.lair/tools/fetch-toolchain
.lair/tools/build --release
target/trail --seed 9 --size 80x24
```

The fetchers verify the pinned engine commit and toolchain archive digests.
The shipped release build deliberately disables the compiler mid-end,
matching the pinned engine's workaround. No system wolf, curses binding,
other game engine or external art is needed. Licences are GPL-3.0-only and
the separate Training Data Permission in the two licence files.

The terminal must be at least 40x16. `--size WxH` fixes the field;
otherwise it uses the opening terminal size. `--plain` forces ASCII
sprites and sixteen colours; rich is selected for a UTF-8 xterm-like
terminal. `--tier rich` forces rich. Invalid input and small/non-terminal
outputs are refused by name. Terminal mode is restored on normal exits,
interrupts and runtime traps.

| key | action |
|---|---|
| Enter or any mapped key except quit/interrupt | start from the title or retry after death |
| arrows | choose the first heading on a card; turn in play, reverse refused |
| Space | dismiss a card; otherwise pause/resume |
| r | retry the same seed after death |
| q / Escape | quit |
| Ctrl-C | quit and restore |

A meal scores 100. A missed or dodged eagle scores 25. The HUD exposes the last roll
and the fixed caught-wolf threshold, 1–7 on a d20. A positional dodge
consumes no roll. Visible approaches last at least two seconds; self-collision
and the last-wolf capture animate for one second before the death card. The death card shows the score,
longest pack, eagles survived and the latest sixteen rolls.

## Replays and tests

```
target/trail --seed 9 --record run.pk
target/trail --replay run.pk
target/trail --headless --script tests/replays/recorded-80-rich.pk \
  --frames 79 --every 79 --dump target/replayed
target/trail --art-study --dump target/study
```

`tools/check` runs the engine and game gates. On Linux,
`.lair/tools/in-container tools/check-linux` runs them inside the engine's
container (podman by default; `LAIR_ENGINE=docker` for Docker).
`LAIR_CPUS=8-11` pins the container's command where that CPU allocation is
appropriate; coordinate the host's lock before using it. The CI PR tier
runs Linux; the full tier adds macOS and performance.

There are 77 checked unit tests including the pinned engine, 41 cases on
both tiers plus the art directory (83 golden directories), thirteen pty rows,
and executable-level gameplay checks on both compiler backends. Two real
pty recordings each pin score 100; an ordinary-key 14-meal/14-wolf dodge
witness pins 1425. Rare visual-scene fixtures are explicitly labelled,
not presented as recordings. Performance gates bound render/diff time,
idle wake-ups and input latency. Physical terminal font/key measurements
and the PAX installer remain follow-on work.

See [design](docs/DESIGN.md), [art](docs/ART.md), [glyphs](docs/GLYPHS.md),
[palette](docs/PALETTE.md), [keys](docs/KEYS.md) and [replay](docs/REPLAY.md).
