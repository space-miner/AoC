#!/usr/bin/env python3


def p1(data, dr, dc):
    r, c = 0, 0
    res = 0
    while r < len(data):
        if data[r][c] == '#':
            res += 1
        r += dr
        c += dc
        c %= len(data[0])
    return res
    

#     Right 1, down 1.
#     Right 3, down 1. (This is the slope you already checked.)
#     Right 5, down 1.
#     Right 7, down 1.
#     Right 1, down 2.
def p2(data):
    res = 1
    arr = [[1,1], [3,1], [5,1], [7,1], [1,2]]
    for slope in arr:
        dc, dr = slope
        res *= p1(data, dr, dc)
    return res
        

input = open('input.txt').readlines()
data = [line.rstrip() for line in input]
print(f'part 1: {p1(data, 1, 3)}')
print(f'part 2: {p2(data)}')

