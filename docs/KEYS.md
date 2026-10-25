# Keys and held input

| input | bytes | action |
|---|---|---|
| Up / Down / Left / Right | ESC [ A / B / D / C; also ESC O A / B / D / C | turn the leader |
| Space | 20 hex | start/retry from a card, otherwise pause/resume |
| Enter | 0D or 0A hex | start/retry from a card |
| r | 72 hex | start from title or retry after death |
| q | 71 hex | quit from any screen |
| Escape | 1B hex, alone for 50 ms | quit |
| Ctrl-C | 03 hex typed into a pty, delivered by its line discipline | interrupt and restore |

The engine's Hold reads autorepeats from tick stamps: a tap lasts twelve
ticks, repeats last their measured interval plus one tick. The latest
press wins; byte order breaks ties inside one tick. When all holds expire,
the heading remains the last chosen direction, as a trail game requires.
Reverse is refused even while held. Replays retain each raw press/repeat,
not an invented key-up. Shift+arrows are currently ignored by trail; the
engine decodes them distinctly. Kitty/CSI-u and tilde forms are ignored;
no enhanced keyboard protocol is enabled.

The selftest feeds the real decoder whole sequences and every byte split
on each shipped backend. Linux pty rows inject the keys above; they do not
claim a physical Terminal.app, iTerm2 or Linux VT keyboard measurement.
Those physical rows remain owed. `.lair/tools/keyprobe` is the engine tool
for collecting them; it does not change trail's bindings.

Both cards dismiss on every mapped non-quit key: legacy Enter, Space, any
arrow, or r. A starting arrow chooses that run's first heading, including
west; a starting Space does not pause. Quit/interrupt never start a run.
Separate real-key pty rows send CR and Space without --no-title and assert
the first gameplay frame, not merely a successful process exit.

Known engine gap, reproduced in Ghostty: the current decoder recognises
CSI-u sequences such as ESC [ 13 u but drops them. CSI-u Enter, arrows,
Escape and Space need mapping to the same keys as their legacy forms in
lair. This game does not enable a keyboard protocol or patch the engine;
that input path remains unsupported until an engine fix is pinned.
