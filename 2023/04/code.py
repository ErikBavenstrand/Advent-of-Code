# Advent of Code 2023 Day 04
# Author: Erik Båvenstrand
# URL: https://adventofcode.com/2023/day/4

import re


def get_num_matches(line: str) -> int:
    """Calculate the number of matches between the winning numbers and the ticket numbers.

    Args:
        line: Line from the input file.

    Returns:
        Number of matches.
    """
    winning_numbers_str, ticket_numbers_str = line.split(": ")[1].split(" | ")
    winning_numbers = {int(num) for num in re.findall(r"\d+", winning_numbers_str)}
    ticket_numbers = {int(num) for num in re.findall(r"\d+", ticket_numbers_str)}
    num_matches = len(winning_numbers.intersection(ticket_numbers))
    return num_matches


def part_a(data: list[str]) -> int | str | None:
    """Solution to part A.

    Args:
        data: Advent of Code challenge input.

    Returns:
        Solution to the challenge.
    """
    score = 0
    for line in data:
        num_matches = get_num_matches(line)
        if num_matches > 0:
            score += int(2 ** (num_matches - 1))
    return score


def part_b(data: list[str]) -> int | str | None:
    """Solution to part B.

    Args:
        data: Advent of Code challenge input.

    Returns:
        Solution to the challenge.
    """
    dict_of_cards = {i: 1 for i in range(len(data))}
    for i, line in enumerate(data):
        cards = get_num_matches(line)
        for j in range(i + 1, i + 1 + cards):
            dict_of_cards[j] += 1 * dict_of_cards[i]
    return sum(dict_of_cards.values())
