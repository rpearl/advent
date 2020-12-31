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

dirs = {"^": complex(*u.N), "<": complex(*u.W), ">": complex(*u.E), "v": complex(*u.S)}


def a():
    return len(set(itertools.accumulate(dirs[c] for c in data)))
    pass


def b():
    cs = u.chunks(data, 2)
    s, rs = zip(*cs)
    sps = set(itertools.accumulate(dirs[c] for c in s))
    srps = set(itertools.accumulate(dirs[c] for c in rs))

    return len(sps | srps)


u.main(a, b, submit=globals().get("submit", False))
