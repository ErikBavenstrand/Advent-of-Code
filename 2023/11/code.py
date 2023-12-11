# Advent of Code 2023 Day 11
# Author: Erik Båvenstrand
# URL: https://adventofcode.com/2023/day/11


import itertools

from adventlib.point import Point2D


def part_a(data: list[str]) -> int | str | None:
    """Solution to part A.

    Args:
        data: Advent of Code challenge input.

    Returns:
        Solution to the challenge.
    """
    galaxies: dict[Point2D, Point2D] = {}
    occupied_rows: set[int] = set()
    occupied_columns: set[int] = set()
    for y, row in enumerate(data):
        for x, char in enumerate(row):
            if char == "#":
                point = Point2D(x, y)
                galaxies[point] = point
                occupied_rows.add(y)
                occupied_columns.add(x)

    expanding_rows = set(range(len(data))).difference(occupied_rows)
    expanding_columns = set(range(len(data[0]))).difference(occupied_columns)
    for galaxy in galaxies.keys():
        row_offset = sum(y < galaxy.y for y in expanding_rows)
        column_offset = sum(x < galaxy.x for x in expanding_columns)
        galaxies[galaxy] = galaxy + (column_offset, row_offset)

    path_lengths = []
    for g1, g2 in itertools.combinations(galaxies.values(), 2):
        path_lengths.append(Point2D.manhattan_distance(g1, g2))
    return sum(path_lengths)


def part_b(data: list[str]) -> int | str | None:
    """Solution to part B.

    Args:
        data: Advent of Code challenge input.

    Returns:
        Solution to the challenge.
    """
    galaxies: dict[Point2D, Point2D] = {}
    occupied_rows: set[int] = set()
    occupied_columns: set[int] = set()
    for y, row in enumerate(data):
        for x, char in enumerate(row):
            if char == "#":
                point = Point2D(x, y)
                galaxies[point] = point
                occupied_rows.add(y)
                occupied_columns.add(x)

    expanding_rows = set(range(len(data))).difference(occupied_rows)
    expanding_columns = set(range(len(data[0]))).difference(occupied_columns)
    for galaxy in galaxies.keys():
        row_offset = sum(y < galaxy.y for y in expanding_rows) * 999999
        column_offset = sum(x < galaxy.x for x in expanding_columns) * 999999
        galaxies[galaxy] = galaxy + (column_offset, row_offset)

    path_lengths = []
    for g1, g2 in itertools.combinations(galaxies.values(), 2):
        path_lengths.append(Point2D.manhattan_distance(g1, g2))
    return sum(path_lengths)
