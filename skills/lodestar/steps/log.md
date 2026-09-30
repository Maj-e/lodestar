# 1. Log — know where we sail

### 1a. Heading
Find the source of truth for this feature (see project rules, Tickets). Quote it.
Write the goal in ONE sentence and a "done when" line. If the goal does not fit in one sentence, stop and ask.

### 1b. Scope
If the project rules name a backlog, read it ONCE, here, in full. Classify each item of the ticket:
already done elsewhere · redundant with <ticket> · deferred to <ticket> · depends on <ticket/person>.
Output an in-scope / out-of-scope table with one reason per line, citing the ticket each time.
Nothing enters scope without a line in the ticket. The table is what later sessions read — never reread the backlog.
Backlog "none": say so in the table header ("no backlog — redundancy not checked") and classify from the ticket alone.

### 1c. Lexicon check
List the jargon this feature needs, tagged `stack` or `product`, as `<subject>/<concept>` keys.
Look each one up with `grep -i` in ~/.claude/lodestar/lexicon.md, on the key AND its likely aliases; for a whole
subject, `grep -i '^<subject>/'`. Never read the whole lexicon.
No lexicon yet: create it from templates/lexicon.md — every term then counts as unknown until the user says otherwise.
Decide per entry:
| level | decision |
|---|---|
| mastered | skip |
| understood, checked < 6 months ago | one-line reminder, skip (open `where` only if the user asks) |
| understood older, or heard | one check question; if it misses, it becomes a study block |
| unknown or absent | study block |
Ask the user ONCE, grouping the check questions. Study blocks become sub-blocks on the archipelago map.
After Theory, write each studied entry back: level demonstrated, today's date, `where` = the island summary
in this voyage's archive.md. Update an existing line; never add a second line for the same key.
This is the spaced revision: a concept is re-checked when a voyage needs it again after six months — never on a
schedule of its own.

### 1d. Theory — the most important part

**Map the archipelago first.** Break the feature into islands (major blocks). Each island may hold sub-blocks,
which may hold their own. Every island states, in one sentence, how it serves the heading; an island that cannot
is out of scope — move it to the scope table with its ticket. Write the map as a nested list in passage-plan.md
before studying anything, in the template's shape: each island opens with its nature (🏝️ ordinary · 🌋 irreversible ·
🏰 security · 🌫️ open questions), and `⛵` moves to the block being studied — on exactly one line.

**One concept per message.** Never explain several concepts in one block. You may first list the topics
ahead (titles only, no explanation), then explain ONE, small and plain, and stop.

**Study depth-first.** Master every sub-block of an island before the next island. For each block, cover what applies:
purpose · users and the decision it serves · what it adds · what it interacts with (inputs, dependents, what breaks) ·
stakes and what is irreversible · domain concepts in plain words.
Every claim points to a file:line or a document, and is marked ✔ verified (read it) or ≈ assumed (inferred).
No concept without an anchor.

**Open questions.** What neither of us can settle by reading goes to the Open questions table:
question · who can answer · what it blocks. It does not block the study.
When the documentation can settle it (a library, an API, a standard), send the researcher (SKILL.md, The crew) in
the background with the question alone; its file lands in `.claude/lodestar/<feature>/research/`. Keep studying;
bring its answer in when it arrives, marked ✔ only for what it quotes.

**After EVERY block — never propose moving on:**
1. Check understanding: ask the user to restate it in their own words; then ask questions only on what the
   restatement missed or got wrong.
2. Recap: list every block covered so far, marked on the map (✓ understood · ⛵ current).
3. Ask whether they want to revisit any of them.
Move on only when the user says so. The user sets the pace, not you.

**Island summary, then compaction.** When an island is fully ✓:
1. The USER writes 3 lines under it in passage-plan.md: what it does · why · what is dangerous.
2. Move that island's theory notes to archive.md (under a heading with the island's name). In passage-plan.md,
   keep the map line, the user's summary, and the anchors (file:line) the Pose step will need.
3. Tick the island, move `⛵` to the next island's first block, and show the chart with the boat under way
   (SKILL.md, The chart, `--transit`). The chart IS the recap at an island's end — do not also list the blocks.

GATE: Pose starts only when every block on the map is ✓. Then set `Stage: Pose` and read `steps/pose.md`.
