# Advent of Code 2023 Day 21
# Author: Erik Båvenstrand
# URL: https://adventofcode.com/2023/day/21


from collections import deque

from adventlib.point import Point2D


def get_plots(data: list[str]) -> tuple[set[Point2D], Point2D]:
    """Get the garden plots and the starting plot.

    Args:
        data: Advent of Code challenge input.

    Returns:
        The garden plots and the starting plot.
    """
    garden_plots: set[Point2D] = set()
    start = Point2D(0, 0)
    for y, row in enumerate(data):
        for x, char in enumerate(row):
            plot = Point2D(x, y)
            if char != "#":
                garden_plots.add(plot)
            if char == "S":
                start = plot
    return garden_plots, start


def simulate_steps(
    garden_plots: set[Point2D],
    start: Point2D,
    n_steps: int,
    tile_size: int,
    part_a: bool = True,
) -> set[Point2D]:
    """Simulate steps using BFS.

    Args:
        garden_plots: The garden plots.
        start: The starting plot.
        n_steps: The number of steps to simulate.
        tile_size: The size of a tile.
        part_a: Whether to simulate part A or part B.

    Returns:
        The set of plots that are watered.
    """
    queue: deque[tuple[Point2D, int]] = deque([(start, n_steps)])
    seen: set[Point2D] = set()
    answer: set[Point2D] = set()

    while queue:
        current, n_steps = queue.popleft()

        if n_steps >= 0:
            if n_steps % 2 == 0:
                answer.add(current)

            if n_steps > 0:
                neighbors = current.neighbors(diagonals=False)
                for neighbor in neighbors:
                    if (
                        neighbor in seen
                        or (part_a and (neighbor not in garden_plots))
                        or (neighbor % tile_size not in garden_plots)
                    ):
                        continue

                    queue.append((neighbor, n_steps - 1))
                    seen.add(neighbor)

    return answer


def part_a(data: list[str]) -> int | str | None:
    """Solution to part A.

    Args:
        data: Advent of Code challenge input.

    Returns:
        Solution to the challenge.
    """
    garden_plots, start_plot = get_plots(data)
    tile_size = len(data)
    return len(simulate_steps(garden_plots, start_plot, 64, tile_size))


def solve_quadratic(plot_counts: list[int], n_steps: int, tile_size: int) -> int:
    """Solve a quadratic equation.

    Args:
        plot_counts: The number of plots at each step.
        n_steps: The number of steps to solve for.
        tile_size: The size of the tile.

    Returns:
        The number of plots at step n_steps.
    """
    c = plot_counts[0]
    b = (4 * plot_counts[1] - 3 * plot_counts[0] - plot_counts[2]) // 2
    a = plot_counts[1] - plot_counts[0] - b
    x = (n_steps - tile_size // 2) // tile_size
    return a * x**2 + b * x + c


def part_b(data: list[str]) -> int | str | None:
    """Solution to part B.

    Args:
        data: Advent of Code challenge input.

    Returns:
        Solution to the challenge.
    """
    garden_plots, start_plot = get_plots(data)
    tile_size = len(data)

    plot_counts = [
        len(simulate_steps(garden_plots, start_plot, n_steps, tile_size, part_a=False))
        for n_steps in [65, 196, 327]
    ]
    return solve_quadratic(plot_counts, 26501365, tile_size)
