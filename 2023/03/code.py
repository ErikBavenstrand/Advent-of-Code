# Advent of Code 2023 Day 03
# Author: Erik Båvenstrand
# URL: https://adventofcode.com/2023/day/3

import re

from adventlib.point import Point2D


def get_number(data: list[str], point: Point2D) -> tuple[int, set[Point2D]]:
    """Gets the full number at a coordinate.

    Args:
        data: Advent of Code challenge input.
        point: Coordinate to get the number at.

    Returns:
        The full number at the coordinate.
    """
    x, y = [int(coord) for coord in point]
    left = "".join(re.findall(r"\d+$", data[y][:x]))
    right = "".join(re.findall(r"^\d+", data[y][x:]))
    return int(left + right), {
        Point2D(x_i, y) for x_i in range(x - len(left), x + len(right))
    }


def part_a(data: list[str]) -> int | str | None:
    """Solution to part A.

    Args:
        data: Advent of Code challenge input.

    Returns:
        Solution to the challenge.
    """
    symbols = [
        Point2D(x, y)
        for y, row in enumerate(data)
        for x, c in enumerate(row)
        if c not in "0123456789."
    ]
    result = 0
    visited: set[Point2D] = set()
    for symbol in symbols:
        for neighbor in symbol.neighbors(0, len(data[0]), 0, len(data)):
            x_n, y_n = [int(coord) for coord in neighbor]
            if data[y_n][x_n].isdigit() and neighbor not in visited:
                number, number_points = get_number(data, neighbor)
                result += number
                visited |= number_points
    return result


def part_b(data: list[str]) -> int | str | None:
    """Solution to part B.

    Args:
        data: Advent of Code challenge input.

    Returns:
        Solution to the challenge.
    """
    gears = [
        Point2D(x, y)
        for y, row in enumerate(data)
        for x, c in enumerate(row)
        if c == "*"
    ]
    result = 0
    visited: set[Point2D] = set()
    for gear in gears:
        gear_ratio = 1
        num_numbers = 0
        for neighbor in gear.neighbors(0, len(data[0]), 0, len(data)):
            x_n, y_n = [int(coord) for coord in neighbor]
            if data[y_n][x_n].isdigit() and neighbor not in visited:
                number, number_points = get_number(data, neighbor)
                gear_ratio *= number
                visited |= number_points
                num_numbers += 1
        if num_numbers == 2:
            result += gear_ratio
    return result
