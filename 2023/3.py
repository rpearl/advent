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

def a():
    grid={}

    height = len(lines)
    width = len(lines[0])
    for y in range(height):
        cur = ''
        curpos = set()
        for x in range(width):
            c = lines[y][x]
            if c.isdigit():
                cur += c
                curpos.add((x,y))
            else:
                for pos in curpos:
                    grid[pos] = (int(cur), min(curpos))
                curpos = set()
                cur = ''
                if c != '.':
                    grid[x,y] = c
        for pos in curpos:
            grid[pos] = (int(cur), min(curpos))


    vals = {}
    for pos, c in grid.items():
        if isinstance(c, str):
            print(pos, c)
            for npos in u.all_neighbors(grid, pos):
                nbr = grid[npos]
                if isinstance(nbr, str):
                    continue
                vals[nbr[1]] = nbr[0]
    return sum(vals.values())

    pass


def b():
    grid={}

    height = len(lines)
    width = len(lines[0])
    for y in range(height):
        cur = ''
        curpos = set()
        for x in range(width):
            c = lines[y][x]
            if c.isdigit():
                cur += c
                curpos.add((x,y))
            else:
                for pos in curpos:
                    grid[pos] = (int(cur), min(curpos))
                curpos = set()
                cur = ''
                if c != '.':
                    grid[x,y] = c
        for pos in curpos:
            grid[pos] = (int(cur), min(curpos))

    s = 0
    for pos, c in grid.items():
        if c == '*':
            adjacent = {}
            for npos in u.all_neighbors(grid, pos):
                nbr = grid[npos]
                if isinstance(nbr, str):
                    continue
                adjacent[nbr[1]] = nbr[0]
            if len(adjacent) == 2:
                ratio = math.prod(adjacent.values())
                s += ratio
    return s
    pass

u.main(a, b, submit=globals().get('submit', False))
