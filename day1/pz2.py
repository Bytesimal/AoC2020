from pz1 import *


def main():
    pwds = []
    with open("day1/input.txt") as f:
        line = f.readline()
        while line != "":
            pwds.append(Pwd(line))
            line = f.readline()

    pwds = [p.is_valid2() for p in pwds]
    print(sum(pwds))


if __name__ == "__main__":
    main()
