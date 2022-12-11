# Advent of Code 2022 Day 09
# Author: Erik Båvenstrand
# URL: https://adventofcode.com/2022/day/9

from typing import Union

from adventlib.point import Point2D
from adventlib.utils.number import clamp


def get_rope_segment_move(s1: Point2D, s2: Point2D) -> tuple[int, int]:
    """Return movement vector of rope segment.

    Args:
        s1: Point 1.
        s2: Point 2.

    Returns:
        Movement vector.
    """
    if Point2D.distance(s1, s2) <= 1.5:
        return (0, 0)
    return tuple([int(clamp(v, -1, 1)) for v in Point2D.distance_vector(s1, s2)])


def part_a(data: list[str]) -> Union[int, str, None]:
    """Solution to part A.

    Args:
        data (list[str]): Advent of Code challenge input.

    Returns:
        Union[int, str, None]: Solution to the challenge.
    """
    rope: list[Point2D] = [Point2D(0, 0) for _ in range(2)]
    positions: set[Point2D] = {rope[-1]}
    for move in data:
        steps = 0
        match move.split(" "):
            case "U", steps:
                steps = int(steps)
                rope[0].y += steps
            case "D", steps:
                steps = int(steps)
                rope[0].y -= steps
            case "L", steps:
                steps = int(steps)
                rope[0].x -= steps
            case "R", steps:
                steps = int(steps)
                rope[0].x += steps
        for _ in range(steps):
            rope[1] += get_rope_segment_move(rope[0], rope[1])
            positions.add(rope[-1])
    return len(positions)


def part_b(data: list[str]) -> Union[int, str, None]:
    """Solution to part B.

    Args:
        data (list[str]): Advent of Code challenge input.

    Returns:
        Union[int, str, None]: Solution to the challenge.
    """
    rope: list[Point2D] = [Point2D(0, 0) for _ in range(10)]
    positions: set[Point2D] = {rope[-1]}
    for move in data:
        steps = 0
        match move.split(" "):
            case "U", steps:
                steps = int(steps)
                rope[0].y += steps
            case "D", steps:
                steps = int(steps)
                rope[0].y -= steps
            case "L", steps:
                steps = int(steps)
                rope[0].x -= steps
            case "R", steps:
                steps = int(steps)
                rope[0].x += steps
        for _ in range(steps):
            for i in range(1, len(rope)):
                rope[i] += get_rope_segment_move(rope[i - 1], rope[i])
            positions.add(rope[-1])
    return len(positions)
