# Advent of Code 2023 Day 16
# Author: Erik Båvenstrand
# URL: https://adventofcode.com/2023/day/16


from adventlib.point import Point2D


def get_grid(data: list[str]) -> dict[Point2D, str]:
    """Convert the challenge input into a grid.

    Args:
        data: Advent of Code challenge input.

    Returns:
        A grid representing the challenge input.
    """
    return {
        Point2D(x, y): char for y, row in enumerate(data) for x, char in enumerate(row)
    }


def count_energized_points(
    grid: dict[Point2D, str], start: Point2D, direction: Point2D
) -> int:
    """Shine a beam of light through the grid and count the number of points it hits.

    Args:
        data: Advent of Code challenge input.
        start: The starting position of the beam of light.
        direction: The direction of the beam of light.

    Returns:
        The number of points the beam of light hits.
    """
    visited: set[tuple[Point2D, Point2D]] = set()
    queue: list[tuple[Point2D, Point2D]] = [(start, direction)]
    while queue:
        position, velocity = queue.pop(0)
        while not (position, velocity) in visited:
            visited.add((position, velocity))
            position += velocity
            match grid.get(position):
                case "|":
                    velocity = Point2D(0, 1)
                    queue.append((position, velocity * -1))
                case "-":
                    velocity = Point2D(-1, 0)
                    queue.append((position, velocity * -1))
                case "/":
                    velocity = Point2D(-velocity.y, -velocity.x)
                case "\\":
                    velocity = Point2D(velocity.y, velocity.x)
                case None:
                    break

    return len(set(pos for pos, _ in visited)) - 1


def part_a(data: list[str]) -> int | str | None:
    """Solution to part A.

    Args:
        data: Advent of Code challenge input.

    Returns:
        Solution to the challenge.
    """
    grid = get_grid(data)
    return count_energized_points(grid, Point2D(-1, 0), Point2D(1, 0))


def part_b(data: list[str]) -> int | str | None:
    """Solution to part B.

    Args:
        data: Advent of Code challenge input.

    Returns:
        Solution to the challenge.
    """
    grid = get_grid(data)
    max_energized_points = 0
    for direction in [Point2D(1, 0), Point2D(0, 1), Point2D(-1, 0), Point2D(0, -1)]:
        for start in [
            position - direction
            for position in grid.keys()
            if position - direction not in grid
        ]:
            max_energized_points = max(
                max_energized_points, count_energized_points(grid, start, direction)
            )

    return max_energized_points
