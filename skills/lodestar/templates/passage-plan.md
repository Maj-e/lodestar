# Passage plan — <feature>

Stage: Log | Plot | Sail | Landfall
Island phase: Study | Waypoints | Build
Voyage approved: no
Branch: <git branch of this voyage>

## 1. Log

### Heading
> <quote of the ticket line — where the project says what it asks for>

- Goal (one sentence):
- Done when:

### Scope
| item | in / out | reason (already done · redundant with · deferred to · depends on) |
|---|---|---|

### Lexicon for this voyage
| term | stack / product | level before | level after |
|---|---|---|---|

### Archipelago map
<!-- Read by scripts/map.py — keep the shape. Sailing order, top to bottom. Block [x] = studied · island [x] = built.
     📍 on ONE line = where we are (⛵ from Sail on).
     Nature, first on each island line: 🏝️ ordinary · 🌋 irreversible · 🏰 security · 🌫️ open questions -->
- [ ] 🏝️ <name> · serves the heading by: <one sentence>
  - [ ] <sub-block name> 📍
- [ ] 🌋 <name> · serves the heading by: <one sentence>

### Survey notes
#### Island 1 — <name>
- touches: · reads: · feeds: · irreversible: yes / no
- concepts to check when studied:

### Open questions
| question | who can answer | what it blocks | islands |
|---|---|---|---|

**Restated by the user:** <the islands, their order, which ones could break the others>

## 2. Plot

### Precedent
- <closest existing feature> — `file:line` · conventions to copy:

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

### Decisions that cross islands
| # | decision | options | chosen | why |
|---|---|---|---|---|

### No-go areas
-

### Contingencies
| risk | how we notice | what we do |
|---|---|---|

## 3. Sail

### Island 1 — <name>
approved: no

#### Theory notes
- <claim> — `file:line` ✔ verified | ≈ assumed

#### Decisions
| # | decision | options | chosen | why |
|---|---|---|---|---|

#### Waypoints
<!-- one waypoint = one commit -->
- [ ] W1 — <what it does, one sentence>
  - serves: <block it builds — where ⛵ sits during this waypoint>
  - files:
  - test: <test-first: why> | suite at the end
  - reached when:
  - commit:

**Island summary (written by the user):** what it does · why · what is dangerous

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
