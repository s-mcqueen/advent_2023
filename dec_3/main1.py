from pathlib import Path
from dataclasses import dataclass


class CandidatePartNumber:
    def __init__(self, y, start_x, char) -> None:
        self.y = y
        self.start_x = start_x
        self.chars = [char]

    def add_char(self, char):
        self.chars.append(char)

    def set_final_idx(self, end_x):
        self.end_x = end_x

    def as_numeral(self):
        return int("".join(self.chars))


def is_part_number(candidate, engine_map):

    coords_to_check = []
    for y in range(candidate.y - 1, candidate.y + 2):
        if y < 0 or y > len(engine_map) + 1:
            continue

        for x in range(candidate.start_x - 1, candidate.end_x + 2):
            if x < 0 or x > len(engine_map[0]) - 1:
                continue

            coords_to_check.append((y, x))

    print(coords_to_check)

    for coord in coords_to_check:
        value = engine_map[coord[0]][coord[1]]
        if value == ".":
            continue
        if value.isdigit():
            continue

        return True

    return False


def calc_sum():
    engine_map = []
    candidate_part_numbers = []

    # build map
    with open(Path("input.txt")) as input_file:
        for line in input_file:
            clean = line.strip("\n")
            engine_map.append(clean)

    # build candidate part numbers
    for line_idx, line in enumerate(engine_map):
        current_part_number = None
        for idx, char in enumerate(line):

            if char == ".":
                if current_part_number:
                    # bank
                    current_part_number.set_final_idx(idx - 1)
                    candidate_part_numbers.append(current_part_number)

                # reset
                current_part_number = None
                continue

            if char.isdigit():
                if current_part_number:
                    current_part_number.add_char(char)
                else:
                    current_part_number = CandidatePartNumber(line_idx, idx, char)

                if idx == len(line) - 1:
                    # bank
                    current_part_number.set_final_idx(idx)
                    candidate_part_numbers.append(current_part_number)

    # evaluate candidates and return sum
    part_numbers = [c for c in candidate_part_numbers if is_part_number(c, engine_map)]
    return sum([pn.as_numeral() for pn in part_numbers])


if __name__ == "__main__":
    print(calc_sum())
