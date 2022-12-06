# Advent of Code 2022 Day 06
# Author: Erik Båvenstrand
# URL: https://adventofcode.com/2022/day/6

from typing import Union


def part_a(data: list[str]) -> Union[int, str, None]:
    """Solution to part A.

    Args:
        data (list[str]): Advent of Code challenge input.

    Returns:
        Union[int, str, None]: Solution to the challenge.
    """
    stream = data[0]
    for i in range(len(stream)):
        if len(set(stream[i : i + 4])) == 4:
            return 4 + i


def part_b(data: list[str]) -> Union[int, str, None]:
    """Solution to part B.

    Args:
        data (list[str]): Advent of Code challenge input.

    Returns:
        Union[int, str, None]: Solution to the challenge.
    """
    stream = data[0]
    for i in range(len(stream)):
        if len(set(stream[i : i + 14])) == 14:
            return 14 + i
