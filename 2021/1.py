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
data2="""199
200
208
210
200
207
240
269
260
263"""

def a():
    d = u.ints(data)
    c=0
    for i in range(1,len(d)):
        prev = d[i-1]
        depth = d[i]
        if depth > prev:
            c+=1
    return c
    pass


def b():
    buf = deque([])
    c=0
    d = u.ints(data)
    for i in range(3,len(d)):
        if d[i-3]<d[i]:
            c+=1
    return c


    pass

u.main(a, b, submit=globals().get('submit', False))
