# Lodestar

**Log. Pose. Sail.** — a Claude Code skill for working through tickets the way a careful navigator crosses a sea:
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
/plugin marketplace add Maj-e/Lodestar
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

Installed as a plugin, Claude Code may list the command as `/lodestar:lodestar`. Lodestar never starts on its own:
when you describe a new ticket, Claude offers it in one line.

The first time in a project, Claude asks a few questions — where tickets live, how to run tests, what must never be
touched, where the docs are — and saves the answers in `.claude/lodestar.md`. Edit that file whenever you like.

## The voyage

A **voyage** is one ticket. Its blocks are **islands**; a small ticket is a one-island voyage. Every voyage goes
through the same four stages, and **you** open every gate.

1. **Log — know where you sail.** Quote the ticket, write the goal in one sentence, sort what is in scope. Check
   your lexicon for the concepts it needs. Then study island by island: one concept per message, every claim
   anchored to a `file:line` and marked ✔ verified or ≈ assumed. After each block you restate it; Claude only moves
   on when you say so. At the end of an island, you write its three-line summary.
2. **Pose — chart the route.** Draw the **pipeline** first: where each piece of information starts, every stage it
   passes through, and who it serves at the end. Then the blocks, every decision (irreversible ones first), the
   waypoints — one waypoint, one commit — and the risks. A fresh reviewer reads the route for gaps. Nothing is
   built until you write **"approved"**.
3. **Sail — one waypoint at a time.** A builder agent writes the waypoint's code and runs its test; Claude reads
   the diff and teaches you what it rests on. Anything off-route is written down, never handled on the way.
   At the end of each island, a fresh reviewer reads its code.
4. **Landfall — close the voyage.** A last check runs the full suite and tests the "done when" line. The docs page
   is updated with verified claims only. Claude writes a summary of how the voyage went; you add your own lines.

## The crew

Fresh agents with no memory of the conversation, sent only where a new pair of eyes is worth a cold start:

| agent | when | job |
|---|---|---|
| researcher | Log | answers a documentation question from primary sources, in the background |
| route reviewer | Pose | finds the gaps in the route before you approve it |
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

`🏝️` ordinary island · `🌋` irreversible · `🏰` security · `🌫️` open questions · `✓` done · `⛵` you are here ·
`⭐` landfall

## Status

Version 0.1 — used by its author, tested on a handful of scenarios. Planned next: going back to an earlier
island from an interactive menu, with the map following the cursor.

Feedback is welcome in the issues.

## License

MIT — see [LICENSE](LICENSE).
