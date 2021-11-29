import aoc
import sys
import itertools
from collections import defaultdict, deque
import functools
import math

inp = [
'#.##.',
'###.#',
'#...#',
'##..#',
'.#...',
]
#inp = [
#'....#',
#'#..#.',
#'#..##',
#'..#..',
#'#....',
#]
def make_grid():
    grid = set()
    for y in range(5):
        for x in range(5):
            if inp[y][x] == '#':
                grid.add((x,y))
    return grid

dirs = [(-1,0), (1, 0), (0, 1), (0, -1)]

def add(pos, d):
    return (pos[0]+d[0], pos[1]+d[1])

def neighbors(grid, pos):
    s = 0
    for d in dirs:
        if add(pos, d) in grid:
            s += 1
    return s

def state(grid, dbg=False):
    state = 0
    for y in range(5):
        for x in range(5):
            idx = y*5 + x
            v = int((x,y) in grid)
            state |= (v << idx)
    return state


def part1():
    grid = make_grid()

    seen = set()
    while True:
        st = state(grid)
        if st in seen:
            return st
        seen.add(st)
        newgrid = set()
        for x in range(5):
            for y in range(5):
                pos = x,y
                nbs = neighbors(grid, pos)
                if pos in grid and nbs == 1:
                    newgrid.add(pos)
                if pos not in grid and nbs in {1,2}:
                    newgrid.add(pos)
        grid = newgrid

def recursive_neighbors(pos):
    x, y, l = pos
    out = []
    for d in dirs:
        n = add((x, y), d)
        nx, ny = n
        if nx == -1:
            out.append((1, 2, l-1))
        elif nx == 5:
            out.append((3, 2, l-1))
        elif ny == -1:
            out.append((2, 1, l-1))
        elif ny == 5:
            out.append((2, 3, l-1))
        elif n == (2, 2):
            if x == 1:
                out.extend([(0, p, l+1) for p in range(5)])
            elif x == 3:
                out.extend([(4, p, l+1) for p in range(5)])
            elif y == 1:
                out.extend([(p, 0, l+1) for p in range(5)])
            elif y == 3:
                out.extend([(p, 4, l+1) for p in range(5)])
        else:
            out.append((nx, ny, l))
    return out

def part2():
    grid = {(x, y, 0) for (x,y) in make_grid()}

    for _ in range(200):
        newgrid = set()
        to_check = set()
        for pos in grid:
            to_check.add(pos)
            to_check.update(recursive_neighbors(pos))

        for pos in to_check:
            count = len([n for n in recursive_neighbors(pos) if n in grid])

            if pos in grid and count == 1:
                newgrid.add(pos)
            if pos not in grid and count in {1,2}:
                newgrid.add(pos)
        grid = newgrid
    return len(grid)
#grid = make_grid()
#print(neighbors(make_grid(), (4,0)))
#aoc.print_matrix(step(grid), {True: '#', False: '.'}, default=False)
print(recursive_neighbors((0,0,0)))
print(part1())
print(part2())
