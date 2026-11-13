# 3. Sail — island by island: study, plot its waypoints, build

Each island runs the same three phases, named on the plan's `Island phase:` line, then closes before the next one:
**Study** (steps/study.md) → **Waypoints** (3b) → **Build** (3c–3g) → **End of island** (3h).
`Island phase: Study`: read `steps/study.md` and do it first; come back here at its gate.

### 3b. Waypoints — this island's route
1. Find every decision before Build does: read the callers of each function the island changes (transaction,
   lock, error path they run in) and fix the content of every message, record or file that leaves the island
   (field by field). Every choice this raises is a decision now, not a question during Build.
   Decisions of this island alone (those Plot wrote under it, the study's, and these): settle them in ONE batch,
   as in Plot 2c. Record each with its reason. If one turns out to touch another island, it is a course change (3d).
2. Mockup: if this island changes a screen noticeably, show a mockup before any code (project rules, Mockups).
3. Cut the island into waypoints. One waypoint = one commit. For each:
   - what it does, in one sentence
   - serves: the block it builds — where ⛵ sits during this waypoint
   - files touched (open each file in one waypoint where possible)
   - test: test-first ONLY for claims you cannot otherwise see (security, immutability, concurrency, data migration);
     otherwise the suite runs once at the end of the waypoint. On a 🏰 island, every attack kept from the red team
     is one such test: written first, as the attacker, and failing before the code
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
A waypoint under ~200 lines of diff: write it yourself — a cold start costs more. Otherwise send the shipwright
(SKILL.md, The crew) with: the waypoint's section of passage-plan.md, the decisions it relies on, the project rules'
Tests and No-go areas, the files it lists. ONE shipwright per island: for the next waypoint, resume it with
SendMessage (it keeps its context) instead of starting a new one. It writes the code and runs the test; it never
commits. When its code departs from a settled decision, correct it yourself — that is not a question for the user.
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
   A test that fails: first check whether it fails the same way on the base branch (its CI, or the fix's
   inherited red). If it does, it is not this waypoint's — write it under Sighted islands and carry on. If it does
   not, find the cause before touching code: read the error and the code it points to; never retry blindly.
2. List what the user should reread themselves.
3. Tick the waypoint, write its commit line, THEN
   commit — the chart is updated before the commit, never after.
Chain to the next waypoint without asking. Stop only for: a failing test that is not inherited red, a course change
(3d), or a decision the plan does not contain.

### 3h. End of an island
When every waypoint of the island is ticked:
1. Send the island reviewer (SKILL.md, The crew) with the island's diff (from its first waypoint's parent commit to
   HEAD) and its part of the route. A fix becomes a waypoint of its own.
   On a 🏰 island, also give it the threat model: it then checks the guarantees too. Only a 🌋 island
   (irreversible: format, migration, published contract) also gets the red team in `code` mode, same diff. An attack
   that holds becomes a waypoint (its test first); one marked `predates` goes to Sighted islands.
   All findings are settled in one batch (3b); fixes become waypoints that chain like the others.
2. Update the voyage README (project rules) once, for the whole island.
3. Move the island's theory notes and waypoint details to archive.md (under a heading with the island's name). In
   passage-plan.md keep the map line, the user's summary, the decisions, and the commit lines.
4. Update the fix in log.md (SKILL.md, Keeping the fix current). Tick the island, move `⛵` to the next island's first block, set `Island phase: Study`, and show the chart with
   `--transit` (SKILL.md, The chart). The chart IS the recap at an island's end — do not also list the blocks.

GATE: when the last island is ticked, set `Stage: Landfall` and read `steps/landfall.md`.
