#  Copyright © 2021 NeuroByte Tech. All rights reserved.
#
#  NeuroByte Tech is the Developer Company of Rohan Mathew.
#
#  Project: AoC
#  File Name: pz1.py
#  Last Modified: 07/12/2020, 21:31

class Bag:
    def __init__(self, raw):
        raw = raw[:-1]  # remove full stop
        spl = raw.split(" contain ")
        self.bag_colour = spl[0].replace(" bags", "")

        if "no other bags" in spl[1]:
            self.children = 0
        else:
            self.children = {}
            for raw_child in spl[1].split(", "):
                spl = raw_child.split()
                qty = int(spl[0])
                col = " ".join(spl[1:-1])
                self.children[col] = qty


bags = {}
with open("input.txt") as f:
    line = f.readline().strip()
    while line != "":
        b = Bag(line)
        bags[b.bag_colour] = b
        line = f.readline().strip()


# Recursive algorithm to search tree
def is_in(bag, col):
    if bag.children == 0:
        return False
    elif col in bag.children:
        return True

    # Go through nested bags
    for bg in bag.children:
        if is_in(bags[bg], col):
            return True
    return False


def main():
    bools = []
    for bgn in bags:
        if is_in(bags[bgn], "shiny gold"):
            bools.append(True)
            continue
        bools.append(False)

    print(sum(bools))


if __name__ == "__main__":
    main()
