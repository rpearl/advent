submit=True
data = """A Y
B X
C Z
"""
lines=data.splitlines()
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

win = {
    'rock': 'paper',
    'paper': 'scissors',
    'scissors': 'rock',
}

lose = {
    'rock': 'scissors',
    'paper': 'rock',
    'scissors': 'paper',
}

opmap = {
    'A': 'rock', 'B': 'paper', 'C': 'scissors',
}
umap = {
    'X': 'rock', 'Y': 'paper', 'Z': 'scissors',
}

shapescore = {'rock': 1, 'paper': 2, 'scissors': 3}


def winscore(opp, you):
    if you == win[opp]: return 6
    elif you == lose[opp]: return 0
    else: return 3

def score(opp, you):
    return shapescore[you]+ winscore(opp, you)

def a():
    s = 0
    for opp, you in toklines:
        s += score(opmap[opp], umap[you])
    return s


def b():
    s = 0
    for opp, youres in toklines:
        oppnorm = opmap[opp]
        if youres == 'X': you = lose[oppnorm]
        elif youres == 'Y': you = oppnorm
        else: you = win[oppnorm]
        s += score(oppnorm, you)
    return s

        
    pass

u.main(a, b, submit=globals().get('submit', False))
