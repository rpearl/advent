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

ints = u.ints(data)
intlines = u.lmap(u.ints, lines)
toklines = [line.split(' ') for line in lines]

weightmap = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}

target = [
    "#############",
    "#...........#",
    "###A#B#C#D###",
    "  #A#B#C#D#",
    "  #########",
]

def freeze(state):
    return frozenset(state.items())

def unfreeze(frozen):
    return {p: c for p, c in frozen}

def build_state(m):
    grid = {}
    for y in range(len(m)):
        for x in range(len(m[y])):
            c = m[y][x]
            if c in 'ABCD.':
                grid[x,y] = c
    return freeze(grid)

target_state = build_state(target)
target_grid = unfreeze(target_state)
initial_state = build_state(lines)
room_positions = {(x,y) for (x,y),c in target_grid.items() if c in weightmap}
doorway_positions = {(x,1) for x, _ in room_positions}
hallway_positions = set(target_grid.keys()) - room_positions - doorway_positions

def print_grid(grid):
    mutable = [list(l) for l in target]
    for (x,y),c in grid.items():
        mutable[y][x] = c
    for line in mutable:
        print(''.join(line))

def make_move(grid, src, dst):
    newgrid = dict(grid)
    c = newgrid[src]
    newgrid[src] = '.'
    newgrid[dst] = c
    return freeze(newgrid)

def room_occupants(grid, p):
    x, y1 = p
    y2 = 2 if y == 3 else 3

def reachable(grid, src, c):
    def neighbors(n):
        for neighbor in u.orthogonal(grid, n):
            if grid[neighbor] == '.':
                yield neighbor
    _, dists = u.bfs(src, neighbors)

    def allowed(dst):
        if src in room_positions:
            return dst in hallway_positions
        else:
            if target_grid[dst] != c:
                return False
            x, y1 = dst
            y2 = 2 if y1 == 3 else 3
            return grid[x,y2] in {'.',c}
    wt = weightmap[c]
    return ((make_move(grid, src, p), wt*dist) for p, dist in dists.items() if allowed(p))

def moves(state):
    grid = unfreeze(state)
    for p, c in state:
        if c in weightmap:
            yield from reachable(grid, p, c)

def a():
    return
    #for newstate, _ in moves(initial_state):
    #    print_grid(unfreeze(newstate))
    #    print()
    #return
    _, dists = u.dijkstra(initial_state, moves, target_state)
    return dists[target_state]


def b():
    pass

u.main(a, b, submit=globals().get('submit', False))
