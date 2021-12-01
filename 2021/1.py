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
    return sum(d[i-1]<d[i] for i in range(1,len(d)))


def b():
    d = u.ints(data)
    return sum(d[i-3]<d[i] for i in range(3,len(d)))

u.main(a, b, submit=globals().get('submit', False))
