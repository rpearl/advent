submit=True
from aocd import data #type: ignore
import sys
from collections import Counter, defaultdict, deque
import functools
from sortedcontainers import SortedList, SortedDict, SortedSet
import itertools
import u
import math
import time
import operator
_data="""Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""
lines = data.splitlines()

ints = u.ints(data)
intlines = u.lmap(u.ints, lines)
toklines = [line.split(' ') for line in lines]

def a():
    s = 0
    for line in lines:
        _, card = line.split(':')
        winning, picked = [set(u.ints(c)) for c in card.split('|')]
        matches = (picked & winning)
        if len(matches) > 0:
            value = 1 << (len(matches)-1)
            s += value
    return s
    pass


def b():
    cards = Counter(range(len(lines)))
    for i,line in enumerate(lines):
        _, card = line.split(':')
        winning, picked = [set(u.ints(c)) for c in card.split('|')]
        matches = len(picked & winning)
        for j in range(matches):
            cards[i+j+1] += cards[i]
    return sum(cards.values())

    pass

u.main(a, b, submit=globals().get('submit', False))
