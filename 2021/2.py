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
    h = depth = 0
    for d, amt in toklines:
        amt = int(amt)
        if d == 'forward':
            h += amt
        elif d == 'down':
            depth += amt
        elif d == 'up':
            depth -= amt
    return h*depth


def b():
    h = depth = aim = 0
    for d, amt in toklines:
        amt = int(amt)
        if d == 'forward':
            h += amt
            depth += aim*amt
        elif d == 'down':
            aim += amt
        elif d == 'up':
            aim -= amt
    return h*depth

u.main(a, b, submit=globals().get('submit', False))
