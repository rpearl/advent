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
    cols = list(zip(*lines))
    out = []
    for col in cols:
        counter = Counter(col)
        (best,) = counter.most_common(1)
        out.append(best[0])
    return "".join(out)


def b():
    cols = list(zip(*lines))
    out = []
    for col in cols:
        counter = Counter(col)
        best = counter.most_common()[-1]
        out.append(best[0])
    return "".join(out)


u.main(a, b, submit=globals().get("submit", False))
