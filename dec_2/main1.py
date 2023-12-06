from pathlib import Path
from dataclasses import dataclass

RED_CUBES = 12
GREEN_CUBES = 13
BLUE_CUBES = 14


@dataclass
class Game:
    id: int
    blues: int = 0
    greens: int = 0
    reds: int = 0

    def add_turn(self, blues, reds, greens):
        if blues > self.blues:
            self.blues = blues
        if reds > self.reds:
            self.reds = reds
        if greens > self.greens:
            self.greens = greens

    def is_possible(self):
        return (
            self.greens <= GREEN_CUBES
            and self.reds <= RED_CUBES
            and self.blues <= BLUE_CUBES
        )


def parse_game_line(line):
    line = line[5:]

    parts = line.split(": ")

    game = Game(id=int(parts[0]))

    rest = parts[1]
    turn_lines = rest.split(";")
    for turn in turn_lines:
        blues = 0
        reds = 0
        greens = 0

        color_amounts = turn.split(",")
        for color_amount in color_amounts:
            color_amount = color_amount.strip(" ")
            if "blue" in color_amount:
                blues = int(color_amount.strip("blues").strip(" "))

            if "red" in color_amount:
                reds = int(color_amount.strip("reds").strip(" "))

            if "green" in color_amount:
                greens = int(color_amount.strip("green").strip(" "))

            game.add_turn(blues=blues, reds=reds, greens=greens)

    return game


def calc_sum():
    total = 0

    with open(Path("input.txt")) as input_file:
        for line in input_file:
            clean = line.strip("\n")
            g = parse_game_line(clean)
            if g.is_possible():
                print(g.id)
                total += g.id

    return total


def calc_power_sum():
    total = 0

    with open(Path("input.txt")) as input_file:
        for line in input_file:
            clean = line.strip("\n")
            g = parse_game_line(clean)
            power = g.reds * g.greens * g.blues
            total += power

    return total


if __name__ == "__main__":
    print(calc_power_sum())
