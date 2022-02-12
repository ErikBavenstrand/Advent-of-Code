# Advent of Code 2021 Day 06
# Author: Erik Båvenstrand
# URL: https://adventofcode.com/2021/day/6

def part_a(data: list[str]):
    data_a = data[0].split(",")

    n_fish = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    t_n_fish = n_fish.copy()
    for fish in data_a:
        n_fish[int(fish)] += 1

    for day in range(80):
        t_n_fish[0] = n_fish[1]
        t_n_fish[1] = n_fish[2]
        t_n_fish[2] = n_fish[3]
        t_n_fish[3] = n_fish[4]
        t_n_fish[4] = n_fish[5]
        t_n_fish[5] = n_fish[6]
        t_n_fish[6] = n_fish[7] + n_fish[0]
        t_n_fish[7] = n_fish[8]
        t_n_fish[8] = n_fish[0]

        n_fish = t_n_fish.copy()

    return sum(n_fish)


def part_b(data: list[str]):
    data_b = data[0].split(",")

    n_fish = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    t_n_fish = n_fish.copy()
    for fish in data_b:
        n_fish[int(fish)] += 1

    for day in range(256):
        t_n_fish[0] = n_fish[1]
        t_n_fish[1] = n_fish[2]
        t_n_fish[2] = n_fish[3]
        t_n_fish[3] = n_fish[4]
        t_n_fish[4] = n_fish[5]
        t_n_fish[5] = n_fish[6]
        t_n_fish[6] = n_fish[7] + n_fish[0]
        t_n_fish[7] = n_fish[8]
        t_n_fish[8] = n_fish[0]

        n_fish = t_n_fish.copy()

    return sum(n_fish)
