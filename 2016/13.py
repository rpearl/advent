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

# data = "10"
num = int(data)


@functools.cache
def is_open(pos):
    x, y = pos
    if x < 0 or y < 0:
        return False
    v = x * x + 3 * x + 2 * x * y + y + y * y + num
    b = bin(v)[2:]
    return b.count("1") % 2 == 0


# print("  " + "".join(str(x) for x in range(10)))
# for y in range(10):
#    s = [str(y), " "]
#    for x in range(10):
#        s.append("." if is_open((x, y)) else "#")
#    print("".join(s))


def a():
    target = (31, 39)

    def neighbors(pos):
        x, y = pos
        for dx, dy in u.dirs:
            npos = (x + dx, y + dy)
            if is_open(npos):
                yield npos

    _, dists = u.bfs((1, 1), neighbors, is_done=lambda node, pred, dist: node == target)
    return dists[target]


def b():
    def neighbors(pos):
        x, y = pos
        for dx, dy in u.dirs:
            npos = (x + dx, y + dy)
            if is_open(npos):
                yield npos

    _, dists = u.bfs(
        (1, 1),
        neighbors,
        is_done=lambda node, p, d: max(d.values()) > 50,
    )
    return len(dists) - 1


u.main(a, b, submit=globals().get("submit", False))
