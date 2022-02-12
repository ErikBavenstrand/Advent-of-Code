# Advent of Code 2021 Day 13
# Author: Erik Båvenstrand
# URL: https://adventofcode.com/2021/day/13

import numpy as np


def construct_paper_inst(data: list[str]):
    arr = []
    inst = []
    for line in data:
        if "fold along" in line:
            [dir, coord] = line.split(" ")[2].split("=")
            inst.append((dir, int(coord)))
        elif line != "":
            [x, y] = line.split(",")
            arr.append((int(x), int(y)))
    paper_coords = np.array(arr)
    paper_max_x = np.max(paper_coords[:, 0])
    paper_max_y = np.max(paper_coords[:, 1])
    paper = np.zeros((paper_max_y + 2, paper_max_x + 1))

    for x, y in paper_coords:
        paper[y, x] = 1

    return paper, inst


def part_a(data: list[str]):
    paper, inst = construct_paper_inst(data)
    for dir, coord in inst:
        if dir == "x":
            paper_left = paper[:, :coord]
            paper_right = paper[:, coord + 1:]
            paper_right = np.flip(paper_right, 1)
            paper = paper_left + paper_right
        else:
            paper_top = paper[:coord, :]
            paper_bottom = paper[coord + 1:, :]
            paper_bottom = np.flip(paper_bottom, 0)
            paper = paper_top + paper_bottom
        break

    return np.count_nonzero(paper)


def part_b(data: list[str]):
    paper, inst = construct_paper_inst(data)
    for dir, coord in inst:
        if dir == "x":
            paper_left = paper[:, :coord]
            paper_right = paper[:, coord + 1:]
            paper_right = np.flip(paper_right, 1)
            paper = paper_left + paper_right
        else:
            paper_top = paper[:coord, :]
            paper_bottom = paper[coord + 1:, :]
            paper_bottom = np.flip(paper_bottom, 0)
            paper = paper_top + paper_bottom

    for row in paper:
        row_str = ""
        for value in row:
            row_str += "#" if value > 0 else "."
        print(row_str)
    return None
