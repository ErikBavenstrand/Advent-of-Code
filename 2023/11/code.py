# Advent of Code 2023 Day 11
# Author: Erik Båvenstrand
# URL: https://adventofcode.com/2023/day/11


import itertools

from adventlib.point import Point2D


def get_galaxy_map(
    data: list[str],
) -> tuple[dict[Point2D, Point2D], set[int], set[int]]:
    """Get a map of galaxies, and the expanding rows and columns.

    Args:
        data: Advent of Code challenge input.

    Returns:
        A tuple of the galaxy map, the expanding rows, and the expanding columns.
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
    return galaxies, expanding_rows, expanding_columns


def expand_galaxies(
    galaxies: dict[Point2D, Point2D],
    expanding_rows: set[int],
    expanding_columns: set[int],
    multiplier: int = 1,
) -> set[Point2D]:
    """Expand the galaxies in the map.

    Args:
        galaxies: The galaxy map.

    Returns:
        The expanded galaxies.
    """
    expanded_galaxies = set()
    for galaxy in galaxies.keys():
        row_offset = sum(y < galaxy.y for y in expanding_rows) * multiplier
        column_offset = sum(x < galaxy.x for x in expanding_columns) * multiplier
        expanded_galaxies.add(galaxy + (column_offset, row_offset))
    return expanded_galaxies


def part_a(data: list[str]) -> int | str | None:
    """Solution to part A.

    Args:
        data: Advent of Code challenge input.

    Returns:
        Solution to the challenge.
    """
    galaxies, expanding_rows, expanding_columns = get_galaxy_map(data)
    expanded_galaxies = expand_galaxies(galaxies, expanding_rows, expanding_columns)

    path_lengths = []
    for g1, g2 in itertools.combinations(expanded_galaxies, 2):
        path_lengths.append(Point2D.manhattan_distance(g1, g2))
    return sum(path_lengths)


def part_b(data: list[str]) -> int | str | None:
    """Solution to part B.

    Args:
        data: Advent of Code challenge input.

    Returns:
        Solution to the challenge.
    """
    galaxies, expanding_rows, expanding_columns = get_galaxy_map(data)
    expanded_galaxies = expand_galaxies(
        galaxies, expanding_rows, expanding_columns, multiplier=999999
    )

    path_lengths = []
    for g1, g2 in itertools.combinations(expanded_galaxies, 2):
        path_lengths.append(Point2D.manhattan_distance(g1, g2))
    return sum(path_lengths)
