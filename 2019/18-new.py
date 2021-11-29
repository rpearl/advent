import string
import sys
from collections import deque,defaultdict
import math
import heapq
import itertools

relevant = string.ascii_lowercase + string.ascii_uppercase + '@1234'
def is_key(node):
    return node in string.ascii_lowercase

def is_door(node):
    return node in string.ascii_uppercase

def make_grid(rows):
    grid = {}
    height = len(rows)
    width = len(rows[0]) -1
    positions = {}

    for y in range(height):
        for x in range(width):
            p = rows[y][x]
            if p != '#':
                grid[x,y] = p
            if p in relevant:
                positions[p] = x,y


    return grid,positions

dirs = [(-1,0), (1, 0), (0, -1), (0, 1)]


def reachable_nodes(grid, pos):
    visited = set()

    queue = deque([(pos, 0)])

    reachable = []

    while queue:
        node, dist = queue.popleft()

        if node in visited:
            continue
        visited.add(node)

        if grid[node] in relevant and dist > 0:
            reachable.append((grid[node], dist))
        else:
            for d in dirs:
                npos = (node[0] + d[0], node[1] + d[1])
                adj = grid.get(npos)
                if adj is not None:
                    queue.append((npos, dist+1))
    return reachable

def make_graph(grid, positions):
    graph = defaultdict(list)

    for node, pos in positions.items():
        graph[node] = reachable_nodes(grid, pos)

    return graph

def add_key(keyset, key):
    c = ord(key) - ord('a')
    return keyset | (1 << c)

def has_key(keyset, key):
    c = ord(key) - ord('a')
    return (keyset >> c) & 1

cache = {}
def adjacent(graphs, us):
    if us in cache:
        return cache[us]
    out = []
    for i,u in enumerate(us):
        for v,dist in graphs[i][u]:
            vs = list(us)
            vs[i] = v
            out.append((tuple(vs),dist))
    cache[us] = out
    return out

def multinodes(graphs):
    keysets = [g.keys() for g in graphs]
    return itertools.product(*keysets)

def shortest_path(graphs, entrances):
    all_keys = 0
    for g in graphs:
        for p in g.keys():
            if is_key(p):
                all_keys = add_key(all_keys, p)
    dist = {node: {} for node in multinodes(graphs)}

    dist[entrances][0] = 0

    queue = [(0, 0, entrances)]

    def smaller(alt, v, vkeys):
        curdist = dist[v].get(vkeys, math.inf)
        return alt < curdist

    while queue:
        udist, ukeys, u = heapq.heappop(queue)
        if ukeys == all_keys:
            return udist

        for v, w_uv in adjacent(graphs, u):
            passable = all(has_key(ukeys, p.lower()) for p in v if is_door(p))
            if not passable:
                continue
            vkeys = ukeys
            for p in v:
                if is_key(p):
                    vkeys = add_key(vkeys, p)
            alt = udist + w_uv
            if smaller(alt, v, vkeys):
                dist[v][vkeys] = alt
                heapq.heappush(queue, (alt, vkeys, v))


inp = sys.stdin.readlines()
def part1():
    grid, positions = make_grid(inp)
    graph = make_graph(grid, positions)
    return shortest_path([graph], ('@',))

def print_grid(grid, width,height):
    for y in range(height):
        row = []
        for x in range(width):
            row.append(grid.get((x,y),'#'))
        print(''.join(row))

def reachable_subgraph(graph, start):
    visited = set()
    subgraph = defaultdict(list)
    stack = [start]

    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        subgraph[node] = graph[node]
        for child, _ in subgraph[node]:
            stack.append(child)
    return subgraph

def part2():
    width = len(inp)
    height = len(inp[0])
    grid, positions = make_grid(inp)
    ox, oy = positions['@']
    for dx,dy in dirs + [(0,0)]:
        del grid[ox+dx,oy+dy]

    grid[ox-1,oy-1] = '1'
    positions['1'] = ox-1,oy-1
    grid[ox+1,oy-1] = '2'
    positions['2'] = ox+1,oy-1
    grid[ox-1,oy+1] = '3'
    positions['3'] = ox-1,oy+1
    grid[ox+1,oy+1] = '4'
    positions['4'] = ox+1,oy+1
    del positions['@']

    fullgraph = make_graph(grid, positions)
    entrances = ['1','2','3','4']
    graphs = [reachable_subgraph(fullgraph, entrance) for entrance in entrances]
    return shortest_path(graphs, tuple(entrances))



print(part1())
#print(part2())
