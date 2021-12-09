import itertools
import cachetools
from math import gcd
from collections import deque, defaultdict
from collections.abc import MutableSequence
from sortedcontainers import SortedSet
import re
import time
import math
from aocd import submit as sbmt

def invert(d, multiple=False):
    out = defaultdict(list)
    for k, v in d.items():
        if multiple:
            out[v].append(k)
        else:
            out[v] = k
    return dict(out)

def to_int(l, base=10):
    o = 0
    for d in l:
        o *= base
        o += d
    return o

flathexdirs = {
    'n': (0, -1),
    'ne': (1, -1),
    'se': (1, 0),
    's': (0, 1),
    'sw': (-1,1),
    'nw': (-1, 0),
}

def sign(n):
    if n > 0:
        return 1
    elif n == 0:
        return 0
    else:
        return -1

def hex_axial_to_cube(pos):
    q,r = pos
    return (q,r,-q-r)

def hex_cube_subtract(a, b):
    return (a[0]-b[0],a[1]-b[1], a[2]-b[2])

def hex_cube_distance(a, b):
    q,r,s = hex_cube_subtract(a, b)
    return max(abs(q), abs(r), abs(s))

def hex_axial_distance(a, b):
    return hex_cube_distance(hex_axial_to_cube(a), hex_axial_to_cube(b))

def lmap(fn, *its):
    return list(map(fn, *its))

def window(seq, n=2):
    "Returns a sliding window (of width n) over data from the iterable"
    "   s -> (s0,s1,...s[n-1]), (s1,s2,...,sn), ...                   "
    it = iter(seq)
    result = tuple(itertools.islice(it, n))
    if len(result) == n:
        yield result
    for elem in it:
        result = result[1:] + (elem,)
        yield result


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


def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return itertools.chain.from_iterable(
        itertools.combinations(s, r) for r in range(len(s) + 1)
    )


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


def make_grid(rows, func=None):
    height = len(rows)
    width = len(rows[0])
    grid = {}

    for y in range(height):
        for x in range(width):
            p = rows[y][x]
            val = p if func is None else func(p, (x, y))
            if val is not None:
                grid[x, y] = val
    return grid, width, height


def _nbrs(grid, p, ds):
    px, py = p
    for dx, dy in ds:
        n = (px + dx, py + dy)
        if n in grid:
            yield n

def max_index(l):
    idx = -1
    m = None
    for i, x in enumerate(l):
        if m is None or x > m:
            m = x
            idx = i
    return idx,m

def orthogonal(grid, p):
    yield from _nbrs(grid, p, dirs)


def diagonal(grid, p):
    yield from _nbrs(grid, p, diags)


def all_neighbors(grid, p):
    yield from orthogonal(grid, p)
    yield from diagonal(grid, p)


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


def djikstra(start, neighbors):
    dist = defaultdict(lambda: math.inf)
    pred = defaultdict(lambda: None)
    dist[start] = 0
    queue = SortedSet(key=lambda v: dist[v])
    queue.add(start)
    print("got here")

    while queue:
        u = queue.pop(0)
        for v, w_uv in neighbors(u):
            alt = dist[u] + w_uv
            if alt < dist[v]:
                if v in queue:
                    queue.remove(v)
                dist[v] = alt
                pred[v] = u
                queue.add(v)
    return pred, dist


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


def main(a, b, submit=False):
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
