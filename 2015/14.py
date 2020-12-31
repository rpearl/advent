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

data = """Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds."""


def a():
    reindeer = {}
    for line in lines:
        name = line.split(" ")[0]
        reindeer[name] = tuple(u.ints(line))

    def dist(name, sec):
        s, mi, ri = reindeer[name]
        full, rem = divmod(sec, mi + ri)
        return full * s * mi + min(mi, rem) * s

    return max(dist(name, 2503) for name in reindeer)


def b():
    reindeer = {}
    for line in lines:
        name = line.split(" ")[0]
        reindeer[name] = tuple(u.ints(line))

    def dist(name, sec):
        s, mi, ri = reindeer[name]
        full, rem = divmod(sec, mi + ri)
        return full * s * mi + min(mi, rem) * s

    points = Counter()

    for sec in range(2503):
        md = -math.inf
        mw = []
        for name in reindeer:
            d = dist(name, sec + 1)
            if d > md:
                mw = [name]
                md = d
            elif d == md:
                mw.append(name)

        points.update(mw)
    return max(points.values())


u.main(a, b, submit=globals().get("submit", False))
