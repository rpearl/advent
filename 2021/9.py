#submit=True
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
    grid, _, _ = u.make_grid(lines, lambda v, p: int(v))
    s = 0
    for p, h in grid.items():
        if all(h < grid[n] for n in u.orthogonal(grid, p)):
            s += (h+1)
    return s
    pass


def b():
    grid, _, _ = u.make_grid(lines, lambda v, p: int(v))
    sizes = []
    def nbrs(p):
        for n in u.orthogonal(grid, p):
            if grid[n] < 9:
                yield n
    for p, h in grid.items():
        if not all(h < grid[n] for n in u.orthogonal(grid, p)):
            continue
        _, dists = u.bfs(p, nbrs)
        sizes.append(len(dists))
    sizes.sort()
    return sizes[-1]*sizes[-2]*sizes[-3]

u.main(a, b, submit=globals().get('submit', False))
