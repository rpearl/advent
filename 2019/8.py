submit = True
from collections import Counter
from aocd import data
import u

img = [int(c) for c in data.strip()]


def a():
    w = 25
    h = 6
    best_zero = None
    res = None
    for layer in u.chunks(img, w * h):
        counts = Counter(layer)
        if best_zero is None or counts[0] < best_zero:
            res = counts[1] * counts[2]
            best_zero = counts[0]
    return res


def b():
    w = 25
    h = 6
    out = [None] * (w * h)
    layers = list(u.chunks(img, w * h))
    for i in range(w * h):
        for layer in layers:
            if layer[i] != 2:
                out[i] = layer[i]
                break
    m = {
        (x, y): row[x] for y, row in enumerate(list(u.chunks(out, w))) for x in range(w)
    }
    u.print_matrix(m, " #")


u.main(a, b, submit=globals().get("submit", False))
