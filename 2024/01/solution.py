# Advent of Code 2024 Day 01
# Author: Erik Båvenstrand
# URL: https://adventofcode.com/2024/day/1


from collections import Counter


def prepare_data(data: list[str]) -> tuple[list[int], list[int]]:
    """Prepare the data for easier processing.

    Args:
        data: Advent of Code challenge input.

    Returns:
        A tuple containing two lists of integers sorted in ascending order.
    """
    l1: list[int] = []
    l2: list[int] = []
    for line in data:
        n1, n2 = line.split("   ")
        l1.append(int(n1))
        l2.append(int(n2))

    return sorted(l1), sorted(l2)


def part_a(data: list[str]) -> int | str | None:
    """Solution to part A.

    Args:
        data: Advent of Code challenge input.

    Returns:
        Solution to the challenge.
    """
    l1, l2 = prepare_data(data)
    diff = 0
    for n1, n2 in zip(l1, l2, strict=True):
        diff += abs(n1 - n2)
    return diff


def part_b(data: list[str]) -> int | str | None:
    """Solution to part B.

    Args:
        data: Advent of Code challenge input.

    Returns:
        Solution to the challenge.
    """
    l1, l2 = prepare_data(data)
    l2_counter = Counter(l2)
    score = 0
    for n in l1:
        score += n * l2_counter[n]

    return score
