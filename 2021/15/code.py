# Advent of Code 2021 Day 15
# Author: Erik Båvenstrand
# URL: https://adventofcode.com/2021/day/15

from collections import defaultdict
from queue import PriorityQueue

import numpy as np


class Graph:
    def __init__(self):
        self.edges = defaultdict(list)
        self.weights = {}

    def add_edge(self, from_node, to_node, weight):
        self.edges[from_node].append(to_node)
        self.weights[(from_node, to_node)] = weight

    def dijsktra(self, start, end):
        queue = PriorityQueue()
        queue.put((start, 0))
        distances = defaultdict(lambda: float('inf'))
        distances[start] = 0

        while not queue.empty():
            node, dist = queue.get()

            if node == end:
                return dist

            if distances[node] < dist:
                continue

            neighbors = self.edges[node]
            for n in neighbors:
                new_d = dist + self.weights[node, n]
                if distances[n] > new_d:
                    distances[n] = new_d
                    queue.put((n, new_d))
        return None


def part_a(data: list[str]):
    graph = Graph()
    grid = np.array([list(line) for line in data], dtype=np.uint8)
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if row > 0:
                graph.add_edge((row, col), (row - 1, col), grid[row - 1, col])
            if col > 0:
                graph.add_edge((row, col), (row, col - 1), grid[row, col - 1])
            if row < len(grid) - 1:
                graph.add_edge((row, col), (row + 1, col), grid[row + 1, col])
            if col < len(grid[0]) - 1:
                graph.add_edge((row, col), (row, col + 1), grid[row, col + 1])
    cost = graph.dijsktra((0, 0), (len(grid) - 1, len(grid[0]) - 1))
    return cost


def part_b(data: list[str]):
    graph = Graph()
    grid_tl = np.array([list(line) for line in data], dtype=np.uint8)
    grid = np.zeros((len(grid_tl) * 5, len(grid_tl[0]) * 5), dtype=np.uint8)

    for i in range(5):
        for j in range(5):
            grid[i * len(grid_tl): (i + 1) * len(grid_tl), j *
                 len(grid_tl[0]): (j + 1) * len(grid_tl[0])] = ((grid_tl + j + i) % 9)
    grid[grid == 0] = 9

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if row > 0:
                graph.add_edge((row, col), (row - 1, col), grid[row - 1, col])
            if col > 0:
                graph.add_edge((row, col), (row, col - 1), grid[row, col - 1])
            if row < len(grid) - 1:
                graph.add_edge((row, col), (row + 1, col), grid[row + 1, col])
            if col < len(grid[0]) - 1:
                graph.add_edge((row, col), (row, col + 1), grid[row, col + 1])
    cost = graph.dijsktra((0, 0), (len(grid) - 1, len(grid[0]) - 1))
    return cost
