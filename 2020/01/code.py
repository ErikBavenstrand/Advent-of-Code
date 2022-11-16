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
        remainder = 2020 - x
        if remainder in value_set:
            return x * remainder


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
            remainder = 2020 - x - y
            if remainder in value_set:
                return x * y * remainder
