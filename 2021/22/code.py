# Advent of Code 2021 Day 22
# Author: Erik Båvenstrand
# URL: https://adventofcode.com/2021/day/22

import re
from collections import Counter


def get_cube_instruction(line: str, val_range: tuple[int, int] = None):
    on = line.split(" ")[0] == "on"
    cube = tuple(map(int, re.findall(r"-?\d+", line)))
    if val_range is not None:
        cube = tuple([min(max(val, val_range[0]), val_range[1])
                     for val in cube])
        cube_itr = iter(cube)
        if any(p1 == p2 for (p1, p2) in zip(cube_itr, cube_itr)):
            cube = None

    return on, cube


def get_intersection(c1: tuple[int, ...], c2: tuple[int, ...]):
    ranges: list[list[int]] = []
    ic1 = iter(c1)
    ic2 = iter(c2)
    for p1, p2, q1, q2 in zip(ic1, ic1, ic2, ic2):
        ranges.append([max(p1, q1), min(p2, q2)])

    if all(p1 <= p2 for (p1, p2) in ranges):
        return tuple(v for sublist in ranges for v in sublist)
    else:
        return None


def part_a(data: list[str]):
    cubes = Counter()
    for line in data:
        on, cube = get_cube_instruction(line, val_range=(-50, 50))
        if cube is None:
            continue
        diff = Counter()
        for existing_cube, count in cubes.items():
            intersection = get_intersection(cube, existing_cube)
            if intersection is not None:
                diff[intersection] -= count

        if on:
            diff[cube] += 1
        cubes.update(diff)
    n_active_cubes = sum((x1 - x0 + 1) * (y1 - y0 + 1) * (z1 - z0 + 1) * sgn
                         for (x0, x1, y0, y1, z0, z1), sgn in cubes.items())
    return n_active_cubes


def part_b(data: list[str]):
    cubes = Counter()
    for line in data:
        on, cube = get_cube_instruction(line)
        if cube is not None:
            diff = Counter()
            for existing_cube, count in cubes.items():
                intersection = get_intersection(cube, existing_cube)
                if intersection is not None:
                    diff[intersection] -= count

            if on:
                diff[cube] += 1
            cubes.update(diff)
    n_active_cubes = sum((x1 - x0 + 1) * (y1 - y0 + 1) * (z1 - z0 + 1) * sgn
                         for (x0, x1, y0, y1, z0, z1), sgn in cubes.items())
    return n_active_cubes
