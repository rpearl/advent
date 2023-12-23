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

#data="""#.#####################
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
        '^': [u.S, u.N],
        'v': [u.N, u.S],
        '<': [u.E, u.W],
        '>': [u.W, u.E],
    }

    slopepoints = defaultdict(list)
    for slope in slopes:
        sc = slopecons[grid[slope]]
        slopepoints[(slope[0] + sc[0][0], slope[1] + sc[0][1])].append((slope[0] + sc[1][0], slope[1] + sc[1][1]))

    graph = defaultdict(list)

    def connections_without_slope(pos):
        for npos in u.orthogonal(grid, pos):
            if grid[npos] == '.':
                yield npos

    queue = deque([start])
    while queue:
        cur = queue.popleft()
        _, dists = u.bfs(cur, connections_without_slope)
        for p, w in dists.items():
            if p in slopepoints:
                graph[cur].extend((tgt, w+2) for tgt in slopepoints[p])
                queue.extend(slopepoints[p])

            if p == end:
                graph[cur].append((end, w))

    def neighbors(pos):
        return [edge[0] for edge in graph[pos]]
    order = u.toposort(start, neighbors)

    mdist = defaultdict(lambda: -math.inf)
    mdist[start] = 0
    for src in order:
        for dst, w in graph[src]:
            if mdist[dst] < mdist[src] + w:
                mdist[dst] = mdist[src] + w
    return mdist[end]





    #def neighbors(pos):
    #    for d in u.dirs:
    #        npos = (pos[0] + d[0], pos[1] + d[1])
    #        c = grid.get(npos)
    #        if c == allowed[d] or c == '.':
    #            yield npos

    #@functools.cache
    #def find_all_paths(source, target, so_far):
    #    for node in neighbors(source):
    #        if node == target:
    #            yield len(so_far)
    #        elif node not in so_far:
    #            yield from find_all_paths(node, target, so_far | {node})
    #return max(plen for plen in find_all_paths(start, end, frozenset({start})))



    pass


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

    print(len(slopes))
    print(len(graph))

    def get_path_lengths(src, dst, path, total_w):
        if src == dst:
            #print(total_w)
            yield total_w
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
