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
#_data=""".....
#.S-7.
#.|.|.
#.L-J.
#....."""
#_data="""..F7.
#.FJ|.
#SJ.L7
#|F--J
#LJ..."""
#
#data="""...........
#.S-------7.
#.|F-----7|.
#.||.....||.
#.||.....||.
#.|L-7.F-J|.
#.|..|.|..|.
#.L--J.L--J.
#..........."""
#
#data="""..........
#.S------7.
#.|F----7|.
#.||....||.
#.||....||.
#.|L-7F-J|.
#.|..||..|.
#.L--JL--J.
#.........."""
#
#data=""".F----7F7F7F7F-7....
#.|F--7||||||||FJ....
#.||.FJ||||||||L7....
#FJL7L7LJLJ||LJ.L-7..
#L--J.L7...LJS7F-7L7.
#....F-J..F7FJ|L7L7L7
#....L7.F7||L7|.L7L7|
#.....|FJLJ|FJ|F7|.LJ
#....FJL-7.||.||||...
#....L---J.LJ.LJLJ..."""

# ..........
# .S------7.
# .|F----7|.
# .||....||.
# .||....||.
# .|L-7F-J|.
# .|..||..|.
# .L--JL--J.
# ..........
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
            o.append(grid.get((x,y),' ').translate(pretty_map))
        print(''.join(o))



def a():
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

    def neighbors(pos):
        x,y = pos
        c = grid[pos]
        if c in connections:
            for dx, dy in connections[c]:
                np = (x+dx,y+dy)
                if np in grid:
                    yield np
        else:
            assert pos == start
            for d in [u.N, u.S, u.E, u.W]:
                dx, dy = d
                np = (x+dx,y+dy)
                nc = grid.get(np)
                if nc and nc in connections and u.opp[d] in connections[nc]:
                    yield np


    _, dists = u.bfs(start, neighbors)

    print_grid(grid, dists)
    return max(dists.values())
    pass

def b():
    fills = {
        '|': [
            ['.','#','.'],
            ['.','#','.'],
            ['.','#','.'],
        ],
        '-': [
            ['.','.','.'],
            ['#','#','#'],
            ['.','.','.'],
        ],
        'L': [
            ['.','#','.'],
            ['.','#','#'],
            ['.','.','.'],
        ],
        'J': [
            ['.','#','.'],
            ['#','#','.'],
            ['.','.','.'],
        ],
        '7': [
            ['.','.','.'],
            ['#','#','.'],
            ['.','#','.'],
        ],
        'F': [
            ['.','.','.'],
            ['.','#','#'],
            ['.','#','.'],
        ],
        '.': [
            ['.','.','.'],
            ['.','^','.'],
            ['.','.','.'],
        ],
    }
    connections = {
        '|': [u.N, u.S],
        '-': [u.E, u.W],
        'L': [u.N, u.E],
        'J': [u.N,u.W],
        '7': [u.S,u.W],
        'F': [u.S,u.E],
    }

    grid = {}
    dots = set()

    for y, row in enumerate(lines):
        for x, c in enumerate(row):
            if c == '.':
                dots.add((3*x+1, 3*y+1))
            if c == 'S':
                start = 3*x+1,3*y+1
            else:
                for i in range(3):
                    for j in range(3):
                        ex = 3*x+i
                        ey = 3*y+j
                        grid[ex,ey] = fills[c][j][i]

    scons = []
    for d in [u.N, u.S, u.E, u.W]:
        sx, sy = start
        dx, dy = d
        if grid[sx-2*dx,sy-2*dy] == '#':
            scons.append(d)
    for k,v in connections.items():
        if v == scons:
            for i in range(3):
                for j in range(3):
                    ex = start[0]-1+i
                    ey = start[1]-1+j
                    grid[ex,ey] = fills[k][j][i]
            break

    def pipe_neighbors(pos):
        for npos in u.orthogonal(grid, pos):
            if grid[npos] == '#':
                yield npos

    _, pipe = u.bfs(start, pipe_neighbors)

    seen = set()
    queue = deque()
    width = len(lines[0])*3
    height = len(lines)*3
    for y in range(height):
        for x in [0, width-1]:
            pos = x,y
            if pos not in pipe:
                queue.append(pos)
    for x in range(width):
        for y in [0, height-1]:
            pos = x,y
            if pos not in pipe:
                queue.append(pos)
    print(len(queue))

    while queue:
        node = queue.popleft()
        if node in seen:
            continue
        seen.add(node)
        for child in u.orthogonal(grid, pos):
            if child not in pipe:
                queue.append(child)
    print(len(dots))
    return len(dots-seen)







    #grid = {}
    #for y, row in enumerate(lines):
    #    for x, c in enumerate(row):
    #        if c != '.':
    #            grid[x,y] = c
    #        if c == 'S':
    #            start = x,y

    #def neighbors(pos):
    #    x,y = pos
    #    c = grid[pos]
    #    if c in connections:
    #        for dx, dy in connections[c]:
    #            np = (x+dx,y+dy)
    #            if np in grid:
    #                yield np
    #    else:
    #        assert pos == start
    #        for d in [u.N, u.S, u.E, u.W]:
    #            dx, dy = d
    #            np = (x+dx,y+dy)
    #            nc = grid.get(np)
    #            if nc and nc in connections and u.opp[d] in connections[nc]:
    #                yield np


    #_, dists = u.bfs(start, neighbors)
    #inside = 0

    #def is_pipe(pos):
    #    return pos in dists

    #for cy, row in enumerate(lines):
    #    for cx, c in enumerate(row):
    #        if is_pipe((cx,cy)):
    #            continue
    #        count = 0
    #        prev = None
    #        for x in range(cx):
    #            if not is_pipe((x, cy)):
    #                continue
    #            pathc = grid[x,cy]
    #            if pathc == '|':
    #                count += 1
    #            elif pathc == '7' and prev == 'L':
    #                count += 1
    #            elif pathc == 'J' and prev == 'F':
    #                count += 1
    #            if pathc not in '|-':
    #                prev = pathc
    #        if count % 2 == 1:
    #            inside += 1
    #return inside





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
