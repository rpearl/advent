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

prio = {c:i+1 for i,c in enumerate(string.ascii_lowercase+string.ascii_uppercase)}

#data="""vJrwpWtwJgWrhcsFMMfFFhFp
#jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
#PmmdzqPrVvPwwTWBwg
#wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
#ttgJtRGJQctTZtZT
#CrZsJsPPZsGzwwsLwLmpwMDw"""
#lines=data.splitlines()

ints = u.ints(data)
intlines = u.lmap(u.ints, lines)
toklines = [line.split(' ') for line in lines]

def a():
    tot = 0
    for line in lines:
        l = int(len(line)/2)
        a, b = line[:l], line[l:]
        s = set(a)
        for x in b:
            if x in s:
                pri = prio[x]
                tot += pri
                break
    return tot
    pass


def b():
    tot = 0
    for group in u.chunks(lines, 3):
        a, b, c = map(set, group)
        inall = a&b&c
        assert len(inall) == 1
        tot += prio[list(inall)[0]]
    return tot
    pass

u.main(a, b, submit=globals().get('submit', False))
