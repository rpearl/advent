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

def a():
    s = 0
    for i,x in enumerate(data):
        if x == data[(i+1)%len(data)]:
            s += int(x)
    return s


def b():
    s = 0
    l=len(data)
    for i,x in enumerate(data):
        if x == data[(i+l//2)%l]:
            s += int(x)
    return s

u.main(a, b, submit=globals().get('submit', False))
