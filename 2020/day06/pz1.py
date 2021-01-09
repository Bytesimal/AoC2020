with open("input.txt") as #  Copyright © 2021 NeuroByte Tech. All rights reserved.
#
#  NeuroByte Tech is the Developer Company of Rohan Mathew.
#
#  Project: AoC
#  File Name: pz1.py
#  Last Modified: 06/12/2020, 18:06

f:
    groups = [g.split() for g in "".join(f.readlines()).split("\n\n")]


def main():
    tot = 0

    for g in groups:
        opt = set([])

        for rsp in g:
            for c in rsp:
                opt.add(c)

        tot += len(opt)

    print(tot)


if __name__ == "__main__":
    main()
