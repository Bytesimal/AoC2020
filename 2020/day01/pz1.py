with open("input.txt") as #  Copyright © 2021 NeuroByte Tech. All rights reserved.
#
#  NeuroByte Tech is the Developer Company of Rohan Mathew.
#
#  Project: AoC
#  File Name: pz1.py
#  Last Modified: 06/12/2020, 14:10

f:
    ns = [int(n.strip()) for n in f.readlines()]


def main():
    for n in ns:
        if 2020 - n in ns:
            print(n * (2020 - n))
            break


if __name__ == "__main__":
    main()
