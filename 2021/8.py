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
import statistics

ints = u.ints(data)
intlines = u.lmap(u.ints, lines)
toklines = [line.split(' ') for line in lines]

def a():
    counts = defaultdict(int)
    for line in lines:
        signals, output = line.split(' | ')
        signals = signals.split()
        output = output.split()
        for o in output:
            if len(o) == 2:
                counts[1] += 1
            elif len(o) == 4:
                counts[4] += 1
            elif len(o) == 3:
                counts[7] += 1
            elif len(o) == 7:
                counts[8] += 1
    return sum(counts.values())
    pass


def b():
    tot = 0
    for line in lines:
        signals, output = line.split(' | ')
        signals = signals.split()
        output = output.split()
        mapping = {}
        invmap = {}
        def add(d, s):
            assert d not in mapping
            mapping[d] = s
            invmap[s] = str(d)
        siggroups = defaultdict(list)
        for s in signals:
            siggroups[len(s)].append(frozenset(s))
        add(1, siggroups[2][0])
        add(4, siggroups[4][0])
        add(7, siggroups[3][0])
        add(8, siggroups[7][0])

        for s in siggroups[6]:
            if mapping[1].issubset(s):
                if mapping[4].issubset(s):
                    add(9, s)
                else:
                    add(0, s)
            else:
                add(6, s)
        for s in siggroups[5]:
            if mapping[7].issubset(s):
                add(3, s)
            elif s.issubset(mapping[6]):
                add(5, s)
            else:
                add(2, s)
        assert(len(mapping) == 10)
        o = int(''.join(invmap[frozenset(digit)] for digit in output))
        tot += o
    return tot

u.main(a, b, submit=globals().get('submit', False))
