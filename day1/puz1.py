target = 2020

with open("day1/input.txt") as f:
    ns = [int(n.strip()) for n in f.readlines()]

for n in ns:
    if 2020 - n in ns:
        print(n * (2020 - n))
