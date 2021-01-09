class Instr:
    def __init__(self, raw):
        self.cmd, self.val = raw.strip().split()
        self.val = int(self.val)
        self.exec_count = 0


with open("input.txt") as f:
    instrs = [Instr(ln) for ln in f.readlines()]


def is_looping():
    acc = 0
    cur = 0
    rsp = False

    while True:
        if cur >= len(instrs):
            # terminated
            break
        instrs[cur].exec_count += 1
        if instrs[cur].exec_count > 1:
            # check if running twice
            rsp = True
            break

        if instrs[cur].cmd == "acc":
            acc += instrs[cur].val
        elif instrs[cur].cmd == "jmp":
            cur += instrs[cur].val
            continue
        cur += 1

    # Reset exec counts
    for i in instrs:
        i.exec_count = 0

    return rsp, acc


def main():
    il, acc = is_looping()
    if il:
        print(acc)


if __name__ == "__main__":
    main()
