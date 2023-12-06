from pathlib import Path


def calc_sum():
    total = 0

    with open(Path("input.txt")) as input_file:
        for line in input_file:
            clean = line.strip("\n")
            first = 0
            last = len(clean) - 1

            while not clean[first].isdigit():
                first += 1

            while not clean[last].isdigit():
                last -= 1

            total += int(f"{clean[first]}{clean[last]}")

    return total


if __name__ == "__main__":
    print(calc_sum())
