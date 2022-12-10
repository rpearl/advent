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

# if h is at (2, 0) and t is at (0, 0) then dx should be 1

dirs = {'R': complex(1, 0), 'L': complex(-1, 0), 'U': complex(0, -1), 'D': complex(0, 1)}
#data="""R 5
#U 8
#L 8
#D 3
#R 17
#D 10
#L 25
#U 20"""
#lines=data.splitlines()

def debug(points):
    print(f'{points=}')
    for y in range(-6,6):
        for x in range(-6,6):
            p = x,y
            c = None
            for i,point in enumerate(points):
                if point != p: continue
                if i == 0:
                    c = 'H'
                    break
                else:
                    c = str(i)
                    break
            if c is None:
                c = 's' if p == (0,0) else '.'
            print(c, end="")
        print()
    print()

def sim(n):
    points=[complex(0,0)]*n
    seen = {complex(0,0)}
    for line in lines:
        instr, amt = line[:1],line[2:]
        amt=int(amt)
        dinstr = dirs[instr]
        for _ in range(amt):
            points[0] += dinstr
            #debug(points)
            for i in range(1,n):
                point = points[i]
                prev = points[i-1]
                d = prev-point
                if abs(d) >= 2:
                    dx = u.clamp(d.real, -1, 1)
                    dy = u.clamp(d.imag, -1, 1)
                    delta = complex(dx,dy)
                    points[i] += delta
            seen.add(points[n-1])
    return len(seen)

def a():
    return sim(2)


def b():
    return sim(10)

u.main(a, b, submit=globals().get('submit', False))
