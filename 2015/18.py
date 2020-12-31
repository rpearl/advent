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

size = 100
steps = 100
data = """.#.#.#
...##.
#....#
..#...
#.#..#
####.."""
# lines = data.splitlines()

deltas = [complex(x, y) for x, y in u.dirs + u.diags]


def neighbors(pos):
    ns = [pos + delta for delta in deltas]
    return [npos for npos in ns if 0 <= npos.real < size and 0 <= npos.imag < size]


def print_grid(active):
    for y in range(size):
        s = []
        for x in range(size):
            s.append("#" if complex(x, y) in active else ".")
        print("".join(s))


def a():
    active = {
        complex(x, y)
        for y, line in enumerate(lines)
        for x, c in enumerate(line)
        if c == "#"
    }
    for step in range(steps):
        active = {
            pos
            for pos, c in Counter(
                itertools.chain.from_iterable(map(neighbors, active))
            ).items()
            if c == 3 or (c == 2 and pos in active)
        }
    return len(active)

    pass


def b():
    active = {
        complex(x, y)
        for y, line in enumerate(lines)
        for x, c in enumerate(line)
        if c == "#"
    } | {0, 0 + 99j, 99, 99 + 99j}
    for step in range(steps):
        active = {
            pos
            for pos, c in Counter(
                itertools.chain.from_iterable(map(neighbors, active))
            ).items()
            if c == 3 or (c == 2 and pos in active)
        } | {0, 0 + 99j, 99, 99 + 99j}
    return len(active)

    pass


u.main(a, b, submit=globals().get("submit", False))
