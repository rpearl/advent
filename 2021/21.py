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

def add2(a, b):
    return (a[0]+b[0], a[1]+b[1])

def sub2(a, b):
    return (a[0]-b[0], a[1]-b[1])

def move(players, rnd, die):
    r = rnd % 100
    m = 3*die + 3
    if rnd % 2 == 0:
        np1 = m# wrap(players[0]+m)
        np2 = 0# players[1]
    else:
        np1 = 0# players[0]
        np2 = m#wrap(players[1]+m)
    ndie = die+3
    ndie = ((ndie-1) % 100) + 1
    return (np1, np2), ndie

def wrap(s):
    return ((s-1)%10) + 1

def a():
    _, p1, _, p2 = ints
    positions = (p1, p2)
    scores = (0, 0)
    die = 1
    rnd = 0
    while max(scores) < 1000:
        dpositions, die = move(positions, rnd, die)
        positions = tuple(map(wrap, add2(positions, dpositions)))
        if rnd % 2 == 0:
            dscores = (positions[0], 0)
        else:
            dscores = (0, positions[1])
        scores = add2(scores, dscores)
        rnd += 1
        #return

    rolls = rnd*3
    return min(scores)*rolls

    pass


def b():

    @functools.cache
    def count_winners(positions, scores, cur):
        wins = (0, 0)
        for rolls in itertools.product([1,2,3], repeat=3):
            total = sum(rolls)
            if cur == 0:
                np = (wrap(positions[0]+total), positions[1])
                ns = (scores[0]+np[0], scores[1])
            else:
                np = (positions[0], wrap(positions[1]+total))
                ns = (scores[0], scores[1]+np[1])

            if ns[0] >= 21:
                wins = add2(wins, (1, 0))
            elif ns[1] >= 21:
                wins = add2(wins, (0, 1))
            else:
                wins = add2(wins, count_winners(np, ns, 1-cur))
        return wins
    _, p1, _, p2 = ints
    positions = (p1, p2)
    scores = (0, 0)
    return max(count_winners(positions, scores, 0))
    pass

u.main(a, b, submit=globals().get('submit', False))
