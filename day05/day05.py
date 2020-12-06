#!/usr/bin/env python3


def p1(data):
    res = 0
    for line in data:
        row = '0b'
        col = '0b'
        for ch in line:
            if ch == 'F':
                row += '0'
            elif ch == 'B':
                row += '1'
            elif ch == 'L':
                col += '0'
            elif ch == 'R':
                col += '1'
        res = max(res, int(row, 2)*8 + int(col, 2))
    return res


def p2(data):
    s = set()
    for line in data:
        row = '0b'
        col = '0b'
        for ch in line:
            if ch == 'F':
                row += '0'
            elif ch == 'B':
                row += '1'
            elif ch == 'L':
                col += '0'
            elif ch == 'R':
                col += '1'
        s.add(int(row, 2)*8 + int(col, 2))
    for i in range(min(s)+1, max(s)):
        if i not in s and i-1 in s and i+1 in s:
            return i


input = open('input5').readlines()
data = [line.rstrip() for line in input]
print(f'part 1: {p1(data)}')
print(f'part 2: {p2(data)}')
