import collections
import re


def p1(data):
    mem = collections.defaultdict(int)
    for line in data:
        if line[:4] == 'mask':
            mask = re.findall("mask = ([X01]*)", line)[0]
        else:
            loc, val = re.findall("mem\[(\d+)\] = (\d+)", line)[0]
            val = bin(int(val))[2:].rjust(len(mask), '0')
            res = ''
            for (x,y) in zip(mask, val):
                if x == 'X':
                    res += y
                else:
                    res += x
            mem[loc] = int(res, 2)
    return sum(mem.values())


def p2(data):
    mem = collections.defaultdict(int)
    for line in data:
        if line[:4] == 'mask':
            mask = re.findall("mask = ([X01]*)", line)[0]
        else:
            loc, val = re.findall("mem\[(\d+)\] = (\d+)", line)[0]
            loc = bin(int(loc))[2:].rjust(len(mask), '0')
            res = ''
            for (x,y) in zip(mask, loc):
                if x == '0':
                    res += y
                else:
                    res += x
            locs = ['']
            for d in res:
                if d != 'X':
                    locs = [loc+d for loc in locs]
                else:
                    locs = [loc+'0' for loc in locs] + [loc+'1' for loc in locs]
            for loc in locs:
                mem[loc] = int(val)   
    return sum(mem.values())


input = open('input.txt').read().rstrip()
data = [line for line in input.split('\n')]
print(f'part 1: {p1(data)}')
print(f'part 2: {p2(data)}')

