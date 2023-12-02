# Advent of Code 2023!
# https://adventofcode.com/2023/day/2
import re
from enum import auto, Enum
from pathlib import Path
from typing import Dict, List, Tuple


class CubeColor(Enum):
    RED = auto()
    GREEN = auto()
    BLUE = auto()


cube_color_map = {
    "red": CubeColor.RED,
    "green": CubeColor.GREEN,
    "blue": CubeColor.BLUE,
}


class Game:
    game_num: int = 0
    rounds: List[Dict[CubeColor, int]]

    def __eq__(self, other):
        return (self.game_num == other.game_num) and (self.rounds == other.rounds)


def read_game_strs(input_file: Path) -> List[str]:
    """Each line in the input file represents the result of one game. Let's read them"""
    return [line.strip() for line in open(input_file).readlines()]


def parse_die_str(die_str: str) -> Tuple[CubeColor, int]:
    """Parse a die string into a tuple.

    Example of a die string:
    3 blue
    """
    count = int(re.match(r"\d+", die_str).group(0))
    color_str = re.search("[a-z]+", die_str).group(0)
    cube_color = cube_color_map[color_str]

    return (cube_color, count)


def parse_round_str(round_str: str) -> Dict[CubeColor, int]:
    """Parse a round string into a dict.

    Example of a round string:
    3 blue, 4 red

    Should return:
    {CubeColor.BLUE: 3, CubeColor.RED: 4}
    """
    die_counts = {}

    die_strs = round_str.split(", ")
    for die_str in die_strs:
        die_count = parse_die_str(die_str)
        die_counts[die_count[0]] = die_count[1]  # [0] is cube color, [1] is cube count

    return die_counts


def parse_game_str(game_str: str) -> Game:
    """Parse a game string into a Game object

    Example of a game string:
    Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
    """
    game = Game()

    # Find the game number
    mx = re.search(r"(?<=Game )\d+", game_str)
    if mx is not None:
        game.game_num = int(mx.group(0))

    # The part of 'game_str' that has "rounds" starts 2 characters after the colon
    rounds_str = game_str[game_str.find(": ") + 2 :]

    # And each round is split by a semicolon
    round_strs = rounds_str.split("; ")

    rounds = [parse_round_str(round_str) for round_str in round_strs]
    game.rounds = rounds

    return game


def is_round_possible(
    round: Dict[CubeColor, int], available_cubes: Dict[CubeColor, int]
) -> bool:
    possible = True

    for cube_color, round_cube_count in round.items():
        if cube_color in available_cubes:
            available_cube_count = available_cubes[cube_color]
        else:
            available_cube_count = 0

        if available_cube_count < round_cube_count:
            possible = False
            break

    return possible


def is_game_possible(game: Game, available_cubes: Dict[CubeColor, int]) -> bool:
    possible = True

    for round in game.rounds:
        round_possible = is_round_possible(round, available_cubes)
        if not round_possible:
            possible = False
            break

    return possible


def calc_sum_of_possible_games(
    games: List[Game], available_cubes: Dict[CubeColor, int]
) -> int:
    total = 0

    for game in games:
        if is_game_possible(game, available_cubes):
            total += game.game_num

    return total


def calc_power_of_possible_games(games: List[Game]) -> int:

    power = 0

    for game in games:
        min_cubes = {CubeColor.RED: 0, CubeColor.GREEN: 0, CubeColor.BLUE: 0}

        for game_round in game.rounds:
            for game_cube_color, game_cube_color_count in game_round.items():
                if game_cube_color_count > min_cubes[game_cube_color]:
                    min_cubes[game_cube_color] = game_cube_color_count

        game_power = (
            min_cubes[CubeColor.RED]
            * min_cubes[CubeColor.GREEN]
            * min_cubes[CubeColor.BLUE]
        )
        power += game_power

    return power


if __name__ == "__main__":
    # we have 12 red cubes, 13 green cubes, and 14 blue cubes
    available_cubes = {CubeColor.RED: 12, CubeColor.GREEN: 13, CubeColor.BLUE: 14}

    game_strs = read_game_strs(Path("input/day02.txt"))
    games = [parse_game_str(game_str) for game_str in game_strs]

    part1 = calc_sum_of_possible_games(games, available_cubes)
    print(f"Part 1: {part1}")

    part2 = calc_power_of_possible_games(games)
    print(f"Part 2: {part2}")
