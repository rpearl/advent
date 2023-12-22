submit=True
from aocd import data #type: ignore
from aocd import submit as sbmt #type: ignore
import sys
from collections import Counter, defaultdict, deque
import functools
from sortedcontainers import SortedList, SortedDict, SortedSet
import itertools
import u
import math
import time
import operator
import string
from copy import deepcopy

_data="""1,0,1~1,2,1
0,0,2~2,0,2
0,2,3~2,2,3
0,0,4~0,2,4
2,0,5~2,2,5
0,1,6~2,1,6
1,1,8~1,1,9"""

lines = data.splitlines()
print(len(lines))

ints = u.ints(data)
intlines = u.lmap(u.ints, lines)
toklines = [line.split(' ') for line in lines]

def sgn(x):
    if x == 0: return 0
    if x > 0: return 1
    if x < 0: return -1
    assert False,x
bricks = []
occupied = set()
for i,line in enumerate(intlines):
    sx,sy,sz,ex,ey,ez = line
    dx = sgn(ex-sx)
    dy = sgn(ey-sy)
    dz = sgn(ez-sz)
    cx,cy,cz = sx,sy,sz
    brick = {(sx,sy,sz), (ex,ey,ez)}
    while (cx,cy,cz) != (ex,ey,ez):
        cx += dx
        cy += dy
        cz += dz
        brick.add((cx,cy,cz))
    bricks.append((i,brick))

for _,brick in bricks:
    occupied |= brick

bricks.sort(key=lambda b: min(block[2] for block in b[1]))

changed = True
while changed:
    #print('\n'.join(map(repr,bricks)))
    #print()
    changed = False
    nbricks = []
    for i,brick in bricks:
        nbrick = {(block[0], block[1], block[2]-1) for block in brick}
        occupied -= brick
        if all(block[2] >= 1 and block not in occupied for block in nbrick):
            #print(f'{i=} fell {brick=} {nbrick=}')
            changed = True
        else:
            nbrick = brick
        occupied |= nbrick
        nbricks.append((i,nbrick))
    bricks = nbricks

bricks.sort(key=lambda b: min(block[2] for block in b[1]))

blockmap = {}
for i,brick in bricks:
    for block in brick:
        blockmap[block] = i

supported_by = defaultdict(set)
supporting = defaultdict(set)

for i,brick in bricks:
    topz = max(brick, key = lambda block: block[2])[2]
    top = {block for block in brick if block[2] == topz}
    for block in top:
        above = (block[0], block[1], block[2]+1)
        supports = blockmap.get(above)
        if supports is not None:
            supported_by[supports].add(i)
            supporting[i].add(supports)

def a():
    s = 0
    for i,brick in bricks:
        if all(len(supported_by[sb]) > 1 for sb in supporting[i]):
            s += 1
    return s

    pass


def b():
    def count_cascade(brickid):
        stack = [(brickid, False)]
        visited = set()
        order = deque()

        while stack:
            node, is_post = stack.pop()
            if is_post and node != brickid:
                order.appendleft(node)
                continue
            if node in visited:
                continue
            visited.add(node)
            stack.append((node, True))
            for child in supporting[node]:
                if child not in visited:
                    stack.append((child, False))

        fell = {brickid}
        count = 0
        for node in order:
            if all(s in fell for s in supported_by[node]):
                fell.add(node)
                count += 1
        return count

    s = 0
    for i,brick in bricks:
        c = count_cascade(i)
        s += c
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
