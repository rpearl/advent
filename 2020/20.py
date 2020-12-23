submit = True
from aocd import data, lines
import sys
from collections import Counter, defaultdict, deque, namedtuple
import functools
from sortedcontainers import SortedList, SortedDict, SortedSet
import itertools
import u
import math
import time
import operator


def nosubmit(answer, part):
    print(f"Part {part}:\n{answer}")


# submit = nosubmit

monster = [
    "                  # ",
    "#    ##    ##    ###",
    " #  #  #  #  #  #   ",
]

print(f"File line count: {len(lines)}")


def rstr(s):
    return "".join(reversed(s))


tiles = {}
ts = data.split("\n\n")
for t in ts:
    tid, *rest = t.splitlines()
    tid = u.ints(tid)[0]
    tiles[tid] = tuple(rest)


def rot(tile):
    r = []
    for i in range(len(tile)):
        r.append("".join(x[i] for x in tile))
    return tuple(reversed(r))


BorderList = namedtuple("Borrderlist", ["top", "left", "bottom", "right"])


def borders(tile):
    return BorderList(
        top=tile[0],
        left="".join(row[0] for row in tile),
        bottom=tile[-1],
        right="".join(row[-1] for row in tile),
    )


def rotations(tile):
    cur = tile

    for _ in range(4):
        yield cur
        cur = rot(cur)


def orientations(tile):
    for t in rotations(tile):
        yield t
        yield tuple(reversed(t))


border_connections = defaultdict(list)
for tid, tile in tiles.items():
    for border in borders(tile):
        border_connections[border].append(tid)
        border_connections[rstr(border)].append(tid)

corners = [
    tid
    for tid, tile in tiles.items()
    if sum(len(border_connections[border]) - 1 for border in borders(tile)) == 2
]


def a():
    return functools.reduce(operator.mul, corners, 1)


size = int(math.sqrt(len(tiles)))


def b():
    grid = {}
    cid = corners[0]
    ctile = tiles[cid]
    for ctile in rotations(tiles[cid]):
        bs = borders(ctile)
        if (
            len(border_connections[bs.top]) == 1
            and len(border_connections[bs.left]) == 1
        ):
            grid[0, 0] = cid, ctile
            break

    tsize = len(tiles[cid])

    for y in range(size):
        for x in range(size):
            if (x, y) == (0, 0):
                continue
            left = grid.get((x - 1, y))
            if left:
                tid, ltile = left
                border_match = borders(ltile).right
                check = "left"
            else:
                tid, ttile = grid[x, y - 1]
                border_match = borders(ttile).bottom
                check = "top"
            (possible,) = [p for p in border_connections[border_match] if p != tid]
            ptile = tiles[possible]
            for tile in orientations(ptile):
                if getattr(borders(tile), check) == border_match:
                    grid[x, y] = (possible, tile)
                    break

    image = []
    for y in range(size):
        for ty in range(1, tsize - 1):
            row = []
            for x in range(size):
                _, tile = grid[x, y]
                row.append(tile[ty][1:-1])
            image.append("".join(row))

    def monster_at(img, x, y):
        return all(
            img[y + my][x + mx] == "#"
            for my in range(len(monster))
            for mx in range(len(monster[0]))
            if monster[my][mx] == "#"
        )

    mcount = 0
    for img in orientations(image):
        for y in range(len(img) - len(monster)):
            for x in range(len(img[0]) - len(monster[0])):
                if monster_at(img, x, y):
                    mcount += 1
    print(mcount)
    tot = sum(row.count("#") for row in img)
    m = sum(row.count("#") for row in monster)
    mhab = m * mcount
    return tot - mhab


u.main(a, b, submit=globals().get("submit", False))
