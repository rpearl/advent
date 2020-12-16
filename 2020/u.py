import itertools
import cachetools
from math import gcd
from collections import deque
import re


def lmap(fn, *its):
    return list(map(fn, *its))


def ints(line):
    return lmap(int, re.findall(r"-?\d+", line))


def print_matrix(matrix, charmap, default=0):
    minx = min(k[0] for k in matrix.keys())
    miny = min(k[1] for k in matrix.keys())
    maxx = max(k[0] for k in matrix.keys()) + 1
    maxy = max(k[1] for k in matrix.keys()) + 1

    for y in range(miny, maxy):
        row = ""
        for x in range(minx, maxx):
            row += charmap[matrix.get((x, y), default)]
        print(row)


def chunks(iterable, n, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    args = [iter(iterable)] * n
    return itertools.zip_longest(fillvalue=fillvalue, *args)


def lcm(a, b):
    return int(a * b / gcd(a, b))


dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
diags = [(-1, -1), (-1, 1), (1, -1), (1, 1)]


class DisjointSets:
    def __init__(self, n):
        self.n = n
        self.parents = [None] * n
        self.ranks = [1] * n
        self.size = n

    def find(self, x):
        p = self.parents[x]
        if p is None:
            return x
        p = self.find(p)
        self.parents[x] = p
        return p

    def in_same_set(self, i, j):
        return self.find(i) == self.find(j)

    def union(self, i, j):
        i = self.find(i)
        j = self.find(j)
        if i == j:
            return
        ir = self.ranks[i]
        jr = self.ranks[j]
        if ir < jr:
            self.parents[i] = j
        elif ir > jr:
            self.parents[j] = i
        else:
            self.parents[j] = i
            self.ranks[i] += 1
        self.size -= 1

    def __len__(self):
        return self.size


class Grid:
    def __init__(self, rows):
        height = len(rows)
        width = len(rows[0])

        grid = {}

        for y in range(height):
            for x in range(width):
                p = rows[y][x]
                grid[x, y] = p

        self.grid = grid
        self.width = width
        self.height = height
        self.include_diags = True

    def neighbors(self, pos):
        for d in dirs:
            npos = (d[0] + pos[0], d[1] + pos[1])

            if npos in self.grid:
                yield npos
        if self.include_diags:
            for d in diags:
                npos = (d[0] + pos[0], d[1] + pos[1])

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

            if is_interesting(gp) and dist > 0:
                r.append((gp, dist))

            else:
                for neighbor in self.neighbors(p):
                    queue.append((neighbor, dist + 1))
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


N = (0, 1)
S = (0, -1)
E = (1, 0)
W = (-1, 0)

rot90 = {N: E, E: S, S: W, W: N}


class Linked:
    def __init__(self, item):
        self.item = item
        self.n = self
        self.p = self

    def add(self, other):
        n = self.n

        other.n = n
        other.p = self
        self.n = other
        n.p = other

    def remove(self):
        n = self.n
        p = self.p
        n.p = p
        p.n = n

    def move(self, count):
        cur = self
        for i in range(abs(count)):
            cur = cur.p if count < 0 else cur.n
        return cur

    def __iter__(self):
        yield self
        ptr = self.n
        while ptr != self:
            yield ptr
            ptr = ptr.n

    def __repr__(self):
        return f"({self.item})"
