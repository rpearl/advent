# submit = True
from aocd import lines
import u

tbl = str.maketrans("FBLR", "0101")

sids = {int(sid.translate(tbl), 2) for sid in lines}


def a():
    return max(sids)


def b():
    seen = set(sids)
    for x in range(2 ** len(lines[0]) - 1):
        if x not in seen and x - 1 in seen and x + 1 in seen:
            return x


u.main(a, b, submit=globals().get("submit", False))
