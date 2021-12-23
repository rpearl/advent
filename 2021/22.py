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

def intersection(box1, box2):
    out = []
    for (alo, ahi), (blo, bhi) in zip(box1, box2):
        if alo > bhi or ahi < blo:
            return None
        out.append((max(alo, blo), min(ahi, bhi)))
    return tuple(out)

def difference(box1, box2):
    inter = intersection(box1, box2)
    if not inter:
        return [box1]

    ax, ay, az = box1
    ix, iy, iz = inter

    new_boxes = [
        (ax, ay, (az[0], iz[0]-1)),
        (ax, ay, (iz[1]+1, az[1])),
        ((ax[0], ix[0]-1), ay, iz),
        ((ix[1]+1, ax[1]), ay, iz),
        (ix, (ay[0], iy[0]-1), iz),
        (ix, (iy[1]+1, ay[1]), iz),
    ]

    def valid(box):
        return all(lo <= hi for lo, hi in box)

    return [box for box in new_boxes if valid(box)]

def size(box):
    return math.prod(max(0, hi - lo + 1) for lo, hi in box)

@u.timed
def solve():
    boxes = []
    for line in lines:
        nboxes = []
        ins, lx, hx, ly, hy, lz, hz = u.fixparse('{} x={:d}..{:d},y={:d}..{:d},z={:d}..{:d}', line)
        cur = ((lx,hx),(ly,hy),(lz,hz))
        for box in boxes:
            nboxes.extend(difference(box, cur))
        if ins == 'on':
            nboxes.append(cur)
        boxes = nboxes
    return boxes
boxes = solve()


def a():
    def cap(box):
        return tuple((max(-50, lo), min(50, hi)) for lo, hi in box)
    return sum(size(cap(box)) for box in boxes)

def b():
    return sum(size(box) for box in boxes)

u.main(a, b, submit=globals().get('submit', False))
