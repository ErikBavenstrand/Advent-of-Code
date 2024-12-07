# Advent of Code 2024 Day 04
# Author: Erik Båvenstrand
# URL: https://adventofcode.com/2024/day/4

import re

from adventlib.utils.grid import get_neighbors

DIRECTIONS = [
    (0, 1),  # Right
    (1, 0),  # Down
    (0, -1),  # Left
    (-1, 0),  # Up
    (1, 1),  # Down-right
    (-1, 1),  # Down-left
    (-1, -1),  # Up-left
    (1, -1),  # Up-right
]


def get_n_xmas_neighbors(data: list[str], y: int, x: int) -> int:
    """Get the number of XMAS neighbors.

    Args:
        data: Input word search.
        y: Starting y-coordinate.
        x: Starting x-coordinate.

    Returns:
        Number of XMAS neighbors.
    """
    xmas_count = 0
    for dy, dx in DIRECTIONS:
        i = 0
        word = ""
        while 0 <= y + (dy * i) < len(data) and 0 <= x + (dx * i) < len(data[y]) and len(word) < 4:
            word += data[y + (dy * i)][x + (dx * i)]
            i += 1

        if word == "XMAS":
            xmas_count += 1
    return xmas_count


def part_a(data: list[str]) -> int | str | None:
    """Solution to part A.

    Args:
        data: Advent of Code challenge input.

    Returns:
        Solution to the challenge.
    """
    xmas_count = 0
    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] == "X":
                xmas_count += get_n_xmas_neighbors(data, y, x)
    return xmas_count


def part_b(data: list[str]) -> int | str | None:
    """Solution to part B.

    Args:
        data: Advent of Code challenge input.

    Returns:
        Solution to the challenge.
    """
    x_mas_count = 0
    for y in range(1, len(data) - 1):
        for x in range(1, len(data[y]) - 1):
            sub_matrix = "\n".join([data[y - 1][x - 1 : x + 2], data[y][x - 1 : x + 2], data[y + 1][x - 1 : x + 2]])
            if re.match(r"M.M\n.A.\nS.S", sub_matrix):
                x_mas_count += 1
            if re.match(r"S.S\n.A.\nM.M", sub_matrix):
                x_mas_count += 1
            if re.match(r"S.M\n.A.\nS.M", sub_matrix):
                x_mas_count += 1
            if re.match(r"M.S\n.A.\nM.S", sub_matrix):
                x_mas_count += 1

    return x_mas_count
