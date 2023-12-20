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
lines = data.splitlines()

ints = u.ints(data)
intlines = u.lmap(u.ints, lines)
toklines = [line.split(' ') for line in lines]

bold_map = str.maketrans({
    '|': '┃',
    '-': '━',
    'L': '┗',
    'J': '┛',
    '7': '┓',
    'F': '┏',
    'S': '╳'
})

light_map = str.maketrans({
    '|': '│',
    '-': '─',
    'L': '└',
    'J': '┘',
    '7': '┐',
    'F': '┌',
})

def print_grid(grid, dists):
    height = len(lines)
    width = len(lines[0])
    for y in range(height):
        o = []
        for x in range(width):
            pretty_map = bold_map if (x,y) in dists else light_map
            o.append(grid.get((x,y),'.').translate(pretty_map))
        print(''.join(o))

connections = {
    '|': [u.N, u.S],
    '-': [u.E, u.W],
    'L': [u.N, u.E],
    'J': [u.N,u.W],
    '7': [u.S,u.W],
    'F': [u.S,u.E],
}
grid = {}
for y, row in enumerate(lines):
    for x, c in enumerate(row):
        if c != '.':
            grid[x,y] = c
        if c == 'S':
            start = x,y
scons = []
for d in [u.N, u.S, u.E, u.W]:
    dx, dy = d
    np = (start[0]+dx,start[1]+dy)
    nc = grid.get(np)
    if nc and nc in connections and u.opp[d] in connections[nc]:
        scons.append(d)
for c, cons in connections.items():
    if cons == scons:
        grid[start] = c
        break

def neighbors(pos):
    x,y = pos
    c = grid[pos]
    if c in connections:
        for dx, dy in connections[c]:
            np = (x+dx,y+dy)
            if np in grid:
                yield np
def a():
    _, dists = u.bfs(start, neighbors)
    return max(dists.values())

def b():
    stack = [start]
    seen = set()
    corners = []
    while stack:
        node = stack.pop()
        if node in seen:
            continue
        seen.add(node)
        if grid[node] in 'LJ7F':
            corners.append(node)
        stack.extend(neighbors(node))

    def det(a,b):
        ax,ay = a
        bx,by = b
        return ax*by - bx*ay

    a = abs(sum(det(corners[i], corners[i-1]) for i in range(len(corners)))) // 2
    perim = len(seen) // 2 - 1
    return a - perim


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
