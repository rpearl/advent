submit=True
from aocd import data, lines #type: ignore
import sys
from collections import Counter, defaultdict, deque
from frozendict import frozendict
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

dirmap = {
    '^': u.N,
    'v': u.S,
    '>': u.E,
    '<': u.W,
}
dchar = {v: k for k,v in dirmap.items()}

#data = """#.#####
##.....#
##>....#
##.....#
##...v.#
##.....#
######.#"""
#
#data="""#.######
##>>.<^<#
##.<..<<#
##>v.><>#
##<^v^^>#
#######.#"""

lines=data.splitlines()


blizzards = {}
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        if c in '^v<>':
            blizzards[x-1,y-1] = dirmap[c]

width = len(lines[0])-2
height = len(lines)-2

print(f'{width=} {height=}')

bstates = []
blizzard_state = [tuple(x) for x in blizzards.items()]
for _ in range(width*height):
    bstates.append({p for p,d in blizzard_state})

    next_state = []
    for pos, d in blizzard_state:
        newx = (pos[0] + d[0]) % width
        newy = (pos[1] + d[1]) % height
        npos = (newx, newy)
        next_state.append((npos, d))
    blizzard_state = next_state

def a():
    startx = lines[0].index('.')-1
    endx = lines[-1].index('.')-1

    startpos = (startx, -1)
    endpos = (endx, height)

    def valid_pos(pos):
        x,y = pos
        return pos == startpos or pos == endpos or (0 <= x < width and 0 <= y < height)
    print(f'{startpos=} {endpos=} {valid_pos(startpos)}')


    def neighbors(state):
        i, pos = state
        ni = (i+1) % len(bstates)
        nbz = bstates[ni]
        for move in [u.S, u.E, u.N, u.W]:
            npos = u.vadd(pos, move)
            v = valid_pos(npos)
            if v and npos not in nbz:
                yield (ni, npos)

        if pos not in nbz:
            yield (ni, pos)

    endstate = None
    def is_done(state, pred, dists):
        nonlocal endstate
        if state[1] == endpos:
            endstate = state
            return True
        else:
            return False


    _, dists = u.bfs((0, startpos), neighbors, is_done)
    return endstate[0]


def b():
    startx = lines[0].index('.')-1
    endx = lines[-1].index('.')-1

    startpos = (startx, -1)
    endpos = (endx, height)

    def valid_pos(pos):
        x,y = pos
        return pos == startpos or pos == endpos or (0 <= x < width and 0 <= y < height)
    print(f'{startpos=} {endpos=} {valid_pos(startpos)}')


    def neighbors(state):
        i, pos = state
        ni = (i+1) % len(bstates)
        nbz = bstates[ni]
        for move in [u.S, u.E, u.N, u.W]:
            npos = u.vadd(pos, move)
            v = valid_pos(npos)
            if v and npos not in nbz:
                yield (ni, npos)

        if pos not in nbz:
            yield (ni, pos)

    endstate = None
    def is_done(state, pred, dists):
        nonlocal endstate, endpos
        if state[1] == endpos:
            endstate = state
            return True
        else:
            return False

    _, dists = u.bfs((0, startpos), neighbors, is_done)

    first_pass = dists[endstate]

    endpos, startpos = startpos, endpos
    _, dists = u.bfs((endstate[0], startpos), neighbors, is_done)
    return_pass = dists[endstate]

    endpos, startpos = startpos, endpos
    _, dists = u.bfs((endstate[0], startpos), neighbors, is_done)
    final_pass = dists[endstate]

    return first_pass+return_pass+final_pass
    pass

u.main(a, b, submit=globals().get('submit', False))
