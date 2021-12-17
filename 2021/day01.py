def p1(inp):
    depth = [ *map(int, inp.split('\n')) ]
    return sum(a < b for (a, b) in zip(depth, depth[1:]))


def p2(inp):
    depth = [ *map(int, inp.split('\n')) ]
    return sum(a < b for (a, b) in zip(depth, depth[3:]))


inp = open("data/01.in").read().strip()
print(f"part 1: {p1(inp)}")
print(f"part 2: {p2(inp)}")
