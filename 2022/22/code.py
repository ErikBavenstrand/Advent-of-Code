# Advent of Code 2022 Day 22
# Author: Erik Båvenstrand
# URL: https://adventofcode.com/2022/day/22

import re
from typing import Literal, Optional, Union

FacingType = Literal["U", "D", "L", "R"]

ROTATE_LEFT: dict[FacingType, FacingType] = {"L": "D", "D": "R", "R": "U", "U": "L"}
ROTATE_RIGHT: dict[FacingType, FacingType] = {"L": "U", "U": "R", "R": "D", "D": "L"}
SEC_SIZE = 50
SEC_START, SEC_END = {0: 0, 1: SEC_SIZE, 2: SEC_SIZE * 2, 3: SEC_SIZE * 3}, {
    0: (SEC_SIZE * 1) - 1,
    1: (SEC_SIZE * 2) - 1,
    2: (SEC_SIZE * 3) - 1,
    3: (SEC_SIZE * 4) - 1,
}


def walk_edge_plane(x: int, y: int, facing: FacingType) -> tuple[int, int, FacingType]:

    # Face 0
    if SEC_START[1] <= x <= SEC_END[1] and SEC_START[0] <= y <= SEC_END[0]:
        match facing:
            case "U":
                return (x, SEC_END[2], facing)
            case "L":
                return (SEC_END[2], y, facing)
    # Face 1
    elif SEC_START[2] <= x <= SEC_END[2] and SEC_START[0] <= y <= SEC_END[0]:
        match facing:
            case "U":
                return (x, SEC_END[0], facing)
            case "D":
                return (x, SEC_START[0], facing)
            case "R":
                return (SEC_START[1], y, facing)
    # Face 2
    elif SEC_START[1] <= x <= SEC_END[1] and SEC_START[1] <= y <= SEC_END[1]:
        match facing:
            case "L":
                return (SEC_END[1], y, facing)
            case "R":
                return (SEC_START[1], y, facing)
    # Face 3
    elif SEC_START[0] <= x <= SEC_END[0] and SEC_START[2] <= y <= SEC_END[2]:
        match facing:
            case "U":
                return (x, SEC_END[3], facing)
            case "L":
                return (SEC_END[1], y, facing)
    # Face 4
    elif SEC_START[1] <= x <= SEC_END[1] and SEC_START[2] <= y <= SEC_END[2]:
        match facing:
            case "D":
                return (x, SEC_START[0], facing)
            case "R":
                return (SEC_START[0], y, facing)
    # Face 5
    elif SEC_START[0] <= x <= SEC_END[0] and SEC_START[3] <= y <= SEC_END[3]:
        match facing:
            case "D":
                return (x, SEC_START[2], facing)
            case "L":
                return (SEC_END[0], y, facing)
            case "R":
                return (SEC_START[0], y, facing)
    return (-1, -1, "R")


def walk_edge_cube(x: int, y: int, facing: FacingType) -> tuple[int, int, FacingType]:

    x_inter = x % SEC_SIZE
    y_inter = y % SEC_SIZE

    # Face 0
    if SEC_START[1] <= x <= SEC_END[1] and SEC_START[0] <= y <= SEC_END[0]:
        match facing:
            case "U":
                return (SEC_START[0], SEC_START[3] + x_inter, "R")
            case "L":
                return (SEC_START[0], SEC_END[2] - y_inter, "R")
    # Face 1
    elif SEC_START[2] <= x <= SEC_END[2] and SEC_START[0] <= y <= SEC_END[0]:
        match facing:
            case "U":
                return (SEC_START[0] + x_inter, SEC_END[3], "U")
            case "D":
                return (SEC_END[1], SEC_START[1] + x_inter, "L")
            case "R":
                return (SEC_END[1], SEC_END[2] - y_inter, "L")
    # Face 2
    elif SEC_START[1] <= x <= SEC_END[1] and SEC_START[1] <= y <= SEC_END[1]:
        match facing:
            case "L":
                return (SEC_START[0] + y_inter, SEC_START[2], "D")
            case "R":
                return (SEC_START[2] + y_inter, SEC_END[0], "U")
    # Face 3
    elif SEC_START[0] <= x <= SEC_END[0] and SEC_START[2] <= y <= SEC_END[2]:
        match facing:
            case "U":
                return (SEC_START[1], SEC_START[1] + x_inter, "R")
            case "L":
                return (SEC_START[1], SEC_END[0] - y_inter, "R")
    # Face 4
    elif SEC_START[1] <= x <= SEC_END[1] and SEC_START[2] <= y <= SEC_END[2]:
        match facing:
            case "D":
                return (SEC_END[0], SEC_START[3] + x_inter, "L")
            case "R":
                return (SEC_END[2], SEC_END[0] - y_inter, "L")
    # Face 5
    elif SEC_START[0] <= x <= SEC_END[0] and SEC_START[3] <= y <= SEC_END[3]:
        match facing:
            case "D":
                return (SEC_START[2] + x_inter, SEC_START[0], "D")
            case "L":
                return (SEC_START[1] + y_inter, SEC_START[0], "D")
            case "R":
                return (SEC_START[1] + y_inter, SEC_END[2], "U")
    return (-1, -1, "R")


