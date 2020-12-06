with open("input.txt") as f:
    groups = [g.split() for g in "".join(f.readlines()).split("\n\n")]


def main():
    tot = 0

    for g in groups:
        opt = set([])

        for rsp in g:
            for c in rsp:
                opt.add(c)

        tot += len(opt)

    print(tot)


if __name__ == "__main__":
    main()
