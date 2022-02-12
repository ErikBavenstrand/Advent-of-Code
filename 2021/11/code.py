# Advent of Code 2021 Day 11
# Author: Erik Båvenstrand
# URL: https://adventofcode.com/2021/day/11

import numpy as np


def part_a(data: list[str]):
    grid = np.empty((len(data), len(data)), int)
    for i, line in enumerate(data):
        grid[i] = list(line)

    flashes = 0
    for day in range(100):
        grid += 1
        chaining = True
        flashed = set()
        while chaining:
            rows, cols = np.where(grid > 9)
            for i, (r, c) in enumerate(zip(rows, cols)):
                if (r, c) in flashed:
                    rows[i] = -1
                    cols[i] = -1
                flashed.add((r, c))
            if np.sum(rows > -1) == 0:
                chaining = False

            for r, c in zip(rows, cols):
                if r == -1 and c == -1:
                    continue
                if r > 0:
                    grid[r-1, c] += 1
                if r < len(data) - 1:
                    grid[r+1, c] += 1
                if c > 0:
                    grid[r, c-1] += 1
                if c < len(data) - 1:
                    grid[r, c+1] += 1
                if r > 0 and c > 0:
                    grid[r-1, c-1] += 1
                if r < len(data) - 1 and c < len(data) - 1:
                    grid[r+1, c+1] += 1
                if c > 0 and r < len(data) - 1:
                    grid[r+1, c-1] += 1
                if c < len(data) - 1 and r > 0:
                    grid[r-1, c+1] += 1

        coords = list(flashed)
        for row, col in coords:
            grid[row, col] = 0
        flashes += len(coords)

    return flashes


def part_b(data: list[str]):
    grid = np.empty((len(data), len(data)), int)
    for i, line in enumerate(data):
        grid[i] = list(line)

    mega_day = 0
    day = 0
    while mega_day == 0:
        grid += 1
        chaining = True
        flashed = set()
        while chaining:
            rows, cols = np.where(grid > 9)
            for i, (r, c) in enumerate(zip(rows, cols)):
                if (r, c) in flashed:
                    rows[i] = -1
                    cols[i] = -1
                flashed.add((r, c))
            if np.sum(rows > -1) == 0:
                chaining = False

            for r, c in zip(rows, cols):
                if r == -1 and c == -1:
                    continue
                if r > 0:
                    grid[r-1, c] += 1
                if r < len(data) - 1:
                    grid[r+1, c] += 1
                if c > 0:
                    grid[r, c-1] += 1
                if c < len(data) - 1:
                    grid[r, c+1] += 1
                if r > 0 and c > 0:
                    grid[r-1, c-1] += 1
                if r < len(data) - 1 and c < len(data) - 1:
                    grid[r+1, c+1] += 1
                if c > 0 and r < len(data) - 1:
                    grid[r+1, c-1] += 1
                if c < len(data) - 1 and r > 0:
                    grid[r-1, c+1] += 1

        coords = list(flashed)
        for row, col in coords:
            grid[row, col] = 0
        if len(coords) == len(data)**2:
            mega_day = day + 1
        day += 1

    return mega_day
