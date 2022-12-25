#submit=True
from aocd import data, lines #type: ignore
import sys
from collections import Counter, defaultdict, deque, namedtuple
import functools
from sortedcontainers import SortedList, SortedDict, SortedSet
import itertools
import u
import math
import time
import operator

#data = """Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.
#Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 12 obsidian."""
#lines = data.splitlines()

ints = u.ints(data)
intlines = u.lmap(u.ints, lines)
toklines = [line.split(' ') for line in lines]

blueprints = {}

for line in intlines:
    num, *bp = line
    blueprints[num] = tuple(bp)
print(blueprints)

@functools.cache
def optimize(timeleft, costs, robot_counts, resource_counts):
    if timeleft <= 1:
        return 0

    max_or_bots = math.ceil((max(costs[0], costs[1], costs[2], costs[4]) * timeleft - resource_counts[0]) / timeleft)
    max_cl_bots = math.ceil((costs[3] * timeleft - resource_counts[1]) / timeleft)
    max_ob_bots = math.ceil((costs[5] * timeleft - resource_counts[2]) / timeleft)

    need_or_bots = robot_counts[0] < max_or_bots
    need_ob_bots = robot_counts[2] < max_ob_bots
    need_cl_bots = robot_counts[1] < max_cl_bots and need_ob_bots

    can_build_ge_bot = resource_counts[0] >= costs[4] and resource_counts[2] >= costs[5]
    can_build_ob_bot = resource_counts[0] >= costs[2] and resource_counts[1] >= costs[3] and need_ob_bots
    can_build_cl_bot = resource_counts[0] >= costs[1] and need_cl_bots
    can_build_or_bot = resource_counts[0] >= costs[0] and need_or_bots

    if can_build_ge_bot:
        new_resource_counts = (
            resource_counts[0] + robot_counts[0] - costs[4],
            resource_counts[1] + robot_counts[1],
            resource_counts[2] + robot_counts[2] - costs[5],
        )
        return optimize(timeleft-1, costs, robot_counts, new_resource_counts) + timeleft-1
    else:
        choices = []
        if can_build_ob_bot:
            new_resource_counts = (
                resource_counts[0] + robot_counts[0] - costs[2],
                resource_counts[1] + robot_counts[1] - costs[3],
                resource_counts[2] + robot_counts[2],
            )
            new_bots = (
                robot_counts[0],
                robot_counts[1],
                robot_counts[2]+1,
            )
            choices.append(
                optimize(timeleft-1, costs, new_bots, new_resource_counts)
            )
        if can_build_cl_bot:
            new_resource_counts = (
                resource_counts[0] + robot_counts[0] - costs[1],
                resource_counts[1] + robot_counts[1],
                resource_counts[2] + robot_counts[2],
            )
            new_bots = (
                robot_counts[0],
                robot_counts[1] + 1,
                robot_counts[2],
            )
            choices.append(
                optimize(timeleft-1, costs, new_bots, new_resource_counts)
            )
        if can_build_or_bot:
            new_resource_counts = (
                resource_counts[0] + robot_counts[0] - costs[0],
                resource_counts[1] + robot_counts[1],
                resource_counts[2] + robot_counts[2],
            )
            new_bots = (
                robot_counts[0] + 1,
                robot_counts[1],
                robot_counts[2],
            )
            choices.append(
                optimize(timeleft-1, costs, new_bots, new_resource_counts)
            )
        new_resource_counts = (
            resource_counts[0] + robot_counts[0],
            resource_counts[1] + robot_counts[1],
            resource_counts[2] + robot_counts[2],
        )
        choices.append(
            optimize(timeleft-1, costs, robot_counts, new_resource_counts)
        )
        return max(choices)

def a():
    return 1413
    tot = 0
    for num, bp in blueprints.items():
        score = optimize(24, bp, (1, 0, 0), (0, 0, 0))
        print(num, score)
        tot += num * score
    return tot
    pass


def b():
    tot = 1
    for num, bp in blueprints.items():
        if num > 3:
            break
        score = optimize(32, bp, (1, 0, 0), (0, 0, 0))
        print(num, score)
        tot *= score
    return tot
    pass

u.main(a, b, submit=globals().get('submit', False))
