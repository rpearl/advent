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
from libnum import factorize

# data = "150"


def cprod(p, k):
    cur = 1
    for _ in range(k + 1):
        yield cur
        cur *= p


def a():
    d = int(data)
    n = d // 10
    presents = [0] * (n + 1)
    for k in range(1, n + 1):
        for i in range(k, n + 1, k):
            presents[i] += k * 10
    for i, np in enumerate(presents):
        if np >= d:
            return i


def b():
    d = int(data)
    n = d // 10
    presents = [0] * (n + 1)
    for k in range(1, n + 1):
        for i in itertools.islice(range(k, n + 1, k), 50):
            presents[i] += k * 11
    for i, np in enumerate(presents):
        if np >= d:
            return i


u.main(a, b, submit=globals().get("submit", False))
