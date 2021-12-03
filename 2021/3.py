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
    cs = []
    for i in range(len(lines[0])):
        cs.append(Counter())
    for line in lines:
        for i, b in enumerate(line):
            cs[i][b] += 1

    g = []
    e = []
    for c in cs:
        b = c.most_common(1)[0][0]
        g.append(b)
        e.append('1' if b == '0' else '0')
    g = int(''.join(g), 2)
    e = int(''.join(e), 2)
    return g*e


def b():
    o2 = list(lines)
    while len(o2) > 1:
        cs = []
        for i in range(len(o2[0])):
            c = Counter()
            for line in o2:
                c[line[i]] += 1
            m, l = c.most_common()
            mb = m[0] if m[1] != l[1] else '1'
            o2 = [line for line in o2 if line[i] == mb]
            if len(o2) == 1: break

    co = list(lines)
    while len(co) > 1:
        for i in range(len(co[0])):
            c = Counter()
            for line in co:
                c[line[i]] += 1
            m, l = c.most_common()
            lb = l[0] if l[1] != m[1] else '0'
            co = [line for line in co if line[i] == lb]
            if len(co) == 1: break
    o2 = int(o2[0], 2)
    co = int(co[0], 2)
    return o2*co

u.main(a, b, submit=globals().get('submit', False))
