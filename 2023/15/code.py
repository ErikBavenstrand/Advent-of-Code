# Advent of Code 2023 Day 15
# Author: Erik Båvenstrand
# URL: https://adventofcode.com/2023/day/15


from collections import defaultdict


def hash_string(string: str) -> int:
    """Hashes a string using the Holiday ASCII String Helper algorithm.

    Args:
        string: String to hash.

    Returns:
        Hashed string.
    """
    current_value = 0
    for char in string:
        current_value += ord(char)
        current_value *= 17
        current_value %= 256
    return current_value


def part_a(data: list[str]) -> int | str | None:
    """Solution to part A.

    Args:
        data: Advent of Code challenge input.

    Returns:
        Solution to the challenge.
    """
    hash_sum = 0
    for string in data[0].split(","):
        hash_sum += hash_string(string)
    return hash_sum


def part_b(data: list[str]) -> int | str | None:
    """Solution to part B.

    Args:
        data: Advent of Code challenge input.

    Returns:
        Solution to the challenge.
    """
    boxes: dict[int, dict[str, int]] = defaultdict(dict)
    for string in data[0].split(","):
        parts = string.split("=") if "=" in string else string.split("-")
        label, operation = parts[0], parts[1]
        box = hash_string(label)
        if operation == "=":
            boxes[box][label] = int(parts[2])
        elif operation == "-":
            if label in boxes[box]:
                del boxes[box][label]

    focusing_power = 0
    for box, lenses in boxes.items():
        for i, (_, focal_length) in enumerate(lenses.items()):
            focusing_power += (1 + box) * (i + 1) * focal_length
    return focusing_power
