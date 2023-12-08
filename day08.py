# Advent of Code 2023!
# https://adventofcode.com/2023/day/8
import re
from dataclasses import dataclass
from enum import auto, Enum
from math import lcm
from typing import Dict, List


class Direction(Enum):
    LEFT = auto()
    RIGHT = auto()


@dataclass
class Node:
    name: str
    left: str
    right: str


def scan_directions_from_input(input_lines: List[str]) -> List[Direction]:
    directions_list: List[Direction] = []

    directions_str = input_lines[0]
    for ch in directions_str:
        if ch == "L":
            directions_list.append(Direction.LEFT)
        elif ch == "R":
            directions_list.append(Direction.RIGHT)

    return directions_list


def scan_graph_from_input(input_lines: List[str]) -> Dict[str, Node]:
    node_lines = input_lines[2:]

    graph_dict: Dict[str, Node] = {}

    for node_line in node_lines:
        # Each node line looks like:
        # AAA = (BBB, CCC)
        mx = re.search(r"(\w+) = \((\w+), (\w+)\)", node_line)

        node_name = mx.group(1)
        left_node_name = mx.group(2)
        right_node_name = mx.group(3)

        graph_dict[node_name] = Node(node_name, left_node_name, right_node_name)

    return graph_dict


def count_steps_from_aaa_to_zzz(
    directions: List[Direction], graph_dict: Dict[str, Node]
) -> int:
    """Traverse the graph from node AAA to node ZZZ, following the directions"""
    num_steps = 0
    direction_i = 0

    cur_node = "AAA"
    while cur_node != "ZZZ":
        direction = directions[direction_i]

        if direction == Direction.LEFT:
            cur_node = graph_dict[cur_node].left
        elif direction == Direction.RIGHT:
            cur_node = graph_dict[cur_node].right
        else:
            print(f"Invalid direction: {direction}")
            exit(1)

        num_steps += 1
        direction_i = (direction_i + 1) % len(directions)

    return num_steps


def find_nodes_ending_in_letter(graph_dict: Dict[str, Node], letter: str):
    return_list: List[str] = []

    for node_name in graph_dict.keys():
        if node_name[-1] == letter:
            return_list.append(node_name)

    return return_list


def count_steps_for_ghosts(
    directions: List[Direction], graph_dict: Dict[str, Node]
) -> int:
    """For part 2

    Ghosts move in lock step, following the same directions, but each starting
    on the nodes that end in A, headed to nodes that end in Z

    After a bit of experimentation, we see each ghost has a fixed period which
    it traverses from its start node to its last node. So, we just have to find
    the LCM of all of these fixed graph traversal periods
    """

    cur_nodes: List[str] = find_nodes_ending_in_letter(graph_dict, "A")
    node_repetition_periods = [0] * len(cur_nodes)
    direction_i = 0
    num_steps = 0

    while 0 in node_repetition_periods:
        direction = directions[direction_i]

        for node_i in range(len(cur_nodes)):
            cur_node = cur_nodes[node_i]

            if direction == Direction.LEFT:
                cur_nodes[node_i] = graph_dict[cur_node].left
            elif direction == Direction.RIGHT:
                cur_nodes[node_i] = graph_dict[cur_node].right
            else:
                print(f"Invalid direction: {direction}")
                exit(1)

            if cur_node[-1] == "Z":
                node_repetition_periods[node_i] = num_steps

        direction_i = (direction_i + 1) % len(directions)
        num_steps += 1

    lcm_of_repetitions = lcm(*node_repetition_periods)
    return lcm_of_repetitions


if __name__ == "__main__":
    input_lines = [line.strip() for line in open("input/day08.txt").readlines()]
    directions = scan_directions_from_input(input_lines)

    graph_dict = scan_graph_from_input(input_lines)

    part1 = count_steps_from_aaa_to_zzz(directions, graph_dict)
    print(f"Part 1: {part1}")

    part2 = count_steps_for_ghosts(directions, graph_dict)
    print(f"Part 2: {part2}")
