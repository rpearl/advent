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

#data = """        ...#
#        .#..
#        #...
#        ....
#...#.......#
#........#...
#..#....#....
#..........#.
#        ...#....
#        .....#..
#        .#......
#        ......#.
#
#10R5L5R10L4R5L5"""

ints = u.ints(data)
intlines = u.lmap(u.ints, lines)
toklines = [line.split(' ') for line in lines]

def rotR(d):
    return u.rot90[d]

def rotL(d):
    return rotR(rotR(rotR(d)))

def vmul(v, s):
    return tuple(s*x for x in v)

score = {
    u.E: 0,
    u.S: 1,
    u.W: 2,
    u.N: 3,
}

pathc = {
    u.N: '^',
    u.S: 'v',
    u.E: '>',
    u.W: '<',
}

def a():
    tiles, path = data.split('\n\n')
    tiles = tiles.splitlines()
    grid = {}
    width = 0
    height = len(tiles)
    startx = None
    for y, line in enumerate(tiles):
        width = max(width, len(line))
        for x, c in enumerate(line):
            if c in '.#':
                if startx is None:
                    startx = x
                grid[x,y] = c
    graph = defaultdict(dict)
    for pos, c in grid.items():
        if c == '#':
            continue
        north = u.vadd(pos, u.N)
        nc = grid.get(north)

        if nc is None:
            ny = max(y for x,y in grid if x==pos[0])
            north = (pos[0], ny)
            nc = grid.get(north)
        if nc == '.':
            graph[pos][u.N] = north
            graph[north][u.S] = pos

        east = u.vadd(pos, u.E)
        ec = grid.get(east)
        if ec is None:
            ex = min(x for x,y in grid if y == pos[1])
            east = (ex, pos[1])
            ec = grid.get(east)
        if ec == '.':
            graph[pos][u.E] = east
            graph[east][u.W] = pos

    cur = (startx, 0)

    insns = [''.join(g) for k,g in itertools.groupby(path, key=lambda x: x.isdigit())]
    insns = [int(x) if x.isdigit() else x for x in insns]
    facing = u.E
    path = {cur: facing}
    for insn in insns:
        #print(f'{cur=} {insn=} {facing=} {graph[cur]=}')
        if insn == 'L':
            facing = rotL(facing)
            path[cur] = facing
        elif insn == 'R':
            facing = rotR(facing)
            path[cur] = facing
        else:
            for step in range(insn):
                nxt = graph[cur].get(facing)
                #print(f'{step=} {cur=} {facing=} {nxt=} {graph[cur]=}')
                if nxt:
                    path[nxt] = facing
                    cur = nxt
                else:
                    break

        #for y in range(height):
        #    for x in range(width):
        #        if (x,y) in path:
        #            print(pathc[path[x,y]], end='')
        #        elif (x,y) in grid:
        #            print(grid[x,y], end='')
        #        else:
        #            print(' ', end='')
        #    print()
        #print()


    cx, cy = cur
    print(f'{cx=} {cy=} {facing=}')
    return 1000*(cy+1) + 4*(cx+1) + score[facing]

def face(pos):
    x,y = pos

    if 50 <= x < 100 and 0 <= y < 50:
        return 'A'
    elif 100 <= x < 150 and 0 <= y < 50:
        return 'B'
    elif 50 <= x < 100 and 50 <= y < 100:
        return 'C'
    elif 50 <= x < 100 and 100 <= y < 150:
        return 'D'
    elif 0 <= x < 50 and 100 <= y < 150:
        return 'E'
    elif 0 <= x < 50 and 150 <= y < 200:
        return 'F'
    else:
        raise Exception('unexpected position')


def next_pos(pos, d):
    x,y = pos
    f = face(pos)
    if y % 50 == 0 and d == u.N:
        if f == 'A':
            newx = 0
            newy = 150 + (x % 50)
            return (newx, newy), u.E
        elif f == 'B':
            newx = x % 50
            newy = 199
            return (newx, newy), u.N
        elif f in {'C', 'D', 'F'}:
            return u.vadd(pos, d), u.N
        elif f == 'E':
            newx = 50
            newy = 50 + (x % 50)
            return (newx, newy), u.E

    if y % 50 == 49 and d == u.S:
        if f in {'A', 'C', 'E'}:
            return u.vadd(pos, d), u.S
        elif f == 'B':
            newx = 99
            newy = 50 + (x % 50)
            return (newx, newy), u.W
        elif f == 'D':
            newx = 49
            newy = 150 + (x % 50)
            return (newx, newy), u.W
        elif f == 'F':
            newx = x
            newy = 100
            return (newx, newy), u.S
    if x % 50 == 0 and d == u.W:
        if f == 'A':
            newx = 0
            newy = 150 + (49-y)
            return (newx, newy), u.E
        elif f in {'B', 'D'}:
            return u.vadd(pos, d), u.W
        elif f == 'C':
            newx = y % 50
            newy = 100
            return (newx, newy), u.S
        elif f == 'E':
            newx = 50
            newy = 49 - (y % 50)
            return (newx, newy), u.E
        elif f == 'F':
            newx = 50 + y % 50
            newy = 0
            return (newx, newy), u.S
    if x % 50 == 49 and d == u.E:
        if f in {'A', 'E'}:
            return u.vadd(pos, d), d
        elif f == 'B':
            newx = 99
            newy = 100 - (y % 50)
            return (newx, newy), u.W
        elif f == 'C':
            newx = 100 + (y % 50)
            newy = 49
            return (newx, newy), u.N
        elif f == 'D':
            newx = 149
            newy = 49 - (y % 50)
            return (newx, newy), u.E
        elif f == 'F':
            newx = 50 + y % 50
            newy = 149
            return (newx, newy), u.N

    return u.vadd(pos, d), d


def b():
    tiles, path = data.split('\n\n')
    tiles = tiles.splitlines()
    grid = {}
    width = 0
    height = len(tiles)
    startx = None
    for y, line in enumerate(tiles):
        width = max(width, len(line))
        for x, c in enumerate(line):
            if c in '.#':
                if startx is None:
                    startx = x
                grid[x,y] = c

    cur = (startx, 0)

    insns = [''.join(g) for k,g in itertools.groupby(path, key=lambda x: x.isdigit())]
    insns = [int(x) if x.isdigit() else x for x in insns]
    facing = u.E

    for insn in insns:
        if insn == 'L':
            facing = rotL(facing)
        elif insn == 'R':
            facing = rotR(facing)
        else:
            for step in range(insn):
                npos, nfacing  = next_pos(cur, facing)
                assert npos in grid, f'{npos=} {cur=} {pathc[facing]=}'
                if grid[npos] == '.':
                    cur = npos
                    facing = nfacing
                else:
                    break
    cx, cy = cur
    print(f'{cx=} {cy=} {facing=}')
    return 1000*(cy+1) + 4*(cx+1) + score[facing]


    pass

u.main(a, b, submit=globals().get('submit', False))
