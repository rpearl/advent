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


def looksay(s, n):
    for _ in range(n):
        ns = []
        for k, g in itertools.groupby(s):
            ns.extend([len(list(g)), k])
        s = ns
    return s


def a():
    s = looksay([int(c) for c in data], 40)
    return len(s)


def b():
    s = looksay([int(c) for c in data], 50)
    return len(s)


u.main(a, b, submit=globals().get("submit", False))
