#!/usr/bin/env python3


def p1(data, target):
    s = set()
    for n in data:
        if target-n in s:
            return n*(target-n)
        else:
            s.add(n)
    return None


def p2(data):
    for i, n in enumerate(data):
        val = p1(data[i+1::], 2020-n)
        if val:
            return n * val


input = open('input.txt').readlines()
data = [int(line.rstrip()) for line in input]
print(f'part 1: {p1(data, 2020)}')
print(f'part 2: {p2(data)}')
