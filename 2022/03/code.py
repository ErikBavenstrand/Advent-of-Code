# Advent of Code 2022 Day 03
# Author: Erik Båvenstrand
# URL: https://adventofcode.com/2022/day/3

from typing import Union

from adventlib.utils.List import chunk_list
from adventlib.utils.String import split_string


def get_item_prioritization(item: str) -> int:
    """Returns the item prioritization.

    Args:
        item (str): Character item.

    Returns:
        int: Prioritization of item.
    """
    if item.isupper():
        return ord(item) - 38
    else:
        return ord(item) - 96


def part_a(data: list[str]) -> Union[int, str, None]:
    """Solution to part A.

    Args:
        data (list[str]): Advent of Code challenge input.

    Returns:
        Union[int, str, None]: Solution to the challenge.
    """
    sum_item_priorities = 0
    for rugsack in data:
        compartment_1, compartment_2 = split_string(rugsack, 2, lambda x: set(x))
        item = list(compartment_1 & compartment_2).pop()
        sum_item_priorities += get_item_prioritization(item)
    return sum_item_priorities


def part_b(data: list[str]) -> Union[int, str, None]:
    """Solution to part B.

    Args:
        data (list[str]): Advent of Code challenge input.

    Returns:
        Union[int, str, None]: Solution to the challenge.
    """
    sum_item_priorities = 0
    for rugsack_1, rugsack_2, rugsack_3 in chunk_list(data, 3, lambda x: set(x)):
        item = list(rugsack_1 & rugsack_2 & rugsack_3).pop()
        sum_item_priorities += get_item_prioritization(item)
    return sum_item_priorities
