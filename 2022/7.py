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
import os.path
from pathlib import Path

ints = u.ints(data)
intlines = u.lmap(u.ints, lines)
toklines = [line.split(' ') for line in lines]


def a():
    cur = '/'
    sizes = {}
    li = 0
    cmds = data.split('$ ')
    for cmd in cmds:
        if cmd.startswith('cd'):
            arg = cmd.split()[-1]
            cur = os.path.abspath(os.path.join(cur, arg))
        else:
            cmdlines = cmd.splitlines()[1:]
            for line in cmdlines:
                sz, fname = line.split()
                if sz == 'dir': continue
                sizes[os.path.join(cur, fname)] = int(sz)
    dir_sizes = Counter()
    for path, sz in sizes.items():
        p = Path(path)
        for parent in p.parents:
            dir_sizes[parent] += sz
    tot = 0
    for _, sz in dir_sizes.items():
        if sz < 100000:
            tot += sz
    return tot


    pass


def b():
    cur = '/'
    sizes = {}
    li = 0
    cmds = data.split('$ ')
    for cmd in cmds:
        if cmd.startswith('cd'):
            arg = cmd.split()[-1]
            cur = os.path.abspath(os.path.join(cur, arg))
        else:
            cmdlines = cmd.splitlines()[1:]
            for line in cmdlines:
                sz, fname = line.split()
                if sz == 'dir': continue
                sizes[os.path.join(cur, fname)] = int(sz)
    dir_sizes = Counter()
    for path, sz in sizes.items():
        p = Path(path)
        for parent in p.parents:
            dir_sizes[parent] += sz

    total_disk = 70000000
    used_disk = dir_sizes[Path('/')]
    free = total_disk - used_disk
    needed = 30000000 - free
    return min(sz for sz in dir_sizes.values() if sz >= needed)

u.main(a, b, submit=globals().get('submit', False))
