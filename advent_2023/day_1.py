import os

script_dir = os.path.dirname(__file__)

##### PART I #####


def find_first_digit(line):
    for i in line.strip():
        if i.isdigit():
            return i
    return 0


def find_last_digit(line):
    for i in line.strip()[::-1]:
        if i.isdigit():
            return i
    return 0


def find_sum(line):
    return int(find_first_digit(line) + find_last_digit(line))


def load_data():
    arr = []
    with open(os.path.join(script_dir, "data/day_1.txt"), encoding="utf-8") as f:
        arr = f.readlines()
    arr = [x.lower() for x in arr]
    return arr


def add_lines(arr):
    total = 0
    for line in arr:
        total += find_sum(line)

    return total


def part_1():
    lines = load_data()
    return add_lines(lines)


##### PART II #####

# My Part II doesn't actually provide the correct answer, despite all of the tests passing.
# The calibration data provided on the AoC website matches up with the tests I wrote,
# and I was unable to find any scenario in which these methods did not behave as expected.

digit_strings = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


def find_first_digit_as_string_index(line):
    # Find if the line has an entry in the digit_strings list
    digit_index = len(line)
    digit_str = ""
    for digit in digit_strings:
        if digit in line:
            if line.find(digit) < digit_index:
                digit_index = line.find(digit)
                digit_str = digit
    return [digit_str, digit_index]


def find_last_digit_as_string_index(line):
    # Find if the line has an entry in the digit_strings list
    digit_index = 0
    digit_str = ""
    for digit in digit_strings:
        if digit in line:
            if line.find(digit) > digit_index:
                digit_index = line.find(digit)
                digit_str = digit
    return [digit_str, digit_index]


def find_first_digit_as_int_index(line):
    # Find if the line has an entry in the digit_strings list
    digit_index = len(line)
    digit_str = ""
    for digit in range(1, 10):
        if str(digit) in line:
            if line.find(str(digit)) < digit_index:
                digit_index = line.find(str(digit))
                digit_str = str(digit)
    return [digit_str, digit_index]


def find_last_digit_as_int_index(line):
    # Find if the line has an entry in the digit_strings list
    digit_index = 0
    digit_str = ""
    for digit in range(1, 10):
        if str(digit) in line:
            if line.find(str(digit)) > digit_index:
                digit_index = line.find(str(digit))
                digit_str = str(digit)
    return [digit_str, digit_index]


def find_first_digit_with_strings_included(line):
    first_string_number = find_first_digit_as_string_index(line)
    first_int_number = find_first_digit_as_int_index(line)

    first_number_as_string = ""

    if first_string_number[1] < first_int_number[1]:
        first_number_as_string = str(digit_strings.index(first_string_number[0]) + 1)
    else:
        first_number_as_string = first_int_number[0]

    return first_number_as_string


def find_last_digit_with_strings_included(line):
    last_string_number = find_last_digit_as_string_index(line)
    last_int_number = find_last_digit_as_int_index(line)

    last_number_as_string = ""

    if last_string_number[1] > last_int_number[1]:
        last_number_as_string = str(digit_strings.index(last_string_number[0]) + 1)
    else:
        last_number_as_string = last_int_number[0]

    return last_number_as_string


def find_sum_with_strings_included(line):
    return int(
        find_first_digit_with_strings_included(line)
        + find_last_digit_with_strings_included(line)
    )


def add_lines_with_strings_included(arr):
    total = 0
    for line in arr:
        total += find_sum_with_strings_included(line)

    return total


def part_2():
    lines = load_data()
    return add_lines_with_strings_included(lines)
