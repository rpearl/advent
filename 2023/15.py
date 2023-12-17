submit=True
from aocd import data #type: ignore
from aocd import submit as sbmt #type: ignore
import sys
from collections import Counter, defaultdict, OrderedDict, deque
import functools
from sortedcontainers import SortedList, SortedDict, SortedSet
import itertools
import u
import math
import time
import operator

_data = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"

lines = data.splitlines()

ints = u.ints(data)
intlines = u.lmap(u.ints, lines)
toklines = [line.split(' ') for line in lines]

def hash(s):
    v = 0
    for c in s:
        v += ord(c)
        v *= 17
        v &= 0xff
    return v

def a():
    return sum(hash(s) for s in data.split(','))
    pass


def b():
    boxes = defaultdict(OrderedDict)
    for insn in data.split(','):
        if '-' in insn:
            lbl = insn[:-1]
            box = boxes[hash(lbl)]
            if lbl in box:
                del box[lbl]
        else:
            lbl,val = insn.split('=')
            val = int(val)
            box = boxes[hash(lbl)]
            box[lbl] = val

    s = 0
    for b,box in boxes.items():
        for i, val in enumerate(box.values()):
            s += (b+1)*(i+1)*val
    return s



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
