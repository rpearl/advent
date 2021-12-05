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
    c = Counter()
    for x1,y1,x2,y2 in intlines:
        if x1 != x2 and y1 != y2:
            continue
        dx = u.sign(x2-x1)
        dy = u.sign(y2-y1)
        delta = complex(dx, dy)
        start = complex(x1, y1)
        end = complex(x2, y2)
        cur = start
        while cur != end:
            c[cur] += 1
            cur += delta
        c[end] += 1
    return sum(n >= 2 for n in c.values())
    pass


def b():
    c = Counter()
    for x1,y1,x2,y2 in intlines:
        dx = u.sign(x2-x1)
        dy = u.sign(y2-y1)
        delta = complex(dx, dy)
        start = complex(x1, y1)
        end = complex(x2, y2)
        cur = start
        while cur != end:
            c[cur] += 1
            cur += delta
        c[end] += 1
    return sum(n >= 2 for n in c.values())
    pass

u.main(a, b, submit=globals().get('submit', False))
