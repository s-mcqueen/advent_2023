from pathlib import Path

digits_in_english = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


# off by 7! why???


def calc_sum():
    total = 0

    with open(Path("input.txt")) as input_file:
        for line in input_file:
            clean = line.strip("\n")

            indicies_to_digits = {}

            potential_digit_strs = []
            for i, char in enumerate(clean):
                if char.isdigit():
                    # bank and reset
                    potential_digit_strs = []
                    indicies_to_digits[i] = int(char)
                    continue

                potential_digit_strs = [(ds + char) for ds in potential_digit_strs]
                potential_digit_strs.append(char)

                for digit_str in potential_digit_strs:
                    try:
                        digit = digits_in_english[digit_str]
                    except KeyError:
                        pass
                    else:
                        # bank and reset -- its okay that we are using `i` here even
                        # though it is the *end* of the digit string, it is still strictly before
                        # the next possible digit and that's the only thing we care about
                        potential_digit_strs = []
                        indicies_to_digits[i] = digit

            first_digit = indicies_to_digits[min(indicies_to_digits.keys())]
            last_digit = indicies_to_digits[max(indicies_to_digits.keys())]

            total += int(f"{first_digit}{last_digit}")

    return total


if __name__ == "__main__":
    print(calc_sum())
