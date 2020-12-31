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

# data = "2x3x4"


def sides(l, w, h):
    return itertools.combinations((l, w, h), 2)


def a():
    def area(l, w, h):
        return sum(2 * math.prod(s) for s in sides(l, w, h))

    def slack(l, w, h):
        return min(math.prod(s) for s in sides(l, w, h))

    return sum(area(l, w, h) + slack(l, w, h) for l, w, h in u.chunks(u.ints(data), 3))


def b():
    def min_perim(l, w, h):
        return min(2 * sum(s) for s in sides(l, w, h))

    return sum(
        math.prod((l, w, h)) + min_perim(l, w, h)
        for l, w, h in u.chunks(u.ints(data), 3)
    )


u.main(a, b, submit=globals().get("submit", False))
