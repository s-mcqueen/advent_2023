from pathlib import Path
from dataclasses import dataclass


# Pile that holds all of the cards in order
# process Card N ->
#   given M matches, then tell data-structure to note that we have +1 copy of each of the cards N+1...N+M
#   repeat for the number of copies of N


@dataclass
class Card:
    winning_numbers: [int]
    numbers: [int]
    copies: [int] = 1

    def get_matches(self):
        matches = 0
        for n in self.numbers:
            if n in self.winning_numbers:
                matches += 1

        return matches


@dataclass
class CardPile:
    cards: [Card]

    def solve(self):
        for i, card in enumerate(self.cards):
            matches = card.get_matches()

            copy = 1
            while copy <= card.copies:
                j = 1
                while j <= matches:
                    self.cards[i + j].copies += 1
                    j += 1

                copy += 1

        total = 0
        for card in self.cards:
            total += card.copies

        return total


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
    cards = []
    with open(Path("input.txt")) as input_file:
        for line in input_file:
            cards.append(parse_card(line.strip("\n")))

    pile = CardPile(cards=cards)
    return pile.solve()


if __name__ == "__main__":
    print(solve())
