submit=True
from aocd import data
import sys
from collections import Counter, defaultdict, deque
import functools
from sortedcontainers import SortedList, SortedDict, SortedSet
import itertools
import u
import math
import time
import operator

data2="""two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""

lines = data.splitlines()
print(lines)

ints = u.ints(data)
intlines = u.lmap(u.ints, lines)
toklines = [line.split(' ') for line in lines]

def a():
    return
    s = 0
    for line in lines:
        l = [c for c in line if c.isdigit()]
        s+= int(l[0]+l[-1])
    return s
    pass
digs = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

digmap = {dig: i+1 for i,dig in enumerate(digs)}
digmap.update({str(i+1): i+1 for i in range(9)})
print(digmap)
def b():
    s = 0
    for line in lines:
        first = float('inf')
        fv = 0
        last = -float('inf')
        lv = 0
        for dig, v in digmap.items():
            idx = line.find(dig)
            if idx < first and idx >= 0:
                first = idx
                fv = v
            ridx = line.rfind(dig)
            if ridx > last and idx >= 0:
                last = ridx
                lv = v
        t = 10*fv+lv
        print(t)
        s += t
    return s
    pass

u.main(a, b, submit=globals().get('submit', False))
