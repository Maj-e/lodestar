# 3. Sail — one waypoint at a time

### 3a. Announce
Before starting a waypoint, state: which one, files touched, "reached when".

### 3b. Build
Send the shipwright (SKILL.md, The crew) with: the waypoint's section of passage-plan.md, the decisions it relies
on, the project rules' Tests and No-go areas, the files it lists. It writes the code and runs the test; it never
commits. Waypoints trivial enough to cost less than a cold start (one small file, a rename) you may write yourself.

### 3c. Stay on the route
The waypoint touches only the files it lists. If the shipwright reports that it needs another file or a decision
that was not taken: STOP — course change. Explain why the route no longer holds, let the user decide, record it in
passage-plan.md with its reason. Never deviate silently.

### 3d. Sighted islands
Anything noticed off-route (nearby bug, possible improvement) goes to the "Sighted islands" list in passage-plan.md.
Do not handle it, do not raise it mid-waypoint.

### 3e. Teach the fundamentals
Read the diff yourself. Explain what it rests on — the concept, why this shape, what it connects to in the
pipeline — one concept at a time; by default only what is not obvious, line by line when the user asks. Then the
check-understanding loop (restate · recap · revisit?). Update the lexicon for every concept met (step 1c format).

### 3f. Log the waypoint
1. Proof: the test output as is, from the shipwright's report or a rerun. No "should work".
2. List what the user should reread themselves.
3. Tick the waypoint, write its commit line, prepend a fix to log.md, THEN commit — the chart is updated before
   the commit, never after.
Move to the next waypoint only when the user says so.

### 3g. End of an island
When every waypoint of an island is ticked, send the island reviewer (SKILL.md, The crew) with the island's diff
(from its first waypoint's parent commit to HEAD) and its part of the route. Settle its findings with the user;
a fix becomes a waypoint of its own.

GATE: when the last waypoint is ticked, set `Stage: Landfall` and read `steps/landfall.md`.
