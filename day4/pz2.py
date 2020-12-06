from pz1 import *

valid_ecls = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


class Passport:
    def __init__(self, string):
        self.fields = {}
        for kv in string.split():
            k, v = kv.split(":")
            self.fields[k] = v

        # type conv
        for k in self.fields:
            if "yr" in k:
                try:
                    self.fields[k] = int(self.fields[k])
                except ValueError:
                    self.fields[k] = 0
            elif k == "hgt":
                try:
                    self.fields[k] = (int(self.fields[k][:-2]), self.fields[k][-2:])
                except ValueError:
                    self.fields[k] = (0, "")

    def is_valid(self):
        bools = []
        try:
            bools.append(1920 <= self.fields["byr"] <= 2002)
            bools.append(2010 <= self.fields["iyr"] <= 2020)
            bools.append(2020 <= self.fields["eyr"] <= 2030)
            bools.append(self.fields["hgt"][1] in ["cm", "in"])
            if self.fields["hgt"][1] == "cm":
                bools.append(150 <= self.fields["hgt"][0] <= 193)
            elif self.fields["hgt"][1] == "in":
                bools.append(59 <= self.fields["hgt"][0] <= 76)
            bools.append(self.fields["hcl"][0] == "#")
            bools.append(len(self.fields["hcl"]) == 7)
            _ = int("0x" + self.fields["hcl"][1:], 0)
            bools.append(self.fields["ecl"] in valid_ecls)
            bools.append(len(self.fields["pid"]) == 9)
            _ = int(self.fields["pid"])
        except:
            bools.append(False)

        return all(bools)


def main():
    passports = []
    for rp in raw_pports:
        passports.append(Passport(rp))
    print(sum([p.is_valid() for p in passports]))


if __name__ == "__main__":
    main()
