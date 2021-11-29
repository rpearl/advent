submit = True
from collections import defaultdict
import sys
import itertools
import intcode
import u
from aocd import data

N = (0, -1)
S = (0, 1)
E = (1, 0)
W = (-1, 0)

left = {N: W, W: S, S: E, E: N}
right = {N: E, E: S, S: W, W: N}


def run(program, init):
    panels = defaultdict(int)
    pos = (0, 0)
    d = N
    panels[pos] = init

    buf = [panels[pos]]
    out = intcode.run(program, buf)

    for color, turn_right in u.chunks(out, 2):
        panels[pos] = color
        d = right[d] if turn_right else left[d]
        pos = (pos[0] + d[0], pos[1] + d[1])
        buf.append(panels[pos])

    return panels


def a():
    panels = run(data, 0)
    return len(panels)


def b():
    panels = run(data, 1)
    u.print_matrix(panels, " #")
    return "KLCZAEGU"


u.main(a, b, submit=globals().get("submit", False))
