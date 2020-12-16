from aocd import data, lines, submit
import sys
from collections import Counter, defaultdict, deque
import functools
from sortedcontainers import SortedList, SortedDict, SortedSet
import itertools
import u
import math


def nosubmit(answer, part):
    print(f"Part {part}:\n{answer}")


submit = nosubmit

# data = """position=< 9,  1> velocity=< 0,  2>
# position=< 7,  0> velocity=<-1,  0>
# position=< 3, -2> velocity=<-1,  1>
# position=< 6, 10> velocity=<-2, -1>
# position=< 2, -4> velocity=< 2,  2>
# position=<-6, 10> velocity=< 2, -2>
# position=< 1,  8> velocity=< 1, -1>
# position=< 1,  7> velocity=< 1,  0>
# position=<-3, 11> velocity=< 1, -2>
# position=< 7,  6> velocity=<-1, -1>
# position=<-2,  3> velocity=< 1,  0>
# position=<-4,  3> velocity=< 2,  0>
# position=<10, -3> velocity=<-1,  1>
# position=< 5, 11> velocity=< 1, -2>
# position=< 4,  7> velocity=< 0, -1>
# position=< 8, -2> velocity=< 0,  1>
# position=<15,  0> velocity=<-2,  0>
# position=< 1,  6> velocity=< 1,  0>
# position=< 8,  9> velocity=< 0, -1>
# position=< 3,  3> velocity=<-1,  1>
# position=< 0,  5> velocity=< 0, -1>
# position=<-2,  2> velocity=< 2,  0>
# position=< 5, -2> velocity=< 1,  2>
# position=< 1,  4> velocity=< 2,  1>
# position=<-2,  7> velocity=< 2, -2>
# position=< 3,  6> velocity=<-1, -1>
# position=< 5,  0> velocity=< 1,  0>
# position=<-6,  0> velocity=< 2,  0>
# position=< 5,  9> velocity=< 1, -2>
# position=<14,  7> velocity=<-2,  0>
# position=<-3,  6> velocity=< 2, -1>"""
#
# lines = data.splitlines()
#

print(f"File line count: {len(lines)}")


def a():
    pvs = []
    for line in lines:
        pvs.append(list(u.ints(line)))
    i = 0
    pa = math.inf
    grid = None
    while True:
        for pv in pvs:
            pv[0] += pv[2]
            pv[1] += pv[3]

        lt = min(pv[0] for pv in pvs)
        rt = max(pv[0] for pv in pvs)
        up = min(pv[1] for pv in pvs)
        dn = max(pv[1] for pv in pvs)
        a = (rt - lt) * (dn - up)

        if pa < a:
            for y in range(up, dn):
                row = []
                for x in range(lt, rt):
                    row.append(grid[x, y])
                print("".join(row))
            print(i)
            break
        else:
            grid = defaultdict(lambda: ".")
            for pv in pvs:
                grid[pv[0], pv[1]] = "#"
            pa = a
            i += 1
    pass


def b():
    pass


def main():
    ra = a()
    if ra is not None:
        submit(ra, part="a")

    rb = b()
    if rb is not None:
        submit(rb, part="b")


main()
