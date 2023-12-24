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

_data="""#.#####################
#.......#########...###
#######.#########.#.###
###.....#.>.>.###.#.###
###v#####.#v#.###.#.###
###.>...#.#.#.....#...#
###v###.#.#.#########.#
###...#.#.#.......#...#
#####.#.#.#######.#.###
#.....#.#.#.......#...#
#.#####.#.#.#########v#
#.#...#...#...###...>.#
#.#.#v#######v###.###v#
#...#.>.#...>.>.#.###.#
#####v#.#.###v#.#.###.#
#.....#...#...#.#.#...#
#.#########.###.#.#.###
#...###...#...#...#.###
###.###.#.###v#####v###
#...#...#.#.>.>.#.>.###
#.###.###.#.###.#.#v###
#.....###...###...#...#
#####################.#"""

lines = data.splitlines()

ints = u.ints(data)
intlines = u.lmap(u.ints, lines)
toklines = [line.split(' ') for line in lines]

def a():
    grid={}
    height = len(lines)
    width = len(lines[0])
    slopes = set()
    for y, row in enumerate(lines):
        for x, c in enumerate(row):
            grid[x,y] = c
            if c == '.':
                if y == 0:
                    start = (x,y)
                if y == height-1:
                    end = (x,y)
            elif c in '^v<>':
                slopes.add((x,y))

    slopecons = {
        '^': u.N,
        'v': u.S,
        '<': u.W,
        '>': u.E,
    }

    def connections_to_slopes(cur, pos):
        c = grid[pos]
        if pos == cur and c != '.':
            yield u.vadd(pos, slopecons[c])
        elif c == '.':
            yield from u.orthogonal(grid, pos)
    graph = defaultdict(set)

    queue = deque([start])
    seen = set()
    while queue:
        cur = queue.popleft()
        if cur in seen:
            continue
        seen.add(cur)
        _, dists = u.bfs(cur, functools.partial(connections_to_slopes, cur))
        for p, w in dists.items():
            if p in slopes:
                d = slopecons[grid[p]]
                pstart = u.vadd(p, u.opp[d])
                pend = u.vadd(p, d)
                if pstart in dists:
                    graph[cur].add((p, w))
                    queue.append(p)
            if p == end:
                graph[cur].add((end, w))


    def neighbors(pos):
        return [edge[0] for edge in graph[pos]]
    order = u.toposort(start, lambda pos: (edge[0] for edge in graph[pos]))

    mdist = defaultdict(lambda: -math.inf)
    mdist[start] = 0
    for src in order:
        for dst, w in graph[src]:
            if mdist[dst] < mdist[src] + w:
                mdist[dst] = mdist[src] + w
    return mdist[end]


def b():
    grid={}
    height = len(lines)
    width = len(lines[0])
    slopes = set()
    for y, row in enumerate(lines):
        for x, c in enumerate(row):
            if c == '#':
                continue
            grid[x,y] = c
            if c == '.':
                if y == 0:
                    start = (x,y)
                if y == height-1:
                    end = (x,y)
            elif c in '^v<>':
                slopes.add((x,y))

    slopecons = {
        '^': u.N,
        'v': u.S,
        '<': u.W,
        '>': u.E,
    }


    graph = defaultdict(set)
    def add_edge(src, dst, w):
        graph[src].add((dst, w))
        graph[dst].add((src, w))

    def remove_edge(src, dst, w):
        graph[src].remove((dst, w))
        graph[dst].remove((src, w))


    def connections_to_slopes(pos):
        if grid[pos] != '.':
            return
        yield from u.orthogonal(grid, pos)

    queue = deque([start])
    seen = set()
    while queue:
        cur = queue.popleft()
        if cur in seen:
            continue
        seen.add(cur)
        _, dists = u.bfs(cur, connections_to_slopes)
        for p, w in dists.items():
            if p in slopes:
                d = slopecons[grid[p]]
                add_edge(cur, p, w)
                queue.append((p[0] + d[0], p[1] + d[1]))
            if p == end:
                add_edge(cur, end, w)

    done = False
    while not done:
        done = True
        for src, dsts in graph.items():
            if len(dsts) == 2:
                (d1, w1), (d2, w2) = dsts
                remove_edge(src, d1, w1)
                remove_edge(src, d2, w2)
                add_edge(d1, d2, w1+w2)
                done = False

    graph = {k: v for k,v in graph.items() if len(v) > 0}
    connected_to_end = {node: w for node, w in graph[end]}

    print(len(slopes))
    print(len(graph))

    def get_path_lengths(src, dst, path, total_w):
        if src in connected_to_end:
            yield total_w + connected_to_end[src]
            return
        for node, w in graph[src]:
            if node not in path:
                yield from get_path_lengths(node, dst, path | { node }, total_w + w)

    return max(get_path_lengths(start, end, frozenset({start}), 0))
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
