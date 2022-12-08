# Advent of Code 2022 Day 08
# Author: Erik Båvenstrand
# URL: https://adventofcode.com/2022/day/8

from typing import Union

import numpy as np


def get_visible_range(height: int, view):
    blockers = np.where(view >= height)
    return len(view) if len(blockers[0]) == 0 else blockers[0][0] + 1


def part_a(data: list[str]) -> Union[int, str, None]:
    """Solution to part A.

    Args:
        data (list[str]): Advent of Code challenge input.

    Returns:
        Union[int, str, None]: Solution to the challenge.
    """
    grid = np.zeros(shape=(len(data), len(data[0])))
    for i, row in enumerate(data):
        grid[i] = [int(height) for height in list(row)]

    internal_visible_trees = 0
    for row in range(1, len(grid) - 1):
        for col in range(1, len(grid[row]) - 1):
            height = grid[row, col]
            if (
                height > np.max(grid[:row, col])
                or height > np.max(grid[row, :col])
                or height > np.max(grid[row + 1 :, col])
                or height > np.max(grid[row, col + 1 :])
            ):
                internal_visible_trees += 1
    return internal_visible_trees + 4 * len(data) - 4


def part_b(data: list[str]) -> Union[int, str, None]:
    """Solution to part B.

    Args:
        data (list[str]): Advent of Code challenge input.

    Returns:
        Union[int, str, None]: Solution to the challenge.
    """
    grid = np.zeros(shape=(len(data), len(data[0])))
    for i, row in enumerate(data):
        grid[i] = [int(height) for height in list(row)]

    max_score = 0
    for row in range(1, len(grid) - 1):
        for col in range(1, len(grid[row]) - 1):
            height = grid[row, col]
            up = get_visible_range(height, np.flip(grid[:row, col]))
            left = get_visible_range(height, np.flip(grid[row, :col]))
            down = get_visible_range(height, grid[row + 1 :, col])
            right = get_visible_range(height, grid[row, col + 1 :])
            tree_score = up * left * down * right
            if tree_score > max_score:
                max_score = tree_score

    return max_score
