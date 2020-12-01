with open("day1/input.txt") as f:
    ns = [int(n.strip()) for n in f.readlines()]

for ln in ns:
    found = False
    nn = 2020 - ln
    for sn in ns:
        if nn - sn in ns:
            print(ln * sn * (nn - sn))
            found = True
            break

    if found:
        break
