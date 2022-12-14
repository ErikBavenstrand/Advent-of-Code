# Advent of Code 2022 Day 14
# Author: Erik Båvenstrand
# URL: https://adventofcode.com/2022/day/14

from typing import Union


def get_rock_walls(data: list[str]) -> tuple[set[complex], int]:
    """Get the rock walls and the abyss level.

    Args:
        data: Puzzle input data.

    Returns:
        Tuple of a set of rock wall locations and the abyss level.
            The rock walls are represented as complex numbers where the imaginary
            part is the elevation.
    """
    solids: set[complex] = set()
    abyss = 0
    for line in data:
        x = [list(map(int, coord.split(","))) for coord in line.split(" -> ")]
        for (x1, y1), (x2, y2) in zip(x, x[1:]):
            x1, x2 = sorted([x1, x2])
            y1, y2 = sorted([y1, y2])
            solids.update(
                [x + y * 1j for y in range(y1, y2 + 1) for x in range(x1, x2 + 1)]
            )
            abyss = max(abyss, y2 + 1)
    return solids, abyss


def part_a(data: list[str]) -> Union[int, str, None]:
    """Solution to part A.

    Args:
        data (list[str]): Advent of Code challenge input.

    Returns:
        Union[int, str, None]: Solution to the challenge.
    """
    solids, abyss = get_rock_walls(data)
    n_sands = 0
    sand = 500 + 0j
    while sand.imag < abyss:
        if sand + 1j not in solids:
            sand += 1j
        elif sand + 1j - 1 not in solids:
            sand += 1j - 1
        elif sand + 1j + 1 not in solids:
            sand += 1j + 1
        else:
            solids.add(sand)
            sand = 500 + 0j
            n_sands += 1
    return n_sands


def part_b(data: list[str]) -> Union[int, str, None]:
    """Solution to part B.

    Args:
        data (list[str]): Advent of Code challenge input.

    Returns:
        Union[int, str, None]: Solution to the challenge.
    """
    solids, abyss = get_rock_walls(data)
    n_sands = 0
    sand = 500 + 0j
    while 500 + 0j not in solids:
        if sand.imag + 1 == abyss + 1:
            solids.add(sand)
            sand = 500 + 0j
            n_sands += 1
        elif sand + 1j not in solids:
            sand += 1j
        elif sand + 1j - 1 not in solids:
            sand += 1j - 1
        elif sand + 1j + 1 not in solids:
            sand += 1j + 1
        else:
            solids.add(sand)
            sand = 500 + 0j
            n_sands += 1
    return n_sands
