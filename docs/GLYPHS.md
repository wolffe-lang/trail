# Glyph inventory

ASCII text, punctuation and the plain sprites need no extended-font row.
The following are all non-ASCII code points used by rich. A pty has no
font: cell-model agreement is not a glyph-width measurement. Physical
Terminal.app, iTerm2, Linux VT and PAX widths remain unmeasured for trail.
Use `target/trail --probe-glyphs` in an 80x24 or larger terminal to collect
the engine's cursor-position-report table; each glyph should be one cell.

| code point | glyph | purpose |
|---|---|---|
| U+00B7 | · | soil fleck and shadow |
| U+2500 | ─ | card horizontal edge |
| U+2502 | │ | card vertical edge |
| U+2580 | ▀ | wolf upper pixel |
| U+2584 | ▄ | wolf lower pixel, eagle |
| U+2588 | █ | solid wolf and meat |
| U+25AA | ▪ | soil clod |
| U+25C6 | ◆ | rock |

The inventory is checked against every rich cell in the golden set, both
ways, including the art sheets. The plain frames are independently held
to Latin-1 and the sixteen-colour palette by the unit tests.
