# Advent of Code 2021 Day 14
# Author: Erik Båvenstrand
# URL: https://adventofcode.com/2021/day/14

from collections import defaultdict


def get_solution(data: list[str], day: int):
    template = list(data[0])
    rules = dict()
    for line in data[2:]:
        inst = line.split(" -> ")
        rules[tuple(inst[0])] = inst[1]

    pairs = defaultdict(int)
    for a, b in zip(template, template[1:]):
        pairs[(a, b)] += 1

    chars = defaultdict(int)
    for a in template:
        chars[a] += 1

    for _ in range(day):
        for (a, b), c in pairs.copy().items():
            x = rules[a, b]
            pairs[a, b] -= c
            pairs[a, x] += c
            pairs[x, b] += c
            chars[x] += c

    return max(chars.values()) - min(chars.values())


def part_a(data: list[str]):
    return get_solution(data, 10)


def part_b(data: list[str]):
    return get_solution(data, 40)
