from pathlib import Path
from enum import IntEnum
from itertools import groupby
import functools

CARD_RANKS = {
    'A': 1,
    'K': 2,
    'Q': 3,
    'J': 4,
    'T': 5,
    '9': 6,
    '8': 7,
    '7': 8,
    '6': 9,
    '5': 10,
    '4': 11,
    '3': 12,
    '2': 13,
}

class HandType(IntEnum):
    FIVE_OF_A_KIND = 1
    FOUR_OF_A_KIND = 2
    FULL_HOUSE = 3
    THREE_OF_A_KIND = 4
    TWO_PAIR = 5
    ONE_PAIR = 6
    HIGH_CARD = 7


class Hand:
    def __init__(self, raw_str, bid) -> None:
        self.bid = int(bid)

        self.raw_str = raw_str
        self.type = None

        groups = [list(j) for i, j in groupby(sorted(raw_str))]
        match len(groups):
            case 1:
                self.type = HandType.FIVE_OF_A_KIND
            case 2:
                if len(groups[0]) in [2, 3]:
                    self.type = HandType.FULL_HOUSE
                else:
                    self.type = HandType.FOUR_OF_A_KIND
            case 3:
                for group in groups:
                    if len(group) == 3:
                        self.type = HandType.THREE_OF_A_KIND

                if not self.type:
                    self.type = HandType.TWO_PAIR
            case 4:
                self.type = HandType.ONE_PAIR
            case 5:
                self.type = HandType.HIGH_CARD
            case _:
                raise Exception("This should not happen")


def order_hands(hand1, hand2):
    if hand1.type == hand2.type:
        for index in range(5):
            rank1 = CARD_RANKS[hand1.raw_str[index]]
            rank2 = CARD_RANKS[hand2.raw_str[index]]
            if rank1 == rank2:
                continue

            return -1 if rank1 < rank2 else 1\

        # These hands are identical
        return 0

    return -1 if hand1.type < hand2.type else 1


def parse_file(file_as_str):
    hands = []
    for line in file_as_str.split('\n'):
        hands.append(Hand(*line.split(" ")))

    return hands


def solve():
    file_as_str = ""
    with open(Path("input.txt")) as input_file:
        for line in input_file:
            file_as_str += line

    hands = parse_file(file_as_str)
    hands.sort(key=functools.cmp_to_key(order_hands))

    total = 0
    for i in range(len(hands)):
        hand = hands[i]
        rank = len(hands) - i
        total += rank * hand.bid

    return total


if __name__ == "__main__":
    print(solve())
