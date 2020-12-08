class Instr:
    def __init__(self, raw):
        self.cmd, self.val = raw.strip().split()
        self.val = int(self.val)
        self.exec_count = 0


with open("input.txt") as f:
    instrs = [Instr(ln) for ln in f.readlines()]


def looping():
    acc = 0
    cursor = 0
    while True:
        instrs[cursor].exec_count += 1
        # check if running twice
        if cursor >= len(instrs) - 100:
            # terminated
            return False, acc
        if instrs[cursor].exec_count > 1:
            return True, acc

        if instrs[cursor].cmd == "acc":
            acc += instrs[cursor].val
        elif instrs[cursor].cmd == "jmp":
            cursor += instrs[cursor].val - 1
        cursor += 1


def main():
    rs, acc = looping()
    if rs:
        print(acc)


if __name__ == "__main__":
    main()
