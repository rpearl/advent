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

def is_vis_from_dir(grid, w, h, pos, dx, dy):
    x, y = pos
    vals = []
    while 0 <= y < h and 0 <= x < w:
        vals.append(grid[x,y])
        x += dx
        y += dy
    cur, *to_edge = vals
    return all(cur > e for e in to_edge)

def is_vis(grid, w, h, pos):
    return (
        is_vis_from_dir(grid, w, h, pos, 0, 1 ) or
        is_vis_from_dir(grid, w, h, pos, 0, -1) or
        is_vis_from_dir(grid, w, h, pos,  1, 0) or
        is_vis_from_dir(grid, w, h, pos, -1, 0)
    )

def view_dist_from_dir(grid, w, h, pos, dx, dy):
    x, y = pos
    ht = grid[pos]
    view_dist = 0
    x += dx
    y += dy
    while 0 <= y < h and 0 <= x < w:
        if ht > grid[x,y]:
            view_dist += 1
            x += dx
            y += dy
        else:
            view_dist += 1
            break
    return view_dist

def view_score(grid, w, h, pos):
    return (
        view_dist_from_dir(grid, w, h, pos, 0, -1) *
        view_dist_from_dir(grid, w, h, pos, -1, 0) *
        view_dist_from_dir(grid, w, h, pos, 0, 1) *
        view_dist_from_dir(grid, w, h, pos, 1, 0)
    )
def a():
    grid, w, h = u.make_grid(lines, lambda p,_:int(p))
    return sum(is_vis(grid, w, h, pos) for pos in grid.keys())

def b():
    grid, w, h = u.make_grid(lines, lambda p,_:int(p))
    return max(view_score(grid, w,h, pos) for pos in grid)

u.main(a, b, submit=globals().get('submit', False))
