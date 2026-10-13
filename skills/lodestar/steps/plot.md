# 2. Plot — chart the voyage

The whole route at the level of the islands: what they build together, and every choice that would break one
island if made later in another. What concerns one island only waits for that island (steps/sail.md, Waypoints).

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
has this shape rather than another. Mark every claim ✔ verified or ≈ assumed.
One block per message; after each, check understanding: the user restates it, ask only about what was missed.

### 2c. Decisions that cross islands
List every decision that more than one island rests on, and every irreversible one (data format, migration,
permission name, published contract) — irreversible first. Every cross-island open question from Log lands here.
Settle them ONE AT A TIME: 2–3 options in plain words, your recommendation, the user's answer.
Record each in passage-plan.md with its reason. A settled decision is not reopened unless the user reopens it.
A decision that concerns one island only: write it under that island, unsettled — it is taken when the island is.

### 2d. Island order
Confirm the sailing order: an island comes after those it reads from. Reorder the map if needed, and say why.

### 2e. No-go areas
List what this route must NOT touch: the project rules' no-go areas, other tickets' files, colleagues' code.

### 2f. Contingencies
For each known risk: how we would notice it, what we do if it happens.

### 2g. Before the gate
1. Open questions: every cross-island one is answered, or written in Contingencies as an accepted risk.
   None may cross the gate silently. Questions of a single island wait for it.
2. The user restates the architecture in their own words: where the information starts, where it goes, who it
   serves, and why each island exists. Ask questions only on what the restatement missed.
3. Send the route reviewer (SKILL.md, The crew). Settle each finding with the user, one at a time.

GATE: show the voyage chart; the user writes "approved". No code file is edited before that word — and each island
will ask for its own "approved" before its code.
Then set `Voyage approved: yes`, `Stage: Sail`, `Island phase: Study`, put the boat `⛵` on the first island's first
block in place of the pin, and read `steps/sail.md`.
