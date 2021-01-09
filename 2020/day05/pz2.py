#  Copyright © 2021 NeuroByte Tech. All rights reserved.
#
#  NeuroByte Tech is the Developer Company of Rohan Mathew.
#
#  Project: AoC
#  File Name: pz2.py
#  Last Modified: 06/12/2020, 16:49

from pz1 import *


def main():
    for n in range(min(seat_ids) + 8, max(seat_ids) + 2 - 8, 2):
        if n not in seat_ids:
            print(n)
            break


if __name__ == "__main__":
    main()
