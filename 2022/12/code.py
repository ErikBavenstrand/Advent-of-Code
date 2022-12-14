# Advent of Code 2022 Day 12
# Author: Erik Båvenstrand
# URL: https://adventofcode.com/2022/day/12

from collections import defaultdict
from typing import DefaultDict, Union


def build_graph(edges: list[tuple[str, str]]) -> DefaultDict[str, list[str]]:
    graph: DefaultDict[str, list[str]] = defaultdict(list)
    for edge in edges:
        a, b = edge
        graph[a].append(b)
    return graph


def BFS_SP(graph, start, goal):
    explored = []

    # Queue for traversing the
    # graph in the BFS
    queue = [[start]]

    if start == goal:
        print("Same Node")
        return None

    # Loop to traverse the graph
    # with the help of the queue
    while queue:
        path = queue.pop(0)
        node = path[-1]

        # Condition to check if the
        # current node is not visited
        if node not in explored:
            neighbours = graph[node]

            # Loop to iterate over the
            # neighbours of the node
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)

                # Condition to check if the
                # neighbour node is the goal
                if neighbour == goal:
                    return new_path
            explored.append(node)

    # Condition when the nodes
    # are not connected
    return None


def find_node(data, node_id: str):
    for row in range(len(data)):
        for col in range(len(data[row])):
            if data[row][col] == node_id:
                return (row, col)


def find_all_nodes(data, node_id: str):
    positions = []
    for row in range(len(data)):
        for col in range(len(data[row])):
            if data[row][col] == node_id:
                positions.append((row, col))
    return positions


def part_a(data: list[str]) -> Union[int, str, None]:
    """Solution to part A.

    Args:
        data (list[str]): Advent of Code challenge input.

    Returns:
        Union[int, str, None]: Solution to the challenge.
    """
    grid: list[list[str]] = [["ö" for _ in range(len(data[0]) + 2)]]
    for row in data:
        cleaned = row.replace("S", "a").replace("E", "z")
        grid.append(["ö"] + list(cleaned) + ["ö"])
    grid.append(["ö" for _ in range(len(data[0]) + 2)])

    start = find_node(data, "S")
    end = find_node(data, "E")
    edges: list[tuple[str, str]] = []
    for row in range(1, len(grid) - 1):
        for col in range(1, len(grid[row]) - 1):
            if ord(grid[row][col]) + 1 >= ord(grid[row + 1][col]):
                edges.append((f"{row - 1},{col - 1}", f"{row},{col - 1}"))
            if ord(grid[row][col]) + 1 >= ord(grid[row - 1][col]):
                edges.append((f"{row - 1},{col - 1}", f"{row - 2},{col - 1}"))
            if ord(grid[row][col]) + 1 >= ord(grid[row][col + 1]):
                edges.append((f"{row - 1},{col - 1}", f"{row - 1},{col}"))
            if ord(grid[row][col]) + 1 >= ord(grid[row][col - 1]):
                edges.append((f"{row - 1},{col - 1}", f"{row - 1},{col - 2}"))

    graph = build_graph(edges)
    path = BFS_SP(graph, f"{start[0]},{start[1]}", f"{end[0]},{end[1]}")
    return len(path) - 1


def part_b(data: list[str]) -> Union[int, str, None]:
    """Solution to part B.

    Args:
        data (list[str]): Advent of Code challenge input.

    Returns:
        Union[int, str, None]: Solution to the challenge.
    """
    grid: list[list[str]] = [["ö" for _ in range(len(data[0]) + 2)]]
    for row in data:
        cleaned = row.replace("S", "a").replace("E", "z")
        grid.append(["ö"] + list(cleaned) + ["ö"])
    grid.append(["ö" for _ in range(len(data[0]) + 2)])

    end = find_node(data, "E")
    edges: list[tuple[str, str]] = []
    for row in range(1, len(grid) - 1):
        for col in range(1, len(grid[row]) - 1):
            if ord(grid[row][col]) + 1 >= ord(grid[row + 1][col]):
                edges.append((f"{row - 1},{col - 1}", f"{row},{col - 1}"))
            if ord(grid[row][col]) + 1 >= ord(grid[row - 1][col]):
                edges.append((f"{row - 1},{col - 1}", f"{row - 2},{col - 1}"))
            if ord(grid[row][col]) + 1 >= ord(grid[row][col + 1]):
                edges.append((f"{row - 1},{col - 1}", f"{row - 1},{col}"))
            if ord(grid[row][col]) + 1 >= ord(grid[row][col - 1]):
                edges.append((f"{row - 1},{col - 1}", f"{row - 1},{col - 2}"))

    graph = build_graph(edges)
    starts = find_all_nodes(data, "a")
    min_path = -1
    for start in starts:
        path = BFS_SP(graph, f"{start[0]},{start[1]}", f"{end[0]},{end[1]}")
        if path is None:
            continue
        if min_path == -1 or len(path) - 1 < min_path:
            min_path = len(path) - 1
    return min_path
