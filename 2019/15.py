submit = True
import sys
import functools
import math
import itertools
from collections import defaultdict, deque
import intcode
from aocd import data
import u

d = {1: (0, -1), 2: (0, 1), 3: (-1, 0), 4: (1, 0)}
reverse = {1: 2, 2: 1, 3: 4, 4: 3}

# ox must be reachable from start, so just do a DFS to build up a graph data structure
def build_graph(program):
    dists = {}
    graph = defaultdict(list)
    inps = []
    prog = intcode.run(program, inps)

    oxpos = None

    def move(cmd):
        inps.append(cmd)
        return next(prog)

    def dfs(pos, dist):
        nonlocal oxpos
        dists[pos] = dist
        for cmd, delta in d.items():
            npos = (pos[0] + delta[0], pos[1] + delta[1])
            curdist = dists.get(npos, math.inf)
            if dist >= curdist:
                continue
            status = move(cmd)
            if status == 2:
                oxpos = npos
            if status == 1 or status == 2:
                graph[pos].append(npos)
                graph[npos].append(pos)
                dfs(npos, dist + 1)
                move(reverse[cmd])

    dfs((0, 0), 0)

    return graph, oxpos, dists[oxpos]


graph, oxpos, odist = build_graph(data)


def a():
    return odist


def b():
    _, dists = u.bfs(oxpos, lambda node: graph[node])
    return max(dists.values())


u.main(a, b, submit=globals().get("submit", False))
