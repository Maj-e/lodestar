# 2. Pose — chart the route

### 2a. Precedent
Find the closest existing feature in the codebase. Name it (file:line) and list the conventions to copy:
naming, structure, tests. Copy before inventing.

### 2b. Architecture — what we build, and why
Before any decision, draw the target. Decisions follow from it.
**The pipeline comes first — the most important part.** For each piece of information the feature handles:
- where it starts: the source that produces it (sensor, user, external API, scheduled job…) — `file:line` if it exists
- every stage it passes through, in order: what each stage does to it (reads, transforms, stores, sends), and where
  it lives in between (table, queue, cache, file)
- who it serves at the end: which user, on which screen or output, for which decision
Draw it as an ASCII flow in passage-plan.md, source on the left, user on the right. A stage whose output nobody
downstream uses is out of the route.
Then the blocks: each new or modified block, its role in one sentence, what it reads and what it feeds, and why it
has this shape rather than another. Mark every claim ✔ verified or ≈ assumed, as in Log.
One block per message; after each, the Log loop applies (restate, recap, revisit).

### 2c. Decisions — all of them, before any code
List every decision the route needs, irreversible ones first (data format, migration, permission name,
published contract). Settle them ONE AT A TIME: 2–3 options in plain words, your recommendation, the user's answer.
Record each in passage-plan.md with its reason. A settled decision is not reopened unless the user reopens it.

### 2d. No-go areas
List what this route must NOT touch: the project rules' no-go areas, other tickets' files, colleagues' code.

### 2e. Waypoints
Cut the route into waypoints. One waypoint = one commit. For each:
- what it does, in one sentence
- files touched (open each file in one waypoint where possible)
- test: test-first ONLY for claims you cannot otherwise see (security, immutability, concurrency, data migration);
  otherwise the suite runs once at the end of the waypoint
- "reached when": the concrete proof
When the project rules name a Docs place, the LAST waypoint updates it: a page built from the Architecture section
(pipeline, blocks, decisions and why). Only ✔ claims go there — verify an ≈ claim first or leave it out.
Each claim keeps its `file:line` anchor so the landfall check can test it.

### 2f. Contingencies
For each known risk: how we would notice it, what we do if it happens.

### 2g. Mockup (UI features only)
If the route changes a screen noticeably, show a mockup before any code (tool and rules: project rules, Mockups).

### 2h. Before the gate
1. Open questions: every one that blocks a decision is answered, or written in Contingencies as an accepted risk.
   None may cross the gate silently.
2. The user restates the architecture in their own words: where the information starts, where it goes, who it
   serves, and why each block exists. Ask questions only on what the restatement missed.
3. The route must be complete enough that someone starting cold could build it without deciding anything —
   the shipwright will.
4. Send the route reviewer (SKILL.md, The crew). Settle each finding with the user, one at a time.

GATE: show the full route; the user writes "approved". No code file is edited before that word.
Then set `Route approved: yes`, `Stage: Sail`, and read `steps/sail.md`.
