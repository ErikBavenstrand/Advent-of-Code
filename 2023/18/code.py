# Advent of Code 2023 Day 18
# Author: Erik Båvenstrand
# URL: https://adventofcode.com/2023/day/18


from adventlib.point import Point2D


def part_a(data: list[str]) -> int | str | None:
    """Solution to part A.

    Args:
        data: Advent of Code challenge input.

    Returns:
        Solution to the challenge.
    """
    boundary_size = 0
    points: list[Point2D] = []
    position = Point2D(0, 0)
    for line in data:
        direction, distance, _ = line.split()
        match direction:
            case "U":
                position += Point2D(0, -int(distance))
            case "D":
                position += Point2D(0, int(distance))
            case "L":
                position += Point2D(-int(distance), 0)
            case "R":
                position += Point2D(int(distance), 0)
        points.append(position)
        boundary_size += int(distance)

    inner_area = abs(
        sum(((p1.x * p2.y) - (p1.y * p2.x)) / 2 for p1, p2 in zip(points, points[1:]))
    )
    return int(inner_area + (boundary_size / 2) + 1)


def part_b(data: list[str]) -> int | str | None:
    """Solution to part B.

    Args:
        data: Advent of Code challenge input.

    Returns:
        Solution to the challenge.
    """
    boundary_size = 0
    points: list[Point2D] = []
    position = Point2D(0, 0)
    for line in data:
        _, color = line.replace(")", "").split("#")
        distance, direction = int(color[:-1], 16), int(color[-1])
        match direction:
            case 3:
                position += Point2D(0, -int(distance))
            case 1:
                position += Point2D(0, int(distance))
            case 2:
                position += Point2D(-int(distance), 0)
            case 0:
                position += Point2D(int(distance), 0)
        points.append(position)
        boundary_size += int(distance)

    inner_area = abs(
        sum(((p1.x * p2.y) - (p1.y * p2.x)) / 2 for p1, p2 in zip(points, points[1:]))
    )
    return int(inner_area + (boundary_size / 2) + 1)
