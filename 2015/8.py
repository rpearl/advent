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


def a():
    s = 0
    for line in lines:
        esc = line[1:-1].encode("utf-8").decode("unicode_escape")
        s += len(line) - len(esc)
    return s
    pass


def b():
    s = 2 * len(lines) + data.count('"') + data.count("\\")
    return s


u.main(a, b, submit=globals().get("submit", False))
