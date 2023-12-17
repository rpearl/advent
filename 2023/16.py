submit=True
from aocd import data
from aocd import submit as sbmt
import sys
from collections import Counter, defaultdict, deque
import functools
from sortedcontainers import SortedList, SortedDict, SortedSet
import itertools
import u
import math
import time
import operator
_data=""".|...\\....
|.-.\\.....
.....|-...
........|.
..........
.........\\
..../.\\\\..
.-.-/..|..
.|....-|.\\
..//.|...."""

sys.setrecursionlimit(10_000)

lines = data.splitlines()

reflections = {
    '/': {
        u.E: [u.N],
        u.N: [u.E],
        u.W: [u.S],
        u.S: [u.W],
    },
    '\\': {
        u.E: [u.S],
        u.S: [u.E],
        u.W: [u.N],
        u.N: [u.W],
    }
}
splits = {
    '|': {
        u.N: [u.N],
        u.S: [u.S],
        u.E: [u.N, u.S],
        u.W: [u.N, u.S],
    },
    '-': {
        u.N: [u.E, u.W],
        u.S: [u.E, u.W],
        u.E: [u.E],
        u.W: [u.W],
    },
}

grid, width, height = u.make_grid(lines)
def trace_beam(start):
    def neighbors(node):
        beam, d = node
        tile = grid[beam]
        if tile == '.':
            nds = [d]
        elif tile in reflections:
            nds = reflections[tile][d]
        elif tile in splits:
            nds = splits[tile][d]

        for nd in nds:
            nbeam = (beam[0]+nd[0], beam[1]+nd[1])
            if nbeam in grid:
                yield (nbeam, nd)
    _, dists = u.bfs(start, neighbors)
    return len({beam for beam,_ in dists})

def a():
    start = ((0, 0), u.E)
    return trace_beam(start)


def b():
    best=0
    ew = (((x,y),d) for y in range(height) for x,d in [(0, u.E), (width-1,u.W)])

    ns = (((x,y),d) for x in range(width) for y,d in [(0, u.S), (height-1,u.N)])

    return max(map(trace_beam, itertools.chain(ew,ns)))

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
