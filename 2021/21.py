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

def rev(p):
    return (p[1], p[0])

def mul(p, c):
    return (c*p[0], c*p[1])

def b():
    rollcounts = Counter(sum(r) for r in itertools.product([1,2,3], repeat=3))

    @functools.cache
    def count_winners(positions, scores):
        wins = (0, 0)
        for total, freq in rollcounts.items():
            np0 = wrap(positions[0]+total)
            np = (positions[1], np0)
            ns = (scores[1], scores[0]+np0)
            if ns[1] >= 21:
                wins = add2(wins, (freq, 0))
            else:
                wins = add2(wins, mul(rev(count_winners(np, ns)), freq))
        return wins
    _, p1, _, p2 = ints
    positions = (p1, p2)
    scores = (0, 0)
    return max(count_winners(positions, scores))
    pass

u.main(a, b, submit=globals().get('submit', False))
