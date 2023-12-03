from day02 import CubeColor, Game, parse_game_str, parse_round_str


def test_parse_game_1():
    target = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"

    expected = Game()
    expected.game_num = 1
    expected.rounds = [
        {CubeColor.BLUE: 3, CubeColor.RED: 4},
        {CubeColor.RED: 1, CubeColor.GREEN: 2, CubeColor.BLUE: 6},
        {CubeColor.GREEN: 2},
    ]

    actual = parse_game_str(target)
    assert expected == actual


def test_parse_round_1():
    target = "3 blue, 4 red"

    expected = {CubeColor.BLUE: 3, CubeColor.RED: 4}
    actual = parse_round_str(target)

    assert expected == actual
