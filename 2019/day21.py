#import aoc
import intcode
import itertools
import math
import sys

rds = 'ABCD'
writes = 'TJ'
ops = ['NOT', 'AND', 'OR']

def fmt(rd, wr, op):
    return f'{op} {rd} {wr}'
prog = sys.stdin.read()
def part1():
    sc = [
        "NOT A J",
        "NOT B T",
        "OR T J",
        "NOT C T",
        "OR T J",
        "AND D J",
        "WALK\n",
    ]
    sc = [ord(c) for c in '\n'.join(sc)]
    vals = list(intcode.run(prog, sc))

    for c in vals:
        if c > 255:
            return c

def part2():
    sc = [
        'NOT A J',
        'OR J T',
        'NOT B J',
        'OR J T',
        'NOT C J',
        'OR J T',
        'AND C J',
        'OR T J',
        'AND D J',
        'NOT J T',
        'AND J T',
        'OR E T',
        'OR H T',
        'AND T J',
        'RUN\n',
    ]
    sc = [ord(c) for c in '\n'.join(sc)]

    for c in intcode.run(prog, sc):
        if c > 255:
            return c

print(part1())
print(part2())
