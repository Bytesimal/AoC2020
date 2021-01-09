#  Copyright © 2021 NeuroByte Tech. All rights reserved.
#
#  NeuroByte Tech is the Developer Company of Rohan Mathew.
#
#  Project: AoC
#  File Name: pz2.py
#  Last Modified: 06/12/2020, 14:10

from pz1 import *


def main():
    pwds = []
    with open("input.txt") as f:
        line = f.readline()
        while line != "":
            pwds.append(Pwd(line))
            line = f.readline()

    pwds = [p.is_valid2() for p in pwds]
    print(sum(pwds))


if __name__ == "__main__":
    main()
