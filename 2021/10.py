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
#data="""[({(<(())[]>[[{[]{<()<>>
#[(()[<>])]({[<{<<[]>>(
#{([(<{}[<>[]}>{[]{[(<()>
#(((({<>}<{<{<>}{[]{[]{}
#[[<[([]))<([[{}[[()]]]
#[{[{({}]{}}([{[{{{}}([]
#{<[[]]>}<{[{[{[]{()[[[]
#[<(<(<(<{}))><([]([]()
#<{([([[(<>()){}]>(<<{{
#<{([{{}}[<[[[<>{}]]]>[]]"""
#lines=data.splitlines()

ints = u.ints(data)
intlines = u.lmap(u.ints, lines)
toklines = [line.split(' ') for line in lines]
braces = {'(': ')', '[': ']', '{':'}', '<': '>'}
invbraces = u.invert(braces)
opens = set(braces.keys())
closes = set(braces.values())
def a():
    scores = {')': 3, ']': 57, '}': 1197, '>': 25137}
    score = 0
    for line in lines:
        s = []
        for c in line:
            if c in braces:
                s.append(c)
            else:
                o = s.pop()
                if braces[o] != c:
                    score += scores[c]
                    break
    return score


def b():
    scores = []
    bracescore = {'(': 1, '[': 2, '{': 3, '<': 4}
    for line in lines:
        linescore = 0
        s = []
        corrupt = False
        for c in line:
            if c in braces:
                s.append(c)
            else:
                o = s.pop()
                if braces[o] != c:
                    corrupt = True
                    break
        if corrupt:
            continue
        while s:
            linescore *= 5
            o = s.pop()
            linescore += bracescore[o]
        scores.append(linescore)
    return statistics.median(scores)

    pass

u.main(a, b, submit=globals().get('submit', False))
