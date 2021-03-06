#  Copyright © 2021 NeuroByte Tech. All rights reserved.
#
#  NeuroByte Tech is the Developer Company of Rohan Mathew.
#
#  Project: AoC
#  File Name: pz2.py
#  Last Modified: 06/12/2020, 14:11

from pz1 import *


def main():
    vectors = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2)
    ]

    prod = 1
    for v in vectors:
        prod *= traverse(environment, *v)
    print(prod)


if __name__ == "__main__":
    main()
