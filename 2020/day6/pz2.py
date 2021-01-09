from pz1 import *


def main():
    tot = 0

    for g in groups:
        opt = {}

        for rsp in g:
            for c in rsp:
                if c in opt:
                    opt[c] += 1
                    continue
                opt[c] = 1

        for c in opt:
            if opt[c] == len(g):
                tot += 1

    print(tot)


if __name__ == "__main__":
    main()
