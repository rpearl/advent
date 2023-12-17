submit=True
from aocd import data #type: ignore
from aocd import submit as sbmt #type: ignore
import sys
from collections import Counter, defaultdict, deque
import functools
from sortedcontainers import SortedList, SortedDict, SortedSet
import itertools
import u
import math
import time
import operator

_data="""O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#...."""

lines = data.splitlines()

ints = u.ints(data)
intlines = u.lmap(u.ints, lines)
toklines = [line.split(' ') for line in lines]

def process_tilt(grid, x, y, d):
    if grid[x,y] != 'O':
        return
    grid[x,y] = '.'
    dx,dy = d
    i = 0
    while grid.get((x+dx*i,y+dy*i)) == '.':
        i += 1
    grid[x+dx*(i-1),y+dy*(i-1)] = 'O'


def tilt(grid, width, height, d):
    dx, dy = d
    ry = range(height)
    rx = range(width)
    if dy > 0:
        ry = reversed(ry)
    if dx > 0:
        rx = reversed(rx)

    if dx == 0:
        for y in ry:
            for x in rx:
                process_tilt(grid, x, y, d)
    else:
        for x in rx:
            for y in ry:
                process_tilt(grid, x, y, d)

def state(grid):
    return frozenset({pos for pos,c in grid.items() if c == 'O'})
def calc(grid, width, height):
    return sum(height-y for x,y in state(grid))

def a():
    grid, width, height = u.make_grid(lines)
    load=0
    tilt(grid, width, height, (0,-1))
    for (x,y),c in grid.items():
        if c == 'O':
            load += height-y
    return load


def b():
    seen = {}
    grid, width, height = u.make_grid(lines)
    steps_remaining = math.inf
    step = 0
    load = 0
    while steps_remaining > 0:
        for d in [u.N, u.W, u.S, u.E]:
            tilt(grid,width,height,d)
        s = state(grid)
        #print(s)
        if s in seen:
            tail = seen[s]
            cycle_length = step-tail
            steps_needed = 1000000000 - tail 
            steps_remaining = (steps_needed % cycle_length) 
            #print(f'{cycle_length=} {steps_remaining=}')
        seen[s] = step
        step += 1
        steps_remaining -= 1
    for (x,y),c in grid.items():
        if c == 'O':
            load += height-y
    return load
    pass

def main():
    submit = globals().get('submit', False)
    astart = time.perf_counter()
    ra = a()
    aend = time.perf_counter()
    if ra is not None:
        print(f"Part a: {ra}")
        print(f"Time taken: {aend-astart:.4f} sec")
        if submit:
            sbmt(ra, part="a")

    bstart = time.perf_counter()
    rb = b()
    bend = time.perf_counter()
    if rb is not None:
        print(f"Part b: {rb}")
        print(f"Time taken: {bend-bstart:.4f} sec")
        if submit:
            sbmt(rb, part="b")
    print()
main()
