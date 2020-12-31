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


def a():
    sizes = u.ints(data)
    out = 0
    for s in u.powerset(sizes):
        if sum(s) == 150:
            out += 1
    return out


def b():
    sizes = u.ints(data)
    bestln = math.inf
    out = 0
    for s in u.powerset(sizes):
        if sum(s) != 150:
            continue
        l = len(s)
        if l < bestln:
            bestln = l
            best = 0
        if l == bestln:
            best += 1
    return best


u.main(a, b, submit=globals().get("submit", False))
