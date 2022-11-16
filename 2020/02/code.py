# Advent of Code 2020 Day 02
# Author: Erik Båvenstrand
# URL: https://adventofcode.com/2020/day/2

from typing import Union


def part_a(data: list[str]) -> Union[int, str, None]:
    """Solution to part A.

    Args:
        data (list[str]): Advent of Code challenge input.

    Returns:
        Union[int, str, None]: Solution to the challenge.
    """
    n_valid = 0
    for [rule, password] in (x.split(": ") for x in data):
        [count, letter] = rule.split(" ")
        [min_count, max_count] = map(int, count.split("-"))
        occurances = password.count(letter)
        if occurances >= min_count and occurances <= max_count:
            n_valid += 1
    return n_valid


def part_b(data: list[str]) -> Union[int, str, None]:
    """Solution to part B.

    Args:
        data (list[str]): Advent of Code challenge input.

    Returns:
        Union[int, str, None]: Solution to the challenge.
    """
    n_valid = 0
    for [rule, password] in (x.split(": ") for x in data):
        [count, letter] = rule.split(" ")
        [idx_first, idx_second] = (int(x) - 1 for x in count.split("-"))

        if (
            password[idx_first] == letter or password[idx_second] == letter
        ) and password[idx_first] != password[idx_second]:
            n_valid += 1
    return n_valid
