from pathlib import Path
import re


def ways_to_win(race_len, race_record):
    outcomes_that_win = 0
    for hold_time in range(1, race_len):
        # speed = hold_time, remaining_time = race_len - hold_time, distance = speed * remaining_time
        distance = hold_time * (race_len - hold_time)
        if distance > race_record:
            outcomes_that_win += 1

    return outcomes_that_win


def parse_file(file_as_str):
    time_line, distance_line = file_as_str.split('\n')
    times = [int(n) for n in re.findall("[0-9]+", time_line.split(":")[1])]
    distances = [int(n) for n in re.findall("[0-9]+", distance_line.split(":")[1])]

    return list(zip(times, distances))


def solve():
    file_as_str = ""
    with open(Path("input.txt")) as input_file:
        for line in input_file:
            file_as_str += line

    races = parse_file(file_as_str)

    result = 1
    for (race_len, race_record) in races:
        result *= ways_to_win(race_len, race_record)

    return result


if __name__ == "__main__":
    print(solve())
