#  Copyright © 2021 NeuroByte Tech. All rights reserved.
#
#  NeuroByte Tech is the Developer Company of Rohan Mathew.
#
#  Project: AoC
#  File Name: pz2.py
#  Last Modified: 06/12/2020, 18:08

from pz1 import *


def main():
    tot = 0

    for g in groups:
        opt = {}

        for rsp in g:
            for c in rsp:
                if c in opt:
                    opt[c] += 1
                    continue
                opt[c] = 1

        for c in opt:
            if opt[c] == len(g):
                tot += 1

    print(tot)


if __name__ == "__main__":
    main()
