submit = True
from aocd import data, lines
import sys
from collections import Counter, defaultdict, deque
import functools
from sortedcontainers import SortedList, SortedDict, SortedSet
import itertools
import u
import math


print(f"File line count: {len(lines)}")


def a():
    d = {}
    hist = u.ints(data)
    for i, x in enumerate(hist[:-1]):
        d[x] = i
    while len(hist) < 2020:
        last = hist[-1]
        idx = len(hist) - 1
        prev = d.get(last, idx)
        hist.append(idx - prev)
        d[last] = idx
    return hist[2020 - 1]


def b():
    d = {}
    hist = u.ints(data)
    for i, x in enumerate(hist[:-1]):
        d[x] = i
    while len(hist) < 30000000:
        last = hist[-1]
        idx = len(hist) - 1
        prev = d.get(last, idx)
        hist.append(idx - prev)
        d[last] = idx
    return hist[30000000 - 1]


u.main(a, b, submit=globals().get("submit", False))
