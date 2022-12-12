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

#data = """Sabqponm
#abcryxxl
#accszExk
#acctuvwj
#abdefghi"""
#lines=data.splitlines()

def a():
    start = None
    end = None
    def elev(p, pos):
        nonlocal start,end
        if p == 'S':
            start = pos
            return 0
        elif p == 'E':
            end = pos
            return 26
        else:
            return ord(p) - ord('a')
    grid, w, h = u.make_grid(lines, elev)

    def neighbors(pos):
        for nbr in u.orthogonal(grid, pos):
            if grid[nbr] - grid[pos] <= 1:
                yield nbr

    pred, dist = u.bfs(start, neighbors)
    return dist[end]

    pass


def b():
    starts = []
    end = None
    def elev(p, pos):
        nonlocal starts,end
        if p == 'S':
            starts.append(pos)
            return 0
        elif p == 'E':
            end = pos
            return 26
        else:
            if p == 'a':
                starts.append(pos)
            return ord(p) - ord('a')
    grid, w, h = u.make_grid(lines, elev)

    def neighbors(pos):
        for nbr in u.orthogonal(grid, pos):
            if grid[nbr] - grid[pos] >= -1:
                yield nbr

    pred, dist = u.bfs(end, neighbors)
    return min(dist[start] for start in starts if start in dist)

u.main(a, b, submit=globals().get('submit', False))
