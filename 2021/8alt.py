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

def get(s):
    assert len(s) == 1, s
    return list(s)[0]

unscrambled = {
    frozenset(segs): str(i) for i, segs in enumerate([
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
])}




def b():
    tot = 0
    segmap = {}
    for line in lines:
        signals, output = line.split(' | ')
        signals = signals.split()
        output = output.split()
        frequencies = Counter(''.join(signals))
        invfreq = defaultdict(list)
        for pseg, count in frequencies.items():
            invfreq[count].append(pseg)

        ac = invfreq[8]
        dg = invfreq[7]

        assert len(invfreq[6]) == 1
        segmap[invfreq[6][0]] = 'b'

        assert len(invfreq[4]) == 1
        segmap[invfreq[4][0]] = 'e'

        assert len(invfreq[9]) == 1
        segmap[invfreq[9][0]] = 'f'

        # 4 has d and not g
        four = [sig for sig in signals if len(sig) == 4][0]
        segmap[get(set(dg)&set(four))] = 'd'
        segmap[get(set(dg)-set(four))] = 'g'

        # 1 has c and not a
        one = [sig for sig in signals if len(sig) == 2][0]
        segmap[get(set(ac) & set(one))] = 'c'
        segmap[get(set(ac) - set(one))] = 'a'
        assert len(segmap)==7
        assert len(set(segmap.values()))==7

        o = int(''.join(unscrambled[frozenset(segmap[d] for d in digit)] for digit in output))
        tot += o
    return tot

u.main(a, b, submit=globals().get('submit', False))
