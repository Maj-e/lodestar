# Setup — first voyage in a project

Runs once per project, when `.claude/lodestar.md` does not exist. Ask ONE question at a time. When the repo shows
an answer (a TODO file, a test command in the README), offer it as a suggestion the user confirms or corrects.
When it shows nothing, say so and ask the question open — a guess dressed as a suggestion gets confirmed out of
politeness and then misleads every voyage after it.

1. **Tickets** — where is the source of truth for a feature (issue tracker, TODO file, spec folder)?
   How is one ticket identified and quoted?
2. **Backlog** — is there a full list of tickets to read, to avoid redundancy with neighbouring work?
   Where? If none, write "none": the Scope step will then say that redundancy was not checked.
3. **Tests** — the command for one test module, and the command for the full suite.
4. **No-go areas** — files or folders never to edit or commit.
5. **Mockups** — for a noticeable screen change: which tool, which design rules to follow. "none" is fine.
6. **Docs** — where does the project explain how the system works (wiki folder, docs site, README)? In which
   language and tone? "none" is fine: the voyage then ends without a docs waypoint.
7. **Git** — should `.claude/lodestar/` be committed with the code, or kept out of git?
   If out: add it to `.gitignore` (show the line before writing it).

Write the answers to `.claude/lodestar.md` from templates/project-rules.md, show the file, then go back to
SKILL.md 0b.
