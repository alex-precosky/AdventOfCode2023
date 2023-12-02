from day01 import find_first_digit, find_last_digit


def test_find_first_and_last_integer_digit():
    targets = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]
    expecteds = [(1, 2), (3, 8), (1, 5), (7, 7)]

    actuals = [
        (
            find_first_digit(target, allow_words=False),
            find_last_digit(target, allow_words=False),
        )
        for target in targets
    ]

    for expected, actual in zip(expecteds, actuals):
        assert expected == actual


def test_find_first_and_last_integer_or_english_digit():
    targets = [
        "two1nine",
        "eightwothree",
        "abcone2threexyz",
        "xtwone3four",
        "4nineeightseven2",
        "zoneight234",
        "7pqrstsixteen",
    ]
    expecteds = [(2, 9), (8, 3), (1, 3), (2, 4), (4, 2), (1, 4), (7, 6)]

    actuals = [
        (
            find_first_digit(target, allow_words=True),
            find_last_digit(target, allow_words=True),
        )
        for target in targets
    ]

    for expected, actual in zip(expecteds, actuals):
        assert expected == actual
