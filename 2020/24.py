submit = True
from aocd import data, lines
import sys
from collections import Counter, defaultdict, deque
import functools
from sortedcontainers import SortedList, SortedDict, SortedSet
import itertools
import u
import math
import time
import operator

deltas = {
    "e": complex(-1, 0),
    "w": complex(1, 0),
    "ne": complex(0, -1),
    "sw": complex(0, 1),
    "nw": complex(1, -1),
    "se": complex(-1, 1),
}

data2 = """sesenwnenenewseeswwswswwnenewsewsw
neeenesenwnwwswnenewnwwsewnenwseswesw
seswneswswsenwwnwse
nwnwneseeswswnenewneswwnewseswneseene
swweswneswnenwsewnwneneseenw
eesenwseswswnenwswnwnwsewwnwsene
sewnenenenesenwsewnenwwwse
wenwwweseeeweswwwnwwe
wsweesenenewnwwnwsenewsenwwsesesenwne
neeswseenwwswnwswswnw
nenwswwsewswnenenewsenwsenwnesesenew
enewnwewneswsewnwswenweswnenwsenwsw
sweneswneswneneenwnewenewwneswswnese
swwesenesewenwneswnwwneseswwne
enesenwswwswneneswsenwnewswseenwsese
wnwnesenesenenwwnenwsewesewsesesew
nenewswnwewswnenesenwnesewesw
eneswnwswnwsenenwnwnwwseeswneewsenese
neswnwewnwnwseenwseesewsenwsweewe
wseweeenwnesenwwwswnew"""
lines = data.splitlines()


def position(line):
    pos = 0
    i = 0
    while i < len(line):
        c = line[i]
        if c in "ns":
            c += line[i + 1]
        pos += deltas[c]
        i += len(c)
    return pos


def a():
    colors = defaultdict(int)
    for line in lines:
        pos = position(line)
        colors[pos] = 1 - colors[pos]
    return sum(colors.values())


def neighbors(pos):
    yield pos
    for delta in deltas.values():
        yield pos + delta


def b():
    c = Counter(map(position, lines))
    active = set(x for x, n in c.items() if n % 2)

    for step in range(100):
        counts = Counter(itertools.chain.from_iterable(map(neighbors, active)))
        for pos, count in counts.items():
            c = pos in active
            if (c and count == 1) or (c and count > 3) or (not c and count == 2):
                active ^= {pos}

    return len(active)
    #        day = step + 1
    # if day < 10 or day % 10 == 0:
    #    print(f"Day {day}: {sum(colors.values())}")
    pass


u.main(a, b, submit=globals().get("submit", False))
