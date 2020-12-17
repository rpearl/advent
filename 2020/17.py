from aocd import data, lines, submit
import sys
from collections import Counter, defaultdict, deque
import functools
from sortedcontainers import SortedList, SortedDict, SortedSet
import itertools
import u
import math


def nosubmit(answer, part):
    print(f"Part {part}:\n{answer}")


# submit = nosubmit

data = """.#.
..#
###"""

# lines = data.splitlines()

print(f"File line count: {len(lines)}")


def a():
    grid = {}
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if lines[y][x] == "#":
                grid[x, y, 0] = 1

    def neighbors(pos):
        x, y, z = pos
        for dx, dy, dz in itertools.product((-1, 0, 1), repeat=3):
            if dx == dy == dz == 0:
                continue
            yield (x + dx, y + dy, z + dz)

    for step in range(6):
        ngrid = {}
        lx = min(p[0] for p in grid)
        hx = max(p[0] for p in grid)
        ly = min(p[1] for p in grid)
        hy = max(p[1] for p in grid)
        lz = min(p[2] for p in grid)
        hz = max(p[2] for p in grid)
        for z in range(lz - 1, hz + 2):
            for y in range(ly - 1, hy + 2):
                for x in range(lx - 1, hx + 2):
                    pos = x, y, z
                    cur = grid.get(pos)
                    c = sum(grid.get(npos, 0) for npos in neighbors(pos))
                    if cur == 1:
                        ngrid[pos] = 1 if c in {2, 3} else 0
                    else:
                        ngrid[pos] = 1 if c == 3 else 0
        grid = ngrid
    return sum(grid.values())
    pass


def b():
    grid = defaultdict(int)
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if lines[y][x] == "#":
                grid[x, y, 0, 0] = 1

    def neighbors(pos):
        x, y, z, w = pos
        for dx, dy, dz, dw in itertools.product((-1, 0, 1), repeat=4):
            if dx == dy == dz == dw == 0:
                continue
            yield (x + dx, y + dy, z + dz, w + dw)

    for step in range(6):
        ngrid = defaultdict(int)
        lx = min(p[0] for p in grid)
        hx = max(p[0] for p in grid)
        ly = min(p[1] for p in grid)
        hy = max(p[1] for p in grid)
        lz = min(p[2] for p in grid)
        hz = max(p[2] for p in grid)
        lw = min(p[3] for p in grid)
        hw = max(p[3] for p in grid)
        for w in range(lw - 1, hw + 2):
            for z in range(lz - 1, hz + 2):
                for y in range(ly - 1, hy + 2):
                    for x in range(lx - 1, hx + 2):
                        pos = x, y, z, w
                        c = sum(grid[npos] for npos in neighbors(pos))
                        if grid[pos] == 1:
                            ngrid[pos] = 1 if c in {2, 3} else 0
                        else:
                            ngrid[pos] = 1 if c == 3 else 0
        grid = ngrid
    return sum(grid.values())
    pass


def main():
    ra = a()
    if ra is not None:
        print(ra)
        submit(ra, part="a")

    rb = b()
    if rb is not None:
        print(rb)
        submit(rb, part="b")


main()
