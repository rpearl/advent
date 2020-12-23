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


ops = {
    "+": operator.add,
    "*": operator.mul,
    "-": operator.sub,
}


def postfix_eval(line, inprec, outprec):
    tokens = line.replace("(", "( ").replace(")", " )").split(" ")
    postfix = []
    stk = []

    inprec["("] = min(inprec.values()) - 10
    outprec["("] = max(outprec.values()) + 10
    for token in tokens:
        if token in inprec.keys():
            p = outprec[token]
            if not stk:
                stk.append(token)
            elif p > inprec[stk[-1]]:
                stk.append(token)
            else:
                while stk and p < inprec[stk[-1]]:
                    postfix.append(stk.pop())
                stk.append(token)
        elif token == ")":
            while stk[-1] != "(":
                postfix.append(stk.pop())
            stk.pop()
        else:
            postfix.append(int(token))
    while stk:
        postfix.append(stk.pop())

    ev = []
    for term in postfix:
        if term in inprec:
            ev.append(ops[term](ev.pop(), ev.pop()))
        else:
            ev.append(term)
    return ev[0]


def a():
    inprec = {"*": 2, "+": 2}
    outprec = {"*": 1, "+": 1}
    return sum(postfix_eval(line, inprec, outprec) for line in lines)


def b():
    inprec = {"*": 2, "+": 4}
    outprec = {"*": 1, "+": 3}

    return sum(postfix_eval(line, inprec, outprec) for line in lines)


u.main(a, b, submit=globals().get("submit", False))
