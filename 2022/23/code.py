# Advent of Code 2022 Day 23
# Author: Erik Båvenstrand
# URL: https://adventofcode.com/2022/day/23

from collections import deque
from typing import Callable, Deque, Union

from adventlib.point import Point2D


def isolated(elf: Point2D, elves: set[Point2D]) -> bool:
    x, y = elf.x, elf.y
    positions = [
        (x - 1, y - 1),
        (x, y - 1),
        (x + 1, y - 1),
        (x - 1, y),
        (x + 1, y),
        (x - 1, y + 1),
        (x, y + 1),
        (x + 1, y + 1),
    ]
    return all([pos not in elves for pos in positions])


def consider_north(elf: Point2D, elves: set[Point2D]) -> bool:
    x, y = elf.x, elf.y
    positions = [(x, y - 1), (x + 1, y - 1), (x - 1, y - 1)]
    return all([pos not in elves for pos in positions])


def consider_south(elf: Point2D, elves: set[Point2D]) -> bool:
    x, y = elf.x, elf.y
    positions = [(x, y + 1), (x + 1, y + 1), (x - 1, y + 1)]
    return all([pos not in elves for pos in positions])


def consider_west(elf: Point2D, elves: set[Point2D]) -> bool:
    x, y = elf.x, elf.y
    positions = [(x - 1, y), (x - 1, y + 1), (x - 1, y - 1)]
    return all([pos not in elves for pos in positions])


def consider_east(elf: Point2D, elves: set[Point2D]) -> bool:
    x, y = elf.x, elf.y
    positions = [(x + 1, y), (x + 1, y + 1), (x + 1, y - 1)]
    return all([pos not in elves for pos in positions])


def part_a(data: list[str]) -> Union[int, str, None]:
    """Solution to part A.

    Args:
        data (list[str]): Advent of Code challenge input.

    Returns:
        Union[int, str, None]: Solution to the challenge.
    """
    elves: set[Point2D] = set()
    for y, row in enumerate(data):
        for x, v in enumerate(row):
            if v == "#":
                elves.add(Point2D(x, y))
    considerations: Deque[tuple[Callable, Point2D]] = deque(
        [
            (consider_north, Point2D(0, -1)),
            (consider_south, Point2D(0, 1)),
            (consider_west, Point2D(-1, 0)),
            (consider_east, Point2D(1, 0)),
        ]
    )

    canceled_moves: set[Point2D] = set()
    moves: set[Point2D] = set()
    for _ in range(10):
        canceled_moves, moves = set(), set()
        elves_copy = elves.copy()
        for elf in list(elves):
            if not isolated(elf, elves):
                for consider, move in considerations:
                    if consider(elf, elves):
                        target_pos = elf + move
                        if target_pos in moves:
                            canceled_moves.add(target_pos)
                        else:
                            moves.add(target_pos)
                        break

        for elf in list(elves):
            if not isolated(elf, elves):
                for consider, move in considerations:
                    if consider(elf, elves):
                        target_pos = elf + move
                        if target_pos not in canceled_moves:
                            elves_copy.remove(elf)
                            elves_copy.add(target_pos)
                        break
        elves = elves_copy
        considerations.rotate(-1)

    x_pos = [pos.x for pos in elves]
    y_pos = [pos.y for pos in elves]
    len_x = (max(x_pos) - min(x_pos)) + 1
    len_y = (max(y_pos) - min(y_pos)) + 1
    return int((len_x * len_y) - len(elves))


def part_b(data: list[str]) -> Union[int, str, None]:
    """Solution to part B.

    Args:
        data (list[str]): Advent of Code challenge input.

    Returns:
        Union[int, str, None]: Solution to the challenge.
    """
    elves: set[Point2D] = set()
    for y, row in enumerate(data):
        for x, v in enumerate(row):
            if v == "#":
                elves.add(Point2D(x, y))
    considerations: Deque[tuple[Callable, Point2D]] = deque(
        [
            (consider_north, Point2D(0, -1)),
            (consider_south, Point2D(0, 1)),
            (consider_west, Point2D(-1, 0)),
            (consider_east, Point2D(1, 0)),
        ]
    )

    canceled_moves: set[Point2D] = set()
    moves: set[Point2D] = set()
    move_round = 1
    while True:
        canceled_moves, moves = set(), set()
        elves_copy = elves.copy()
        for elf in list(elves):
            if not isolated(elf, elves):
                for consider, move in considerations:
                    if consider(elf, elves):
                        target_pos = elf + move
                        if target_pos in moves:
                            canceled_moves.add(target_pos)
                        else:
                            moves.add(target_pos)
                        break

        for elf in list(elves):
            if not isolated(elf, elves):
                for consider, move in considerations:
                    if consider(elf, elves):
                        target_pos = elf + move
                        if target_pos not in canceled_moves:
                            elves_copy.remove(elf)
                            elves_copy.add(target_pos)
                        break
        if elves == elves_copy:
            return move_round
        elves = elves_copy
        considerations.rotate(-1)
        move_round += 1
