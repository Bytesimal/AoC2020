#  Copyright © 2021 NeuroByte Tech. All rights reserved.
#
#  NeuroByte Tech is the Developer Company of Rohan Mathew.
#
#  Project: AoC
#  File Name: pz2.py
#  Last Modified: 09/01/2021, 10:37

from pz1 import *


def get_cont_set(num):
    if num == 0:
        return []

    for i in range(len(ns)):
        for j in range(i + 2, len(ns)):
            if sum(ns[i:j]) == num:
                return ns[i:j]


def main():
    sel_rg = get_cont_set(invalid())
    print(min(sel_rg) + max(sel_rg))


if __name__ == "__main__":
    main()
