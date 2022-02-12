# Advent of Code 2021 Day 17
# Author: Erik Båvenstrand
# URL: https://adventofcode.com/2021/day/17

import re


def get_coords(data: list[str]):
    regex = re.compile(r"=|,|\..")
    res = re.split(regex, data[0])
    return int(res[1]), int(res[2]), int(res[4]), int(res[5])


def part_a(data: list[str]):
    _, _, y1, _ = get_coords(data)
    return y1 * (y1 + 1) // 2


def part_b(data: list[str]):
    x1, x2, y1, y2 = get_coords(data)

    def simulate(dx: int, dy: int):
        px = py = 0
        while dy >= y1:
            px += dx
            py += dy
            if x1 <= px <= x2 and y1 <= py <= y2:
                return 1
            dx -= 1 if dx > 0 else 0
            dy -= 1
        return 0
    count = sum(simulate(dx, dy) for dx in range(1, x2 + 1)
                for dy in range(y1, -y1))

    return count
