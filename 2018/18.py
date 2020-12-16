from aocd import data, lines, submit
import sys
from collections import Counter, defaultdict, deque
import functools
from sortedcontainers import SortedList, SortedDict, SortedSet
import itertools
import u
import math


def nosubmit(answer, part):
    print(f"Part {part}:\n{answer}")


submit = nosubmit


print(f"File line count: {len(lines)}")


def a():
    tracks = u.Grid(lines)
    carts = SortedDict({pos: (c, 0) for pos, c in tracks.items() if c in "v^><"})

    uncarts = str.maketrans("v^><", "||--")

    for pos, (c, _) in carts.items():
        track[pos] = c.translate(uncarts)

    corners = {
        ("\\", "<"): "^",
        ("\\", ">"): "v",
        ("\\", "v"): ">",
        ("\\", "^"): "<",
        ("/", "<"): "v",
        ("/", ">"): "^",
        ("/", "v"): "<",
        ("/", "^"): ">",
    }

    left = {
        '>': '^',
        '^': '<',
        '<': 'v',
        'v': '>',
    }
    right = {
        '^': '>',
        '>': 'v',
        'v': '<',
        '<': '^',
    }


    dirs = {
        '>': (1, 0),
        '<': (-1, 0),
        'v': (0, 1),
        '^': (0, -1),
    }

    while True:
        ncarts = SortedDict()
        for pos, (c, i) in carts.items()
            d = dirs[c]
            nc = c
            npos = (pos[0] + d[0], pos[1] + d[1])
            tr = tracks.grid[npos]
            if tr == '+':
                i += 1
                if i % 3 == 0:
                    nc = left[c]
                elif i % 3 == 2:
                    nc = right[c]
            elif tr in '\\/':
                nc = corners[tr,c]
            if npos in ncarts:
                return f'{npos[0]},{npos[1]}'
            ncarts
            ncarts.append((npos, nc, i))



def b():
    pass


def main():
    ra = a()
    if ra is not None:
        submit(ra, part="a")

    rb = b()
    if rb is not None:
        submit(rb, part="b")


main()
