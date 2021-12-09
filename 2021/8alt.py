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

#    0:      1:      2:      3:      4:
#   aaaa    ....    aaaa    aaaa    ....
#  b    c  .    c  .    c  .    c  b    c
#  b    c  .    c  .    c  .    c  b    c
#   ....    ....    dddd    dddd    dddd
#  e    f  .    f  e    .  .    f  .    f
#  e    f  .    f  e    .  .    f  .    f
#   gggg    ....    gggg    gggg    ....
#  
#    5:      6:      7:      8:      9:
#   aaaa    aaaa    aaaa    aaaa    aaaa
#  b    .  b    .  .    c  b    c  b    c
#  b    .  b    .  .    c  b    c  b    c
#   dddd    dddd    ....    dddd    dddd
#  .    f  e    f  .    f  e    f  .    f
#  .    f  e    f  .    f  e    f  .    f
#   gggg    gggg    ....    gggg    gggg

# a: 8
# b: 6
# c: 8
# d: 7
# e: 4
# f: 9
# g: 7

def a():
    tot = 0
    for line in lines:
        _, output = line.split(' | ')
        output = output.split()
        for o in output:
            if len(o) in {2,3,4,7}:
                tot += 1
    return tot

unscrambled_segs = [
    'abcefg',
    'cf',
    'acdeg',
    'acdfg',
    'bcdf',
    'abdfg',
    'abdefg',
    'acf',
    'abcdefg',
    'abcdfg',
]

score = Counter(''.join(unscrambled_segs))

unscrambled = {
    sum(score[seg] for seg in segs): i for i, segs in enumerate(unscrambled_segs)
}

def b():
    tot = 0
    for line in lines:
        mapping = {}
        signals, output = line.split(' | ')
        signals = signals.split()
        output = output.split()
        frequencies = Counter(''.join(signals))
        for sig in signals:
            sigscore = sum(frequencies[s] for s in sig)
            mapping[frozenset(sig)] = unscrambled[sigscore]
        o = u.to_int(mapping[frozenset(digit)] for digit in output)
        tot += o
    return tot

u.main(a, b, submit=globals().get('submit', False))
