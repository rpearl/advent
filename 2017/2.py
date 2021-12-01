#submit=True
from aocd import data, lines #type: ignore
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
        xs = u.ints(line)
        d = max(xs)-min(xs)
        s += d
    return s


def b():
    s=0
    for line in lines:
        for p in itertools.combinations(u.ints(line), 2):
            y,x = min(p), max(p)
            d,r = divmod(x,y)
            if r == 0:
                s += d
    return s

u.main(a, b, submit=globals().get('submit', False))
