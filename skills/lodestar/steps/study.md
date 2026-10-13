# 3a. Study — understand this island before its code

Read only when the plan says `Island phase: Study`. Covers the current island alone; the others wait.

### Lexicon check — this island's concepts
Take the concepts listed under this island in the Survey notes, tagged `stack` or `product`, as `<subject>/<concept>`
keys. Look each one up with `grep -i` in ~/.claude/lodestar/lexicon.md, on the key AND its likely aliases; for a
whole subject, `grep -i '^<subject>/'`. Never read the whole lexicon.
No lexicon yet: create it from templates/lexicon.md — every term then counts as unknown until the user says otherwise.
Decide per entry:
| level | decision |
|---|---|
| mastered | skip |
| understood, checked < 6 months ago | one-line reminder, skip (open `where` only if the user asks) |
| understood older, or heard | one check question; if it misses, it becomes a study block |
| unknown or absent | study block |
Check one concept at a time, never a grouped list or a level menu: ask the user to explain what they understand
of it, and deduce the level from the explanation — a level shown, not declared. An answer that does not say what
the concept is ("it's SQL stuff") is not an explanation: ask for one, once. Study blocks become sub-blocks of the
island on the map.
After the island, write each studied entry back: level demonstrated, today's date, `where` = the island summary
in this voyage's archive.md. Update an existing line; never add a second line for the same key.
This is the spaced revision: a concept is re-checked when a voyage needs it again after six months — never on a
schedule of its own.

### Theory — the most important part

**One concept per message.** Never explain several concepts in one block. You may first list the topics
ahead (titles only, no explanation), then explain ONE, small and plain, and stop.

**Depth-first.** Master every sub-block of the island in order. Open each block with why we look at it for THIS
ticket — what it changes, or does not, in the work — before explaining anything.
For each block, cover what applies:
purpose · users and the decision it serves · what it adds · what it interacts with (inputs, dependents, what breaks) ·
stakes and what is irreversible · domain concepts in plain words.
Every claim points to a file:line or a document, and is marked ✔ verified (read it) or ≈ assumed (inferred).
No concept without an anchor.

**Open questions.** What neither of us can settle by reading goes to the Open questions table. If it touches an
island already built, or a decision already settled, it is a course change (steps/sail.md, Stay on the route).
When the documentation can settle it, send the researcher (SKILL.md, The crew) in the background; keep studying.

**When the user is stuck**, do not reword the same explanation: take one real case end to end — the rows in the
database, the code that reads them, what the screen shows.

**After EVERY block — never propose moving on:**
1. Check understanding, in proportion to what can be misunderstood. A block that can be misread: ask the user to
   restate it in their own words, then ask only about what the restatement missed or got wrong. A trivial block,
   or a concept already `understood` in the lexicon: one line, then offer to tick it — a question asked for form's
   sake is noise.
2. Recap: list every block of the island covered so far (✓ understood · ⛵ current).
3. Ask whether they want to revisit any of them.
Move on only when the user says so. The user sets the pace, not you. When the boat moves to the next block, tick the
one left, update the fix (SKILL.md, Keeping the fix current), then show the chart.

GATE: when every block of the island is ✓, set `Island phase: Waypoints` and go back to `steps/sail.md`.
