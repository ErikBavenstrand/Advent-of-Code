# Advent of Code 2024 Day 03
# Author: Erik Båvenstrand
# URL: https://adventofcode.com/2024/day/3


import re


def part_a(data: list[str]) -> int | str | None:
    """Solution to part A.

    Args:
        data: Advent of Code challenge input.

    Returns:
        Solution to the challenge.
    """
    result = sum([int(v1) * int(v2) for v1, v2 in re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", "".join(data))])
    return result


def part_b(data: list[str]) -> int | str | None:
    """Solution to part B.

    Args:
        data: Advent of Code challenge input.

    Returns:
        Solution to the challenge.
    """
    enabled = 1
    result = 0
    for v1, v2, do, dont in re.findall(r"mul\((\d{1,3}),(\d{1,3})\)|(do\(\))|(don\'t\(\))", "".join(data)):
        enabled = 1 if do else (0 if dont else enabled)
        if v1 and v2:
            result += enabled * int(v1) * int(v2)
    return result
