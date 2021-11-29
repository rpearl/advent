import itertools
import cachetools
from math import gcd
from collections import deque


def print_matrix(matrix, charmap, default=0):
    minx = min(k[0] for k in matrix.keys())
    miny = min(k[1] for k in matrix.keys())
    maxx = max(k[0] for k in matrix.keys())+1
    maxy = max(k[1] for k in matrix.keys())+1

    for y in range(miny, maxy):
        row = ''
        for x in range(minx, maxx):
            row += charmap[matrix.get((x, y), default)]
        print(row)


def chunks(iterable, n, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    args = [iter(iterable)] * n
    return itertools.zip_longest(fillvalue=fillvalue, *args)


def lcm(a, b):
    return int(a * b / gcd(a, b))

dirs = [(-1,0), (1, 0), (0, -1), (0, 1)]

class Grid:
    def __init__(self, rows):
        width = len(rows)
        height = len(rows[0])

        grid = {}

        for y in range(height):
            for x in range(width):
                p = rows[y][x]
                grid[x,y] = p

        self.grid = grid
        self.width = width
        self.height = height


    def neighbors(self, pos):
        for d in dirs:
            npos = (d[0]+pos[0], d[1]+pos[1])

            if npos in self.grid:
                yield npos

    @cachetools.cached(cache={}, key=lambda *args: args[0])
    def reachable(self, pos, is_interesting):
        visited = set()
        queue = deque([(pos, 0)])

        r = []

        while queue:
            p, dist = queue.popleft()
            if p in visited:
                continue
            visited.add(p)

            gp = grid[p]

            if is_node(gp) and dist > 0:
                r.append((gp, dist))

            else:
                for neighbor in self.neighbors(p):
                    queue.append((neighbor, dist+1))
        return r


def bfs(start, neighbors, is_done=None):
    pred = {}
    dists = {}
    dists[start] = 0
    queue = deque([(start, None)])

    while queue:
        node, parent = queue.popleft()
        if node in pred:
            continue
        pred[node] = parent
        if parent:
            dists[node] = dists.get(parent) + 1

        if is_done is not None and is_done(node, pred, dists):
            break

        for child in neighbors(node):
            queue.append((child, node))
    return pred, dists
