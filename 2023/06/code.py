# Advent of Code 2023 Day 06
# Author: Erik Båvenstrand
# URL: https://adventofcode.com/2023/day/6
import re


def get_time(max_time: int, max_distance: int, maximum: bool = True) -> int:
    """Get the time to wait to get a distance above 9 mm.

    Args:
        max_time: The maximum time to wait.
        max_distance: The maximum distance to get.
        maximum: Whether to get the maximum or maximum time.

    Returns:
        The time to wait to get a distance above 9 mm.
    """
    times = range(max_time, -1, -1) if maximum else range(max_time + 1)
    for hold_time in times:
        distance = hold_time * (max_time - hold_time)
        if distance > max_distance:
            return hold_time
    return max_time


def part_a(data: list[str]) -> int | str | None:
    """Solution to part A.

    Args:
        data: Advent of Code challenge input.

    Returns:
        Solution to the challenge.
    """
    times = [int(time) for time in re.findall(r"\d+", data[0])]
    distances = [int(distance) for distance in re.findall(r"\d+", data[1])]

    value = 1
    for max_time, max_distance in zip(times, distances):
        value *= (
            get_time(max_time, max_distance, maximum=True)
            - get_time(max_time, max_distance, maximum=False)
            + 1
        )

    return value


def part_b(data: list[str]) -> int | str | None:
    """Solution to part B.

    Args:
        data: Advent of Code challenge input.

    Returns:
        Solution to the challenge.
    """
    max_time = int(data[0].split(":")[1].strip().replace(" ", ""))
    max_distance = int(data[1].split(":")[1].strip().replace(" ", ""))

    solutions = (
        get_time(max_time, max_distance, maximum=True)
        - get_time(max_time, max_distance, maximum=False)
        + 1
    )

    return solutions
