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
#lines=[
#    'aa bb cc dd ee',
#    'aa bb cc dd aa',
#    'aa bb cc dd aaa',
#]
def a():
    c=0
    for line in lines:
        s = set()
        valid = True
        for word in line.split(' '):
            if word in s:
                valid = False
                break
            s.add(word)
        if valid: c+=1
    return c


def b():
    c=0
    for line in lines:
        s = set()
        valid = True
        for word in line.split(' '):
            word = ''.join(sorted(word))
            if word in s:
                valid = False
                break
            s.add(word)
        if valid: c+=1
    return c

u.main(a, b, submit=globals().get('submit', False))
