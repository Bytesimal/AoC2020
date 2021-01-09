#  Copyright © 2021 NeuroByte Tech. All rights reserved.
#
#  NeuroByte Tech is the Developer Company of Rohan Mathew.
#
#  Project: AoC
#  File Name: pz1.py
#  Last Modified: 06/12/2020, 14:10

class Pwd:
    def __init__(self, s):
        spl = s.split()
        self.pwd = spl[2]
        rge = spl[0].split("-")
        self.pos1 = int(rge[0]) - 1
        self.pos2 = int(rge[1]) - 1
        self.char = spl[1][:-1]

    def is_valid1(self):
        return self.pos1 <= self.pwd.count(self.char) <= self.pos2

    def is_valid2(self):
        # Use XOR logic "one but not the other"
        return (self.pwd[self.pos1] == self.char) ^ (self.pwd[self.pos2] == self.char)


def main():
    pwds = []
    with open("input.txt") as f:
        line = f.readline()
        while line != "":
            pwds.append(Pwd(line))
            line = f.readline()

    pwds = [p.is_valid1() for p in pwds]
    print(sum(pwds))


if __name__ == "__main__":
    main()
