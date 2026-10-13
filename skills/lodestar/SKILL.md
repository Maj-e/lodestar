---
name: lodestar
description: "Plan-first, multi-session feature workflow that teaches as it goes. Use on /lodestar, or to resume
  a voyage when .claude/lodestar/<name>/ exists. For a new ticket, only offer it in one line; never auto-launch."
argument-hint: <feature name>
---

# lodestar

Motto: **Log. Plot. Sail.** — survey the whole voyage, chart what crosses islands, then sail island by island:
study it, plot its waypoints, build it. Theory and code alternate, island after island.
The goal is that the user understands the fundamentals of what gets built — not that they type it.

| file | what it holds |
|---|---|
| `.claude/lodestar.md` | project rules: tickets, backlog, tests, no-go areas, mockups, docs, git policy |
| `.claude/lodestar/<feature>/passage-plan.md` | the voyage: heading, map, architecture, decisions, then each island's notes and waypoints |
| `.claude/lodestar/<feature>/log.md` | one fix per session, newest on top, kept current as we go (templates/log.md) |
| `.claude/lodestar/<feature>/archive.md` | details of finished islands and old fixes, read only on demand |
| `.claude/lodestar/<feature>/summary.md` | written at landfall: how the voyage went, read only on demand |
| `~/.claude/lodestar/lexicon.md` | an index of what the user knows, across all projects |

Three levels: **the sea** is every ticket of the project · **a voyage** is one ticket, one problem to solve ·
**an island** is one block of that voyage.

## Read only what the moment needs

- Load ONE step file at a time, per the plan's `Stage:` line: `steps/log.md` · `steps/plot.md` · `steps/sail.md`
  · `steps/landfall.md`. In Sail, `Island phase: Study` loads `steps/study.md` instead, until its gate.
- State files grow every session, so read them by section, not whole: `grep -n '^#' <file>` to find the
  headings, then read only the line range you need. A file under ~100 lines is cheaper to read whole than to
  search — read it whole. On resume: the top fix of log.md, the plan's header and map, the section of the current
  island or waypoint. Anything else only when a question needs it.
- Never read archive.md or summary.md unless the user asks about something in them.
- Why: a session must cost the same on day 1 and day 30 of a voyage.

## 0. Start

### 0a. Project rules
Look for `.claude/lodestar.md` in the current directory, then in each parent up to the repository root, then
below: `find . -maxdepth 4 -path '*/.claude/lodestar.md' -not -path '*/node_modules/*'`. A voyage started from a
subfolder lives there, not where the session opens.
- One found elsewhere: say where, and work from that folder — every path below is relative to it.
- Several: list them and let the user pick.
- None: read `steps/setup.md` and do it before anything else.
- First use ever (`~/.claude/lodestar/lexicon.md` does not exist): before anything else, introduce the skill once,
  in the user's language, in at most 6 lines: what it does (understand the code, not only get it) · the four stages,
  one line each · the words and their plain meaning (README, How it works) · that the user opens every gate.

### 0b. The sea — find or sort the voyage
`/lodestar <feature>`: open `.claude/lodestar/<feature>/`.
`/lodestar` alone: show the sea — one line per folder in `.claude/lodestar/` (name + `Stage:` line; `Landed`
ones last), then the next ticket from the project rules' ticket source when it gives an order. Let the user pick.
A new ticket: propose where it belongs, in one line, and let the user decide:
- **part of a voyage in progress** → a new island on that voyage, recorded as a course change;
- **a small problem** → a one-island voyage: every step still runs, each one short;
- **a larger problem** → a full voyage.
New voyage: create its folder from templates/, then read `steps/log.md`.

### 0c. Check the chart against the ground
Before telling anything, compare the top fix of log.md with reality:
- the current branch is the plan's `Branch:` line, and is not behind the main branch
  (`git rev-list --count HEAD..<main branch>`);
- the last commit matches the last ticked waypoint;
- uncommitted changes.
If they disagree, report it FIRST and let the user decide — before reading the ticket or any code.

### 0d. Take the fix
Show the chart first (no flag), then in a few lines: stage and position on the map, what happened last session, open questions waiting on someone,
the next action. Refresh only the current block: reread its island summary or notes, not the others. Then wait.

