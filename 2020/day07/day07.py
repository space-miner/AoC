import collections
import re


def p1(data):
    # parse
    d = collections.defaultdict(lambda: set())
    for line in data:
        a, b = line.split('contain')
        pat = r'(\w+ \w+)'
        outer = re.findall(pat, a)[0]
        pat = r'(\d+) (\w+ \w+)'
        inner = re.findall(pat, b)
        for (num, bag) in inner:
            d[bag].add(outer)
    # part 1
    s = set()
    q = collections.deque(['shiny gold'])
    while q:
        bag = q.popleft()
        for outer in d[bag]:
            if outer not in s:
                s.add(outer)
                q.append(outer)
    return len(s)


def p2(data):
    # parse
    d = collections.defaultdict(lambda: collections.defaultdict(int))
    for line in data:
        a, b = line.split('contain')
        pat = r'(\w+ \w+)'
        outer = re.findall(pat, a)[0]
        pat = r'(\d+) (\w+ \w+)'
        inner = re.findall(pat, b)
        for (num, bag) in inner:
            d[outer][bag] = int(num)
    # part 2
    def helper(bag):
        ct = 1
        for inner in d[bag]:
            ct += d[bag][inner] * helper(inner)
        return ct
    return helper('shiny gold')-1


input = open('input.txt').read().rstrip()
data = [line.rstrip() for line in input.split('\n')]
print(f'part 1: {p1(data)}')
print(f'part 2: {p2(data)}')
