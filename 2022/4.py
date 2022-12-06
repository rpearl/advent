submit=True
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

ints = u.ints(data)
intlines = u.lmap(u.ints, lines)
toklines = [line.split(' ') for line in lines]

def a():
    s=0
    for line in lines:
        p1, p2 = line.split(',')
        l1, h1 = map(int,p1.split('-'))
        l2, h2 = map(int,p2.split('-'))
        if (l1 <= l2 and h1 >= h2) or (l2 <= l1  and h2 >= h1):
            s += 1
    return s
    pass


def b():
    s=0
    for line in lines:
        p1, p2 = line.split(',')
        l1, h1 = map(int,p1.split('-'))
        l2, h2 = map(int,p2.split('-'))
        r1 = set(range(l1, h1+1))
        r2 = set(range(l2, h2+1))
        if len(r1&r2):
            s += 1
    return s
    pass

u.main(a, b, submit=globals().get('submit', False))
