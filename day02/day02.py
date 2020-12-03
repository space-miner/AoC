#!/usr/bin/env python3

import collections
import re

def p1(data):
    res = 0
    for (a, b, ch, s) in data:
        c = collections.Counter(s)
        if int(a) <= c[ch] <= int(b):
            res += 1
    return res


def p2(data):
    res = 0
    for (a, b, ch, s) in data:
        if (s[int(a)-1] == ch) != (s[int(b)-1] == ch):
            res += 1
    return res


input = open('input.txt').readlines()
pat = r'(\d*)-(\d*) (\w): (\w+)'
data = [re.findall(pat, line)[0] for line in input]
print(f'part 1: {p1(data)}')
print(f'part 2: {p2(data)}')
