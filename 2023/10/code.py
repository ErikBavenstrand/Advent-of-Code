# Advent of Code 2023 Day 10
# Author: Erik Båvenstrand
# URL: https://adventofcode.com/2023/day/10


from collections import defaultdict
from queue import Queue

from adventlib.point import Point2D


NORTH = Point2D(0, -1)
SOUTH = Point2D(0, 1)
EAST = Point2D(1, 0)
WEST = Point2D(-1, 0)

NEIGHBORS_TO_SYMBOL: dict[tuple[Point2D, ...], str] = {
    (NORTH, SOUTH): "|",
    (EAST, WEST): "-",
    (NORTH, EAST): "L",
    (NORTH, WEST): "J",
    (SOUTH, WEST): "7",
    (SOUTH, EAST): "F",
}


def get_map_directions(
    data: list[str],
) -> tuple[Point2D, dict[Point2D, str], dict[str, tuple[Point2D, ...]]]:
    """Get the map and directions from the input.

    Args:
        data: Advent of Code challenge input.

    Raises:
        ValueError: If no start is found.

    Returns:
        A tuple of the start, the map, and the directions.
    """
    directions: dict[str, tuple[Point2D, ...]] = {
        symbol: direction for direction, symbol in NEIGHBORS_TO_SYMBOL.items()
    }
    directions["."] = ()

    start = None
    map: dict[Point2D, str] = {}

    for y, row in enumerate(data):
        for x, char in enumerate(row):
            point = Point2D(x, y)
            if char == "S":
                start = point
            map[point] = char
    if not start:
        raise ValueError("No start found")

    directions["S"] = ()
    if start + NORTH in map and SOUTH in directions[map[start + NORTH]]:
        directions["S"] = (*directions["S"], NORTH)
    if start + SOUTH in map and NORTH in directions[map[start + SOUTH]]:
        directions["S"] = (*directions["S"], SOUTH)
    if start + EAST in map and WEST in directions[map[start + EAST]]:
        directions["S"] = (*directions["S"], EAST)
    if start + WEST in map and EAST in directions[map[start + WEST]]:
        directions["S"] = (*directions["S"], WEST)

    return start, map, directions


def flood_fill(
    start: Point2D, map: dict[Point2D, str], directions: dict[str, tuple[Point2D, ...]]
) -> dict[Point2D, int]:
    """Flood fill the map.

    Args:
        start: The starting point.
        map: The map.
        directions: The directions.

    Returns:
        The cost of each point.
    """
    Q: Queue[Point2D] = Queue()
    Q.put(start)
    cost: defaultdict[Point2D, int] = defaultdict(lambda: -1)
    cost[start] = 0

    while not Q.empty():
        point = Q.get()
        for direction in directions[map[point]]:
            neighbor = point + direction
            if map[neighbor] != "." and cost[neighbor] == -1:
                cost[neighbor] = cost[point] + 1
                Q.put(neighbor)
    return dict(cost)


def part_a(data: list[str]) -> int | str | None:
    """Solution to part A.

    Args:
        data: Advent of Code challenge input.

    Returns:
        Solution to the challenge.
    """
    start, map, directions = get_map_directions(data)
    cost = flood_fill(start, map, directions)
    return max(cost.values())


def part_b(data: list[str]) -> int | str | None:
    """Solution to part B.

    Args:
        data: Advent of Code challenge input.

    Returns:
        Solution to the challenge.
    """
    start, map, directions = get_map_directions(data)
    cost = flood_fill(start, map, directions)

    for point in map.keys():
        if point not in cost:
            map[point] = "."
        elif map[point] == "S":
            map[point] = NEIGHBORS_TO_SYMBOL[directions["S"]]

    # Time for Raycasting
    n_enclosed = 0
    enclosed = []
    for point, value in map.items():
        if value != ".":
            continue

        intersections = 0
        current = point
        while current in map:
            if map[current] not in ".7L":
                intersections += 1
            current += SOUTH + EAST

        if intersections % 2 == 1:
            n_enclosed += 1
            enclosed.append(point)

    return n_enclosed
