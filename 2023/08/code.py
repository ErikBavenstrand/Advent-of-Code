# Advent of Code 2023 Day 08
# Author: Erik Båvenstrand
# URL: https://adventofcode.com/2023/day/8


import math


def get_directions_and_nodes(data: list[str]) -> tuple[str, dict[str, tuple[str, str]]]:
    """Get directions and nodes from input data.

    Args:
        data: Advent of Code challenge input.

    Returns:
        A tuple containing the directions and nodes.
    """
    directions: str = data[0]
    nodes: dict[str, tuple[str, str]] = {}
    for line in data[2:]:
        node, connections = line.split(" = ")
        left, right = connections.replace("(", "").replace(")", "").split(", ")
        nodes[node] = (left, right)

    return directions, nodes


def get_path_length(
    node: str, directions: str, nodes: dict[str, tuple[str, str]]
) -> int:
    """Get the path length from a node to the end.

    Args:
        node: The node to start from.
        directions: The directions to follow.
        nodes: The node connections.

    Returns:
        The path length.
    """
    step = 0
    while not node.endswith("Z"):
        direction = directions[step % len(directions)]
        node = nodes[node][0] if direction == "L" else nodes[node][1]
        step += 1
    return step


def part_a(data: list[str]) -> int | str | None:
    """Solution to part A.

    Args:
        data: Advent of Code challenge input.

    Returns:
        Solution to the challenge.
    """
    directions, nodes = get_directions_and_nodes(data)
    return get_path_length("AAA", directions, nodes)


def part_b(data: list[str]) -> int | str | None:
    """Solution to part B.

    Args:
        data: Advent of Code challenge input.

    Returns:
        Solution to the challenge.
    """
    directions, nodes = get_directions_and_nodes(data)
    start_nodes = [node for node in nodes if node.endswith("A")]
    path_lengths = []
    for start_node in start_nodes:
        path_lengths.append(get_path_length(start_node, directions, nodes))
    return math.lcm(*path_lengths)
