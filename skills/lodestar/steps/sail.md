# 3. Sail — island by island: study, plot its waypoints, build

Each island runs the same three phases, named on the plan's `Island phase:` line, then closes before the next one:
**Study** (steps/study.md) → **Waypoints** (3b) → **Build** (3c–3g) → **End of island** (3h).
`Island phase: Study`: read `steps/study.md` and do it first; come back here at its gate.

### 3b. Waypoints — this island's route
1. Decisions of this island alone (those Plot wrote under it, and any the study raised): settle them ONE AT A TIME,
   2–3 options in plain words, your recommendation, the user's answer. Record each with its reason. If one turns out
   to touch another island, it is a course change (3d).
2. Mockup: if this island changes a screen noticeably, show a mockup before any code (project rules, Mockups).
3. Cut the island into waypoints. One waypoint = one commit. For each:
   - what it does, in one sentence
   - serves: the block it builds — where ⛵ sits during this waypoint
   - files touched (open each file in one waypoint where possible)
   - test: test-first ONLY for claims you cannot otherwise see (security, immutability, concurrency, data migration);
     otherwise the suite runs once at the end of the waypoint
   - "reached when": the concrete proof
   On the last island, when the project rules name a Docs place, the LAST waypoint updates it: a page built from the
   Architecture section (pipeline, blocks, decisions and why). Only ✔ claims go there — verify an ≈ claim first or
   leave it out. Each claim keeps its `file:line` anchor so the landfall check can test it.
4. The waypoints must be complete enough that someone starting cold could build them without deciding anything —
   the shipwright will.

GATE: show the island's waypoints; the user writes "approved". No code file of this island is edited before that
word. Then set the island's `approved: yes`, `Island phase: Build`.

### 3c. Announce
Move `⛵` in the plan to the block named on the waypoint's `serves:` line and show the chart. Then state: which
waypoint, files touched, "reached when".

### 3d. Build, and stay on the route
Send the shipwright (SKILL.md, The crew) with: the waypoint's section of passage-plan.md, the decisions it relies
on, the project rules' Tests and No-go areas, the files it lists. It writes the code and runs the test; it never
commits. Waypoints trivial enough to cost less than a cold start (one small file, a rename) you may write yourself.
The waypoint touches only the files it lists. If the shipwright reports that it needs another file or a decision
that was not taken, or the work shows that an island already built must change: STOP — course change, in two messages:
1. The problem alone, concrete, end to end: who calls what, what happens today, what would happen after. No
   options yet. Check it is understood.
2. Only then the solution and its options; the user decides. Record it in the Course changes table with its reason.
A one-line fix that is already obvious may fit in one message — the problem still comes first.
Never deviate silently.

### 3e. Sighted islands
Anything noticed off-route (nearby bug, possible improvement) goes to the "Sighted islands" list in passage-plan.md.
Do not handle it, do not raise it mid-waypoint.

### 3f. Teach the fundamentals
Read the diff yourself. Explain what it rests on — the concept, why this shape, what it connects to in the
pipeline — one concept at a time; by default only what is not obvious, line by line when the user asks. Then the
check-understanding loop (restate · recap · revisit?). Update the lexicon for every concept met (steps/study.md format).

### 3g. Log the waypoint
1. Proof: the test output as is, from the shipwright's report or a rerun. No "should work".
2. List what the user should reread themselves.
3. Tick the waypoint, write its commit line, update the fix in log.md (SKILL.md, Keeping the fix current), THEN
   commit — the chart is updated before the commit, never after.
Move to the next waypoint only when the user says so.

### 3h. End of an island
When every waypoint of the island is ticked:
1. Send the island reviewer (SKILL.md, The crew) with the island's diff (from its first waypoint's parent commit to
   HEAD) and its part of the route. Settle its findings with the user; a fix becomes a waypoint of its own.
2. The USER writes 3 lines under the island in passage-plan.md: what it does · why · what is dangerous.
   Do not hand over three empty lines: recall the island's theme and its blocks in one line, then put a real
   question on each line, worded for this island ("what does this part do?", "why is it built this way?",
   "what can go wrong here?").
3. Move the island's theory notes and waypoint details to archive.md (under a heading with the island's name). In
   passage-plan.md keep the map line, the user's summary, the decisions, and the commit lines.
4. Tick the island, move `⛵` to the next island's first block, set `Island phase: Study`, and show the chart with
   `--transit` (SKILL.md, The chart). The chart IS the recap at an island's end — do not also list the blocks.

GATE: when the last island is ticked, set `Stage: Landfall` and read `steps/landfall.md`.
