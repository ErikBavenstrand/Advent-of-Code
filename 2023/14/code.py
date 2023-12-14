# Advent of Code 2023 Day 14
# Author: Erik Båvenstrand
# URL: https://adventofcode.com/2023/day/14


from adventlib.point import Point2D
from adventlib.utils.string import rotate_2d_list


def tilt_left(grid: list[str]) -> list[str]:
    """Tilt a grid left.

    Args:
        grid: Grid to be tilted.

    Returns:
        Tilted grid.
    """
    return [
        "#".join(
            ("O" * section.count("O")).ljust(len(section), ".")
            for section in "".join(row).split("#")
        )
        for row in grid
    ]


def part_a(data: list[str]) -> int | str | None:
    """Solution to part A.

    Args:
        data: Advent of Code challenge input.

    Returns:
        Solution to the challenge.
    """
    total_load = 0
    for line in tilt_left(rotate_2d_list(data)):
        for i, char in enumerate(line):
            if char == "O":
                total_load += len(data) - i
    return total_load


def tilt_cycle(grid: list[str]) -> list[str]:
    return rotate_2d_list(
        tilt_left(
            rotate_2d_list(
                tilt_left(
                    rotate_2d_list(
                        tilt_left(
                            rotate_2d_list(
                                tilt_left(
                                    rotate_2d_list(grid),
                                ),
                                clockwise=True,
                            ),
                        ),
                        clockwise=True,
                    )
                ),
                clockwise=True,
            )
        ),
        steps=2,
        clockwise=True,
    )


def part_b(data: list[str]) -> int | str | None:
    """Solution to part B.

    Args:
        data: Advent of Code challenge input.

    Returns:
        Solution to the challenge.
    """
    n_cycles = 1_000_000_000
    grid = list(data)
    grids: dict[tuple[str, ...], int] = {}
    for i in range(n_cycles):
        grid_tuple = tuple(grid)
        if grid_tuple in grids:
            prev_i = grids[grid_tuple]
            loop_length = i - prev_i
            grid = list(
                list(grids.keys())[prev_i + ((n_cycles - prev_i) % loop_length)]
            )
            break

        grids[grid_tuple] = i
        grid = tilt_cycle(grid)

    total_load = 0
    for line in rotate_2d_list(grid):
        for i, char in enumerate(line):
            if char == "O":
                total_load += len(data) - i
    return total_load
