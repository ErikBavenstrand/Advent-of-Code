# Advent of Code 2020 Day 06
# Author: Erik Båvenstrand
# URL: https://adventofcode.com/2020/day/6

from typing import Union


def part_a(data: list[str]) -> Union[int, str, None]:
    """Solution to part A.

    Args:
        data (list[str]): Advent of Code challenge input.

    Returns:
        Union[int, str, None]: Solution to the challenge.
    """
    groups = "\n".join(data).split("\n\n")
    n_yes = 0
    for raw_group in groups:
        group = raw_group.replace("\n", "")
        n_yes += len(set(group))
    return n_yes


def part_b(data: list[str]) -> Union[int, str, None]:
    """Solution to part B.

    Args:
        data (list[str]): Advent of Code challenge input.

    Returns:
        Union[int, str, None]: Solution to the challenge.
    """
    groups = "\n".join(data).split("\n\n")
    n_yes = 0
    for raw_group in groups:
        group = raw_group.splitlines()
        n_yes += len(set.intersection(*[set(answer) for answer in group]))
    return n_yes
