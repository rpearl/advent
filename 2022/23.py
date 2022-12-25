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

dirs = {
    'NW': (-1, -1),
     'N': ( 0, -1),
    'NE': ( 1, -1),
     'E': ( 1,  0),
    'SE': ( 1,  1),
     'S': ( 0,  1),
    'SW': (-1,  1),
     'W': (-1,  0),
}

northwards = {'N', 'NE', 'NW'}
southwards = {'S', 'SE', 'SW'}
westwards =  {'W', 'SW', 'NW'}
eastwards =  {'E', 'SE', 'NE'}

checks = [
    ('N', northwards),
    ('S', southwards),
    ('W', westwards),
    ('E', eastwards),
]

#data="""..............
#..............
#.......#......
#.....###.#....
#...#...#.#....
#....#...##....
#...#.###......
#...##.#.##....
#....#..#......
#..............
#..............
#.............."""
#lines=data.splitlines()

def p(elves):
    return
    lx = min(x for x,y in elves)
    ly = min(y for x,y in elves)
    hx = max(x for x,y in elves)
    hy = max(y for x,y in elves)

    for y in range(ly, hy+1):
        for x in range(lx, hx+1):
            c = '#' if (x,y) in elves else '.'
            print(c, end='')
        print()
    print()

def a():
    elves = set()
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == '#':
                elves.add((x,y))

    p(elves)
    for i in range(10):
        proposed = defaultdict(list)
        for elf in elves:
            neighbors = {k for k, d in dirs.items() if u.vadd(elf, d) in elves}
            if len(neighbors) == 0:
                proposed[elf].append(elf)
            else:
                for j in range(len(checks)):
                    d, check = checks[(j + i) % len(checks)]
                    if len(check & neighbors) == 0:
                        proposed[u.vadd(elf, dirs[d])].append(elf)
                        break
                else:
                    proposed[elf].append(elf)

        nelves = set()
        for pos, movers in proposed.items():
            if len(movers) == 1:
                nelves.add(pos)
            else:
                for elf in movers:
                    nelves.add(elf)

        elves = nelves

        p(elves)


    lx = min(x for x,y in elves)
    ly = min(y for x,y in elves)
    hx = max(x for x,y in elves)
    hy = max(y for x,y in elves)

    width = hx-lx+1
    height = hy-ly+1
    return width*height-len(elves)


    pass


def b():
    elves = set()
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == '#':
                elves.add((x,y))

    for i in itertools.count():
        proposed = defaultdict(list)
        for elf in elves:
            neighbors = {k for k, d in dirs.items() if u.vadd(elf, d) in elves}
            if len(neighbors) == 0:
                proposed[elf].append(elf)
            else:
                for j in range(len(checks)):
                    d, check = checks[(j + i) % len(checks)]
                    if len(check & neighbors) == 0:
                        proposed[u.vadd(elf, dirs[d])].append(elf)
                        break
                else:
                    proposed[elf].append(elf)

        nelves = set()
        for pos, movers in proposed.items():
            if len(movers) == 1:
                nelves.add(pos)
            else:
                for elf in movers:
                    nelves.add(elf)

        if elves == nelves:
            return i+1
        elves = nelves

        p(elves)


    lx = min(x for x,y in elves)
    ly = min(y for x,y in elves)
    hx = max(x for x,y in elves)
    hy = max(y for x,y in elves)

    width = hx-lx+1
    height = hy-ly+1
    return width*height-len(elves)
    pass

u.main(a, b, submit=globals().get('submit', False))
