submit=True
from aocd import data
import sys
from collections import Counter, defaultdict, deque
import functools
from sortedcontainers import SortedList, SortedDict, SortedSet
import itertools
import u
import math
import time
import operator

_data="""467..114.
...*.....
..35..633
......#..
617*.....
.....+.58
..592....
......755
...$.*...
.664.598."""

lines = data.splitlines()

ints = u.ints(data)
intlines = u.lmap(u.ints, lines)
toklines = [line.split(' ') for line in lines]

def make_grid():
    grid={}
    for y, line in enumerate(lines):
        line += '.'
        cur = ''
        curpos = set()
        for x, c in enumerate(line):
            if c.isdigit():
                cur += c
                curpos.add((x,y))
            else:
                for pos in curpos:
                    grid[pos] = (int(cur), min(curpos))
                curpos = set()
                cur = ''
                if c != '.':
                    grid[x,y] = (c, None)
    return grid

def a():
    grid = make_grid()
    vals = {}
    for pos, (sym, meta) in grid.items():
        if meta is None:
            for npos in u.all_neighbors(grid, pos):
                nsym, nm = grid[npos]
                if nm is None:
                    continue
                vals[nm] = nsym
    return sum(vals.values())



def b():
    grid = make_grid()
    s = 0
    for pos, (sym, meta) in grid.items():
        if sym == '*':
            adjacent = {}
            for npos in u.all_neighbors(grid, pos):
                nsym, nm = grid[npos]
                if nm is None:
                    continue
                adjacent[nm] = nsym
            if len(adjacent) == 2:
                ratio = math.prod(adjacent.values())
                s += ratio
    return s

u.main(a, b, submit=globals().get('submit', False))
