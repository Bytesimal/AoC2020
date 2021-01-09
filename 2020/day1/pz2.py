from pz1 import *


def main():
    for ln in ns:
        found = False
        nn = 2020 - ln
        for sn in ns:
            if nn - sn in ns:
                print(ln * sn * (nn - sn))
                found = True
                break

        if found:
            break


if __name__ == "__main__":
    main()
