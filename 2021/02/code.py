# Advent of Code 2021 Day 02
# Author: Erik Båvenstrand
# URL: https://adventofcode.com/2021/day/2

def part_a(data: list[str]):
    depth = 0
    forward = 0
    for line in data:
        if "forward" in line:
            forward += int(line.split(" ")[1])
        elif "down" in line:
            depth += int(line.split(" ")[1])
        elif "up" in line:
            depth -= int(line.split(" ")[1])

    return forward * depth


def part_b(data: list[str]):
    depth = 0
    forward = 0
    aim = 0
    for line in data:
        if "forward" in line:
            forward += int(line.split(" ")[1])
            depth += aim * int(line.split(" ")[1])
        elif "down" in line:
            aim += int(line.split(" ")[1])
        elif "up" in line:
            aim -= int(line.split(" ")[1])

    return forward * depth
