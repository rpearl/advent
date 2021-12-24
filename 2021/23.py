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
from tqdm import tqdm

ints = u.ints(data)
intlines = u.lmap(u.ints, lines)
toklines = [line.split(' ') for line in lines]

weightmap = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}

target = [
    "#############",
    "#...........#",
    "###A#B#C#D###",
#    "  #A#B#C#D#",
#    "  #A#B#C#D#",
    "  #A#B#C#D#",
    "  #########",
]

#lines = lines[:3] + [
#"  #D#C#B#A#",
#"  #D#B#A#C#",
#] + lines[3:]

#print(lines)

#lines = lines[:3

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


def print_grid(grid):
    width = max(x for x,_ in grid)
    height = max(y for _,y in grid)
    for y in u.incrange(height):
        for x in u.incrange(width):
            c = grid.get((x,y), ' ')
            print(c, end='')
        print()
    print()

def solve(init, end):
    target_state = build_state(end)
    target_grid = unfreeze(target_state)
    initial_state = build_state(init)
    room_positions = {(x,y) for (x,y),c in target_grid.items() if c in weightmap}
    doorway_positions = {(x,1) for x, _ in room_positions}
    hallway_positions = set(target_grid.keys()) - room_positions - doorway_positions
    def make_move(grid, src, dst):
        newgrid = dict(grid)
        c = newgrid[src]
        newgrid[src] = '.'
        newgrid[dst] = c
        return freeze(newgrid)

    def room_occupants(grid, p):
        x, _ = p
        return {grid[r] for r in room_positions if r[0] == x}

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
                return room_occupants(grid, dst).issubset({'.',c})
        wt = weightmap[c]
        return ((make_move(grid, src, p), wt*dist) for p, dist in dists.items() if allowed(p))

    with tqdm() as pbar:
        def moves(state):
            grid = unfreeze(state)
            for p, c in state:
                if c in weightmap:
                    for c in reachable(grid, p, c):
                        pbar.update(1)
                        yield c

        _, dists = u.dijkstra(initial_state, moves, target_state)
    return dists[target_state]

def a():
    return solve(lines, target)

def b():
    new_initial = lines[:3] + [
        "  #D#C#B#A#",
        "  #D#B#A#C#",
    ] + lines[3:]

    new_target = target[:3] + [target[3], target[3]] + target[3:]
    return solve(new_initial, new_target)

u.main(a, b, submit=globals().get('submit', False))
