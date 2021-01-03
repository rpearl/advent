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
from libnum import solve_crt

# data = """Disc #1 has 5 positions; at time=0, it is at position 4.
# Disc #2 has 2 positions; at time=0, it is at position 1."""
# lines = data.splitlines()

# t = 0: 4
# t = 1: 0
# t = 2: 1
# t = 3: 2
# t = 4: 3
# t = 5: 4

# (t - 2) % 13 = 0
# t % 13 = 2
def a():
    mods = []
    remainders = []
    info = [(-pos - disc, mod) for disc, mod, _, pos in map(u.ints, lines)]
    return solve_crt(*zip(*info))


def b():
    mods = []
    remainders = []
    info = [(-pos - disc, mod) for disc, mod, _, pos in map(u.ints, lines)] + [
        (-len(lines) - 1, 11)
    ]
    return solve_crt(*zip(*info))


u.main(a, b, submit=globals().get("submit", False))
