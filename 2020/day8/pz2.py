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
