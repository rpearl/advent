from aocd import lines, submit
import sys
from collections import Counter, defaultdict, deque
import functools
from sortedcontainers import SortedList, SortedDict, SortedSet
import itertools
import u


def nosubmit(answer, part):
    print(f"Part {part}:\n{answer}")


submit = nosubmit

# data = """#.##.##.##
########.##
##.#.#..#..
#####.##.##
##.##.##.##
##.#####.##
# ..#.#.....
###########
##.######.#
##.#####.##"""
#
# lines = data.split("\n")

print(f"File line count: {len(lines)}")
ds = u.dirs + u.diags


def a():
    b = u.Grid(lines)

    def occd(pos, d):
        npos = (pos[0] + d[0], pos[1] + d[1])
        return int(b.grid.get(npos) == "#")

    chairs = [pos for pos, c in b.grid.items() if c != "."]
    while True:
        count = 0
        swaps = []
        for pos in chairs:
            c = b.grid[pos]
            if c == ".":
                continue
            if c == "#":
                count += 1
            s = sum(occd(pos, d) for d in ds)
            if c == "L" and s == 0 or c == "#" and s >= 4:
                swaps.append((pos, "L" if c == "#" else "#"))

        if len(swaps) == 0:
            return count
        for pos, c in swaps:
            b.grid[pos] = c


def b():
    b = u.Grid(lines)

    def occd(pos, d):
        npos = (pos[0] + d[0], pos[1] + d[1])
        while b.grid.get(npos) == ".":
            npos = (npos[0] + d[0], npos[1] + d[1])
        return int(b.grid.get(npos) == "#")

    chairs = [pos for pos, c in b.grid.items() if c != "."]

    while True:
        count = 0
        swaps = []
        for pos in chairs:
            c = b.grid[pos]
            if c == ".":
                continue
            if c == "#":
                count += 1
            s = sum(occd(pos, d) for d in ds)
            if c == "L" and s == 0 or c == "#" and s >= 5:
                swaps.append((pos, "L" if c == "#" else "#"))

        if len(swaps) == 0:
            return count
        for pos, c in swaps:
            b.grid[pos] = c


def main():
    ra = a()
    if ra is not None:
        submit(ra, part="a")

    rb = b()
    if rb is not None:
        submit(rb, part="b")


main()
