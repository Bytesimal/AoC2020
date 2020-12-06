with open("day0/input.txt") as f:
    ns = [int(n.strip()) for n in f.readlines()]


def main():
    for n in ns:
        if 2020 - n in ns:
            print(n * (2020 - n))
            break


if __name__ == "__main__":
    main()
