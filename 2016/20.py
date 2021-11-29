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
from intervaltree import Interval, IntervalTree

banned = IntervalTree.from_tuples(
    [
        (low, high + 1)
        for low, high in map(lambda line: map(int, line.split("-")), lines)
    ]
)
banned.merge_overlaps()


def a():
    i = 0
    while True:
        ivls = banned.at(i)
        if not ivls:
            return i
        else:
            i = max(ivl.end for ivl in ivls)


def b():
    allowed = 2 ** 32
    for ivl in banned:
        ln = ivl.end - ivl.begin
        allowed -= ln
    return allowed
    pass


u.main(a, b, submit=globals().get("submit", False))
