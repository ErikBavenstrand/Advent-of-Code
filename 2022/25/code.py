# Advent of Code 2022 Day 25
# Author: Erik Båvenstrand
# URL: https://adventofcode.com/2022/day/25

from typing import Union

SNAFU_TO_NUM = {"2": 2, "1": 1, "0": 0, "-": -1, "=": -2}
NUM_TO_SNAFU = {2: "2", 1: "1", 0: "0", 4: "-", 3: "=", 5: "0"}


def part_a(data: list[str]) -> Union[int, str, None]:
    """Solution to part A.

    Args:
        data (list[str]): Advent of Code challenge input.

    Returns:
        Union[int, str, None]: Solution to the challenge.
    """
    sum_fuel = 0
    s, c = [], 0
    for snafu in data:
        for i, digit in enumerate(snafu):
            sum_fuel += SNAFU_TO_NUM[digit] * (5 ** (len(snafu) - 1 - i))
    while sum_fuel > 0:
        x = sum_fuel % 5 + c
        s.append(NUM_TO_SNAFU[x])
        c = 1 if x > 2 else 0
        sum_fuel //= 5
    return "".join(reversed(s))


def part_b(data: list[str]) -> Union[int, str, None]:
    """Solution to part B.

    Args:
        data (list[str]): Advent of Code challenge input.

    Returns:
        Union[int, str, None]: Solution to the challenge.
    """
    return None
