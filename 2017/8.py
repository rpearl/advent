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

cmps = {'>': operator.gt, '>=': operator.ge, '<': operator.lt, '<=': operator.le, '==': operator.eq, '!=': operator.ne}
#data = """b inc 5 if a > 1
#a inc 1 if b < 5
#c dec -10 if a >= 1
#c inc -20 if c == 10"""
#lines=data.split('\n')

def a():
    regs = defaultdict(int)
    for line in lines:
        toks = line.split(' ')
        treg, op, n, _, c, cmp, v = toks
        n = int(n)
        if op == 'dec': n = -n
        v = int(v)
        if cmps[cmp](regs[c], v):
            regs[treg] += n
    return max(regs.values())
    pass


def b():
    mx = 0
    regs = defaultdict(int)
    for line in lines:
        toks = line.split(' ')
        treg, op, n, _, c, cmp, v = toks
        n = int(n)
        if op == 'dec': n = -n
        v = int(v)
        if cmps[cmp](regs[c], v):
            regs[treg] += n
        mx = max(mx, *regs.values())
    #return max(regs.values())
    return mx
    pass

u.main(a, b, submit=globals().get('submit', False))
