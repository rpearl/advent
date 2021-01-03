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


def possible(tri):
    return all(a + b > c for a, b, c in itertools.permutations(tri))


def a():
    s = 0
    for line in lines:
        s += possible(u.ints(line))
    return s


def b():
    nums = [u.ints(line) for line in lines]
    cs = zip(*nums)

    s = 0
    for tri in u.chunks(itertools.chain.from_iterable(cs), 3):
        s += possible(tri)
    return s


u.main(a, b, submit=globals().get("submit", False))