## Gates — never crossed without the user
- Log → Plot: every island is surveyed and the user has restated the map.
- Plot → Sail: the user wrote "approved" in answer to the voyage chart.
- Study → Waypoints: every block of the island is ✓.
- Waypoints → Build: the user wrote "approved" in answer to the island's waypoints. No code file of an island is
  edited before its own "approved".
- Waypoint → next waypoint, island → next island: the user says so.
- Landfall → Landed: the user has added their lines to summary.md.

## The crew
Fresh agents with no memory of this conversation. Use one only at the moments below — each costs a full cold
start. Launch it with the Agent tool (general-purpose), its prompt = the agent file + the inputs it lists, never
the conversation. Show its report as is, then settle its findings with the user one at a time.

| agent | when | file |
|---|---|---|
| researcher | Log or Study: an open question the documentation can settle — runs in the background | `agents/researcher.md` |
| route reviewer | Plot: before asking for the voyage's "approved" | `agents/route-reviewer.md` |
| shipwright | Sail: writes each waypoint's code; never commits | `agents/shipwright.md` |
| island reviewer | Sail: when every waypoint of an island is done | `agents/island-reviewer.md` |
| landfall check | Landfall: before the summary | `agents/landfall-check.md` |

## The chart
`python3 <this skill>/scripts/map.py .claude/lodestar/<feature>/passage-plan.md [--transit]` draws the voyage.
Paste its output as is, in a code block, with no comment — never draw or re-align it yourself.
Show it every time the marker moves, and only then — the user finds their place on it, not in prose:
- on resume (0d) and when a session ends — no flag, the marker on the current block;
- when the marker moves to another block, or to another waypoint's block in Sail — no flag, before explaining it;
- on an island change — `--transit`, the marker on the route between the two islands.
The marker is the pin `📍` while the voyage is surveyed and charted (Stage: Log or Plot) and the boat `⛵` from Sail
on, while an island is studied as well as built. Write it on exactly one map line of the plan; the script reads either and draws the one the `Stage:` line calls for.

## Going back
When the user wants to revisit something already covered:
1. Run the chart with `--pick` and paste it as is. The user answers with a place and a reason, e.g. `2b code`
   (a number alone = the whole island). No reason given: ask it in one line.
2. Move the marker (`📍` or `⛵`) to that block and note where we were. Then act on the reason — read only what it needs:

| reason | when | what you do | what it leaves |
|---|---|---|---|
| theory | forgotten or not understood | reread the block's notes (archive.md if compacted); explain it differently from the first time; restate loop | the lexicon level, corrected; a second theory return to the same block → rewrite the island summary with the user |
| code | how it was built | find the block's waypoint commits in the plan; show the key lines; teach what they rest on | nothing to change |
| decision | doubting a choice | show the decision row: options, choice, why. If the user wants to change it, list what depends on it first | confirmed, or reopened as a course change the user settles |
| problem | current work shows the block is wrong | check it; the fix becomes a new waypoint | a waypoint added, with its reason |
| link | how it connects to where we are | show the stretch of pipeline from that block to the current one | nothing to change |

3. Record it in the plan's Going back table: date · from · to · reason · outcome.
4. Before carrying on, say whether the outcome changes the route. When the user says to carry on, move the marker back
   to where we were.

## Keeping the fix current
A session can end without warning (crash, full context, closed window), so the fix is not left for the stop.
Each time a block is done — an island surveyed in Log, a section of Plot finished, a block studied or a waypoint built in Sail — write the
fix from templates/log.md: what was done, exactly where we are, the next action, what waits on whom.
The first time in a session, prepend a new fix; after that, rewrite that same fix in place — one fix per session.
Why per block: the block is the unit of resume, so at worst the block in progress is lost.

## Ending a session
Everything needed is here — do not open a step file. When the user signals a stop, update the session's fix
(Keeping the fix current) with exactly where we stopped, even mid-island or mid-waypoint. Check the marker sits on
that spot in the plan, then show the chart.
If log.md holds more than 5 fixes, move the oldest ones to archive.md.
