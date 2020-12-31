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

data2 = """inc a
jio a, +2
tpl a
inc a"""
lines = data.splitlines()


instrs = []
for line in lines:
    op = line[:3]
    args = line[4:].split(", ")
    if op in {"jio", "jie", "jmp"}:
        args[-1] = int(args[-1])
    args = tuple(args)
    instrs.append((op, args))

# print("\n".join(repr(i) for i in instrs))
def interpret(a, b):
    ip = 0
    regs = dict(a=a, b=b)
    while 0 <= ip < len(instrs):
        op, args = instrs[ip]
        if op == "hlf":
            regs[args[0]] //= 2
            ip += 1
        elif op == "tpl":
            regs[args[0]] *= 3
            ip += 1
        elif op == "inc":
            regs[args[0]] += 1
            ip += 1
        elif op == "jmp":
            ip += args[0]
        elif op == "jie":
            if regs[args[0]] % 2 == 0:
                ip += args[1]
            else:
                ip += 1
        elif op == "jio":
            if regs[args[0]] == 1:
                ip += args[1]
            else:
                ip += 1
    return regs["a"], regs["b"]


def a():
    ip = 0
    _, b = interpret(a=0, b=0)
    return b


def b():
    ip = 0
    _, b = interpret(a=1, b=0)
    return b


u.main(a, b, submit=globals().get("submit", False))
