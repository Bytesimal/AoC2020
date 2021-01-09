from pz1 import *


def main():
    for n in range(min(seat_ids) + 8, max(seat_ids) + 2 - 8, 2):
        if n not in seat_ids:
            print(n)
            break


if __name__ == "__main__":
    main()
