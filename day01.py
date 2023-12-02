# Advent of Code 2023!
# https://adventofcode.com/2023/day/1
from typing import Optional

number_words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


def find_first_number_word_positions(input_str: str):
    """Given a string, find the index each English word digit one-nine appears in that string

    :return: A list of length 10. Position i-1 is the position in the string that digit appers.
             An example explains it better. For string "abonecdtwohijoneklmtwo"
             this returns [2, 7, -1, -1, -1, -1, -1, -1, -1]
    """
    number_word_positions = [
        input_str.find(number_word) for number_word in number_words
    ]

    return number_word_positions


def find_last_number_word_positions(input_str: str):
    """Given a string, find the index each English word digit one-nine appears in that string

    :return: A list of length 10. Position i-1 is the position in the string that digit appers.
             An example explains it better. For string "abonecdtwohijoneklmtwo"
             this returns [13, 19, -1, -1, -1, -1, -1, -1, -1]
    """
    number_word_positions = [
        input_str.rfind(number_word) for number_word in number_words
    ]

    return number_word_positions


def find_first_digit(input_str: str, allow_words: bool) -> Optional[int]:
    """Given a string, find the first digit, or English word for a digit. 1, 2, one, two, etc. None if none found"""
    number_word_positions = find_last_number_word_positions(input_str)

    for i, ch in enumerate(input_str):
        if ch.isdigit():
            return int(ch)
        elif allow_words and (i in number_word_positions):
            # number_word_positions looks for example like [3, 12, -1, -1, -1, -1, -1, -1, -1, -1]
            # 3 at index 0 means that char 3 in input_str is the start of the word "one"
            return (
                number_word_positions.index(i) + 1
            )  # +1 because 'number_word_positions[0]' is where the word 'one' appears in the input

    return None


def find_last_digit(input_str: str, allow_words: bool) -> Optional[int]:
    """Given a string, find the final digit, or English word for a digit. 1, 2, one, two, etc. None if none found"""

    right_number_word_positions = [
        input_str.rfind(number_word) for number_word in number_words
    ]

    for i in range(len(input_str) - 1, -1, -1):  # Iterate backwards through input_str
        ch = input_str[i]

        if ch.isdigit():
            return int(ch)
        elif allow_words and (i in right_number_word_positions):
            # number_word_positions looks for example like [3, 12, -1, -1, -1, -1, -1, -1, -1, -1]
            # 3 at index 0 means that char 3 in input_str is the start of the word "one"
            return (
                right_number_word_positions.index(i) + 1
            )  # +1 because 'number_word_positions[0]' is where the word 'one' appears in the input


def calc_calibration_value(input_str: str, allow_words: bool) -> int:
    """Convert an input strings into a calibration value.

    Calibration values are two digits. The first digit in the string is the
    first digit in the calibration value, and the last digit in the string is
    the second digit in the calibration value

    Digits might be integers, or the english word for the digit

    Return the calibration value, or 0 if there isn't one"""

    first_digit = find_first_digit(input_str, allow_words)
    last_digit = find_last_digit(input_str, allow_words)

    if first_digit is not None and last_digit is not None:
        return first_digit * 10 + last_digit
    else:
        return 0


if __name__ == "__main__":
    with open("input/day01.txt") as f:
        input_lines = [line.strip() for line in f.readlines()]

    # Part 1 - Digits in the input can only be integers
    calibration_values = [
        calc_calibration_value(input_line, allow_words=False)
        for input_line in input_lines
    ]
    print(f"Part 1: {sum(calibration_values)}")

    # Part 2 - Digits in the input can only be integers or english words for integers
    calibration_values = [
        calc_calibration_value(input_line, allow_words=True)
        for input_line in input_lines
    ]
    print(f"Part 2: {sum(calibration_values)}")
