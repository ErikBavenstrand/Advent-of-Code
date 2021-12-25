# Advent of Code 2021 Day 02
# Author: Erik Båvenstrand
# URL: https://adventofcode.com/2021/day/2

def part_a(data: list[str]):
    depth = 0
    forward = 0
    for direction, amount in [(line.split(" ")[0], int(line.split(" ")[1]))
                              for line in data]:
        match direction:
            case "forward":
                forward += amount
            case "down":
                depth += amount
            case "up":
                depth -= amount

    return forward * depth


def part_b(data: list[str]):
    depth = 0
    forward = 0
    aim = 0
    for direction, amount in [(line.split(" ")[0], int(line.split(" ")[1]))
                              for line in data]:
        match direction:
            case "forward":
                forward += amount
                depth += aim * amount
            case "down":
                aim += amount
            case "up":
                aim -= amount

    return forward * depth
