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

happiness = defaultdict(int)
ppl = set()
for line in lines:
    (w,) = u.ints(line)
    if "lose" in line:
        w *= -1
    names = line.split(" ")
    a = names[0]
    b = names[-1][:-1]
    happiness[a, b] = w
    ppl |= {a, b}
print(happiness)


def a():
    m = -math.inf
    mp = None
    for p in itertools.permutations(ppl):
        prev, *rest = p
        s = 0
        for chair in rest + [prev]:
            s += happiness[prev, chair]
            s += happiness[chair, prev]
            prev = chair
        if s > m:
            m = s
            mp = p
    return m


def b():
    m = -math.inf
    mp = None
    nppl = ppl | {"me"}
    for p in itertools.permutations(nppl):
        prev, *rest = p
        s = 0
        for chair in rest + [prev]:
            s += happiness[prev, chair]
            s += happiness[chair, prev]
            prev = chair
        if s > m:
            m = s
            mp = p
    return m


u.main(a, b, submit=globals().get("submit", False))
