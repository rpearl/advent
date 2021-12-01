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

dirs = {
    'n': (0, -1),
    'ne': (1, -1),
    'se': (1, 0),
    's': (0, 1),
    'sw': (-1,1),
    'nw': (-1, 0),
}

#data = 'se,sw,se,sw,sw'

def a():
    c = (0, 0)
    for d in data.split(','):
        dq, dr = dirs[d]
        c = (c[0]+dq, c[1]+dr)
    return u.hex_axial_distance(c, (0, 0))


def b():
    m = 0
    c = (0, 0)
    for d in data.split(','):
        dq, dr = dirs[d]
        c = (c[0]+dq, c[1]+dr)
        dist = u.hex_axial_distance(c, (0, 0))
        if dist > m:
            m = dist
    return m
    pass

u.main(a, b, submit=globals().get('submit', False))
