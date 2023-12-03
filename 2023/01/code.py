# Advent of Code 2023 Day 01
# Author: Erik Båvenstrand
# URL: https://adventofcode.com/2023/day/1

import re


def part_a(data: list[str]) -> int | str | None:
    """Solution to part A.

    Args:
        data: Advent of Code challenge input.

    Returns:
        Solution to the challenge.
    """

    values = []
    for line in data:
        digits = re.findall(r"\d", line)
        values.append(int(digits[0] + digits[-1]))
    return sum(values)


def convert_string_to_int(string: str) -> str:
    match string:
        case "one":
            return "1"
        case "two":
            return "2"
        case "three":
            return "3"
        case "four":
            return "4"
        case "five":
            return "5"
        case "six":
            return "6"
        case "seven":
            return "7"
        case "eight":
            return "8"
        case "nine":
            return "9"
        case _:
            return string


def part_b(data: list[str]) -> int | str | None:
    """Solution to part B.

    Args:
        data: Advent of Code challenge input.

    Returns:
        Solution to the challenge.
    """
    values = []
    for line in data:
        digits = [
            match.group()
            for start in range(len(line))
            for match in [
                re.match(
                    r"\d|one|two|three|four|five|six|seven|eight|nine", line[start:]
                )
            ]
            if match
        ]
        values.append(
            int(
                f"{convert_string_to_int(digits[0])}{convert_string_to_int(digits[-1])}"
            )
        )
    return sum(values)
