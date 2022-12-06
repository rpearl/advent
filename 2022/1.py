submit=True
from aocd import data, lines #type: ignore
import sys
from collections import Counter, defaultdict, deque
import functools
import heapq
from sortedcontainers import SortedList, SortedDict, SortedSet
import itertools
import u
import math
import time
import operator

_data = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""

ints = u.ints(data)
intlines = u.lmap(u.ints, lines)
toklines = [line.split(' ') for line in lines]

def a():
    best = 0
    chunks = data.split('\n\n')
    return max(sum(u.ints(chunk))for chunk in chunks)

    pass


def b():
    chunks = data.split('\n\n')
    sums = (sum(u.ints(chunk)) for chunk in chunks)
    return sum(heapq.nlargest(3, (sum(u.ints(chunk)) for chunk in chunks)))
    pass

u.main(a, b, submit=globals().get('submit', False))
