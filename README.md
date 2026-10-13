# Lodestar

**Log. Plot. Sail.** — a Claude Code skill for working through tickets the way a careful navigator crosses a sea:
understand where you are, chart the whole route, then sail it one waypoint at a time.

Lodestar is for developers who want to **understand the fundamentals of what gets built**, not just get code. Claude
studies the ticket with you, checks what you already know, makes you restate each block in your own words, decides
the whole architecture with you before a single line of code, and then builds — explaining what the code rests on.
Everything is written to small files, so a voyage can span many sessions and each one costs the same.

```
✦ Cap — customers can pay an order by card or with a voucher

                  ✓🏰 Card payments                    ⛵🌋 Order migration                         ⭐
                 ╱                  ╲                 ╱                     ╲                      ╱
                ╱                    ╲               ╱                       ╲                    ╱
               ╱                      ╲             ╱                         ╲                  ╱
✓🏝️ Cart model                         ✓🏝️ Vouchers                            🏝️ Receipt screen
```

## Install

**As a plugin** (recommended — you get updates):

```
/plugin marketplace add Maj-e/lodestar
/plugin install lodestar@lodestar
```

**By hand:** copy `skills/lodestar/` to `~/.claude/skills/lodestar/`.

Requirements: Claude Code, and `python3` on the PATH (it draws the map; standard library only).

## Use

| you type | what happens |
|---|---|
| `/lodestar <feature>` | starts a voyage for that ticket, or resumes it |
| `/lodestar` | shows the sea: every voyage of the project and its stage, then the next ticket |
| "let's stop" (in any language) | Claude writes where you stopped and shows the map |
| "let's go back" | Claude shows the map with every island and block numbered; answer with a place and a reason, e.g. `2b code` |

Installed as a plugin, Claude Code may list the command as `/lodestar:lodestar`. Lodestar never starts on its own:
when you describe a new ticket, Claude offers it in one line.

The first time in a project, Claude asks a few questions — where tickets live, how to run tests, what must never be
touched, where the docs are — and saves the answers in `.claude/lodestar.md`. Edit that file whenever you like.

## How it works

Every ticket goes through the same four stages, and **you** open every gate. The skill names things after a sea
crossing; here is what each word means:

| word | plain meaning |
|---|---|
| the sea | every ticket of the project |
| a voyage | one ticket, one problem to solve |
| an island · a town | a block of that ticket · a smaller part of that block |
| a waypoint | one step of the build, one commit |
| the fix | the saved position: where you stopped, and what comes next |
| 📍 · ⛵ | where you are while surveying and charting · from the first island on |

1. **Log — survey the whole voyage.** Quote the ticket, write the goal in one sentence, sort what is in scope.
   Map the islands, then look at each one briefly: what it touches, what depends on it, whether it is
   irreversible, what questions it raises. No deep study yet. You restate the map once, at the end.
2. **Plot — chart what crosses islands.** Draw the **pipeline** first: where each piece of information starts,
   every stage it passes through, and who it serves at the end. Then settle only the decisions that more than one
   island rests on, irreversible ones first, and the order of the islands. A fresh reviewer reads the chart for
   gaps. You write **"approved"**.
3. **Sail — island by island.** For each island: **study** it — Claude checks your lexicon for its concepts, explains
   one concept per message, every claim anchored to a `file:line` and marked ✔ verified or ≈ assumed, and you
   restate each block. Then its **waypoints** — one waypoint, one commit — and its own decisions; nothing of the
   island is built until you write **"approved"** again. Then **build**: a builder agent writes each waypoint's
   code and runs its test; Claude reads the diff and teaches you what it rests on. A fresh reviewer reads the
   island's code, and you write its three-line summary before the next island.
4. **Landfall — close the voyage.** A last check runs the full suite and tests the "done when" line. The docs page
   is updated with verified claims only. Claude writes a summary of how the voyage went; you add your own lines.

## The crew

Fresh agents with no memory of the conversation, sent only where a new pair of eyes is worth a cold start:

| agent | when | job |
|---|---|---|
| researcher | Log | answers a documentation question from primary sources, in the background |
| route reviewer | Plot | finds the gaps in the route before you approve it |
| shipwright | Sail | builds one waypoint; never commits |
| island reviewer | Sail | reviews an island's code against the plan |
| landfall check | Landfall | runs the suite, checks "done when", scope and docs anchors |

## Files it writes

| file | what it holds |
|---|---|
| `.claude/lodestar.md` | the project's rules |
| `.claude/lodestar/<feature>/passage-plan.md` | the voyage: map, architecture, decisions, waypoints |
| `.claude/lodestar/<feature>/log.md` | one entry per session, newest first |
| `.claude/lodestar/<feature>/archive.md` | finished islands and old entries — never read unless you ask |
| `.claude/lodestar/<feature>/summary.md` | written at landfall |
| `~/.claude/lodestar/lexicon.md` | what you know, across all projects — one line per concept |

The first voyage asks whether `.claude/lodestar/` goes into git or stays out of it.

### The lexicon

One line per concept, keyed by subject so one search returns everything on it:

```
postgres/indexes | index, b-tree | stack | understood | 2026-09-30 | shop/checkout archive.md#Order-migration
```

When a voyage needs a concept, Claude looks it up: *mastered* is skipped, *understood* in the last six months gets a
one-line reminder, anything older or shakier gets one check question, and the rest becomes a block to study. The
line points to where you learnt it; the explanation itself stays there.

## Map legend

`🏝️` ordinary island · `🌋` irreversible · `🏰` security · `🌫️` open questions · `✓` done · `📍` you are here while surveying and charting, `⛵` once you sail ·
`⭐` landfall

## Status

Version 0.2 — used by its author, tested on a handful of scenarios. 0.2 changes the passage plan's shape (the voyage
is studied and built island by island): a voyage started with 0.1 needs its plan converted before it resumes. Planned next: an interactive menu for going
back, with the map following the cursor.

Feedback is welcome in the issues.

## License

MIT — see [LICENSE](LICENSE).
