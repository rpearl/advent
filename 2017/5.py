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
    insns = u.ints(data)
    ptr = 0
    s = 0
    while 0 <= ptr < len(insns):
        s += 1
        offs = insns[ptr]
        insns[ptr] += 1
        ptr += offs
    return s


def b():
    insns = u.ints(data)
    ptr = 0
    s = 0
    while 0 <= ptr < len(insns):
        s += 1
        offs = insns[ptr]
        d = 1 if offs < 3 else -1
        insns[ptr] += d
        ptr += offs
    return s

u.main(a, b, submit=globals().get('submit', False))
