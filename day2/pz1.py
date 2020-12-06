class PwdPolicy:
    def __init__(self, s):
        spl = s.split()
        self.pwd = spl[2]
        rge = spl[0].split("-")
        self.min = int(rge[0])
        self.max = int(rge[1])
        self.char = spl[1][:-1]

    def is_valid(self):
        return self.min <= self.pwd.count(self.char) <= self.max


pwds = []
with open("day2/input.txt") as f:
    line = f.readline()
    while line != "":
        pwds.append(PwdPolicy(line))
        line = f.readline()

pwds = [p.is_valid() for p in pwds]
print(sum(pwds))
