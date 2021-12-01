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

#data = """
#pbga (66)
#xhth (57)
#ebii (61)
#havc (66)
#ktlj (57)
#fwft (72) -> ktlj, cntj, xhth
#qoyq (66)
#padx (45) -> pbga, havc, qoyq
#tknk (41) -> ugml, padx, fwft
#jptl (61)
#ugml (68) -> gyxo, ebii, jptl
#gyxo (61)
#cntj (57)
#"""
#lines = data.split('\n')[1:-1]
def a():
    g = defaultdict(list)
    parents = {}
    for line in lines:
        if '->' in line:
            src, dsts = line.split(' -> ')
            dsts = dsts.split(', ')
        else:
            src, dsts = line, []
        src, wt = src.split(' (')
        wt = int(wt[:-1])
        g[src] = dsts
        for dst in dsts:
            parents[dst] = src

    for src in g:
        if src not in parents:
            return src

def b():
    g = defaultdict(list)
    weights = {}
    parents = {}
    for line in lines:
        if '->' in line:
            src, dsts = line.split(' -> ')
            dsts = dsts.split(', ')
        else:
            src, dsts = line, []
        src, wt = src.split(' (')
        wt = int(wt[:-1])
        weights[src] = wt
        g[src] = dsts
        for dst in dsts:
            parents[dst] = src

    root = None
    for src in g:
        if src not in parents:
            root = src
            break

    def tower_weight(node):
        s = weights[node]
        subweights = defaultdict(list)
        unbalanced = None
        for child in g[node]:
            subweight, nd = tower_weight(child)
            if nd is not None:
                unbalanced = nd
            subweights[subweight].append(child)
            s += subweight
        if unbalanced:
            return s, unbalanced
        if len(subweights) > 1:
            assert len(subweights) == 2
            (s1,c1), (s2, c2) = subweights.items()
            if len(c1) != 1:
                s1, s2 = s2, s1
                c1, c2 = c2, c1
            diff = s2-s1
            unbalanced = weights[c1[0]] + diff
        return s, unbalanced

    _, unbalanced = tower_weight(root)
    return unbalanced

u.main(a, b, submit=globals().get('submit', False))
