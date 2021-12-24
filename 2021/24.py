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
import numpy as np
import bisect

ints = u.ints(data)
intlines = u.lmap(u.ints, lines)
toklines = [line.split(' ') for line in lines]

def parse_segments(prog):
    segments = [seg.splitlines() for seg in prog.split('inp w\n')[1:]]
    out = []
    for segment in segments:
        param1 = u.ints(segment[4]).pop()
        param2 = u.ints(segment[14]).pop()
        out.append((param1, param2))
    return out

def compute(opt):
    segments = parse_segments(data)
    links = []
    stack = []
    for i, (p1, p2) in enumerate(segments):
        if p1 > 0:
            stack.append((i, p2))
        else:
            j, v = stack.pop()
            links.append((i, j, v+p1))
    assignments = {}
    for i, j, delta in links:
        assignments[i] = opt(delta)
        assignments[j] = opt(-delta)
    return int("".join(str(assignments[i]) for i in range(14)))

def a():
    return compute(lambda d: min(9, 9+d))



def b():
    return compute(lambda d: max(1, 1+d))

u.main(a, b, submit=globals().get('submit', False))
