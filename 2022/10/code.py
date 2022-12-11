# Advent of Code 2022 Day 10
# Author: Erik Båvenstrand
# URL: https://adventofcode.com/2022/day/10

from typing import Union

from adventlib.utils.list import chunk_list


def part_a(data: list[str]) -> Union[int, str, None]:
    """Solution to part A.

    Args:
        data (list[str]): Advent of Code challenge input.

    Returns:
        Union[int, str, None]: Solution to the challenge.
    """
    x = 1
    cycle = 0
    sum_of_values = 0
    for instr in data:
        timeout = 0
        addition = 0
        match instr.split(" "):
            case ["noop"]:
                timeout = 1
            case "addx", val:
                timeout = 2
                addition = int(val)

        for _ in range(timeout):
            cycle += 1
            if cycle % 20 == 0 and cycle % 40 != 0:
                sum_of_values += x * cycle
        x += addition
    return sum_of_values


def part_b(data: list[str]) -> Union[int, str, None]:
    """Solution to part B.

    Args:
        data (list[str]): Advent of Code challenge input.

    Returns:
        Union[int, str, None]: Solution to the challenge.
    """
    x = 1
    cycle = 0
    screen = ["."] * 40 * 6
    for instr in data:
        timeout = 0
        addition = 0
        match instr.split(" "):
            case ["noop"]:
                timeout = 1
            case "addx", val:
                timeout = 2
                addition = int(val)

        for _ in range(timeout):
            screen[cycle] = "#" if cycle % 40 in [x - 1, x, x + 1] else "."
            cycle += 1
        x += addition
    return "\n" + "\n".join(["".join(row) for row in chunk_list(screen, 40)])
