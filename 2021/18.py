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
import json

ints = u.ints(data)
intlines = u.lmap(u.ints, lines)
toklines = [line.split(' ') for line in lines]

def add_left(num, n):
    if n is None:
        return num
    if isinstance(num, list):
        return [add_left(num[0], n), num[1]]
    else:
        return num + n

def add_right(num, n):
    if n is None:
        return num
    if isinstance(num, list):
        return [num[0], add_right(num[1], n)]
    else:
        return num + n

def explode(num, depth):
    if isinstance(num, int):
        return False, None, num, None
    a, b = num
    if depth == 4:
        return True, a, 0, b

    did_explode, left, a, right = explode(a, depth+1)
    if did_explode:
        return True, left, [a, add_left(b, right)], None

    did_explode, left, b, right = explode(b, depth+1)
    if did_explode:
        return True, None, [add_right(a, left), b], right

    return False, None, num, None

def split(num):
    if isinstance(num, int):
        if num >= 10:
            return True, [num // 2, math.ceil(num/2)]
        else:
            return False, num
    else:
        a, b = num
        did_split, a = split(a)
        if did_split:
            return True, [a, b]

        did_split, b = split(b)
        return did_split, [a, b]

def add(a, b):
    num = [a, b]
    changed = True
    while changed:
        changed, _, num, _ = explode(num, 0)
        if not changed:
            changed, num = split(num)
    return num

def magnitude(num):
    if isinstance(num, int):
        return num
    else:
        return 3*magnitude(num[0]) + 2*magnitude(num[1])

def a():
    nums = [json.loads(line) for line in lines]
    tot = functools.reduce(add, nums)
    return magnitude(tot)


def b():
    nums = [json.loads(line) for line in lines]
    return max(magnitude(add(a,b)) for a, b in itertools.permutations(nums, 2))
    pass

u.main(a, b, submit=globals().get('submit', False))
