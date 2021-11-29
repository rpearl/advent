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


def play(turns):
    spoken = [None] * turns
    d = u.ints(data)
    for i, k in enumerate(d[:-1]):
        spoken[k] = i + 1
    last = d[-1]
    for i in range(len(d), turns):
        s = spoken[last] or i
        spoken[last] = i
        last = i - s
    return last


def a():
    return play(2020)


def b():
    return play(30000000)


u.main(a, b, submit=globals().get("submit", False))
