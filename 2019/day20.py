import sys
import string
from collections import defaultdict, deque
import heapq
import math

def is_portal_label(v):
    return all(c in string.ascii_uppercase for c in v)

def is_portal_node(node):
    return node[1] < 2
def make_grid(rows):
    grid = {}
    height = len(rows)
    width = len(rows[0])
    for y in range(height):
        for x in range(width):
            if rows[y][x] not in ' #'+string.ascii_uppercase and (x,y) not in grid:
                grid[x,y] = (rows[y][x], 2)
            if x < width-1:
                v = rows[y][x]+rows[y][x+1]
                if is_portal_label(v):
                    outer = (x == 0 or x == width-2)
                    if x < width/2:
                        px = x+2 if outer else x-1
                    else:
                        px = x-1 if outer else x+2
                    grid[px,y] = (v, int(outer))
            if y < height-1:
                v2 = rows[y][x]+rows[y+1][x]
                if is_portal_label(v2):
                    outer = (y == 0 or y == height-2)
                    if y < height/2:
                        py = y+2 if outer else y-1
                    else:
                        py = y-1 if outer else y+2
                    grid[x,py] = (v2, int(outer))
    return grid
rows = [row[:-1] for row in sys.stdin.readlines()]

dirs = [(-1,0),(1,0),(0,-1),(0,1)]
def reachable_nodes(grid, pos):
    queue = deque([(pos, 0)])
    reachable = []
    visited = set()

    while queue:
        node, dist = queue.popleft()
        if node in visited:
            continue

        visited.add(node)

        if is_portal_node(grid[node]) and dist > 0:
            reachable.append((grid[node], dist))
        else:
            for d in dirs:
                npos = (node[0] + d[0], node[1] + d[1])
                adj = grid.get(npos)
                if adj is not None:
                    queue.append((npos, dist+1))
    return reachable


def make_graph(rows):
    grid = make_grid(rows)
    portals = [(pos,node) for (pos, node) in grid.items() if is_portal_node(node)]

    graph = {node: reachable_nodes(grid, pos) for pos, node in portals}

    return graph

def shortest_path(adjacencies, start, end):
    dist = defaultdict(lambda: math.inf)
    dist[start] = 0

    queue = [(0, start)]

    while queue:
        udist, u = heapq.heappop(queue)
        if u == end:
            return udist
        for v, w_uv in adjacencies(u):
            alt = udist + w_uv
            if alt < dist[v]:
                dist[v] = alt
                heapq.heappush(queue, (alt, v))

def part1():
    graph = make_graph(rows)
    for node in graph:
        label, outer = node
        if label not in {'AA','ZZ'}:
            other = (label, 1-outer)
            graph[node].append((other, 1))
    start = ('AA', 1)
    end = ('ZZ', 1)
    def adjacencies(u):
        return graph[u]
    return shortest_path(adjacencies, start, end)

def part2():
    graph = make_graph(rows)

    def adjacencies(node):
        u,level = node
        for v, dist in graph[u]:
            yield (v,level),dist
        label,outer = u
        if label not in {'AA','ZZ'}:
            other = (label, 1-outer)
            newlevel = (level - 1) if outer else (level + 1)
            if newlevel >= 0:
                yield (other, newlevel), 1

    start = (('AA', 1),0)
    end = (('ZZ', 1),0)
    return shortest_path(adjacencies, start, end)
print(part1())
print(part2())
