submit=True
from aocd import data #type: ignore
from aocd import submit as sbmt #type: ignore
import sys
from collections import Counter, defaultdict, deque
from dataclasses import dataclass
import functools
from sortedcontainers import SortedList, SortedDict, SortedSet
import itertools
import u
import math
import time
import operator

data1 = """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)"""

data2 = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)"""

data3 = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)"""

#data = data3


lines = data.splitlines()

ints = u.ints(data)
intlines = u.lmap(u.ints, lines)
toklines = [line.split(' ') for line in lines]

def a():
    return
    insns, node_data = data.split('\n\n')
    insns = insns.strip()
    node_data = node_data.splitlines()
    nodes = {}
    for line in node_data:
        name, left, right = u.fixparse('{} = ({}, {})', line)
        nodes[name] = {'L': left, 'R': right}


    cur = 'AAA'

    for step, insn in enumerate(itertools.cycle(insns)):
        cur = nodes[cur][insn]
        if cur == 'ZZZ':
            return step+1


    pass


def b():
    insns, node_data = data.split('\n\n')
    insns = insns.strip()
    node_data = node_data.splitlines()
    nodes = {}
    for line in node_data:
        name, left, right = u.fixparse('{} = ({}, {})', line)
        nodes[name] = {'L': left, 'R': right}


    starts = [node for node in nodes.keys() if node.endswith('A')]

    step_counts = []

    for cur in starts:
        for step, insn in enumerate(itertools.cycle(insns)):
            cur = nodes[cur][insn]
            if cur.endswith('Z'):
                step_counts.append(step+1)
                break
    return functools.reduce(u.lcm, step_counts)
    pass

def main():
    submit = globals().get('submit', False)
    astart = time.perf_counter()
    ra = a()
    aend = time.perf_counter()
    if ra is not None:
        print(f"Part a: {ra}")
        print(f"Time taken: {aend-astart:.4f} sec")
        if submit:
            sbmt(ra, part="a")

    bstart = time.perf_counter()
    rb = b()
    bend = time.perf_counter()
    if rb is not None:
        print(f"Part b: {rb}")
        print(f"Time taken: {bend-bstart:.4f} sec")
        if submit:
            sbmt(rb, part="b")
    print()
main()
