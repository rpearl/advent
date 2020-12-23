# submit = True
from aocd import lines
import sys
from collections import Counter, defaultdict, deque
import functools
from sortedcontainers import SortedList, SortedDict, SortedSet
import itertools
import u


print(f"File line count: {len(lines)}")
ds = u.dirs + u.diags


def a():
    grid, _, _ = u.make_grid(lines, lambda val, pos: val if val != "." else None)

    while True:
        count = 0
        counts = Counter()
        for pos, c in grid.items():
            if c == "#":
                count += 1
                counts.update(u.all_neighbors(grid, pos))

        done = True
        for pos, c in grid.items():
            s = counts[pos]
            if c == "L" and s == 0:
                grid[pos] = "#"
                done = False
            elif c == "#" and s >= 4:
                grid[pos] = "L"
                done = False
        if done:
            return count


def b():
    grid, width, height = u.make_grid(
        lines, lambda val, pos: val if val != "." else None
    )

    def neighbors(pos):
        for d in ds:
            npos = (pos[0] + d[0], pos[1] + d[1])
            while npos not in grid and 0 <= npos[0] <= width and 0 <= npos[1] <= height:
                npos = (npos[0] + d[0], npos[1] + d[1])
            if npos in grid:
                yield npos

    while True:
        count = 0
        counts = Counter()
        for pos, c in grid.items():
            if c == "#":
                count += 1
                counts.update(neighbors(pos))
        done = True
        for pos, c in grid.items():
            s = counts[pos]
            if c == "L" and s == 0:
                grid[pos] = "#"
                done = False
            elif c == "#" and s >= 5:
                grid[pos] = "L"
                done = False
        if done:
            return count


u.main(a, b, submit=globals().get("submit", False))
