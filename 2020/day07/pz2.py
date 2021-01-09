#  Copyright © 2021 NeuroByte Tech. All rights reserved.
#
#  NeuroByte Tech is the Developer Company of Rohan Mathew.
#
#  Project: AoC
#  File Name: pz2.py
#  Last Modified: 07/12/2020, 21:40

from pz1 import *


def count_children(bg):
    if bg.children == 0:
        return 0

    tot = 0
    for bag in bg.children:
        tot += bg.children[bag] + bg.children[bag] * count_children(bags[bag])

    return tot


def main():
    print(count_children(bags["shiny gold"]))


if __name__ == "__main__":
    main()
