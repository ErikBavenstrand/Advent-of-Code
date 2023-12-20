# Advent of Code 2023 Day 12
# Author: Erik Båvenstrand
# URL: https://adventofcode.com/2023/day/12

from functools import cache


@cache
def get_n_arrangements(
    springs: str,
    groups: tuple[int],
) -> int:
    """Get the number of arrangements of springs and groups.

    Args:
        springs: The springs.
        groups: The groups.

    Returns:
        The number of arrangements.
    """
    if not springs:
        return int(not groups)

    current_spring = springs[0]
    if current_spring == "?":
        return get_n_arrangements("#" + springs[1:], groups) + get_n_arrangements(
            "." + springs[1:], groups
        )
    if current_spring == ".":
        return get_n_arrangements(springs.lstrip("."), groups)

    if (
        not groups
        or len(springs) < groups[0]
        or "." in springs[: groups[0]]
        or springs[groups[0] :].startswith("#")
    ):
        return 0

    if len(springs) > groups[0] and springs[groups[0]] == "?":
        return get_n_arrangements(springs[groups[0] + 1 :].lstrip("."), groups[1:])

    return get_n_arrangements(springs[groups[0] :].lstrip("."), groups[1:])


def part_a(data: list[str]) -> int | str | None:
    """Solution to part A.

    Args:
        data: Advent of Code challenge input.

    Returns:
        Solution to the challenge.
    """
    arrangements = 0
    for line in data:
        springs, groups = line.split()
        groups = tuple(int(val) for val in groups.split(","))
        arrangements += get_n_arrangements(springs, groups)
    return arrangements


def part_b(data: list[str]) -> int | str | None:
    """Solution to part B.

    Args:
        data: Advent of Code challenge input.

    Returns:
        Solution to the challenge.
    """
    arrangements = 0
    for line in data:
        springs, groups = line.split()
        springs = "?".join([springs] * 5)
        groups = tuple(int(val) for val in groups.split(",") * 5)
        arrangements += get_n_arrangements(springs, groups)
    return arrangements
