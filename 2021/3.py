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

def most_common(s, i):
    ones = sum(line[i] == '1' for line in s)
    return '1' if 2*ones >= len(s) else '0'

def least_common(s, i):
    return '0' if most_common(s, i)=='1' else '1'

def a():
    g = []
    e = []
    for i in range(len(lines[0])):
        g.append(most_common(lines,i))
        e.append(least_common(lines,i))
    g = int(''.join(g), 2)
    e = int(''.join(e), 2)
    return g*e

def oxy(l, i=0):
    if len(l) == 1:
        return int(l[0], 2)
    mc = most_common(l, i)
    return oxy([line for line in l if line[i] == mc], i+1)
def co2(l, i=0):
    if len(l) == 1:
        return int(l[0], 2)
    lc = least_common(l, i)
    return co2([line for line in l if line[i] == lc], i+1)

def b():
    return oxy(lines) * co2(lines)

u.main(a, b, submit=globals().get('submit', False))
