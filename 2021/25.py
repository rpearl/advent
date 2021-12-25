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
    grid, width, height = u.make_grid(lines)

    def ahead(cuke, pos):
        x,y = pos
        if cuke == '>':
            return ((x+1)%width, y)
        else:
            return (x, (y+1)%height)

    def move(grid, cuke):
        changed = False
        newgrid = {}
        for pos, c in grid.items():
            if pos not in newgrid:
                newgrid[pos] = c
            ap = ahead(cuke, pos)
            if c == cuke and grid[ap] == '.':
                changed = True
                newgrid[ap] = c
                newgrid[pos] = '.'
        return newgrid, changed

    for step in itertools.count(1):
        grid, c1 = move(grid, '>')
        grid, c2 = move(grid, 'v')
        if not c1 and not c2: return step


def b():
    pass

u.main(a, b, submit=globals().get('submit', False))
