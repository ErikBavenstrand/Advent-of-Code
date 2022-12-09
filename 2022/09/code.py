# Advent of Code 2022 Day 09
# Author: Erik Båvenstrand
# URL: https://adventofcode.com/2022/day/9

from typing import Union

from adventlib.point import Point2D
from adventlib.utils.number import clamp


def get_rope_segment_move(s1: Point2D, s2: Point2D) -> tuple[int, int]:
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
        match move.split(" "):
            case "U", steps:
                for _ in range(int(steps)):
                    rope[0].y += 1
                    rope[1] -= get_rope_segment_move(rope[0], rope[1])
                    positions.add(rope[-1])
            case "D", steps:
                for _ in range(int(steps)):
                    rope[0].y -= 1
                    rope[1] += get_rope_segment_move(rope[0], rope[1])
                    positions.add(rope[-1])
            case "L", steps:
                for _ in range(int(steps)):
                    rope[0].x -= 1
                    rope[1] += get_rope_segment_move(rope[0], rope[1])
                    positions.add(rope[-1])
            case "R", steps:
                for _ in range(int(steps)):
                    rope[0].x += 1
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
        match move.split(" "):
            case "U", steps:
                for _ in range(int(steps)):
                    rope[0].y += 1
                    for i in range(1, len(rope)):
                        rope[i] += get_rope_segment_move(rope[i - 1], rope[i])
                    positions.add(rope[-1])
            case "D", steps:
                for _ in range(int(steps)):
                    rope[0].y -= 1
                    for i in range(1, len(rope)):
                        rope[i] += get_rope_segment_move(rope[i - 1], rope[i])
                    positions.add(rope[-1])
            case "L", steps:
                for _ in range(int(steps)):
                    rope[0].x -= 1
                    for i in range(1, len(rope)):
                        rope[i] += get_rope_segment_move(rope[i - 1], rope[i])
                    positions.add(rope[-1])
            case "R", steps:
                for _ in range(int(steps)):
                    rope[0].x += 1
                    for i in range(1, len(rope)):
                        # print(get_rope_segment_move(rope[i - 1], rope[i]))
                        rope[i] += get_rope_segment_move(rope[i - 1], rope[i])
                    positions.add(rope[-1])
    return len(positions)
