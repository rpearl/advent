submit=True
from aocd import data #type: ignore
from aocd import submit as sbmt #type: ignore
import sys
from collections import Counter, defaultdict, deque
import functools
from sortedcontainers import SortedList, SortedDict, SortedSet
import itertools
import u
import math
import time
import operator

_data="""...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""

lines = data.splitlines()

ints = u.ints(data)
intlines = u.lmap(u.ints, lines)
toklines = [line.split(' ') for line in lines]



def run(expansion):
    def empty(l):
        return all(c == '.' for c in l)

    expansion_rows = {y for y, row in enumerate(lines) if empty(row)}
    expansion_cols = {x for x, col in enumerate(zip(*lines)) if empty(col)}

    galaxies = set()
    ey = 0
    for y, row in enumerate(lines):
        ey += expansion if y in expansion_rows else 1
        ex = 0
        for x, c in enumerate(row):
            ex += expansion if x in expansion_cols else 1
            if c == '#':
                galaxies.add((ex,ey))
    s = 0
    for a, b in itertools.combinations(galaxies, r=2):
        ax, ay = a
        bx, by = b
        d = abs(ax-bx) + abs(ay-by)
        s += d
    return s

def a():
    return run(2)


def b():
    return run(1_000_000)

def main():
    submit = globals().get('submit', False)
    astart = time.perf_counter()
    ra = a()
    aend = time.perf_counter()
    if ra is not None:
        print(f"Part a: {ra}")
        print(f"Time taken: {aend-astart:.4f} sec")
        if submit:
            sbmt(ra, part="a")

    bstart = time.perf_counter()
    rb = b()
    bend = time.perf_counter()
    if rb is not None:
        print(f"Part b: {rb}")
        print(f"Time taken: {bend-bstart:.4f} sec")
        if submit:
            sbmt(rb, part="b")
    print()
main()
