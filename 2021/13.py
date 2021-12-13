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
    for insn in insns:
        axis, val = u.fixparse('fold along {}={:d}', insn)
        newgrid = set()
        for pos in grid:
            x,y = newx, newy = pos
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
    grid = {tuple(p): True for p in dots}
    for insn in insns:
        axis, val = u.fixparse('fold along {}={:d}', insn)
        newgrid = {}
        for pos in grid:
            x,y = newx, newy = pos
            if axis == 'y' and y > val:
                newx = x
                newy = val-(y-val)
            elif axis == 'x' and x > val:
                newx = val-(x-val)
                newy = y
            newgrid[newx,newy] = True
        grid=newgrid
    print()
    u.print_matrix(grid, {True: '#', False: ' '}, default=False)
    pass

u.main(a, b, submit=globals().get('submit', False))
