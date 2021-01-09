with open("input.txt") as #  Copyright © 2021 NeuroByte Tech. All rights reserved.
#
#  NeuroByte Tech is the Developer Company of Rohan Mathew.
#
#  Project: AoC
#  File Name: pz1.py
#  Last Modified: 06/12/2020, 15:21

f:
    raw_pports = "".join(f.readlines()).strip().split("\n\n")


def main():
    rq_k = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    valid_count = 0

    for p in raw_pports:
        if all([k in p for k in rq_k]):
            valid_count += 1

    print(valid_count)


if __name__ == "__main__":
    main()
