from pathlib import Path
from dataclasses import dataclass


@dataclass
class Card:
    winning_numbers: [int]
    numbers: [int]

    def get_value(self):
        points = 0
        for n in self.numbers:
            if n in self.winning_numbers:
                if not points:
                    points = 1
                    continue

                points *= 2

        return points


def parse_numbers(num_str):
    """Returns a list of numbers from a string of numbers"""

    numbers = []

    number_sections = num_str.split(" ")
    for n_s in number_sections:
        if n_s == "":
            continue
        numbers.append(int(n_s))

    return numbers


def parse_card(line):
    """Returns a card from a line"""

    winning_numbers_raw, numbers_raw = line.split(":")[1].split("|")

    winning_numbers = parse_numbers(winning_numbers_raw)
    numbers = parse_numbers(numbers_raw)

    return Card(winning_numbers=winning_numbers, numbers=numbers)


def solve():
    total = 0

    with open(Path("input.txt")) as input_file:
        for line in input_file:
            card = parse_card(line.strip("\n"))
            total += card.get_value()

    return total


if __name__ == "__main__":
    print(solve())
