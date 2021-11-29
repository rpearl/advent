submit = True
import intcode
import math
from itertools import permutations
from aocd import data
import u


def run_amps(settings):
    inps = [[setting] for setting in settings]
    inps[0].append(0)
    progs = [intcode.run(data, inp) for inp in inps]

    while True:
        for i, program in enumerate(progs):
            try:
                out = next(program)
                inps[(i + 1) % len(inps)].append(out)
            except StopIteration:
                return out


def a():
    best_signal = -math.inf
    for settings in permutations(range(5)):
        signal = 0
        for setting in settings:
            inps = [setting, signal]
            prog = intcode.run(data, inps)

            signal = next(prog)

        best_signal = max(best_signal, signal)
    return best_signal


def b():
    return max(run_amps(settings) for settings in permutations(range(5, 10)))


u.main(a, b, submit=globals().get("submit", False))
