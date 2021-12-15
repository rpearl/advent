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
    grid, width, height = u.make_grid(lines, lambda v, p: int(v))

    def neighbors(pos):
        for n in u.orthogonal(grid, pos):
            yield (n, grid[n])

    pred, dist = u.dijkstra((0,0), neighbors)
    return dist[width-1,height-1]
    pass


def b():
    g, width, height = u.make_grid(lines, lambda v, p: int(v))

    grid = {}

    for x,y in g:
        risk = g[x,y]
        for col in range(5):
            for row in range(5):
                nx = row*width+x
                ny = col*height+y
                grid[nx,ny] = ((risk+col+row-1) % 9) +1

    def neighbors(pos):
        for n in u.orthogonal(grid, pos):
            yield (n, grid[n])
    pred, dist = u.dijkstra((0,0), neighbors)
    return dist[5*width-1,5*height-1]

u.main(a, b, submit=globals().get('submit', False))
