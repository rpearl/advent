#submit=True
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


def a():
    G = defaultdict(list)
    for line in lines:
        src, dst = line.split('-')
        G[src].append(dst)
        G[dst].append(src)
    @functools.cache
    def count_paths_to_end(start, path=tuple()):
        paths = 0
        newpath = (*path, start)
        for node in G[start]:
            if node == 'end':
                paths+= 1
            elif node.islower() and node in newpath:
                continue
            else:
                paths += count_paths_to_end(node, newpath)
        return paths
    return count_paths_to_end('start')


def b():
    def can_go(path, node):
        if node.isupper():
            return True
        if node in {'start', 'end'}:
            return node not in path
        else:
            lowers = [p for p in path if p.islower()]
            uniq = set(lowers)
            if node in uniq:
                return len(lowers) == len(uniq)
            else:
                return True

    G = defaultdict(list)
    for line in lines:
        src, dst = line.split('-')
        G[src].append(dst)
        G[dst].append(src)
    @functools.cache
    def count_paths_to_end(curr, path=tuple()):
        paths = 0
        newpath = (*path, curr)
        for node in G[curr]:
            if node == 'end':
                paths += 1
                continue
            if not can_go(newpath, node):
                continue
            paths += count_paths_to_end(node, newpath)
        return paths
    return count_paths_to_end('start')
    pass

u.main(a, b, submit=globals().get('submit', False))
