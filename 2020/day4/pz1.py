with open("input.txt") as f:
    raw_pports = "".join(f.readlines()).strip().split("\n\n")


def main():
    rq_k = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    valid_count = 0

    for p in raw_pports:
        if all([k in p for k in rq_k]):
            valid_count += 1

    print(valid_count)


if __name__ == "__main__":
    main()
