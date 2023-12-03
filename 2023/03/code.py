# Advent of Code 2023 Day 03
# Author: Erik Båvenstrand
# URL: https://adventofcode.com/2023/day/3

import re


def get_neighbors(x: int, y: int) -> list[tuple[int, int]]:
    """Gets the neighbors of a coordinate.

    Args:
        x: X-coordinate.
        y: Y-coordinate.

    Returns:
        A list of the coordinates neighbors.
    """
    return [
        (x - 1, y - 1),
        (x, y - 1),
        (x + 1, y - 1),
        (x - 1, y),
        (x + 1, y),
        (x - 1, y + 1),
        (x, y + 1),
        (x + 1, y + 1),
    ]


def get_number(data: list[str], x: int, y: int):
    """Gets the full number at a coordinate.

    Args:
        data: Advent of Code challenge input.
        x: X-coordinate.
        y: Y-coordinate.

    Returns:
        The full number at the coordinate.
    """
    left = "".join(re.findall(r"\d+$", data[y][:x]))
    right = "".join(re.findall(r"^\d+", data[y][x:]))
    return int(left + right), {(x_i, y) for x_i in range(x - len(left), x + len(right))}


def part_a(data: list[str]) -> int | str | None:
    """Solution to part A.

    Args:
        data: Advent of Code challenge input.

    Returns:
        Solution to the challenge.
    """
    symbols = [
        (x, y)
        for y, row in enumerate(data)
        for x, c in enumerate(row)
        if c not in "0123456789."
    ]
    result = 0
    visited = set()
    for x, y in symbols:
        for x_i, y_i in get_neighbors(x, y):
            if data[y_i][x_i].isdigit() and (x_i, y_i) not in visited:
                number, coords = get_number(data, x_i, y_i)
                result += number
                visited |= coords
    return result


def part_b(data: list[str]) -> int | str | None:
    """Solution to part B.

    Args:
        data: Advent of Code challenge input.

    Returns:
        Solution to the challenge.
    """
    symbols = [
        (x, y) for y, row in enumerate(data) for x, c in enumerate(row) if c == "*"
    ]
    result = 0
    visited = set()
    for x, y in symbols:
        gear_ratio = 1
        num_numbers = 0
        for x_i, y_i in get_neighbors(x, y):
            if data[y_i][x_i].isdigit() and (x_i, y_i) not in visited:
                number, coords = get_number(data, x_i, y_i)
                gear_ratio *= number
                visited |= coords
                num_numbers += 1
        if num_numbers == 2:
            result += gear_ratio
    return result
