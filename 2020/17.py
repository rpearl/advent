submit = True
from aocd import data, lines
import sys
from collections import Counter, defaultdict, deque
import functools
from sortedcontainers import SortedList, SortedDict, SortedSet
import itertools
import u
import math
import time
import operator


def deltas(dim):
    z = (0,) * dim
    return [delta for delta in itertools.product((-1, 0, 1), repeat=dim) if delta != z]


dts = {3: deltas(3), 4: deltas(4)}


@functools.cache
def neighbors(pos):
    dim = len(pos)
    return [tuple(map(sum, zip(pos, delta))) for delta in dts[dim]]


initial = [
    (x, y)
    for y in range(len(lines))
    for x in range(len(lines[0]))
    if lines[y][x] == "#"
]


def run(n):
    active = {p + (0,) * (n - 2) for p in initial}
    for step in range(6):
        active = {
            pos
            for pos, c in Counter(itertools.chain(*map(neighbors, active))).items()
            if c == 3 or (c == 2 and pos in active)
        }

    return len(active)


def a():
    return run(3)


def b():
    return run(4)


u.main(a, b, submit=globals().get("submit", False))
