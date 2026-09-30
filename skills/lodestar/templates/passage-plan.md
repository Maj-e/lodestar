# Passage plan — <feature>

Stage: Log | Pose | Sail | Landfall
Route approved: no

## 1. Log

### Heading
> <quote of the ticket line — the source of truth>

- Goal (one sentence):
- Done when:

### Scope
| item | in / out | reason (already done · redundant with · deferred to · depends on) |
|---|---|---|

### Lexicon for this voyage
| term | stack / product | level before | level after |
|---|---|---|---|

### Archipelago map
<!-- Read by scripts/map.py — keep the shape. [x] understood · [ ] not yet · ⛵ on ONE line = where we are.
     Nature, first on each island line: 🏝️ ordinary · 🌋 irreversible · 🏰 security · 🌫️ open questions -->
- [ ] 🏝️ <name> · serves the heading by: <one sentence>
  - [ ] <sub-block name> ⛵
- [ ] 🌋 <name> · serves the heading by: <one sentence>

### Theory notes
#### Island 1 — <name>
- <claim> — `file:line` ✔ verified | ≈ assumed

**Island summary (written by the user):** what it does · why · what is dangerous

### Open questions
| question | who can answer | what it blocks |
|---|---|---|

## 2. Pose

### Precedent
- <feature> — `file:line` · conventions to copy:

### Architecture
#### Pipeline
<!-- source → stage → stage → user. For each stage: what it does to the information, where it lives. -->
```
<source> ──> <stage> ──> <store> ──> <stage> ──> <user · screen · decision>
```
#### Blocks
| block | new / modified | role | reads | feeds | why this shape |
|---|---|---|---|---|---|

**Restated by the user:** <where the information starts, where it goes, who it serves, why each block>

### Decisions
| # | decision | options | chosen | why |
|---|---|---|---|---|

### No-go areas
-

### Waypoints
<!-- one waypoint = one commit -->
- [ ] W1 — <what it does, one sentence>
  - files:
  - test: <test-first: why> | suite at the end
  - reached when:
  - commit:

### Contingencies
| risk | how we notice | what we do |
|---|---|---|

## 3. Sail

### Course changes
| date | change | why |
|---|---|---|

### Going back
<!-- reason: theory · code · decision · problem · link -->
| date | from | to | reason | outcome |
|---|---|---|---|---|

### Sighted islands
<!-- noticed off-route, not handled -->
-
