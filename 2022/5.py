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

def a():
    initial, moves = [x.splitlines() for x in data.split('\n\n')]
    initial = initial[:-1]
    state = defaultdict(list)
    for line in reversed(initial):
        for i, crate in enumerate(u.chunks(line, 4)):
            if crate[0] == '[':
                state[i+1].append(crate[1])

    for move in moves:
        qty, src, dst = u.ints(move)
        for _ in range(qty):
            c = state[src].pop()
            state[dst].append(c)
    out = ''
    for k in sorted(state.keys()):
        out += state[k][-1]
    return out
    pass


def b():
    initial, moves = [x.splitlines() for x in data.split('\n\n')]
    initial = initial[:-1]
    state = defaultdict(list)
    for line in reversed(initial):
        for i, crate in enumerate(u.chunks(line, 4)):
            if crate[0] == '[':
                state[i+1].append(crate[1])
    for move in moves:
        qty, src, dst = u.ints(move)
        mv = state[src][-qty:]
        state[src] = state[src][:-qty]
        state[dst].extend(mv)
    out = ''
    for k in sorted(state.keys()):
        out += state[k][-1]
    return out
    pass

u.main(a, b, submit=globals().get('submit', False))
