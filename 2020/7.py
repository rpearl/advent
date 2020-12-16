from aocd import data, submit
import sys
from collections import Counter, defaultdict, deque
import cachetools
import u

lines = data.split("\n")

print(f"File lines: {len(lines)}")


def nosubmit(answer, part):
    print(f"Part {part}: {answer}")


submit = nosubmit


# data = """light red bags contain 1 bright white bag, 2 muted yellow bags.
# dark orange bags contain 3 bright white bags, 4 muted yellow bags.
# bright white bags contain 1 shiny gold bag.
# muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
# shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
# dark olive bags contain 3 faded blue bags, 4 dotted black bags.
# vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
# faded blue bags contain no other bags.
# dotted black bags contain no other bags."""

target = "shiny gold bag"

contains = defaultdict(list)
contained_by = defaultdict(list)

for line in data.split("\n"):
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
    @cachetools.cached(cache={})
    def bags_inside(bag):
        s = 0
        for w, nbag in contains[bag]:
            s += w * (1 + bags_inside(nbag))
        return s

    return bags_inside(target)


def main():
    ra = a()
    if ra is not None:
        submit(ra, part="a")

    rb = b()
    if rb is not None:
        submit(rb, part="b")
    print()


main()
