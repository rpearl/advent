# submit=True
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


def a():
    grid = defaultdict(int)
    ops = {
        "turn on": lambda pos: 1,
        "turn of": lambda pos: 0,
        "toggle ": lambda pos: 1 - grid[pos],
    }
    for line in lines:
        l, t, r, b = u.ints(line)
        op = line[: len("turn on")]
        for pos in itertools.product(range(l, r + 1), range(t, b + 1)):
            grid[pos] = ops[op](pos)
    return sum(grid.values())

    pass


def b():
    grid = defaultdict(int)
    ops = {
        "turn on": lambda pos: grid[pos] + 1,
        "turn of": lambda pos: max(grid[pos] - 1, 0),
        "toggle ": lambda pos: grid[pos] + 2,
    }
    for line in lines:
        l, t, r, b = u.ints(line)
        op = line[: len("turn on")]
        for pos in itertools.product(range(l, r + 1), range(t, b + 1)):
            grid[pos] = ops[op](pos)
    return sum(grid.values())

    pass


u.main(a, b, submit=globals().get("submit", False))
