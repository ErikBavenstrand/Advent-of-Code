# Advent of Code 2020 Day 03
# Author: Erik Båvenstrand
# URL: https://adventofcode.com/2020/day/3

import math
from typing import Union


def find_trees_in_slope(dx: int, dy: int, slope: list[str]) -> int:
    """Finds the number of tree collisions using a certain dx/dy for a slope.

    Args:
        dx (int): X axis stepsize (sideways).
        dy (int): Y axis stepsize (downwards).
        slope (list[str]): The slope containing open spaces and trees (., #).

    Returns:
        int: Number of tree collisions using dx/dy.
    """
    n_trees = 0
    x = 0
    for y in range(0, len(slope), dy):
        if slope[y][x] == "#":
            n_trees += 1
        x = (x + dx) % len(slope[y])
    return n_trees


def part_a(data: list[str]) -> Union[int, str, None]:
    """Solution to part A.

    Args:
        data (list[str]): Advent of Code challenge input.

    Returns:
        Union[int, str, None]: Solution to the challenge.
    """
    return find_trees_in_slope(3, 1, data)


def part_b(data: list[str]) -> Union[int, str, None]:
    """Solution to part B.

    Args:
        data (list[str]): Advent of Code challenge input.

    Returns:
        Union[int, str, None]: Solution to the challenge.
    """
    inputs: list[tuple] = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    return math.prod(find_trees_in_slope(dx, dy, data) for dx, dy in inputs)
