submit=True
import json
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

ints = u.ints(data)
intlines = u.lmap(u.ints, lines)
toklines = [line.split(' ') for line in lines]

#data = """[1,1,3,1,1]
#[1,1,5,1,1]
#
#[[1],[2,3,4]]
#[[1],4]
#
#[9]
#[[8,7,6]]
#
#[[4,4],4,4]
#[[4,4],4,4,4]
#
#[7,7,7,7]
#[7,7,7]
#
#[]
#[3]
#
#[[[]]]
#[[]]
#
#[1,[2,[3,[4,[5,6,7]]]],8,9]
#[1,[2,[3,[4,[5,6,0]]]],8,9]"""
#lines=data.splitlines()

def is_in_order(left, right):
    if isinstance(left, list) and isinstance(right, list):
        for i in range(len(left)):
            if i >= len(right):
                return 1
            r = is_in_order(left[i], right[i])
            if r != 0:
                return r
        return -1 if len(left) < len(right) else 0
    elif isinstance(left, int) and isinstance(right, int):
        return left-right
    elif isinstance(left, int):
        return is_in_order([left], right)
    else:
        assert isinstance(right, int)
        return is_in_order(left, [right])

def a():
    s=0
    for i, chunk in enumerate(data.split('\n\n')):
        left, right = [json.loads(line) for line in chunk.splitlines()]
        if is_in_order(left, right) < 0:
            k=i+1
            s += k
    return s

    pass


def b():
    packets = [json.loads(line) for line in lines if line != ''] + [ [[2]], [[6]] ]

    key = functools.cmp_to_key(is_in_order)
    packets.sort(key=key)

    s = 1
    for i,packet in enumerate(packets):
        k = i+1
        if packet == [[2]] or packet == [[6]]:
            s *= k
    return s
    pass

u.main(a, b, submit=globals().get('submit', False))
