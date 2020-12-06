class Pwd:
    def __init__(self, s):
        spl = s.split()
        self.pwd = spl[2]
        rge = spl[0].split("-")
        self.pos1 = int(rge[0]) - 1
        self.pos2 = int(rge[1]) - 1
        self.char = spl[1][:-1]

    def is_valid(self):
        # Use XOR logic "one but not the other"
        return (self.pwd[self.pos1] == self.char) ^ (self.pwd[self.pos2] == self.char)


pwds = []
with open("day2/input.txt") as f:
    line = f.readline()
    while line != "":
        pwds.append(Pwd(line))
        line = f.readline()

pwds = [p.is_valid() for p in pwds]
print(sum(pwds))
