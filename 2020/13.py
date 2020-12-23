submit = True
from aocd import data, lines
import sys
from collections import Counter, defaultdict, deque
import functools
from sortedcontainers import SortedList, SortedDict, SortedSet
import itertools
import u
import math
from libnum import solve_crt

from functools import reduce


def a():
    ts = int(lines[0])
    ids = u.ints(lines[1])

    best = math.inf
    bi = None

    for b in ids:
        earliest = math.ceil(ts / b) * b
        l = earliest - ts
        if l < best:
            best = l
            bi = b
    return bi * best

    pass


def b():
    ids = lines[1].split(",")

    return solve_crt(
        [-i for i, x in enumerate(ids) if x != "x"],
        [int(x) for x in ids if x != "x"],
    )
    pass


u.main(a, b, submit=globals().get("submit", False))
