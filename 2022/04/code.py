# Advent of Code 2022 Day 04
# Author: Erik Båvenstrand
# URL: https://adventofcode.com/2022/day/4

from typing import Union


def part_a(data: list[str]) -> Union[int, str, None]:
    """Solution to part A.

    Args:
        data (list[str]): Advent of Code challenge input.

    Returns:
        Union[int, str, None]: Solution to the challenge.
    """
    n_full_overlaps = 0
    for ranges in data:
        [start_1, end_1], [start_2, end_2] = [
            [int(pos) for pos in range_x.split("-")] for range_x in ranges.split(",")
        ]
        if (start_1 <= start_2 and end_1 >= end_2) or (
            start_2 <= start_1 and end_2 >= end_1
        ):
            n_full_overlaps += 1
    return n_full_overlaps


def part_b(data: list[str]) -> Union[int, str, None]:
    """Solution to part B.

    Args:
        data (list[str]): Advent of Code challenge input.

    Returns:
        Union[int, str, None]: Solution to the challenge.
    """
    n_overlaps = 0
    for ranges in data:
        [start_1, end_1], [start_2, end_2] = [
            [int(pos) for pos in range_x.split("-")] for range_x in ranges.split(",")
        ]
        if (
            (start_1 <= start_2 and end_1 >= end_2)
            or (start_2 <= start_1 and end_2 >= end_1)
            or (start_2 >= start_1 and start_2 <= end_1)
            or (start_1 >= start_2 and start_1 <= end_2)
        ):
            n_overlaps += 1
    return n_overlaps
