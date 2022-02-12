# Advent of Code 2021 Day 08
# Author: Erik Båvenstrand
# URL: https://adventofcode.com/2021/day/8

def part_a(data: list[str]):
    count = 0
    for line in data:
        line = line.split("|")[1]
        for val in line.split(" "):
            if len(val) in [7, 4, 3, 2]:
                count += 1

    return count


def part_b(data: list[str]):
    total = 0
    for patterns, outputs in [line.split("|") for line in data]:
        line = {len(pattern): set(pattern) for pattern in patterns.split()}

        num = ''
        for output in map(set, outputs.split()):
            # https://imgur.com/a/LIS2zZr use sets and pattern match
            match len(output), len(output & line[3]), len(output & line[4]):
                case 2, _, _: num += '1'
                case 3, _, _: num += '7'
                case 4, _, _: num += '4'
                case 7, _, _: num += '8'
                case 5, 3, _: num += '3'
                case 5, _, 3: num += '5'
                case 5, _, _: num += '2'
                case 6, _, 4: num += '9'
                case 6, 3, _: num += '0'
                case 6, _, _: num += '6'
        total += int(num)

    return total
