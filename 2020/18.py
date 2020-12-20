from aocd import data, lines, submit
import sys
from collections import Counter, defaultdict, deque
import functools
from sortedcontainers import SortedList, SortedDict, SortedSet
import itertools
import u
import math
import time
import operator


def nosubmit(answer, part):
    pass


submit = nosubmit

print(f"File line count: {len(lines)}")

ops = {
    "+": operator.add,
    "*": operator.mul,
    "-": operator.sub,
}

# data = """1 + 2 * 3 + 4 * 5 + 6"""
# data = """1 + 2 * 3"""
# lines = data.splitlines()


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


def main():
    astart = time.perf_counter()
    ra = a()
    aend = time.perf_counter()
    if ra is not None:
        print("part a")
        print(ra)
        print(f"Time taken: {aend-astart:.4f} sec")
        submit(ra, part="a")

    bstart = time.perf_counter()
    rb = b()
    bend = time.perf_counter()
    if rb is not None:
        print("part b")
        print(rb)
        print(f"Time taken: {bend-bstart:.4f} sec")
        submit(rb, part="b")


main()
