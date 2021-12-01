#submit=True
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
#1=right, 1up, left, left, down, down, right, right
#2=right, 3up, 4l, 4d, 4r
#3=right, 5up, 6l, 6d, 6r
def seq(sz):
    yield u.E
    for _ in range(sz*2-1):
        yield u.N
    for _ in range(sz*2):
        yield u.W
    for _ in range(sz*2):
        yield u.S
    for _ in range(sz*2):
        yield u.E


def a():
    d = int(data)
    x = 0
    y = 0
    n = 1
    while n != d:
        s = seq(x+1)
        for dx, dy in s:
            x += dx
            y += dy
            n+=1
            if n==d: break
    return abs(x)+abs(y)

def b():
    d=int(data)
    x,y = 0,0
    mem = defaultdict(int)
    mem[x,y]=1
    n=1
    while True:
        s = list(seq(x+1))
        for dx, dy in s:
            x += dx
            y += dy
            val = sum(mem[p] for p in u.all_neighbors(mem, (x, y)))
            n+=1
            if val > d:
                return val
            mem[x,y] = val
    pass

u.main(a, b, submit=globals().get('submit', False))
