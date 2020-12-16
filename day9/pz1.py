with open("input.txt") as f:
    ns = [int(e) for e in f.readlines()]

preamble = 25


def invalid():
    for i, n in enumerate(ns):
        if i < preamble:
            continue

        is_in = False
        for comp_n in ns[i - preamble: i]:
            if n - comp_n in ns[i - preamble: i]:
                is_in = True
                break

        if not is_in:
            return n


def main():
    print(invalid())


if __name__ == "__main__":
    main()
