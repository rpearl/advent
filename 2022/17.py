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

#data = ">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"

ints = u.ints(data)
intlines = u.lmap(u.ints, lines)
toklines = [line.split(' ') for line in lines]

def horiz(pos):
    return {u.vadd(pos, (x, 0)) for x in range(4)}

def plus(pos):
    return {
        u.vadd(pos, (1, 0)),
        u.vadd(pos, (0, -1)),
        u.vadd(pos, (1, -1)),
        u.vadd(pos, (2, -1)),
        u.vadd(pos, (1, -2)),
    }

def angle(pos):
    return {
        u.vadd(pos, (2, 0)),
        u.vadd(pos, (0, 0)),
        u.vadd(pos, (1, 0)),
        u.vadd(pos, (2, -1)),
        u.vadd(pos, (2, -2)),
    }

def vert(pos):
    return {u.vadd(pos, (0, -y)) for y in range(4)}

def square(pos):
    return {u.vadd(pos, (1-x, -y)) for x in range(2) for y in range(2)}

rocks = [horiz, plus, angle, vert, square]

jet_dirs = {'>': (1, 0), '<': (-1, 0)}

debug = False

def dprint(s): 
    if not debug: return
    print(s)

def stringify(chamber, rock):
    out = []
    c = chamber|rock
    min_x = min(x for x,y in c)
    max_x = max(x for x,y in c)
    min_y = min(y for x,y in c)
    max_y = max(0, max(y for x,y in c))

    for y in range(min_y, max_y+1):
        out.append(''.join(
            ('#' if (x,y) in chamber else '@' if (x,y) in rock else ' ')
            for x in range(7)
        ))
    return out
def dbg(chamber, rock):
    if debug:
        for line in stringify(chamber, rock):
            print(f'|{line}|')
        print('+-------+')
        print()


def sim(chamber, start, cur_rock, jets):
    rock_pos = (2, start-3)
    for jetindex, jet in jets:
        new_rock_pos = u.vadd(rock_pos, jet_dirs[jet])
        new_rock = cur_rock(new_rock_pos)
        dprint(f"Jet of gas pushes rock {'left' if jet=='<' else 'right'}:")
        if all(0 <= pos[0] <= 6 and pos not in chamber for pos in new_rock):
            rock_pos = new_rock_pos
            dbg(chamber, new_rock)
        else:
            dprint('No movement')
        new_rock_pos = u.vadd(rock_pos, (0, 1))
        new_rock = cur_rock(new_rock_pos)
        if all(pos[1] <= 0 and pos not in chamber for pos in new_rock):
            dprint('Rock falls one unit:')
            dbg(chamber, new_rock)
            rock_pos = new_rock_pos
        else:
            dprint('Rock falls one unit, causing it to come to rest:')
            dbg(chamber, cur_rock(rock_pos))
            rock = cur_rock(rock_pos)
            chamber |= rock
            end = min(start, min(y for x,y in rock)-1)
            return (jetindex, end)

def a():
    chamber = set()
    start = 0
    jets = itertools.cycle(enumerate(data))
    for i in range(2022):
        cur_rock = rocks[i % len(rocks)]
        _, start = sim(chamber, start, cur_rock, jets)

    return -start

def b():
    chamber = set()
    start = 0
    jets = itertools.cycle(enumerate(data))
    rockfns = enumerate(itertools.cycle(rocks))
    count = 0
    seen = {}
    stop = None

    for i,cur_rock in rockfns:
        jetindex, start = sim(chamber, start, cur_rock, jets)

        needle = []
        for y in range(start+1, start+50):
            line = []
            for x in range(7):
                if (x,y) in chamber:
                    line.append(x)
            needle.append(tuple(line))
        needle = tuple(needle)
        if i == stop:
            return -start + loops*loopheight- 1
        if i>2022 and (needle,jetindex) in seen and stop is None:
            last,lastheight = seen[needle,jetindex]
            curheight=-start
            remaining = 1000000000000-i
            loops, remainder = divmod(remaining, i - last)
            loopheight = curheight-lastheight
            stop = i+remainder
            print(f'repeat at {i=} {last=} {loopheight=} {remainder=}')
        seen[needle,jetindex] = i,-start
    pass

u.main(a, b, submit=globals().get('submit', False))
