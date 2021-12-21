# Advent of Code 2021 Day 01
# Author: Erik Båvenstrand
# URL: https://adventofcode.com/2021/day/1

def part_a(data: list[str]):
    count = 0
    for i in range(len(data)):
        if i >= 1 and int(data[i]) > int(data[i-1]):
            count += 1
    return count


def part_b(data: list[str]):
    counter = 0
    for i in range(len(data)):
        if i >= 3 and int(data[i]) > int(data[i-3]):
            counter += 1
    return counter
