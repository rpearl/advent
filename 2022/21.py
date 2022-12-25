submit=True
import z3
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

#data = """root: pppw + sjmn
#dbpl: 5
#cczh: sllz + lgvd
#zczc: 2
#ptdq: humn - dvpt
#dvpt: 3
#lfqf: 4
#humn: 5
#ljgn: 2
#sjmn: drzm * dbpl
#sllz: 4
#pppw: cczh / lfqf
#lgvd: ljgn * ptdq
#drzm: hmdt - zczc
#hmdt: 32"""
#lines=data.splitlines()

ops = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}

def a():
    exprs = {}
    for line in lines:
        name, expr = line.split(': ')
        if expr.isdigit():
            exprs[name] = ('const', int(expr))
        else:
            a, op, b = expr.split()
            exprs[name] = ('binop', ops[op], a, b)
    vals = {}
    order = []
    wl = [('root', False)]
    while wl:
        cur, post = wl.pop()
        if post:
            order.append(cur)
        else:
            typ, *expr = exprs[cur]
            if typ == 'binop':
                _, a, b = expr
                wl.append((a, False))
                wl.append((b, False))
            wl.append((cur, True))

    order.reverse()
    for name in order:
        typ, *expr = exprs[name]
        if typ == 'const':
            vals[name] = expr[0]
        else:
            op = expr[0]
            a = expr[1]
            b = expr[2]
            vals[name] = op(vals[a],vals[b])

    print(exprs['humn'])
    return int(vals['root'])

def cmp(a,b):
    if a < b: return -1
    elif a > b: return 1
    else: return 0

def b():
    exprs = {}
    for line in lines:
        name, expr = line.split(': ')
        if expr.isdigit():
            exprs[name] = ('const', int(expr))
        else:
            a, op, b = expr.split()
            exprs[name] = ('binop', ops[op], a, b)
    humn = z3.Int('humn')
    exprs['humn'] = ('const', humn)
    order = []
    wl = [('root', False)]
    while wl:
        cur, post = wl.pop()
        if post:
            order.append(cur)
        else:
            typ, *expr = exprs[cur]
            if typ == 'binop':
                _, a, b = expr
                wl.append((a, False))
                wl.append((b, False))
            wl.append((cur, True))

    order.reverse()

    s = z3.Solver()

    vals = {}
    for name in order:
        typ, *expr = exprs[name]
        if typ == 'const':
            vals[name] = expr[0]
        else:
            op = expr[0]
            a = expr[1]
            b = expr[2]
            if name == 'root':
                s.add(vals[a]==vals[b])
            else:
                vals[name] = op(vals[a],vals[b])
    s.check()
    m = s.model()
    return m[humn]

    #return vals['root']
    pass

u.main(a, b, submit=globals().get('submit', False))
