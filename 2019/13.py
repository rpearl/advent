submit = True
import intcode
import u
import itertools
from collections import defaultdict
import sys
from aocd import data

c = " +#_O"


def print_tiles(board, score=None):
    print(score)
    u.print_matrix(board, c)


def a():
    out = defaultdict(int)
    for x, y, tile in u.chunks(intcode.run(data, []), 3):
        out[(x, y)] = tile
    # print_tiles(out)
    blocks = len([v for v in out.values() if v == 2])
    return blocks


def b():
    prog = [int(c) for c in data.split(",")]
    prog[0] = 2
    ball = None
    for i in range(len(prog) - 2):
        if prog[i] == 0 and prog[i + 1] == 3 and prog[i + 2] == 0:
            ball = i + 1
            break
    for r in range(ball - 17, ball + 18):
        prog[r] = 1
    score = 0
    inps = [0] * 6500
    out = defaultdict(int)
    for x, y, tile in u.chunks(intcode.run(prog, inps), 3):
        if (x, y) == (-1, 0):
            score = tile
            # print_tiles(out, score)
        else:
            out[(x, y)] = tile
    return score


u.main(a, b, submit=globals().get("submit", False))
