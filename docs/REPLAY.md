# Replaying the trail

Trail uses the pinned lair engine's `.pk` version 1 parser and recorder.
A file starts with `pk 1`, `seed N`, `tier rich|plain` and `size WxH`.
`t TICK WORD` records a key; `t TICK size WxH` records a layout change.
Ticks never decrease. Keys are `up`, `down`, `left`, `right`, `pause`,
`quit`, `interrupt`, `start` and `restart`. No terminal key-up is invented.
The optional `start` header is zero for trail.

```
pk 1
seed 52
tier rich
size 80x24
# score 100
t 0 start
t 78 quit
```

`target/trail --replay FILE` plays until the last event; q, Escape or
Ctrl-C may leave early. `--ticks N` overrides the endpoint. `--seed`,
`--size` and `--tier` explicitly override the header. `--record FILE`
records ordinary play on exit, including start, quit/interrupt and window
changes, and writes a score comment through the engine. Recording and
replaying in the same invocation are refused rather than losing events.
No record is written after a process trap or machine loss.

Headless verification needs no terminal:

```
target/trail --headless --script tests/replays/recorded-80-rich.pk \
  --frames 79 --every 79 --dump target/replayed
```

The headless run checks the score comment when it reaches the replay's
last event, prints `verified score N`, or fails with `UNVERIFIED` and both
scores. A shorter prefix does not claim verification. `--frames N`,
`--every K` and `--from T` select snapshots; `final.txt`, `final.sty` and
`final.state` always describe the endpoint. The `.state` file contains
tick, rule counters, four seam counts, wolves and meat.

## Fixtures are not recordings

`t TICK scene N` is an explicit test-data channel: 1 summons halfway in,
2 telegraph, 3 hit, 4 miss, 5–8 north/south/west/east seam, 9 death card,
10 busy benchmark. These place a labelled starting state before the
ordinary step; a claimed score in such a file is not evidence of ordinary
play. The rare-scene goldens disclose this channel in their comments.

`tests/replays/` holds two actual pty recordings, each score 100 with one
meal and an arrived follower. `tests/cases/natural-80.pk` is a scripted
ordinary-key run, without scene events: 25 meals, longest pack 23, first
eagle roll 3, final score 2500. The refresh tools are not run by CI.
The integration gate checks all three using both compiled backends.
