# Advent of Code 2021 Day 25
# Author: Erik Båvenstrand
# URL: https://adventofcode.com/2021/day/25

import numpy as np


def step_east(grid: list[list[str]], rows: int, cols: int):
    n_moved = 0
    move_candidates = []
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == ">" and grid[r][(c + 1) % cols] == ".":
                move_candidates.append((r, c))
    for (r, c) in move_candidates:
        grid[r][c] = "."
        grid[r][(c + 1) % cols] = ">"
        n_moved += 1

    return n_moved


def step_south(grid: list[list[str]], rows: int, cols: int):
    n_moved = 0
    move_candidates = []
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "v" and grid[(r + 1) % rows][c] == ".":
                move_candidates.append((r, c))
    for (r, c) in move_candidates:
        grid[r][c] = "."
        grid[(r + 1) % rows][c] = "v"
        n_moved += 1

    return n_moved


def part_a(data: list[str]):
    grid = [list(line) for line in data]
    rows, cols = len(grid), len(grid[0])

    step = 0
    moved = -1
    while moved != 0:
        step += 1
        moved = step_east(grid, rows, cols)
        moved += step_south(grid, rows, cols)

    return step


def part_b(data: list[str]):
    return None
