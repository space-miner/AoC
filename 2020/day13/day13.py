import re
import heapq
import math
import functools


def p1(data):
    t = int(data[0])
    h = [(int(x), int(x)) for x in re.findall('(\d+)', data[1])]
    heapq.heapify(h)
    while h:
        a, b = heapq.heappop(h)
        if a > t:
            return (a-t) * b
        else:
            heapq.heappush(h, (a+b, b))


def mod_inverse(k, n):
    k %= n
    for i in range(1,n):
        if k*i % n == 1:
            return i
    return 1


def p2(data):
    ls = [[int(n),k] for k,n in enumerate(data[1].split(',')) if n.isnumeric()]
    ns = [n for (n,k) in ls]
    ks = [k for (n,k) in ls]
    m = functools.reduce(lambda x,y: x*y, ns)
    res = 0
    for (n,k) in ls:
        p = m//n
        res += p * mod_inverse(p,n) * k
    return -res % m


input = open('input.txt').read().rstrip()
data = [line for line in input.split('\n')]
print(f'part 1: {p1(data)}')
print(f'part 2: {p2(data)}')
