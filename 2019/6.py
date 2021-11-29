submit = True
from collections import defaultdict, deque
import sys
from aocd import lines
import u

edges = [edge.strip().split(")") for edge in lines]
orbits = defaultdict(set)

for s, t in edges:
    orbits[s].add(t)


preds, dists = u.bfs("COM", lambda node: orbits[node])


def a():
    return sum(dists.values())


def b():
    spath = {}
    i = 0
    ptr = "SAN"
    while ptr != "COM":
        spath[ptr] = i
        i += 1
        ptr = preds[ptr]

    ptr = "YOU"
    i = 0
    count = None
    while ptr != "COM":
        if ptr in spath:
            count = i + spath[ptr]
            break
        i += 1
        ptr = preds[ptr]
    return count - 2


u.main(a, b, submit=globals().get("submit", False))
