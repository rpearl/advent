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

# data = "10000"


def dragon(a):
    b = tuple(itertools.chain(a, [0], map(lambda x: 1 - x, reversed(a))))
    return b


def checksum(s):
    return tuple(1 - operator.xor(*c) for c in u.chunks(s, 2))


def stretch(s, l):
    while len(s) < l:
        s = dragon(s)
    return s[:l]


def a():
    s = stretch(tuple(map(int, data)), 272)
    done = False
    while not done:
        s = checksum(s)
        done = len(s) % 2 == 1
    return "".join(map(str, s))


def b():
    s = stretch(tuple(map(int, data)), 35651584)
    done = False
    while not done:
        s = checksum(s)
        done = len(s) % 2 == 1
    return "".join(map(str, s))
    pass


u.main(a, b, submit=globals().get("submit", False))
