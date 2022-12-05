# Advent of Code 2022 Day 05
# Author: Erik Båvenstrand
# URL: https://adventofcode.com/2022/day/5

from collections import deque
from typing import Union


def get_stacks_datastructure(initial_stacks: str) -> list[deque[str]]:
    """Returns a list of linked lists according to the initial stacks.

    Args:
        initial_stacks (str): Puzzle input.

    Returns:
        list[deque[str]]: List of linked lists,
            where each linked list is a stack of boxes.
    """
    box_indices = range(1, len(initial_stacks.splitlines()[0]), 4)
    stacks: list[deque[str]] = [deque() for _ in range(len(box_indices))]
    for boxes in initial_stacks.splitlines():
        box_indices = range(1, len(boxes), 4)
        for i, box in enumerate([boxes[idx] for idx in box_indices]):
            if box.isalpha():
                stacks[i].append(box)
    return stacks


def get_parsed_moves(move: str) -> tuple[int, int, int]:
    """Parses the moves to decoded integer format.

    Args:
        move (str): Puzzle input.

    Returns:
        tuple[int, int, int]: Number of boxes, from stack, to stack
    """
    num, from_stack, to_stack = (
        move.replace("move ", "").replace(" from ", "-").replace(" to ", "-").split("-")
    )
    return int(num), int(from_stack) - 1, int(to_stack) - 1


def part_a(data: list[str]) -> Union[int, str, None]:
    """Solution to part A.

    Args:
        data (list[str]): Advent of Code challenge input.

    Returns:
        Union[int, str, None]: Solution to the challenge.
    """
    initial_stacks, moves = "\n".join(data).split("\n\n")
    stacks = get_stacks_datastructure(initial_stacks)
    for move in moves.splitlines():
        num, from_stack, to_stack = get_parsed_moves(move)
        stacks[to_stack].extendleft([stacks[from_stack].popleft() for _i in range(num)])

    return "".join([stack[0] for stack in stacks])


def part_b(data: list[str]) -> Union[int, str, None]:
    """Solution to part B.

    Args:
        data (list[str]): Advent of Code challenge input.

    Returns:
        Union[int, str, None]: Solution to the challenge.
    """
    initial_stacks, moves = "\n".join(data).split("\n\n")
    stacks = get_stacks_datastructure(initial_stacks)
    for move in moves.splitlines():
        num, from_stack, to_stack = num, from_stack, to_stack = get_parsed_moves(move)
        stacks[to_stack].extendleft(
            reversed([stacks[from_stack].popleft() for _i in range(num)])
        )

    return "".join([stack[0] for stack in stacks])
