submit = True
from aocd import data, lines
from collections import Counter, defaultdict, deque
import functools
import u

target = "shiny gold bag"

contains = defaultdict(list)
contained_by = defaultdict(list)

for line in lines:
    line = line.replace(".", "").replace("bags", "bag")
    src, dsts = line.split(" contain ")
    if dsts == "no other bag":
        continue
    dsts = dsts.split(", ")

    for dst in dsts:
        w, *rest = dst.split(" ")
        w = int(w.strip())
        dst = " ".join(rest).strip()
        contains[src].append((w, dst))
        contained_by[dst].append((w, src))


def a():
    _, dists = u.bfs(target, lambda node: [nbr for _, nbr in contained_by[node]])
    s = len(dists) - 1
    return s


def b():
    @functools.cache
    def bags_inside(bag):
        s = 0
        for w, nbag in contains[bag]:
            s += w * (1 + bags_inside(nbag))
        return s

    return bags_inside(target)


u.main(a, b, submit=globals().get("submit", False))
