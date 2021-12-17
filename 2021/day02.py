def p1(inp):
    commands = [l.split() for l in inp.split('\n')] 
    x, y = 0, 0
    for (direction, n) in commands:
        n = int(n)
        if direction == "forward":
            x += n
        elif direction == "up":
            y -= n
        elif direction == "down":
            y += n
    return x * y


def p2(inp):
    commands = [l.split() for l in inp.split('\n')] 
    x, y, aim = 0, 0, 0
    for (direction, n) in commands:
        n = int(n)
        if direction == "forward":
            x += n
            y += aim * n
        elif direction == "up":
            aim -= n
        elif direction == "down":
            aim += n
    return x * y


inp = open("data/02.in").read().strip()
print(f"part 1: {p1(inp)}")
print(f"part 2: {p2(inp)}")
