# Advent of Code 2023 Day 05
# Author: Erik Båvenstrand
# URL: https://adventofcode.com/2023/day/5


from adventlib.range import Range
from adventlib.utils.list import chunk_list


def get_seeds(data: list[str]) -> list[int]:
    """Get the seeds from the challenge input.

    Args:
        data: Advent of Code challenge input.

    Returns:
        The seeds.
    """
    return [int(seed) for seed in data[0].split(":")[1].strip().split(" ")]


def get_ranges(line: str) -> tuple[Range, Range]:
    """Get the ranges from a challenge input range line.

    Args:
        line: Advent of Code challenge input range line.

    Returns:
        The ranges.
    """
    dest_start, source_start, length = [int(value) for value in line.split(" ")]
    return (
        Range(source_start, source_start + length),
        Range(dest_start, dest_start + length),
    )


def part_a(data: list[str]) -> int | str | None:
    """Solution to part A.

    Args:
        data: Advent of Code challenge input.

    Returns:
        Solution to the challenge.
    """
    ranges: list[tuple[Range, Range]] = []
    prev_values = get_seeds(data)
    for line in data[2:] + [""]:
        if line == "":
            for i, prev_value in enumerate(prev_values):
                for source_range, dest_range in ranges:
                    if prev_value in source_range:
                        offset = dest_range.start - source_range.start
                        prev_values[i] = prev_value + offset
            ranges = []
        elif ":" not in line:
            ranges.append(get_ranges(line))
    return min(prev_values)


def part_b(data: list[str]) -> int | str | None:
    """Solution to part B.

    Args:
        data: Advent of Code challenge input.

    Returns:
        Solution to the challenge.
    """
    ranges: list[tuple[Range, Range]] = []
    prev_ranges = list(
        chunk_list(
            get_seeds(data), 2, lambda x: Range(x[0], x[0] + x[1]), apply_to_chunk=True
        )
    )

    for line in data[2:] + [""]:
        if line == "":
            for i, prev_range in enumerate(prev_ranges):
                for source_range, dest_range in ranges:
                    intersection = prev_range.intersection(source_range)
                    if intersection:
                        prev_ranges[i] = Range(
                            dest_range.start
                            + (intersection.start - source_range.start),
                            dest_range.end + (intersection.end - source_range.end),
                        )

                        remainder = prev_range.remainder(source_range)
                        if remainder:
                            prev_ranges.extend(remainder)
                        break
            ranges = []
        elif ":" not in line:
            ranges.append(get_ranges(line))
    return min(prev_range.start for prev_range in prev_ranges)
