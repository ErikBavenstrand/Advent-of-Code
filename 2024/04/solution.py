# Advent of Code 2024 Day 04
# Author: Erik Båvenstrand
# URL: https://adventofcode.com/2024/day/4

import re

from adventlib.utils.grid import QUEEN_DIRECTIONS_2D


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
                for dy, dx in QUEEN_DIRECTIONS_2D:
                    i = 0
                    word = ""
                    while 0 <= y + (dy * i) < len(data) and 0 <= x + (dx * i) < len(data[y]) and len(word) < 4:
                        word += data[y + (dy * i)][x + (dx * i)]
                        i += 1

                    if word == "XMAS":
                        xmas_count += 1
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
            if re.match(r"M.M\n.A.\nS.S|S.S\n.A.\nM.M|S.M\n.A.\nS.M|M.S\n.A.\nM.S", sub_matrix):
                x_mas_count += 1

    return x_mas_count
