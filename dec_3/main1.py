from pathlib import Path
from dataclasses import dataclass


class PotentialPartNumber:
    def __init__(self, start_idx, char) -> None:
        self.start_idx = start_idx
        self.chars = [char]

    def add_char(self, char):
        self.chars.append(char)

    def set_final_idx(self, final_idx):
        self.final_idx = final_idx

    def is_part_number(self):
        pass


def calc_sum():
    total = 0

    engine_map = []

    with open(Path("input.txt")) as input_file:
        for line in input_file:
            clean = line.strip("\n")
            engine_map.append(clean)

    for line_idx, line in enumerate(engine_map):
        current_part_number = None
        for idx, char in enumerate(line):
            if char == ".":

                if current_part_number:
                    # we need to potentially bank
                    current_part_number.set_final_idx(idx - 1)
                    if current_part_number.is_part_number():

                    pass

                # reset
                current_part_number = None
                continue

            if char.isdigit():
                if not current_part_number:
                    current_part_number = PotentialPartNumber(line_idx, idx, char)
                else:
                    current_part_number.add_char(char)

    return total


if __name__ == "__main__":
    print(calc_sum())
