submit=True
from aocd import data, lines #type: ignore
import sys
from collections import Counter, defaultdict, deque
import functools
from sortedcontainers import SortedList, SortedDict, SortedSet
import itertools
import re
import u
import math
import time
import operator
#tests = [
#    ('{<!!!>>}', 1),
#    #('{}',1),
#    #('{{{}}}', 6),
#    #('{{},{}}', 5),
#    #('{{{},{},{{}}}}', 16),
#    ('{<a>,<a>,<a>,<a>}',1),
#    #('{{<ab>},{<ab>},{<ab>},{<ab>}}', 9),
#    #('{{<!!>},{<!!>},{<!!>},{<!!>}}', 9),
#    #('{{<a!>},{<a!>},{<a!>},{<ab>}}', 3),
#]
def a():
    score = 0
    depth = 0
    i = 0
    d = re.sub(r'!.','',data)

    while i < len(d):
        c = d[i]
        if c == '{':
            depth += 1
            score += depth
        elif c == '}':
            depth -= 1
            assert depth >= 0
        elif c == '<':
            while c != '>':
                i += 1
                c = d[i]
        i += 1
    return score

def b():
    score = 0
    depth = 0
    i = 0
    d = re.sub(r'!.','',data)

    while i < len(d):
        c = d[i]
        if c == '{':
            depth += 1
        elif c == '}':
            depth -= 1
            assert depth >= 0
        elif c == '<':
            while c != '>':
                i += 1
                score += 1
                c = d[i]
            score -= 1
        i += 1
    return score
    pass

u.main(a, b, submit=globals().get('submit', False))
