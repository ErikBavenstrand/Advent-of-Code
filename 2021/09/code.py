# Advent of Code 2021 Day 09
# Author: Erik Båvenstrand
# URL: https://adventofcode.com/2021/day/9

import numpy as np


def part_a(data: list[str]):
    def is_minimum(x, y, caves: np.ndarray):
        up = caves[x - 1, y]
        down = caves[x + 1, y]
        left = caves[x, y - 1]
        right = caves[x, y + 1]
        curr = caves[x, y]
        if curr < up and curr < down and curr < left and curr < right:
            return True
        else:
            return False

    caves = np.full((len(data) + 2, len(data[0]) + 2), 9, dtype=np.int32)
    valid_range = np.array(range(1, len(caves[0]) - 1))
    for i, line in enumerate(map(lambda l: np.array(list(map(int, list(l)))),
                                 data)):
        line = np.array(line)
        np.put(caves[i+1], valid_range, line)

    sum = 0
    lows = []
    for x in range(1, len(caves) - 1):
        for y in range(1, len(caves[0]) - 1):
            if is_minimum(x, y, caves):
                sum += 1 + caves[x, y]
                lows.append((x, y))

    return sum


def part_b(data: list[str]):

    def is_minimum(x, y, caves: np.ndarray):
        up = caves[x - 1, y]
        down = caves[x + 1, y]
        left = caves[x, y - 1]
        right = caves[x, y + 1]
        curr = caves[x, y]
        if curr < up and curr < down and curr < left and curr < right:
            return True
        else:
            return False

    caves = np.full((len(data) + 2, len(data[0]) + 2), 9, dtype=np.int32)
    valid_range = np.array(range(1, len(caves[0]) - 1))
    for i, line in enumerate(map(lambda l: np.array(list(map(int, list(l)))),
                                 data)):
        line = np.array(line)
        np.put(caves[i+1], valid_range, line)

    sum = 0
    lows = []
    for x in range(1, len(caves) - 1):
        for y in range(1, len(caves[0]) - 1):
            if is_minimum(x, y, caves):
                sum += 1 + caves[x, y]
                lows.append((x, y))

    basins = []
    for low in lows:
        q = [low]
        visited = set()
        while q:
            p = q.pop(0)

            for n in [(p[0] - 1, p[1]), (p[0] + 1, p[1]),
                      (p[0], p[1] - 1), (p[0], p[1]+1)]:
                if n in visited or caves[n[0], n[1]] == 9:
                    continue
                visited.add(n)
                q.append(n)
        basins.append(len(visited))
    basins = sorted(basins, reverse=True)
    prod = basins[0] * basins[1] * basins[2]

    return prod
