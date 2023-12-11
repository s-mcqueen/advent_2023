from pathlib import Path
from dataclasses import dataclass


@dataclass
class Range:
    dest_range_start: int
    src_range_start: int
    range_len: int

@dataclass
class Map:
    ranges: [int]

    def __post_init__(self):
        # important: these are sorted in desc by range start, so we can interate through these in a meaningful way
        self.ranges.sort(reverse = True, key=lambda r: r.src_range_start)

    def get_dest(self, src):
        """Given a source number, return the destination based on the ranges in this map"""

        relevant_range = None
        for r in self.ranges:
            if r.src_range_start < src:
                relevant_range = r
                break

        if not relevant_range:
            # dest == src
            return src

        distance =  src - relevant_range.src_range_start
        if distance > relevant_range.range_len:
            # dest == src
            return src

        return relevant_range.dest_range_start + distance


def parse_map(map_lines):
    ranges = []
    for line in map_lines:
        range_values = [int(n) for n in line.split(" ")]
        ranges.append(Range(
            dest_range_start=range_values[0],
            src_range_start=range_values[1],
            range_len=range_values[2]))

    return Map(ranges=ranges)


def parse_file(file_as_str):
    maps = []

    lines = file_as_str.split('\n')

    seed_line = lines[0]
    seeds = [int(n) for n in seed_line.split(": ")[1].split(" ")]

    rest = lines[2:]
    current_map_lines = []
    for line in rest:
        if line == '':
            # indicates the end of a map layer, so we build the map and bank it
            maps.append(parse_map(current_map_lines))
            current_map_lines = []
            continue

        if "map" in line:
            continue

        current_map_lines.append(line)

    if current_map_lines:
        maps.append(parse_map(current_map_lines))

    return seeds, maps


def solve():
    file_as_str = ""
    with open(Path("input.txt")) as input_file:
        for line in input_file:
            file_as_str += line

    seeds, maps = parse_file(file_as_str)

    locations = []
    for seed in seeds:
        current_number = seed
        for map in maps:
            current_number = map.get_dest(current_number)

        locations.append(current_number)

    return min(locations)


if __name__ == "__main__":
    print(solve())
