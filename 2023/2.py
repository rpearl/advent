submit=True
from aocd import data
import sys
from collections import Counter, defaultdict, deque
import functools
from sortedcontainers import SortedList, SortedDict, SortedSet
import itertools
import u
import math
import time
import operator

_data="""Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

lines = data.splitlines()

ints = u.ints(data)
intlines = u.lmap(u.ints, lines)
toklines = [line.split(' ') for line in lines]

def a():
    allowed = {'red': 12, 'green': 13, 'blue': 14}
    s = 0
    for line in lines:
        game, rounds = line.split(': ')
        game = u.ints(game)[0]
        rounds = rounds.split('; ')
        impossible = False
        for r in rounds:
            cubelist = r.split(', ')
            for c in cubelist:
                num, color = c.split(' ')
                num=int(num)
                if num > allowed.get(color, 0):
                    impossible = True
                    break
        if not impossible: s += game

    return s
    pass

def b():
    s = 0
    for line in lines:
        mincubes = defaultdict(int)
        game, rounds = line.split(': ')
        game = u.ints(game)[0]
        rounds = rounds.split('; ')
        impossible = False
        for r in rounds:
            cubelist = r.split(', ')
            for c in cubelist:
                num, color = c.split(' ')
                num=int(num)
                mincubes[color] = max(num, mincubes[color])
        power = math.prod(c for c in mincubes.values() if c > 0)
        s += power
    return s
    pass

u.main(a, b, submit=globals().get('submit', False))
