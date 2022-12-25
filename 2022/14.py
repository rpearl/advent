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

#data = """498,4 -> 498,6 -> 496,6
#503,4 -> 502,4 -> 502,9 -> 494,9"""
#lines=data.splitlines()

ints = u.ints(data)
intlines = u.lmap(u.ints, lines)
toklines = [line.split(' ') for line in lines]

def dbg(grid):
    minx = min(x for x,y in grid.keys())-5
    maxx = max(x for x,y in grid.keys())+5
    miny = min(y for x,y in grid.keys())-5
    maxy = max(y for x,y in grid.keys())+5
    for y in range(miny, maxy+1):
        for x in range(minx, maxx+1):
            if (x,y) == (500,0):
                print('+',end='')
            else:
                print(grid[x,y], end='')
        print()

def drop_sand(grid, lowest):
    cur = complex(500, 0)
    if grid[cur] != '.':
        return True
    grid[cur] = 'o'
    while cur.imag <= lowest:

        for d in [0, -1, 1]:
            nxt = cur + d + 1j
            if grid[nxt] == '.':
                grid[cur] = '.'
                grid[nxt] = 'o'
                cur = nxt
                break
        else:
            return True
    return False

def a():
    grid = defaultdict(lambda: '.')
    for line in intlines:
        for (x1, y1), (x2, y2) in u.window(u.chunks(line, 2), 2):
            dx = u.sign(x2-x1)
            dy = u.sign(y2-y1)
            x, y = x1, y1

            while (x, y) != (x2, y2):
                grid[complex(x,y)] = '#'
                x += dx
                y += dy
            grid[complex(x2,y2)]='#'

    maxy = max(c.imag for c in grid.keys())+5
    rest = True
    tot = 0
    while rest:
        rest = drop_sand(grid, maxy)
        if rest:
            tot += 1
    return tot
    pass

class keydefaultdict(defaultdict):
    def __missing__(self, key):
        if self.default_factory is None:
            raise KeyError( key )
        else:
            ret = self[key] = self.default_factory(key)
            return ret


def b():
    grid = {}
    for line in intlines:
        for (x1, y1), (x2, y2) in u.window(u.chunks(line, 2), 2):
            dx = u.sign(x2-x1)
            dy = u.sign(y2-y1)
            x, y = x1, y1

            while (x, y) != (x2, y2):
                grid[complex(x,y)] = '#'
                x += dx
                y += dy
            grid[complex(x2,y2)]='#'

    maxy = max(c.imag for c in grid.keys())
    def default_tile(p):
        if p.imag == maxy+2:
            return '#'
        else:
            return '.'

    floorgrid = keydefaultdict(default_tile)
    for k,v in grid.items():
        floorgrid[k] = v
    tot = 0

    while floorgrid[500] != 'o':
        rest = drop_sand(floorgrid, maxy)
        tot += 1
    return tot



    pass

u.main(a, b, submit=globals().get('submit', False))
