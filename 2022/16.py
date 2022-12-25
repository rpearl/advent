submit=True
from aocd import data, lines #type: ignore
import heapq
import sys
from collections import Counter, defaultdict, deque
import functools
from sortedcontainers import SortedList, SortedDict, SortedSet
import itertools
import u
import math
import time
import operator

#data = """Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
#Valve BB has flow rate=13; tunnels lead to valves CC, AA
#Valve CC has flow rate=2; tunnels lead to valves DD, BB
#Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
#Valve EE has flow rate=3; tunnels lead to valves FF, DD
#Valve FF has flow rate=0; tunnels lead to valves EE, GG
#Valve GG has flow rate=0; tunnels lead to valves FF, HH
#Valve HH has flow rate=22; tunnel leads to valve GG
#Valve II has flow rate=0; tunnels lead to valves AA, JJ
#Valve JJ has flow rate=21; tunnel leads to valve II"""
#lines=data.splitlines()

ints = u.ints(data)
intlines = u.lmap(u.ints, lines)
toklines = [line.split(' ') for line in lines]

naive_graph = defaultdict(list)
rate = {}

for line in lines:
    flow, tunnels = line.split(';')
    src = flow[6:8]
    _, flow = flow.split('=')
    flow = int(flow)
    dsts = tunnels.split(', ')
    dsts[0] = dsts[0].split(' ')[-1]
    naive_graph[src] = dsts
    rate[src] = flow

all_valves = frozenset(v for v,x in rate.items() if x > 0)
graph = defaultdict(list)

dists = u.floyd_warshall(rate.keys(), lambda u: [(v, 1) for v in naive_graph[u]])

def paths(timeleft, cur='AA', available_valves=all_valves, open_valves=dict()):
    for nxt in available_valves:
        new_time = timeleft - dists[cur,nxt] - 1
        if new_time < 2:
            continue
        new_open = open_valves | {nxt: new_time}
        yield from paths(new_time, nxt, available_valves-{nxt}, new_open)
    yield open_valves

def score(path):
    return sum(rate[v]*t for v, t in path.items())

def a():
    return max(score(p) for p in paths(timeleft=30))

def b():
    score_for_valves = defaultdict(int)
    for path in paths(timeleft=26):
        valves = frozenset(path.keys())
        s = score(path)
        if s > score_for_valves[valves]:
            score_for_valves[valves] = s

    best = 0
    for (you, you_score), (ele, ele_score) in itertools.combinations(score_for_valves.items(), 2):
        if len(you & ele) > 0:
            continue

        cur_score = you_score + ele_score
        if cur_score > best:
            best = cur_score
    return best



#def neighbors(state):
#    cur, time, flow, valves = state
#    if time == 30:
#        return
#    if valves == target_valves:
#        time_remaining = 30-time
#        newflow = flow + time_remaining*full_flow
#        weight = 30*full_flow - newflow
#        yield (cur, 30, newflow, valves), weight
#        return
#    dflow = sum(rate[valve] for valve in valves)
#
#    newflow = flow + dflow
#    weight = 30*full_flow - newflow
#    if cur not in valves and rate[cur] > 0:
#        yield (cur, time+1, newflow, valves | frozenset({cur})), weight
#
#    for dst in graph[cur]:
#        yield (dst, time+1, newflow, valves), weight

#    start = ('AA', 0, 0, frozenset())
#
#    end_state = None
#    dist = defaultdict(lambda: math.inf)
#    pred = {}
#    dist[start] = 0
#    seen = set()
#    queue = [(0, start)]
#    while queue:
#        d, u = heapq.heappop(queue)
#        if u in seen:
#            continue
#        seen.add(u)
#        for v, w_uv in neighbors(u):
#            if v in seen: continue
#            alt = dist[u] + w_uv
#            if alt < dist[v]:
#                dist[v] = alt
#                pred[v] = u
#                heapq.heappush(queue, (alt, v))
#
#    return max(flow for (_, time, flow, _) in seen if time == 30)

u.main(a, b, submit=globals().get('submit', False))
