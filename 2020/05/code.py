# Advent of Code 2020 Day 05
# Author: Erik Båvenstrand
# URL: https://adventofcode.com/2020/day/5

from typing import Union


def get_sorted_seats(boarding_passes: list[str]) -> list[int]:
    """Calculates a list of seat IDs.

    Args:
        boarding_passes (list[str]): List of boarding passes.

    Returns:
        list[int]: Sorted list of seat IDs.
    """
    seats = [
        int(
            boarding_pass.replace("L", "F")
            .replace("R", "B")
            .replace("F", "0")
            .replace("B", "1"),
            2,
        )
        for boarding_pass in boarding_passes
    ]
    seats.sort()
    return seats


def part_a(data: list[str]) -> Union[int, str, None]:
    """Solution to part A.

    Args:
        data (list[str]): Advent of Code challenge input.

    Returns:
        Union[int, str, None]: Solution to the challenge.
    """
    return get_sorted_seats(data)[-1]


def part_b(data: list[str]) -> Union[int, str, None]:
    """Solution to part B.

    Args:
        data (list[str]): Advent of Code challenge input.

    Returns:
        Union[int, str, None]: Solution to the challenge.
    """
    seats = get_sorted_seats(data)
    for idx in range(len(seats)):
        if abs(seats[idx] - seats[idx + 1]) != 1:
            return seats[idx] + 1
