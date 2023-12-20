submit=True
import z3
from aocd import data #type: ignore
from aocd import submit as sbmt #type: ignore
import sys
from collections import Counter, defaultdict, deque
import functools
from sortedcontainers import SortedList, SortedDict, SortedSet
import itertools
import u
import math
import time
import operator
import json

_data = """px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}"""

lines = data.splitlines()

ints = u.ints(data)
intlines = u.lmap(u.ints, lines)
toklines = [line.split(' ') for line in lines]

ops = {
    '<': operator.lt,
    '>': operator.gt,
}

def eval_rules(rules, part):
    for rule in rules:
        if len(rule) == 4:
            cat,op,val,dest = rule
            if ops[op](part[cat], val):
                return dest
        else:
            return rule[0]
    assert False

def eval_part(workflows, part):
    cur = 'in'

    while True:
        cur = eval_rules(workflows[cur], part)
        if cur in 'AR':
            return cur


def a():
    workflow_lines, part_lines = data.split('\n\n')

    workflows = defaultdict(list)

    for line in workflow_lines.splitlines():
        name,rules = line.split('{')
        rules = rules[:-1].split(',')
        for rule in rules:
            if ':' in rule:
                (cat,op,*val),dest = rule.split(':')
                val = int(''.join(val))
                workflows[name].append((cat,op,val,dest))
            else:
                workflows[name].append((rule,))

    parts = []
    for line in part_lines.splitlines():
        line = line.replace('=', '":')
        line = line.replace('{','{"')
        line = line.replace(',',',"')
        part = json.loads(line)
        parts.append(part)

    s = 0
    for part in parts:
        res = eval_part(workflows, part)
        if res == 'A':
            s += sum(part.values())
    return s
    pass






def b():
    workflow_lines, part_lines = data.split('\n\n')

    workflows = defaultdict(list)

    for line in workflow_lines.splitlines():
        name,rules = line.split('{')
        rules = rules[:-1].split(',')
        for rule in rules:
            if ':' in rule:
                (cat,op,*val),dest = rule.split(':')
                val = int(''.join(val))
                workflows[name].append((cat,op,val,dest))
            else:
                workflows[name].append((rule,))

    cats = {c: i for i,c in enumerate('xmas')}

    def constraint(rule, ranges):
        ranges = list(ranges)
        cat,op,val = rule
        c = cats[cat]
        l,h = ranges[c]
        if op == '>':
            ranges[c] = (max(val, l), h)
        else:
            ranges[c] = (l, min(val,h))
        return tuple(ranges)

    @functools.cache
    def count_workflows(name, ranges):
        if not all(l<h for l,h in ranges):
            return 0
        if name == 'A':
            return math.prod(h-l+1 for h,l in ranges)
        elif name == 'R':
            return 0
        rules = workflows[name]
        count = 0
        for rule in rules:
            if len(rule) == 4:
                cat,op,val,dest = rule
                count += count_workflows(dest, constraint((cat,op,val), ranges))

                if op == '<':
                    ranges = constraint((cat,'>',val-1), ranges)
                else:
                    ranges = constraint((cat,'<',val+1), ranges)
            else:
                return count + count_workflows(rule[0], ranges)




    expected = int('167409079868000')
    s = count_workflows('in', ((0,4001), (0,4001), (0,4001), (0,4001)))
    return s







    pass

def main():
    submit = globals().get('submit', False)
    astart = time.perf_counter()
    ra = a()
    aend = time.perf_counter()
    if ra is not None:
        print(f"Part a: {ra}")
        print(f"Time taken: {aend-astart:.4f} sec")
        if submit:
            sbmt(ra, part="a")

    bstart = time.perf_counter()
    rb = b()
    bend = time.perf_counter()
    if rb is not None:
        print(f"Part b: {rb}")
        print(f"Time taken: {bend-bstart:.4f} sec")
        if submit:
            sbmt(rb, part="b")
    print()
main()
