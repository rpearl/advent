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


def run(days):
    state = list(ints)
    phases = deque(ints.count(i) for i in range(9))
    for i in range(days):
        num = phases.popleft()
        phases.append(num)
        phases[6] += num
    return sum(phases)

def a():
    return run(80)


def b():
    return run(256)



u.main(a, b, submit=globals().get('submit', False))
