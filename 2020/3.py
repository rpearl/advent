# submit=True
from aocd import lines
import u


def a():
    grid = lines
    s = 0
    x = 0
    y = 0
    while y < len(grid):
        if grid[y][x % len(grid[0])] == "#":
            s += 1
        x += 3
        y += 1
    return s


def b():
    grid = lines
    ss = 1
    for dx, dy in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
        s = 0
        x = 0
        y = 0
        while y < len(grid):
            if grid[y][x % len(grid[0])] == "#":
                s += 1
            x += dx
            y += dy
        ss *= s
    return ss


u.main(a, b, submit=globals().get("submit", False))
