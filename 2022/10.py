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

ints = u.ints(data)
intlines = u.lmap(u.ints, lines)
toklines = [line.split(' ') for line in lines]

data2= """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop"""
lines=data.splitlines()

def a():
    cycles = 0
    x = 1
    strengths = 0
    def update_strengths():
        nonlocal cycles, strengths
        if (cycles - 20) % 40 == 0:
            ss = cycles * x
            print(cycles, x, ss)
            strengths += ss
    for line in lines:
        if line == 'noop':
            cycles += 1
            update_strengths()
        else:
            v = u.ints(line)[0]
            cycles += 1
            update_strengths()
            cycles += 1
            update_strengths()
            x += v
    return strengths

    pass


def b():
    cycles = 0
    x = 1
    strengths = 0
    pixels = []

    def draw_pixel():
        col = cycles % 40
        lit = abs(x-col) <= 1
        if lit:
            pixels.append('█')
        else:
            pixels.append(' ')

    for line in lines:
        if line == 'noop':
            draw_pixel()
            cycles += 1
        else:
            v = u.ints(line)[0]
            draw_pixel()
            cycles += 1
            draw_pixel()
            cycles += 1
            x += v
    i = 0
    for row in range(6):
        for col in range(40):
            print(pixels[i], end='')
            i += 1
        print()
    pass

u.main(a, b, submit=globals().get('submit', False))
