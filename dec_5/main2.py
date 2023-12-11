from pathlib import Path
from dataclasses import dataclass


@dataclass
class MapRange:
    dest_range_start: int
    src_range_start: int
    range_len: int


@dataclass
class Map:
    ranges: [MapRange]

    def __post_init__(self):
        # important: these are sorted in desc by dest range start, so we can interate through these in a meaningful way
        self.ranges.sort(reverse = True, key=lambda r: r.dest_range_start)

    def get_src(self, dest):
        """Given a destination number, return the source based on the ranges in this map"""

        relevant_range = None
        for r in self.ranges:
            if r.dest_range_start <= dest:
                relevant_range = r
                break

        if not relevant_range:
            # dest == src
            return dest

        distance =  dest - relevant_range.dest_range_start
        if distance > relevant_range.range_len:
            # dest == src
            return dest

        return relevant_range.src_range_start + distance


@dataclass
class SeedRange:
    start: int
    range_len: int

    def contains(self, seed):
        return self.start <= seed <= (self.start + self.range_len)

def parse_map(map_lines):
    ranges = []
    for line in map_lines:
        range_values = [int(n) for n in line.split(" ")]
        ranges.append(MapRange(
            dest_range_start=range_values[0],
            src_range_start=range_values[1],
            range_len=range_values[2]))

    return Map(ranges=ranges)


def parse_file(file_as_str):
    maps = []

    lines = file_as_str.split('\n')

    seed_line = lines[0]
    seeds = [int(n) for n in seed_line.split(": ")[1].split(" ")]

    seed_ranges = []
    i = 0
    while i < len(seeds):
        seed_ranges.append(SeedRange(start=seeds[i], range_len=seeds[i+1]))
        i += 2

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

    return seed_ranges, maps


def solve():
    file_as_str = ""
    with open(Path("input.txt")) as input_file:
        for line in input_file:
            file_as_str += line

    seed_ranges, maps = parse_file(file_as_str)

    # start with candidate = 0
    # go through the maps backwards, to get from location to seed
    # if result is within seed range, candidate is the lowest for that seed, so we can return

    location_candidate = 0

    # We know this will eventually succeed
    while True:
        current_number = location_candidate
        # consider the maps backwards
        for map in reversed(maps):
            current_number = map.get_src(current_number)

        if not any([seed_range.contains(current_number) for seed_range in seed_ranges]):
            location_candidate += 1
            if location_candidate % 1000000 == 0:
                print(location_candidate)

            continue

        # we know this is the lowest location that's within the seed range, so we can break
        return location_candidate


if __name__ == "__main__":
    print(solve())
