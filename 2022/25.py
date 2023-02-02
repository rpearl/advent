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
import string

digs = string.digits + string.ascii_letters

ints = u.ints(data)
intlines = u.lmap(u.ints, lines)
toklines = [line.split(' ') for line in lines]

def int2base(x, base):
    if x < 0:
        sign = -1
    elif x == 0:
        return digs[0]
    else:
        sign = 1

    x *= sign
    digits = []

    while x:
        digits.append(digs[x % base])
        x = x // base

    if sign < 0:
        digits.append('-')

    digits.reverse()

    return ''.join(digits)



print(int2base(4, 3))

tab = str.maketrans('01234', '=-012')
rtab = str.maketrans('=-012', '01234')

def to_balanced(x):
    n = math.ceil(math.log(2*abs(x)+1, 5))
    b = (5**n-1) // 2
    s = int2base(x+b, 5).zfill(n)
    return s.translate(tab)

def from_balanced(s):
    r = s.translate(rtab)
    n = len(r)
    b = (5**n-1) // 2
    return int(r,5)-b

print(from_balanced('2=-1=0'))


def a():
    s = 0
    for line in lines:
        s += from_balanced(line)
    return to_balanced(s)
    pass


def b():
    pass

u.main(a, b, submit=globals().get('submit', False))
