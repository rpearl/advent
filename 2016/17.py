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
import hashlib

passcode = data.encode("ascii")

dirs = {
    b"U": (0, -1),
    b"D": (0, 1),
    b"L": (-1, 0),
    b"R": (1, 0),
}
order = b"UDLR"

valid = set(itertools.product(range(4), repeat=2))


def neighbors(node):
    pos, path = node
    x, y = pos
    h = hashlib.md5(passcode + path).hexdigest()[:4]
    for i, c in enumerate(h):
        if c < "b":
            continue
        d = order[i : i + 1]
        dx, dy = dirs[d]
        npos = (x + dx, y + dy)
        if npos in valid:
            yield (npos, path + d)


def a():

    terminal = None

    def is_done(node, preds, dists):
        nonlocal terminal
        if node[0] == (3, 3):
            terminal = node
            return True
        else:
            return False

    start = ((0, 0), b"")
    _, dists = u.bfs(start, neighbors, is_done)
    return terminal[1].decode("ascii")


def b():
    stack = [((0, 0), b"")]
    visited = set()
    best = -math.inf

    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        if node[0] == (3, 3):
            best = max(best, len(node[1]))
        else:
            for neighbor in neighbors(node):
                stack.append(neighbor)
    return best


u.main(a, b, submit=globals().get("submit", False))
