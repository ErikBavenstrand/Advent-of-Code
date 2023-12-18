# Advent of Code 2023 Day 17
# Author: Erik Båvenstrand
# URL: https://adventofcode.com/2023/day/17

import heapq
from hmac import new
from turtle import pos

from adventlib.point import Point2D


DIRECTIONS = [Point2D(0, -1), Point2D(1, 0), Point2D(0, 1), Point2D(-1, 0)]


def dijkstra(
    grid: dict[Point2D, int],
    start: Point2D,
    end: Point2D,
    min_steps: int = 1,
    max_steps: int = 3,
) -> int:
    queue: list[tuple[int, int, Point2D, Point2D]] = [
        (0, 0, start, direction * min_steps)
        for direction in DIRECTIONS
        if start + direction in grid
    ]
    distances: dict[tuple[Point2D, Point2D, int], int] = {}
    while queue:
        heat_loss, steps, position, direction = heapq.heappop(queue)
        if position == end:
            return heat_loss

        if (position, direction, steps) in distances:
            continue

        distances[(position, direction, steps)] = heat_loss
        for new_direction in DIRECTIONS:
            # Don't go back the way we came
            if new_direction == direction * -1:
                continue

            # Don't keep going in the same direction if we took too many steps
            if new_direction == direction and steps + 1 > max_steps:
                continue

            if new_direction == direction:
                new_position = position + new_direction
                new_steps = steps + 1
                new_heat_loss = heat_loss + grid.get(new_position, -1)
            else:
                new_position = position + (new_direction * min_steps)
                new_steps = min_steps
                new_heat_loss = heat_loss + sum(
                    [
                        grid.get(position + (new_direction * step), -1)
                        for step in range(1, min_steps + 1)
                    ]
                )

            if new_position in grid:
                heapq.heappush(
                    queue, (new_heat_loss, new_steps, new_position, new_direction)
                )
    return -1


def part_a(data: list[str]) -> int | str | None:
    """Solution to part A.

    Args:
        data: Advent of Code challenge input.

    Returns:
        Solution to the challenge.
    """
    grid = {
        Point2D(x, y): int(heat_loss)
        for y, row in enumerate(data)
        for x, heat_loss in enumerate(row)
    }
    return dijkstra(grid, Point2D(0, 0), Point2D(len(data[0]) - 1, len(data) - 1))


def part_b(data: list[str]) -> int | str | None:
    """Solution to part B.

    Args:
        data: Advent of Code challenge input.

    Returns:
        Solution to the challenge.
    """
    grid = {
        Point2D(x, y): int(heat_loss)
        for y, row in enumerate(data)
        for x, heat_loss in enumerate(row)
    }
    return dijkstra(
        grid, Point2D(0, 0), Point2D(len(data[0]) - 1, len(data) - 1), 4, 10
    )
