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
#data = '0 2 7 0'
def a():
    state = tuple(u.ints(data))
    seen = set()
    def nxt(idx):
        return (idx+1) % len(state)

    stepcount = 0
    while True:
        stepcount += 1
        idx, m = u.max_index(state)
        ns = list(state)
        ns[idx] = 0
        ptr = idx
        while m > 0:
            ptr = nxt(ptr)
            ns[ptr] += 1
            m -= 1
        state = tuple(ns)
        if state in seen:
            return stepcount
        seen.add(state)

    pass


def b():
    state = tuple(u.ints(data))
    seen = dict()
    def nxt(idx):
        return (idx+1) % len(state)

    stepcount = 0
    while True:
        stepcount += 1
        idx, m = u.max_index(state)
        ns = list(state)
        ns[idx] = 0
        ptr = idx
        while m > 0:
            ptr = nxt(ptr)
            ns[ptr] += 1
            m -= 1
        state = tuple(ns)
        if state in seen:
            return stepcount - seen[state]
        seen[state] = stepcount
    pass

u.main(a, b, submit=globals().get('submit', False))
