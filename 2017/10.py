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

#data = '3, 4, 1, 5'

def a():
    cpos = 0
    skip = 0
    l = list(range(256))

    for length in u.ints(data):
        left = cpos
        right = cpos + length - 1
        while left < right:
            lt = left % len(l)
            rt = right % len(l)
            tmp = l[lt]
            l[lt] = l[rt]
            l[rt] = tmp
            left += 1
            right -= 1
        cpos += length
        cpos += skip
        skip += 1
    return l[0]*l[1]
#data = '1,2,3'

def b():
    cpos = 0
    skip = 0
    l = list(range(256))

    vals = [ord(d) for d in data] + [17, 31, 73, 47, 23]
    #vals = [3, 4, 1, 5, 17, 31, 73, 47, 23]

    for round in range(64):
        print('.', end='')
        for length in vals:
            left = cpos
            right = cpos + length - 1
            while left < right:
                lt = left % len(l)
                rt = right % len(l)
                tmp = l[lt]
                l[lt] = l[rt]
                l[rt] = tmp
                left += 1
                right -= 1
            cpos += length
            cpos += skip
            skip += 1

    out = []
    for chunk in u.chunks(l, 16):
        val = functools.reduce(operator.xor, chunk)
        out.append(f'{val:02x}')
    return ''.join(out)



u.main(a, b, submit=globals().get('submit', False))
