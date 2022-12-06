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
#data = "nppdvjthqldpwncqszvftbrmjlhg"

ints = u.ints(data)
intlines = u.lmap(u.ints, lines)
toklines = [line.split(' ') for line in lines]

def a():
    for i in range(4,len(data)):
        if len(set(data[i-4:i])) == 4:
            return i


def b():
    for i in range(14,len(data)):
        if len(set(data[i-14:i])) == 14:
            return i

u.main(a, b, submit=globals().get('submit', False))
