# submit=True
from aocd import data, lines
import sys
from collections import Counter, defaultdict, deque
import functools
from sortedcontainers import SortedList, SortedDict, SortedSet
import itertools
import u
import math
import time
import operator

width = 50
height = 6

# data = """rect 3x2
# rotate column x=1 by 1
# rotate row y=0 by 4
# rotate column x=1 by 1"""
# lines = data.splitlines()


def a():
    grid = defaultdict(bool)
    for line in lines:
        nums = u.ints(line)
        if line.startswith("rect"):
            a, b = nums
            for x in range(a):
                for y in range(b):
                    grid[x, y] = True
        elif "row" in line:
            y, b = nums
            row = [grid[x, y] for x in range(width)]
            for x, val in enumerate(row):
                grid[(x + b) % width, y] = val
        else:
            x, b = nums
            col = [grid[x, y] for y in range(height)]
            for y, val in enumerate(col):
                grid[x, (y + b) % height] = val
    for y in range(height):
        o = []
        for x in range(width):
            o.append("█" if grid[x, y] else " ")
        print("".join(o))
    return sum(grid.values())


def b():
    return "ZFHFSFOGPO"


u.main(a, b, submit=globals().get("submit", False))
