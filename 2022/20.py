submit=True
from aocd import data, lines #type: ignore
from llist import dllist
import sys
from collections import Counter, defaultdict, deque
import functools
from sortedcontainers import SortedList, SortedDict, SortedSet
import itertools
import u
import math
import time
import operator

#data = """1
#2
#-3
#3
#-2
#0
#4"""

ints = u.ints(data)
intlines = u.lmap(u.ints, lines)
toklines = [line.split(' ') for line in lines]

def a():
    zero = ints.index(0)
    d = list(enumerate(ints))
    order = list(d)

    for pos, i in order:
        j = d.index((pos, i))
        del d[j]
        idx = (j+i) % len(d)
        d[idx:idx] = [(pos, i)]

    idx = d.index((zero, 0))
    _, x = d[(idx + 1000) % len(d)]
    _, y = d[(idx + 2000) % len(d)]
    _, z = d[(idx + 3000) % len(d)]
    return x+y+z

def b():
    d = [811589153*x for x in ints]
    zero = d.index(0)
    d = list(enumerate(d))
    order = list(d)

    for _ in range(10):
        for pos, i in order:
            j = d.index((pos, i))
            del d[j]
            idx = (j+i) % (len(order)-1)
            d[idx:idx] = [(pos, i)]
    idx = d.index((zero, 0))
    _, x = d[(idx + 1000) % len(d)]
    _, y = d[(idx + 2000) % len(d)]
    _, z = d[(idx + 3000) % len(d)]
    return x+y+z
    pass

u.main(a, b, submit=globals().get('submit', False))
