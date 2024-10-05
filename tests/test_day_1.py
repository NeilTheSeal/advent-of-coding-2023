from advent_2023.day_1 import *


class TestDay1Part1:
    def test_find_first_digit(self):
        assert find_first_digit("123") == "1"
        assert find_first_digit("a123") == "1"

    def test_find_last_digit(self):
        assert find_last_digit("123") == "3"
        assert find_last_digit("123a") == "3"

    def test_find_sum(self):
        assert find_sum("123") == 13
        assert find_sum("b123a") == 13

    def test_load_data(self):
        assert len(load_data()) == 1000

    def test_add_lines(self):
        line1 = "1abc2"
        line2 = "pqr3stu8vwx"
        line3 = "a1b2c3d4e5f"
        line4 = "treb7uchet"
        assert add_lines([line1, line2, line3, line4]) == 142


class TestDay1Part2:
    def test_find_first_digit_as_string_index(self):
        assert find_first_digit_as_string_index("one two three") == ["one", 0]
        assert find_first_digit_as_string_index("two three") == ["two", 0]
        assert find_first_digit_as_string_index("1 two three") == ["two", 2]
        assert find_first_digit_as_string_index("1 2 3") == ["", 5]

    def test_find_last_digit_as_string_index(self):
        assert find_last_digit_as_string_index("one two three") == ["three", 8]
        assert find_last_digit_as_string_index("one two2") == ["two", 4]
        assert find_last_digit_as_string_index("one two 1") == ["two", 4]
        assert find_last_digit_as_string_index("1 2 3") == ["", 0]

    def test_find_first_digit_as_int_index(self):
        assert find_first_digit_as_int_index("one 0 1 two three") == ["1", 6]
        assert find_first_digit_as_int_index("one two three") == ["", 13]

    def test_find_last_digit_as_int_index(self):
        assert find_last_digit_as_int_index("one 0 1 two three") == ["1", 6]
        assert find_last_digit_as_int_index("one 0 1 two 2 three") == ["2", 12]
        assert find_last_digit_as_int_index("one two three") == ["", 0]

    def test_find_first_digit_with_strings_included(self):
        assert find_first_digit_with_strings_included("one 0 1 two three") == "1"
        assert find_first_digit_with_strings_included("2 one two three") == "2"
        assert find_first_digit_with_strings_included("two 3 four 1") == "2"
        assert find_first_digit_with_strings_included("1 2 3") == "1"

    def test_find_last_digit_with_strings_included(self):
        assert find_last_digit_with_strings_included("one 0 1 two three") == "3"
        assert find_last_digit_with_strings_included("2 one two 3") == "3"
        assert find_last_digit_with_strings_included("two 3 four 1 abc") == "1"
        assert find_last_digit_with_strings_included("1 2 threeacb") == "3"

    def test_find_sum_with_strings_included(self):
        assert find_sum_with_strings_included("one 0 1 two three") == 13
        assert find_sum_with_strings_included("2 one two three") == 23
        assert find_sum_with_strings_included("two 3 four 1") == 21
        assert find_sum_with_strings_included("1 2 3") == 13
        assert find_sum_with_strings_included("1 2 3 4 5 6 7 8") == 18
        assert (find_sum_with_strings_included("two1nine")) == 29
        assert (find_sum_with_strings_included("eightwothree")) == 83
        assert (find_sum_with_strings_included("abcone2threexyz")) == 13
        assert (find_sum_with_strings_included("xtwone3four")) == 24
        assert (find_sum_with_strings_included("4nineeightseven2")) == 42
        assert (find_sum_with_strings_included("zoneight234")) == 14
        assert (find_sum_with_strings_included("7pqrstsixteen")) == 76
        assert (find_sum_with_strings_included("eighthree")) == 83
        assert (find_sum_with_strings_included("sevenine")) == 79

    def test_add_lines_with_strings_included(self):
        line1 = "two1nine"
        line2 = "eightwothree"
        line3 = "abcone2threexyz"
        line4 = "xtwone3four"
        line5 = "4nineightseven2"
        line6 = "zoneight234"
        line7 = "7pqrstsixteen"
        assert (
            add_lines_with_strings_included(
                [line1, line2, line3, line4, line5, line6, line7]
            )
            == 281
        )
