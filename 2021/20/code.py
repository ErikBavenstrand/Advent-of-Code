# Advent of Code 2021 Day 20
# Author: Erik Båvenstrand
# URL: https://adventofcode.com/2021/day/20

import numpy as np
from scipy.ndimage import convolve


def part_a(data: list[str]):
    n = 2
    key, _, *img = data
    key = np.array([int(v == "#") for v in key])
    img = np.array([[int(v == "#") for v in line] for line in img])
    img = np.pad(np.array(img, dtype=int), n)
    kernel = np.array([[1, 2, 4], [8, 16, 32], [64, 128, 256]])

    for _ in range(n):
        img = key[convolve(img, kernel)]

    return img.sum()


def part_b(data: list[str]):
    n = 50
    key, _, *img = data
    key = np.array([int(v == "#") for v in key])
    img = np.array([[int(v == "#") for v in line] for line in img])
    img = np.pad(np.array(img, dtype=int), n)
    kernel = np.array([[1, 2, 4], [8, 16, 32], [64, 128, 256]])

    for _ in range(n):
        img = key[convolve(img, kernel)]

    return img.sum()
