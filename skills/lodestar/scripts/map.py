#!/usr/bin/env python3
"""Draw a voyage's chart as a horizontal zigzag, from its passage-plan.md.

    map.py <passage-plan.md>            the boat on the current spot (end of session)
    map.py <passage-plan.md> --transit  the boat on the route after the last finished island (island change)
    map.py <passage-plan.md> --pick     the chart, then every island reached so far, numbered, with its blocks
                                        lettered — the user answers "2.b" to go back there

Reads only the plan's `- Goal` line and its "Archipelago map" section. A checklist line is `- [x] <nature emoji> <name> · …`; indented ones are sub-blocks.
`⛵` on exactly one line marks where we are. No dependency beyond the standard library.
"""
import re
import sys
import unicodedata

SLOPE = 3            # rows between the two lines of islands
BAND = 6             # islands per zigzag band; a longer voyage wraps onto a new band
NAME_MAX = 18        # longer names are cut with …
BOAT = "⛵"
NATURES = ("🏝️", "🌋", "🏰", "🌫️")
CHECK = re.compile(r"^(\s*)- \[([ xX])\] (.*)$")


def width(s):
    """Columns a string takes in a terminal: wide chars and emoji followed by VS16 take 2."""
    n = 0
    for i, c in enumerate(s):
        if c == "️":
            continue
        wide = unicodedata.east_asian_width(c) in "WF" or s[i + 1:i + 2] == "️"
        n += 2 if wide else 1
    return n


def cut(name):
    return name if len(name) <= NAME_MAX else name[:NAME_MAX - 1] + "…"


def parse(path):
    text = open(path, encoding="utf-8").read()
    goal = re.search(r"^- Goal \(one sentence\):[ \t]*(.*)$", text, re.M)
    goal = goal.group(1).strip() if goal else ""
    heading = "### Archipelago map"
    section = text.split(heading, 1)[1] if heading in text else ""
    section = re.split(r"^#{1,3} ", section, maxsplit=1, flags=re.M)[0]

    islands = []
    for line in section.splitlines():
        m = CHECK.match(line)
        if not m:
            continue
        indent, done, rest = m.groups()
        here = BOAT in rest
        rest = rest.replace(BOAT, "").split(" · ")[0].split(" — ")[0].strip()
        nature = next((e for e in NATURES if rest.startswith(e)), "")
        full = rest[len(nature):].strip()
        name = cut(full)
        item = {"full": full, "done": done in "xX", "here": here, "nature": nature, "name": name, "subs": []}
        if indent and islands:
            islands[-1]["subs"].append(item)
        elif not indent:
            islands.append(item)
    return goal, islands


def current_index(islands):
    for i, isl in enumerate(islands):
        if isl["here"] or any(s["here"] for s in isl["subs"]):
            return i
    return None


def draw_band(labels, boat_on_slope, stem_island, subs):
    """labels: texts left to right, alternating bottom/top. Returns the band's lines."""
    height = SLOPE + 2
    rows = [{} for _ in range(height + len(subs))]
    x, top, stem_col = 0, False, None
    for i, lab in enumerate(labels):
        r = 0 if top else height - 1
        rows[r][x] = lab
        if i == stem_island:
            stem_col, stem_row = x + (1 if lab.startswith("✓") else 0), r
        end = x + width(lab)
        if i == len(labels) - 1:
            break
        for k in range(SLOPE):
            boat = i == boat_on_slope and k == SLOPE // 2
            col = end + 1 + k - (1 if boat else 0)
            ch = BOAT if boat else ("╲" if top else "╱")
            rows[1 + k if top else height - 2 - k][col] = ch
        x, top = end + 1 + SLOPE, not top
    if stem_col is not None and subs:
        if stem_row == 0:
            for r in range(1, height):
                rows[r][stem_col] = "│"
        for j, s in enumerate(subs):
            mark = BOAT if s["here"] else ("✓" if s["done"] else "○")
            branch = "└ " if j == len(subs) - 1 else "├ "
            rows[height + j][stem_col] = branch + mark + " " * (2 - width(mark)) + " " + s["name"]
    out = []
    for row in rows:
        line = ""
        for col in sorted(row):
            line += " " * max(0, col - width(line)) + row[col]
        if line.strip():
            out.append(line.rstrip())
    return out


def label(isl, cur, i, transit):
    mark = "✓" if isl["done"] else ""
    if not transit and i == cur and not isl["subs"]:
        mark = BOAT
    return f"{mark}{isl['nature']} {isl['name']}".replace("  ", " ").strip()


def main(argv):
    if len(argv) < 2:
        print(__doc__.strip())
        return 1
    transit = "--transit" in argv
    pick = "--pick" in argv
    goal, islands = parse(argv[1])
    if not islands:
        print("(no chart yet)")
        return 0
    cur = current_index(islands)
    if transit:
        done = [i for i, isl in enumerate(islands) if isl["done"]]
        leaving = done[-1] if done else -1          # the boat sails from the last finished island
    lines = [f"✦ Cap — {goal}" if goal else "✦ Cap — (goal not written yet)", ""]
    for start in range(0, len(islands), BAND):
        chunk = islands[start:start + BAND]
        last_band = start + BAND >= len(islands)
        labels = [label(isl, cur, start + j, transit) for j, isl in enumerate(chunk)]
        labels.append("⭐" if last_band else "↴")
        boat_on_slope = (leaving - start) if transit and start <= leaving < start + len(chunk) else None
        stem = (cur - start) if not transit and cur is not None and start <= cur < start + len(chunk) else None
        subs = chunk[stem]["subs"] if stem is not None else []
        lines += draw_band(labels, boat_on_slope, stem, subs) + [""]
    if pick:
        lines = [l.rstrip() for l in "\n".join(lines).rstrip().splitlines()] + [""] + pick_list(islands, cur)
    print("\n".join(lines).rstrip())
    return 0


def pick_list(islands, cur):
    """Islands reached so far (done, or the current one), numbered; their sub-blocks lettered."""
    lines = ["Go back to:"]
    last = cur if cur is not None else max((i for i, isl in enumerate(islands) if isl["done"]), default=-1)
    for i, isl in enumerate(islands[:last + 1]):
        lines.append(f"  {i + 1}  {isl['nature']} {isl['full']}")
        for j, s in enumerate(isl["subs"]):
            lines.append(f"       {chr(97 + j)}  {s['full']}")
    return lines


if __name__ == "__main__":
    sys.exit(main(sys.argv))
