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
from tqdm import tqdm

ints = u.ints(data)
intlines = u.lmap(u.ints, lines)
toklines = [line.split(' ') for line in lines]

def binary(ds):
    return u.to_int(ds, base=2)

def kernel(image, pos):
    dirs = [
        (-1,-1), (0,-1), (1,-1),
        (-1, 0), (0, 0), (1, 0),
        (-1, 1), (0, 1), (1, 1)
    ]
    x,y = pos
    return binary(image[x+dx,y+dy] for dx,dy in dirs)

def enhance(enhancement, image):
    d = image.default_factory()
    e = enhancement[binary([d]*9)]
    enhanced = defaultdict(lambda: e)
    minx = min(p[0] for p in image)-1
    maxx = max(p[0] for p in image)+1
    miny = min(p[1] for p in image)-1
    maxy = max(p[1] for p in image)+1
    #print(minx, miny, maxx, maxy)
    for x in u.incrange(minx, maxx):
        for y in u.incrange(miny, maxy):
            k = kernel(image, (x, y))
            val = enhancement[k]
            enhanced[x,y] = val
    return enhanced

def solve(its):
    enhancement, img = data.split('\n\n')
    img = img.splitlines()
    e = [int(c == '#') for c in enhancement]

    image = defaultdict(int)
    for y in range(len(img)):
        for x in range(len(img[0])):
            image[x,y] = int(img[y][x] == '#')
    for _ in tqdm(range(its)):
        image = enhance(e, image)
    return sum(image.values())

def a():
    return solve(2)

def b():
    return solve(50)

u.main(a, b, submit=globals().get('submit', False))
