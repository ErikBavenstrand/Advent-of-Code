# Advent of Code 2021 Day 07
# Author: Erik Båvenstrand
# URL: https://adventofcode.com/2021/day/7

import statistics


def part_a(data: list[str]):
    data_a = [int(d) for d in data[0].split(",")]
    target = int(statistics.median(data_a))

    fuel = 0
    for c in data_a:
        fuel += abs(c - target)

    return fuel


def part_b(data: list[str]):
    data_b = [int(d) for d in data[0].split(",")]
    targetFloor = int(statistics.mean(data_b))
    targetCeil = targetFloor + 1

    fuelFloor = 0
    fuelCeil = 0
    for c in data_b:
        lenFloor = abs(c - targetFloor)
        lenCeil = abs(c - targetCeil)
        fuelFloor += (lenFloor * (1 + lenFloor)) / 2
        fuelCeil += (lenCeil * (1 + lenCeil)) / 2

    return int(fuelFloor) if fuelFloor < fuelCeil else int(fuelCeil)
