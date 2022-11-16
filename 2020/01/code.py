# Advent of Code 2020 Day 01
# Author: Erik Båvenstrand
# URL: https://adventofcode.com/2020/day/1

from typing import Union


def part_a(data: list[str]) -> Union[int, str, None]:
    """Solution to part A.

    Args:
        data (list[str]): Advent of Code challenge input.

    Returns:
        Union[int, str, None]: Solution to the challenge.
    """
    value_list = list(map(int, data))
    value_set = set(value_list)
    for x in value_list:
        if 2020 - x in value_set:
            return x * (2020 - x)


def part_b(data: list[str]) -> Union[int, str, None]:
    """Solution to part B.

    Args:
        data (list[str]): Advent of Code challenge input.

    Returns:
        Union[int, str, None]: Solution to the challenge.
    """
    value_list = list(map(int, data))
    value_set = set(value_list)
    for x in value_list:
        for y in value_list:
            if 2020 - x - y in value_set:
                return x * y * (2020 - x - y)
