# Advent of Code 2022 Day 01
# Author: Erik Båvenstrand
# URL: https://adventofcode.com/2022/day/1

from typing import Union


def part_a(data: list[str]) -> Union[int, str, None]:
    """Solution to part A.

    Args:
        data (list[str]): Advent of Code challenge input.

    Returns:
        Union[int, str, None]: Solution to the challenge.
    """
    elf_calories = []
    for str_calories in " ".join(data).split("  "):
        total_calories = sum([int(calories) for calories in str_calories.split(" ")])
        elf_calories.append(total_calories)
    elf_calories.sort(reverse=True)
    return elf_calories[0]


def part_b(data: list[str]) -> Union[int, str, None]:
    """Solution to part B.

    Args:
        data (list[str]): Advent of Code challenge input.

    Returns:
        Union[int, str, None]: Solution to the challenge.
    """
    elf_calories = []
    for str_calories in " ".join(data).split("  "):
        total_calories = sum([int(calories) for calories in str_calories.split(" ")])
        elf_calories.append(total_calories)
    elf_calories.sort(reverse=True)
    return sum(elf_calories[0:3])
