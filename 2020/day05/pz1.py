def seat_coords(bin_spc):
    # find row
    lbound = 0
    hbound = 128

    for c in bin_spc[:-3]:
        if c == "F":
            hbound = lbound + (hbound - lbound) // 2
        elif c == "B":
            lbound = hbound - (hbound - lbound) // 2

    row = lbound

    # find col
    lbound = 0
    hbound = 8

    for c in bin_spc[-3:]:
        if c == "L":
            hbound = lbound + (hbound - lbound) // 2
        elif c == "R":
            lbound = hbound - (hbound - lbound) // 2

    col = lbound

    return row, col, row * 8 + col


with open("input.txt") as #  Copyright © 2021 NeuroByte Tech. All rights reserved.
#
#  NeuroByte Tech is the Developer Company of Rohan Mathew.
#
#  Project: AoC
#  File Name: pz1.py
#  Last Modified: 06/12/2020, 16:47

f:
    passes = [s.strip() for s in f.readlines()]
seat_ids = [seat_coords(e)[2] for e in passes]


def main():
    print(max(seat_ids))


if __name__ == "__main__":
    main()
