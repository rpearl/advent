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

ints = u.ints(data)
intlines = u.lmap(u.ints, lines)
toklines = [line.split(' ') for line in lines]

def zeroes():
    return [0]*9

def a():
    state = list(ints)
    phases = zeroes()
    for fish in state:
        phases[fish] += 1
    for i in range(80):
        new_phases = zeroes()
        for d, count in enumerate(phases):
            if d == 0:
                new_phases[8] += count
                new_phases[6] += count
            else:
                new_phases[d-1] += count
        phases = new_phases
    return sum(new_phases)


def b():
    state = list(ints)
    phases = zeroes()
    for fish in state:
        phases[fish] += 1
    for i in range(256):
        new_phases = zeroes()
        for d, count in enumerate(phases):
            if d == 0:
                new_phases[8] += count
                new_phases[6] += count
            else:
                new_phases[d-1] += count
        phases = new_phases

    return sum(new_phases)



u.main(a, b, submit=globals().get('submit', False))
