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
braces = {'(': ')', '[': ']', '{':'}', '<': '>'}
def a():
    scores = {')': 3, ']': 57, '}': 1197, '>': 25137}
    score = 0
    for line in lines:
        s = []
        for c in line:
            if c in braces:
                s.append(c)
            else:
                if braces[s.pop()] != c:
                    score += scores[c]
                    break
    return score


def b():
    scores = []
    bracescore = {'(': 1, '[': 2, '{': 3, '<': 4}
    for line in lines:
        s = []
        for c in line:
            if c in braces:
                s.append(c)
            else:
                if braces[s.pop()] != c:
                    break
        else:
            linescore = functools.reduce(lambda tot, o: tot*5+bracescore[o], reversed(s), 0)
            scores.append(linescore)
    return statistics.median(scores)

    pass

u.main(a, b, submit=globals().get('submit', False))
