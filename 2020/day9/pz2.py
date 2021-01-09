from pz1 import *


def get_cont_set(num, depth=2):
    if num == 0:
        return []

    for n in ns[:ns.index(num)]:
        if num - n in ns[:ns.index(num)]:
            return [n, num - n]

    # If hasnt found, repeat with increased depth
    for


def main():
    t = invalid()


if __name__ == "__main__":
    main()
