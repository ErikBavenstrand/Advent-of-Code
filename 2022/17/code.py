# Advent of Code 2022 Day 17
# Author: Erik Båvenstrand
# URL: https://adventofcode.com/2022/day/17

from typing import Union

from adventlib.point import Point2D

rocks: list[tuple[Point2D, ...]] = [
    (Point2D(0, 0), Point2D(1, 0), Point2D(2, 0), Point2D(3, 0)),
    (Point2D(1, 0), Point2D(0, 1), Point2D(1, 1), Point2D(2, 1), Point2D(1, 2)),
    (Point2D(0, 0), Point2D(1, 0), Point2D(2, 0), Point2D(2, 1), Point2D(2, 2)),
    (Point2D(0, 0), Point2D(0, 1), Point2D(0, 2), Point2D(0, 3)),
    (Point2D(0, 0), Point2D(1, 0), Point2D(0, 1), Point2D(1, 1)),
]


def simulate_falling_rocks(n_rocks: int, jets: list[tuple[int, int]]) -> int:
    """Run falling rock simulation and return the height after a number of fallen rocks.

    Args:
        n_rocks: Number of rocks to fall.
        jets: Jets configuration.

    Returns:
        Height of tower after all rocks have fallen.
    """
    rock_idx = jet_idx = 0
    tower: set[Point2D] = {Point2D(-1, 0)}
    cache: dict[tuple[int, int], tuple[int, int]] = {}

    def empty_point(point: Point2D) -> bool:
        """Check if Point is empty in the tower.

        Args:
            point: Point to be checked.

        Returns:
            True of point is empty.
        """
        return point.x >= 0 and point.x < 7 and point.y > 0 and point not in tower

    for rock_n in range(n_rocks):
        height = int(max(point.y for point in tower))
        pos = Point2D(2, height + 4)
        rock = rocks[rock_idx]
        rock_idx = (rock_idx + 1) % len(rocks)

        key = rock_idx, jet_idx
        if key in cache:
            n, h = cache[key]
            d, m = divmod(n_rocks - n, rock_n - n)
            if not m:
                return int((h + (height - h) * d))
        else:
            cache[key] = rock_n, height

        while True:
            jet = jets[jet_idx]
            jet_idx = (jet_idx + 1) % len(jets)
            if all(empty_point(pos + jet + r) for r in rock):
                pos += jet
            if all(empty_point(pos - (0, 1) + r) for r in rock):
                pos -= (0, 1)
            else:
                break
        tower |= {pos + r for r in rock}
    return int(max(point.y for point in tower))


def part_a(data: list[str]) -> Union[int, str, None]:
    """Solution to part A.

    Args:
        data (list[str]): Advent of Code challenge input.

    Returns:
        Union[int, str, None]: Solution to the challenge.
    """
    jets: list[tuple[int, int]] = [(1, 0) if jet == ">" else (-1, 0) for jet in data[0]]
    return simulate_falling_rocks(2022, jets)


def part_b(data: list[str]) -> Union[int, str, None]:
    """Solution to part B.

    Args:
        data (list[str]): Advent of Code challenge input.

    Returns:
        Union[int, str, None]: Solution to the challenge.
    """
    jets: list[tuple[int, int]] = [(1, 0) if jet == ">" else (-1, 0) for jet in data[0]]
    return simulate_falling_rocks(int(1e12), jets)
