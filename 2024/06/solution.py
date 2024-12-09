# Advent of Code 2024 Day 06
# Author: Erik Båvenstrand
# URL: https://adventofcode.com/2024/day/6

GUARD_ROTATIONS = {
    (0, -1): (1, 0),
    (1, 0): (0, 1),
    (0, 1): (-1, 0),
    (-1, 0): (0, -1),
}


def parse_input(data: list[str]) -> tuple[tuple[int, int], tuple[int, int], set[tuple[int, int]]]:
    """Parses the input data into a more useful format.

    Args:
        data: Advent of Code challenge input.

    Returns:
        A tuple containing the guard's position, direction and a set of obstacles
        in the form of (x, y) coordinates.
    """
    guard_pos: tuple[int, int] = (-1, -1)
    guard_dir: tuple[int, int] = (0, 0)
    obstacles: set[tuple[int, int]] = set()
    for y, row in enumerate(data):
        for x, char in enumerate(row):
            if char in ("^", "v", "<", ">"):
                guard_pos = (x, y)
                guard_dir = {"^": (0, -1), "v": (0, 1), "<": (-1, 0), ">": (1, 0)}[char]
            elif char == "#":
                obstacles.add((x, y))
    return guard_pos, guard_dir, obstacles


def get_visited_states(
    guard_pos: tuple[int, int], guard_dir: tuple[int, int], obstacles: set[tuple[int, int]], max_x: int, max_y: int
) -> tuple[set[tuple[tuple[int, int], tuple[int, int]]], bool]:
    """Get all visited states of the guard.

    Args:
        guard_pos: Position of the guard.
        guard_dir: Direction the guard is facing.
        obstacles: The set of obstacles.
        max_x: Maximum x value.
        max_y: Maximum y value.

    Returns:
        A set of visited states of the guard and a boolean indicating if the guard
        is stuck in a cycle.
    """
    visited: set[tuple[tuple[int, int], tuple[int, int]]] = set()
    while 0 <= guard_pos[0] < max_x and 0 <= guard_pos[1] < max_y:
        if (guard_pos, guard_dir) in visited:
            return visited, True

        visited.add((guard_pos, guard_dir))
        while (guard_pos[0] + guard_dir[0], guard_pos[1] + guard_dir[1]) in obstacles:
            guard_dir = GUARD_ROTATIONS[guard_dir]
        guard_pos = (guard_pos[0] + guard_dir[0], guard_pos[1] + guard_dir[1])

    return visited, False


def part_a(data: list[str]) -> int | str | None:
    """Solution to part A.

    Args:
        data: Advent of Code challenge input.

    Returns:
        Solution to the challenge.
    """
    guard_pos, guard_dir, obstacles = parse_input(data)
    visited_states, _ = get_visited_states(guard_pos, guard_dir, obstacles, len(data[0]), len(data))
    visited_positions = {pos for pos, _ in visited_states}
    return len(visited_positions)


def print_grid(obstacles: set[tuple[int, int]], max_x: int, max_y: int) -> None:
    """Prints the grid with obstacles.

    Args:
        obstacles: The set of obstacles.
        max_x: Maximum x value.
        max_y: Maximum y value.
    """
    for y in range(max_y):
        row = ""
        for x in range(max_x):
            row += "#" if (x, y) in obstacles else "."
        print(row)


def part_b(data: list[str]) -> int | str | None:
    """Solution to part B.

    Args:
        data: Advent of Code challenge input.

    Returns:
        Solution to the challenge.
    """
    guard_pos, guard_dir, obstacles = parse_input(data)
    visited_states, _ = get_visited_states(guard_pos, guard_dir, obstacles, len(data[0]), len(data))
    new_obstacle_candidates = {pos for pos, _ in visited_states if pos != guard_pos}

    cycle_count = 0
    for new_obstacle in new_obstacle_candidates:
        _, is_cycle = get_visited_states(guard_pos, guard_dir, obstacles.union({new_obstacle}), len(data[0]), len(data))
        if is_cycle:
            cycle_count += 1

    return cycle_count
