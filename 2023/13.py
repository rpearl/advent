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

_data="""#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#"""

lines = data.splitlines()

ints = u.ints(data)
intlines = u.lmap(u.ints, lines)
toklines = [line.split(' ') for line in lines]

def find_mirror_row(grid, needed):
    for i in range(1,len(grid)):
        up = ''.join(reversed(grid[:i]))
        down = ''.join(grid[i:])
        diffs = sum(a != b for a, b in zip(up, down))
        if diffs == needed:
            return i
    return None

def find_mirror(grid, needed):
    r = find_mirror_row(grid, needed)
    if r is not None:
        return 100*r
    tpos = [''.join(c) for c in zip(*grid)]
    return find_mirror_row(tpos, needed)

def a():
    s = 0
    for chunk in data.split('\n\n'):
        grid = chunk.splitlines()
        s += find_mirror(grid, 0)
    return s


def b():
    s = 0
    for i,chunk in enumerate(data.split('\n\n')):
        grid = chunk.splitlines()
        s += find_mirror(grid, 1)
    return s

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
