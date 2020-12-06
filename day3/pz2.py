from pz1 import *


def main():
    vectors = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2)
    ]

    prod = 1
    for v in vectors:
        prod *= traverse(environment, *v)
    print(prod)


if __name__ == "__main__":
    main()
