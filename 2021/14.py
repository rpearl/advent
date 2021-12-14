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


ints = u.ints(data)
intlines = u.lmap(u.ints, lines)
toklines = [line.split(' ') for line in lines]

def solve(steps):
    inp, ruleset = data.split('\n\n')
    first=inp[0]
    rules = {}
    for rule in ruleset.splitlines():
        src, dst = u.fixparse('{} -> {}', rule)
        rules[tuple(src)] = dst
    inp = Counter(u.window(inp, 2))

    for _ in range(steps):
        nextinp = defaultdict(int)
        for (a,b), count in inp.items():
            if (a,b) in rules:
                dst = rules[a,b]
                nextinp[(a,dst)] += count
                nextinp[(dst,b)] += count
            else:
                nextinp[(a,b)] += count
        inp = nextinp
    els = defaultdict(int)
    els[first] = 1
    for (a, b), count in inp.items():
        els[b] += count
    return max(els.values()) - min(els.values())

def a():
    return solve(10)

def b():
    return solve(40)


u.main(a, b, submit=globals().get('submit', False))
