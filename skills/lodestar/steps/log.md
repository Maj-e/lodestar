# 1. Log — survey the whole voyage

A short pass over everything, so that what would break another island is known before any island is built.
No deep study here: that happens island by island, in Sail (steps/study.md). Aim for one session.

### 1a. Heading
Find where the project says what this ticket asks for (see project rules, Tickets). Quote it.
Write the goal in ONE sentence and a "done when" line. If the goal does not fit in one sentence, stop and ask.

### 1b. Scope
First say what the ticket asks, in plain words and without ticket codes: what exists today · what we build ·
what we do not. Names first; a code only in brackets after the name. Then the table.
If the project rules name a backlog, read it ONCE, here, in full. Classify each item of the ticket:
already done elsewhere · redundant with <ticket> · deferred to <ticket> · depends on <ticket/person>.
Output an in-scope / out-of-scope table with one reason per line, citing the ticket each time.
Nothing enters scope without a line in the ticket. The table is what later sessions read — never reread the backlog.
Backlog "none": say so in the table header ("no backlog — redundancy not checked") and classify from the ticket alone.

### 1c. Map the archipelago
Break the feature into islands (major blocks). Each island may hold sub-blocks, which may hold their own. Every
island states, in one sentence, how it serves the heading; an island that cannot is out of scope — move it to the
scope table with its ticket. The map's order is the sailing order; Plot may change it.
Write the map as a nested list in passage-plan.md, in the template's shape: each island opens with its nature
(🏝️ ordinary · 🌋 irreversible · 🏰 security · 🌫️ open questions), and the pin `📍` sits on the island being
surveyed — on exactly one line. Nothing is ticked in Log: a block is ticked once studied, an island once built.
The boat `⛵` only appears from Sail on: until the route is approved nobody sails.
Show the proposed map to the user in this shape — each island its own paragraph, one block per line, a blank line
after an island's last block (a numbered list collapses those blank lines, so do not use one):
```
**1 · 🏝️ <island>** — <how it serves the heading>
- <block>
- <block>

**2 · 🌋 <island>** (irreversible) — <how it serves the heading>
- <block>
```

### 1d. Survey each island — one message per island
For each island, in plain words, with `file:line` anchors marked ✔ verified (read it) or ≈ assumed (inferred):
- what it touches: the files or tables it creates or changes
- what it reads, and what it feeds — which other islands depend on it
- whether it is irreversible (data format, migration, published contract, permission name) — then it is 🌋
- the questions it raises, in the Open questions table: question · who can answer · what it blocks · **which
  islands** it touches. A question that touches more than one island is cross-island: Plot settles it before any code.
- the concepts it needs, by title only, under the island in the plan's Survey notes — checked when the island is
  studied, not now.
When the documentation can settle a question (a library, an API, a standard), send the researcher (SKILL.md, The
crew) in the background with the question alone; its file lands in `.claude/lodestar/<feature>/research/`.
No restate loop per island here: say it, answer the user's questions, move on when they say so. Move `📍` to the
next island, update the fix (SKILL.md, Keeping the fix current), show the chart.

### 1e. Restate the whole map
When every island is surveyed, the user restates the voyage in their own words: the islands, in which order, and
which ones could break the others. Ask only about what the restatement missed.

GATE: Plot starts when every island is surveyed and the restatement holds. Set `Stage: Plot` and read `steps/plot.md`.
