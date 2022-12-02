# Advent of Code 2022 Day 02
# Author: Erik Båvenstrand
# URL: https://adventofcode.com/2022/day/2

from typing import Union


def part_a(data: list[str]) -> Union[int, str, None]:
    """Solution to part A.

    Args:
        data (list[str]): Advent of Code challenge input.

    Returns:
        Union[int, str, None]: Solution to the challenge.
    """
    score = 0
    for moves in data:
        elf_move = ord(moves[0]) - 65
        player_move = ord(moves[2]) - 88
        if player_move == elf_move:
            score += player_move + 4
        elif player_move == (elf_move + 1) % 3:
            score += player_move + 7
        elif player_move == (elf_move - 1) % 3:
            score += player_move + 1
    return score


def part_b(data: list[str]) -> Union[int, str, None]:
    """Solution to part B.

    Args:
        data (list[str]): Advent of Code challenge input.

    Returns:
        Union[int, str, None]: Solution to the challenge.
    """
    score = 0
    for moves in data:
        elf_move = ord(moves[0]) - 65
        outcome = moves[2]
        if outcome == "X":
            score += 1 + (elf_move - 1) % 3
        elif outcome == "Y":
            score += 4 + elf_move
        elif outcome == "Z":
            score += 7 + (elf_move + 1) % 3
    return score
