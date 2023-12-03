# Advent of Code 2022 Day 18
# Author: Erik Båvenstrand
# URL: https://adventofcode.com/2022/day/18

from typing import Iterator, Union


def neighbors(coords: tuple[int, int, int]) -> Iterator[tuple[int, int, int]]:
    """Yields all neighbors of coords.

    Args:
        coords: Coordinate to get neighbors for.

    Yields:
        Neighbor coords.
    """
    x, y, z = coords
    for dx, dy, dz in (
        (1, 0, 0),
        (-1, 0, 0),
        (0, 1, 0),
        (0, -1, 0),
        (0, 0, 1),
        (0, 0, -1),
    ):
        yield x + dx, y + dy, z + dz


def part_a(data: list[str]) -> Union[int, str, None]:
    """Solution to part A.

    Args:
        data (list[str]): Advent of Code challenge input.

    Returns:
        Union[int, str, None]: Solution to the challenge.
    """
    surface = 0
    cubes: set[tuple[int, int, int]] = set()
    for line in data:
        coords = tuple([int(val) for val in line.split(",")])
        surface += 6
        cubes.add(coords)
        for neighbor in neighbors(coords):
            if neighbor in cubes:
                surface -= 2
    return surface


def part_b(data: list[str]) -> Union[int, str, None]:
    """Solution to part B.

    Args:
        data (list[str]): Advent of Code challenge input.

    Returns:
        Union[int, str, None]: Solution to the challenge.
    """

    def coordinate_in_bounds(
        coords: tuple[int, int, int], bounds: list[set[int]]
    ) -> bool:
        for coordinate, axis_bounds in zip(coords, bounds):
            if coordinate not in axis_bounds:
                return False
        return True

    cubes: set[tuple[int, int, int]] = set()
    for line in data:
        coordinates = tuple([int(val) for val in line.split(",")])
        cubes.add(coordinates)

    mins = (100, 100, 100)
    maxs = (0, 0, 0)
    for cube in cubes:
        mins = tuple(map(min, zip(cube, mins)))
        maxs = tuple(map(max, zip(cube, maxs)))
    bounds = [set(range(lo - 1, hi + 2)) for lo, hi in zip(mins, maxs)]

    queue = [mins]
    seen = {mins}
    outer_surface = 0
    while queue:
        coordinates = queue.pop()
        for neighbor in neighbors(coordinates):
            if neighbor in seen or not coordinate_in_bounds(neighbor, bounds):
                continue
            if neighbor in cubes:
                outer_surface += 1
            else:
                seen.add(neighbor)
                queue.append(neighbor)
    return outer_surface
