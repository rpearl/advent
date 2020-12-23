submit = True
from aocd import lines
import sys
from collections import Counter, defaultdict, deque
import u


insns = []

for line in lines:
    op, offs = line.split(" ")
    offs = int(offs.replace("+", ""))
    insns.append((op, offs))


def interpret(insns):
    seen = set()
    acc = 0
    ip = 0

    while True:
        if ip == len(insns):
            return (ip, acc, True)
        op, off = insns[ip]
        # print((op, off, acc))
        if ip in seen:
            return (ip, acc, False)

        seen.add(ip)
        if op == "jmp":
            ip += off
        elif op == "acc":
            acc += off
            ip += 1
        elif op == "nop":
            ip += 1
        else:
            raise Exception("bad op")


def a():
    _, acc, _ = interpret(insns)
    return acc


def b():
    for i in range(len(insns)):
        rop, o = insns[i]
        if rop == "jmp":
            insns[i] = ("nop", o)
        elif rop == "nop":
            insns[i] = ("jmp", o)
        else:
            continue
        ip, acc, halted = interpret(insns)
        if halted:
            return acc
        insns[i] = (rop, o)


u.main(a, b, submit=globals().get("submit", False))
