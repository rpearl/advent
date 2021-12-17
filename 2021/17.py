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
lowx, hix, lowy, hiy = u.fixparse('target area: x={:d}..{:d}, y={:d}..{:d}', data)
def simulate(vx, vy):
    x, y= 0,0
    maxy = -math.inf
    while y >= lowy and (vx != 0 or lowx <= x <= hix):
        x += vx
        y += vy
        maxy = max(maxy, y)
        vx -= u.sign(vx)
        vy -= 1
        if lowx <= x <= hix and lowy <= y <= hiy:
            break
    else:
        maxy = -math.inf
    return maxy

def a():
    return max(simulate(vx, vy) for vx in range(1,hix+1) for vy in range(1,abs(lowy)))

def b():
    sims = [(vx, vy, simulate(vx, vy)) for vx in range(1, hix+1) for vy in range(lowy,abs(lowy))]
    hits = [s for s in sims if s[2] > -math.inf]
    return len(hits)

u.main(a, b, submit=globals().get('submit', False))
