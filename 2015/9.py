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

dist = {}
nodes = set()
for line in lines:
    edge, weight = line.split(" = ")
    s, t = edge.split(" to ")
    weight = int(weight)
    dist[s, t] = weight
    dist[t, s] = weight
    nodes |= {s, t}


def a():
    def plength(path):
        return sum(dist.get(p, math.inf) for p in zip(path, path[1:]))

    return min(plength(list(p)) for p in itertools.permutations(nodes))


def b():
    def plength(path):
        return sum(dist.get(p, -math.inf) for p in zip(path, path[1:]))

    return max(plength(list(p)) for p in itertools.permutations(nodes))


u.main(a, b, submit=globals().get("submit", False))
