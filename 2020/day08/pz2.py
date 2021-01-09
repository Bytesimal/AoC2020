#  Copyright © 2021 NeuroByte Tech. All rights reserved.
#
#  NeuroByte Tech is the Developer Company of Rohan Mathew.
#
#  Project: AoC
#  File Name: pz2.py
#  Last Modified: 16/12/2020, 21:26

from pz1 import *

for i in instrs:
    # Change command
    orig_cmd = ""
    if i.cmd == "jmp":
        i.cmd = "nop"
        orig_cmd = "jmp"
    elif i.cmd == "nop":
        i.cmd = "jmp"
        orig_cmd = "nop"
    else:
        continue

    # Check if still looping
    il, acc = is_looping()
    i.cmd = orig_cmd
    if not il:
        print(acc)
        break
