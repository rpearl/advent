# submit = True
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
import hashlib

# data = "abc"


@functools.cache
def get_info(val, hashfn):
    s = data + str(val)
    h = hashfn(s)
    three = None
    fives = set()
    for k, g in itertools.groupby(h):
        ln = len(list(g))
        if ln >= 3 and not three:
            three = k
        if ln >= 5:
            fives.add(k)
    return (three, fives)


@functools.cache
def is_key(val, hashfn):
    three, _ = get_info(val, hashfn)

    for nv in range(val + 1, val + 1 + 1000):
        _, fives = get_info(nv, hashfn)
        if three in fives:
            return True
    return False


def a():
    def hashfn(s):
        return hashlib.md5(s.encode("ascii")).hexdigest()

    keys = []
    for i in itertools.count(0):
        if is_key(i, hashfn):
            keys.append(i)
            if len(keys) == 64:
                return i


def b():
    def hashfn(s):
        v = s.encode("ascii")
        for _ in range(2017):
            v = hashlib.md5(v).hexdigest().encode("ascii")
        return v

    keys = []
    for i in itertools.count(0):
        if is_key(i, hashfn):
            keys.append(i)
            if len(keys) == 64:
                return i
    pass


u.main(a, b, submit=globals().get("submit", False))
