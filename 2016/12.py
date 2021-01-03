submit = True
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

data2 = """cpy 41 a
inc a
inc a
dec a
jnz a 2
dec a"""
lines = data.splitlines()
instrs = [tuple(line.split()) for line in lines]


def interpret(a=0, b=0, c=0, d=0):
    regs = dict(a=a, b=b, c=c, d=d)
    ip = 0

    def get(arg):
        if arg in regs:
            return regs[arg]
        else:
            return int(arg)

    while 0 <= ip < len(instrs):
        op, *args = instrs[ip]
        if op == "cpy":
            x, y = args
            assert y in regs
            regs[y] = get(x)
            ip += 1
        elif op == "inc":
            (x,) = args
            regs[x] += 1
            ip += 1
        elif op == "dec":
            (x,) = args
            regs[x] -= 1
            ip += 1
        elif op == "jnz":
            x, y = args
            if get(x) != 0:
                ip += get(y)
            else:
                ip += 1
    return regs


def a():
    regs = interpret()
    return regs["a"]


def b():
    regs = interpret(c=1)
    return regs["a"]


u.main(a, b, submit=globals().get("submit", False))
