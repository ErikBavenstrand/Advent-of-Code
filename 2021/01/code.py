# Advent of Code 2021 Day 01
# Author: Erik Båvenstrand
# URL: https://adventofcode.com/2021/day/1

from typing import Union


def part_a(data: list[str]) -> Union[int, str, None]:
    """Solution to part A.

    Args:
        data (list[str]): Advent of Code challenge input.

    Returns:
        Union[int, str, None]: Solution to the challenge.
    """
    count = 0
    for i in range(len(data)):
        if i >= 1 and int(data[i]) > int(data[i - 1]):
            count += 1
    return count


def part_b(data: list[str]) -> Union[int, str, None]:
    """Solution to part B.

    Args:
        data (list[str]): Advent of Code challenge input.

    Returns:
        Union[int, str, None]: Solution to the challenge.
    """
    counter = 0
    for i in range(len(data)):
        if i >= 3 and int(data[i]) > int(data[i - 3]):
            counter += 1
    return counter
