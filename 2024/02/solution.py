# Advent of Code 2024 Day 02
# Author: Erik Båvenstrand
# URL: https://adventofcode.com/2024/day/2


def is_safe(report: list[int]) -> bool:
    """Check if a report is safe.

    Args:
        report: The report to check.

    Returns:
        True if the report is safe, False otherwise.
    """
    previous_level = report[0]
    order = 1 if report[0] < report[-1] else -1
    for previous_level, current_level in zip(report[:-1], report[1:], strict=True):
        level_diff = current_level - previous_level
        if (not 1 <= abs(level_diff) <= 3) or (level_diff * order < 0):
            return False
    return True


def part_a(data: list[str]) -> int | str | None:
    """Solution to part A.

    Args:
        data: Advent of Code challenge input.

    Returns:
        Solution to the challenge.
    """
    reports = [[int(x) for x in level.split(" ")] for level in data]
    safe_count = 0
    for report in reports:
        if is_safe(report):
            safe_count += 1
    return safe_count


def part_b(data: list[str]) -> int | str | None:
    """Solution to part B.

    Args:
        data: Advent of Code challenge input.

    Returns:
        Solution to the challenge.
    """
    reports = [[int(x) for x in level.split(" ")] for level in data]
    safe_count = 0
    for report in reports:
        if is_safe(report) or any([is_safe(report[:i] + report[i + 1 :]) for i in range(len(report))]):
            safe_count += 1
    return safe_count
