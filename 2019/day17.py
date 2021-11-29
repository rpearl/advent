import intcode
import itertools
import numpy
import math
import functools
import aoc
from collections import defaultdict

import sys
inp = sys.stdin.read()

def get_map():
    prog = intcode.run(inp, [])
    s = []
    for out in prog:
        s.append(chr(out))

    m = ''.join(s).strip()
    print(m)
    rows = m.split('\n')

    return rows

rows = get_map()

def part1():
    intersections = []
    try:
        for i in range(1,len(rows)-1):
            if len(rows[i]) == 0:
                continue
            for j in range(1,len(rows[0])-1):
                up = rows[i-1][j-1]+rows[i-1][j]+rows[i-1][j+1]
                mid = rows[i][j-1]+rows[i][j]+rows[i][j+1]
                down = rows[i+1][j-1]+rows[i+1][j]+rows[i+1][j+1]

                if up == '.#.' and mid == '###' and down == '.#.':
                    intersections.append((i,j))
    except:
        print(i,j)
        print(rows[45])
        raise
    return sum(i*j for i,j in intersections)

def part2():
    intersections = []
    for i in range(1,len(rows)-1):
        if len(rows[i]) == 0:
            continue
        for j in range(1,len(rows[0])-1):
            up = rows[i-1][j-1]+rows[i-1][j]+rows[i-1][j+1]
            mid = rows[i][j-1]+rows[i][j]+rows[i][j+1]
            down = rows[i+1][j-1]+rows[i+1][j]+rows[i+1][j+1]

            if up == '.#.' and mid == '###' and down == '.#.':
                intersections.append((i,j))

    for i in range(len(rows)):
        for j in range(len(rows[0])):
            if rows[i][j] == '^':
                loc = (i, j)


    print(intersections)

part2()
