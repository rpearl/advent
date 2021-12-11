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

def step(grid):
    queue = deque([])
    flashed = set()
    for pos, val in grid.items():
        grid[pos] += 1
        if grid[pos] > 9:
            queue.append(pos)

    while queue:
        node = queue.popleft()
        if grid[node] > 9 and node not in flashed:
            flashed.add(node)
            for neighbor in u.all_neighbors(grid, node):
                grid[neighbor] += 1
                queue.append(neighbor)
    for pos in flashed:
        grid[pos] = 0
    return flashed


def a():
    grid, w, h = u.make_grid(lines, lambda v,p: int(v))

    flashes = 0
    for _ in range(100):
        flashes += len(step(grid))
    return flashes


def b():
    grid, w, h = u.make_grid(lines, lambda v,p: int(v))
    for s in itertools.count(1):
        flashed = step(grid)
        if len(flashed) == len(grid):
            return s

u.main(a, b, submit=globals().get('submit', False))
