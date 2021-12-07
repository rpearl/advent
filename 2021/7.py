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

#data = "16,1,2,0,4,2,7,1,2,14"

ints = u.ints(data)
intlines = u.lmap(u.ints, lines)
toklines = [line.split(' ') for line in lines]
crabs=ints

def cost(n):
    n=abs(n)
    return n*(n+1)//2

def a():
    lo = min(crabs)
    hi = max(crabs)
    return min(sum(abs(crab-i) for crab in crabs) for i in range(lo, hi+1))


def b():
    lo = min(crabs)
    hi = max(crabs)
    return min(sum(cost(crab-i) for crab in crabs) for i in range(lo, hi+1))

u.main(a, b, submit=globals().get('submit', False))
