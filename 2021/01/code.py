# Advent of Code 2021 Day 01
# Author: Erik Båvenstrand
# URL: https://adventofcode.com/2021/day/1

def part_a(data: list[str]):
    previous_value = float("inf")
    counter = 0
    for line in data:
        current_value = int(line)
        if previous_value < current_value:
            counter += 1
        previous_value = current_value
    return counter


def part_b(data: list[str]):
    previous_value = float("inf")
    window = [float("inf"), float("inf"), float("inf")]
    window_idx = 0
    counter = 0
    for line in data:
        current_value = int(line)
        window[window_idx] = current_value
        window_idx = (window_idx + 1) % 3
        window_sum = sum(window)
        if previous_value < window_sum:
            counter += 1
        previous_value = window_sum
    return counter
