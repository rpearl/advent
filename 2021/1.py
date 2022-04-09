submit=True
from aocd import data, lines
import sys
from collections import Counter, defaultdict, deque
import functools
from sortedcontainers import SortedList, SortedDict, SortedSet
import itertools
import u
import math
import time
import operator

def solve(x):
    d = u.ints(data)
    return sum(d[i-x]<d[x] for i in range(x,len(d)))

def a():
    return solve(1)


def b():
    return solve(3)

u.main(a, b, submit=globals().get('submit', False))
