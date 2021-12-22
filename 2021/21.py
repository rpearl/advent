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

def a():
    _, p0, _, p1 = ints
    s0 = s1 = 0
    die = zip(itertools.count(1), itertools.cycle(range(1,101)))
    rolls = ((max(a), sum(b)) for a, b in (zip(*c) for c in u.chunks(die, 3)))
    for rollcount, total in rolls:
        np0 = (p0+total) % 10 or 10
        ns0 = s0 + np0
        if ns0 >= 1000:
            break
        s1, s0 = ns0, s1
        p1, p0 = np0, p1
    return s1*rollcount

def b():
    rollcounts=[(3, 1), (4, 3), (5, 6), (6, 7), (7, 6), (8, 3), (9, 1)]
    cache = {}

    def count_winners(p0, p1, s0, s1):
        key = (p0,p1,s0,s1)
        if key in cache:
            return cache[key]
        w0 = w1 = 0
        for total, freq in rollcounts:
            np0 = (p0+total) % 10 or 10
            ns0 = s0+np0
            if ns0 >= 21:
                w0 += freq
            else:
                rw1, rw0 = count_winners(p1, np0, s1, ns0)
                w0 += freq*rw0
                w1 += freq*rw1
        res=w0,w1
        cache[key]=res
        return res
    _, p1, _, p2 = ints
    return max(count_winners(p1, p2, 0, 0))
    pass

u.main(a, b, submit=globals().get('submit', False))