def get_neighbor_pos(
    x: int,
    y: int,
    facing: FacingType,
    board: dict[tuple[int, int], str],
    is_cube: Optional[bool] = False,
) -> tuple[int, int, FacingType]:
    x_new, y_new, facing_new = (
        walk_edge_cube(x, y, facing) if is_cube else walk_edge_plane(x, y, facing)
    )
    if board[(x_new, y_new)] == ".":
        return (x_new, y_new, facing_new)
    return (x, y, facing)


def walk_directions(x, y, facing, board, directions, is_cube=False):
    for d in directions:
        if isinstance(d, int):
            for _ in range(d):
                match facing:
                    case "U":
                        if (x, y - 1) not in board:
                            x, y, facing = get_neighbor_pos(
                                x, y, facing, board, is_cube
                            )
                        elif board[(x, y - 1)] == ".":
                            y -= 1
                    case "D":
                        if (x, y + 1) not in board:
                            x, y, facing = get_neighbor_pos(
                                x, y, facing, board, is_cube
                            )
                        elif board[(x, y + 1)] == ".":
                            y += 1
                    case "L":
                        if (x - 1, y) not in board:
                            x, y, facing = get_neighbor_pos(
                                x, y, facing, board, is_cube
                            )
                        elif board[(x - 1, y)] == ".":
                            x -= 1
                    case "R":
                        if (x + 1, y) not in board:
                            x, y, facing = get_neighbor_pos(
                                x, y, facing, board, is_cube
                            )
                        elif board[(x + 1, y)] == ".":
                            x += 1
        else:
            facing = ROTATE_LEFT[facing] if d == "L" else ROTATE_RIGHT[facing]
    return 1000 * (y + 1) + 4 * (x + 1) + {"R": 0, "D": 1, "L": 2, "U": 3}[facing]


def parse_input_data(data: list[str]):
    board_str, directions = "\n".join(data).split("\n\n")
    directions = [
        int(v) if v.isnumeric() else v
        for v in [str(v) for v in re.findall(r"(\d+|\D+)", directions)]
    ]

    board: dict[tuple[int, int], str] = {}
    start_pos = None
    for y, row in enumerate(board_str.splitlines()):
        for x, v in enumerate(row):
            if v in ["#", "."]:
                board[(x, y)] = v
                if start_pos is None:
                    start_pos = (x, y)

    assert start_pos is not None

    facing: FacingType = "R"
    x, y = start_pos
    return x, y, facing, board, directions


def part_a(data: list[str]) -> Union[int, str, None]:
    """Solution to part A.

    Args:
        data (list[str]): Advent of Code challenge input.

    Returns:
        Union[int, str, None]: Solution to the challenge.
    """
    x, y, facing, board, directions = parse_input_data(data)
    return walk_directions(x, y, facing, board, directions)


def part_b(data: list[str]) -> Union[int, str, None]:
    """Solution to part B.

    Args:
        data (list[str]): Advent of Code challenge input.

    Returns:
        Union[int, str, None]: Solution to the challenge.
    """
    x, y, facing, board, directions = parse_input_data(data)
    return walk_directions(x, y, facing, board, directions, is_cube=True)
