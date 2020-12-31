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
    return sum(1 if c == "(" else -1 for c in data)


def b():
    for i, s in enumerate(itertools.accumulate(1 if c == "(" else -1 for c in data)):
        if s == -1:
            return i + 1


u.main(a, b, submit=globals().get("submit", False))
