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

#data = """6,10
#0,14
#9,10
#0,3
#10,4
#4,11
#6,0
#6,12
#4,1
#0,13
#10,12
#3,4
#3,0
#8,4
#1,10
#2,14
#8,10
#9,0
#
#fold along y=7
#fold along x=5"""

ints = u.ints(data)
intlines = u.lmap(u.ints, lines)
toklines = [line.split(' ') for line in lines]

def a():
    dots, insns = data.split('\n\n')
    dots = [u.ints(d) for d in dots.splitlines()]
    insns = insns.splitlines()
    grid = set(tuple(p) for p in dots)
    width = max(x for x,y in grid)+1
    height = max(y for x,y in grid)+1
    for insn in insns:
        val = u.ints(insn)[0]
        axis = insn[len('fold along ')][-1]
        newgrid = set()
        for pos in grid:
            if pos not in grid:
                continue
            x,y = pos
            newx = x
            newy = y
            if axis == 'y' and y > val:
                newx = x
                newy = val-(y-val)
            elif axis == 'x' and x > val:
                newx = val-(x-val)
                newy = y
            newgrid.add((newx, newy))
        grid=newgrid
        #FUCK
        break

    return len(grid)


def b():
    dots, insns = data.split('\n\n')
    dots = [u.ints(d) for d in dots.splitlines()]
    insns = insns.splitlines()
    grid = set(tuple(p) for p in dots)
    for insn in insns:
        val = u.ints(insn)[0]
        axis = insn[len('fold along ')][-1]
        newgrid = set()
        for pos in grid:
            if pos not in grid:
                continue
            x,y = pos
            newx = x
            newy = y
            if axis == 'y' and y > val:
                newx = x
                newy = val-(y-val)
            elif axis == 'x' and x > val:
                newx = val-(x-val)
                newy = y
            newgrid.add((newx, newy))
        grid=newgrid
        #break
    width = max(x for x,y in grid)+1
    height = max(y for x,y in grid)+1
    print()
    for y in range(height):
        for x in range(width):
            print('#' if (x,y) in grid else ' ', end='')
        print()
    print()
    pass

u.main(a, b, submit=globals().get('submit', False))
