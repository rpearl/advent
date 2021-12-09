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
import heapq

ints = u.ints(data)
intlines = u.lmap(u.ints, lines)
toklines = [line.split(' ') for line in lines]
grid, _, _ = u.make_grid(lines, lambda v, p: int(v))

def is_basin(p):
    return all(grid[p] < grid[n] for n in u.orthogonal(grid, p))

def a():
    return sum(h+1 for p, h in grid.items() if is_basin(p))

def b():
    sizes = [0,0,0]
    def nbrs(p):
        return (n for n in u.orthogonal(grid, p) if grid[n] < 9)
    for p in grid:
        if is_basin(p):
            _, dists = u.bfs(p, nbrs)
            heapq.heappushpop(sizes, len(dists))
    return math.prod(sizes)

u.main(a, b, submit=globals().get('submit', False))
