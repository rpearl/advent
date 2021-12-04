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

def winner(board, draws):
    h = len(board)
    w = len(board[0])
    rowmarks = [0]*w
    colmarks = [0]*h
    unmarked = set()
    for y in range(h):
        for x in range(w):
            unmarked.add(board[y][x])
    for i, draw in enumerate(draws):
        for y in range(h):
            for x in range(w):
                if board[y][x] == draw:
                    rowmarks[x] += 1
                    colmarks[y] += 1
                    unmarked.remove(draw)
        if any(rowmark == w for rowmark in rowmarks) or any(colmark == h for colmark in colmarks):
            return i, unmarked, draw
    return None

def a():
    draws = intlines[0]
    boards = [board[1:] for board in u.chunks(intlines[1:], 6)]
    results = filter(bool, [winner(board, draws) for board in boards])
    _, unmarked, draw = min(results, key=lambda p:p[0])
    return sum(unmarked) * draw


def b():
    draws = intlines[0]
    boards = [board[1:] for board in u.chunks(intlines[1:], 6)]
    results = filter(bool, [winner(board, draws) for board in boards])
    _, unmarked, draw = max(results, key=lambda p:p[0])
    return sum(unmarked) * draw

u.main(a, b, submit=globals().get('submit', False))
