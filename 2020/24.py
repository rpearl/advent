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


positions = set(x for x, n in Counter(map(position, lines)).items() if n % 2)


def a():
    return len(positions)


def neighbors(pos):
    yield pos
    for delta in deltas.values():
        yield pos + delta


def b():
    active = set(positions)

    for step in range(100):
        for pos, count in Counter(
            itertools.chain.from_iterable(map(neighbors, active))
        ).items():
            if pos in active:
                if count == 1 or count > 3:
                    active.remove(pos)
            elif count == 2:
                active.add(pos)

    return len(active)
    #        day = step + 1
    # if day < 10 or day % 10 == 0:
    #    print(f"Day {day}: {sum(colors.values())}")
    pass


u.main(a, b, submit=globals().get("submit", False))
