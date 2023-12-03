# Advent of Code 2022 Day 24
# Author: Erik Båvenstrand
# URL: https://adventofcode.com/2022/day/24

from typing import Union

DIRECTIONS: dict[str, tuple[int, int]] = {
    ">": (1, 0),
    "<": (-1, 0),
    "v": (0, 1),
    "^": (0, -1),
    ".": (0, 0),
}


def traverse(
    start: tuple[int, int], end: tuple[int, int], time: int, grid, height, width
):
    positions: set[tuple[int, int]] = {start}
    while True:
        next_step_positions: set[tuple[int, int]] = set()
        for x, y in positions:
            for t_x, t_y in ((x + d_x, y + d_y) for d_x, d_y in DIRECTIONS.values()):
                if (t_x, t_y) == end:
                    return time
                if (
                    0 <= t_x < width
                    and 0 <= t_y < height
                    and grid[t_y][(t_x - time) % width] != ">"
                    and grid[t_y][(t_x + time) % width] != "<"
                    and grid[(t_y - time) % height][t_x] != "v"
                    and grid[(t_y + time) % height][t_x] != "^"
                ):
                    next_step_positions.add((t_x, t_y))
        positions = next_step_positions
        if not positions:
            positions.add(start)
        time += 1


def part_a(data: list[str]) -> Union[int, str, None]:
    """Solution to part A.

    Args:
        data (list[str]): Advent of Code challenge input.

    Returns:
        Union[int, str, None]: Solution to the challenge.
    """
    grid = [row[1:-1] for row in data[1:-1]]
    height, width = len(grid), len(grid[0])
    start, stop = (0, -1), (width - 1, height)
    return traverse(start, stop, 0, grid, height, width)


def part_b(data: list[str]) -> Union[int, str, None]:
    """Solution to part B.

    Args:
        data (list[str]): Advent of Code challenge input.

    Returns:
        Union[int, str, None]: Solution to the challenge.
    """
    grid = [row[1:-1] for row in data[1:-1]]
    height, width = len(grid), len(grid[0])
    start, stop = (0, -1), (width - 1, height)
    a = traverse(start, stop, 0, grid, height, width)
    b = traverse(stop, start, a, grid, height, width)
    return traverse(start, stop, b, grid, height, width)
