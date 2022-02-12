# Advent of Code 2021 Day 19
# Author: Erik Båvenstrand
# URL: https://adventofcode.com/2021/day/19


from collections import defaultdict
from itertools import combinations
from math import sqrt
from typing import Union


def get_scanners(data: list[str]):
    scanners: list[tuple[tuple[int, ...], ...]] = []
    curr_scanner: list[tuple[int, ...]] = []
    for line in data:
        if line == "":
            scanners.append(tuple(curr_scanner))
        elif line.startswith('---'):
            curr_scanner = []
        else:
            curr_scanner.append(tuple(map(int, line.split(","))))
    scanners.append(tuple(curr_scanner))
    return scanners


def distance(a: tuple[int, ...], b: tuple[int, ...]):
    dist = [a_i - b_i for a_i, b_i in zip(a, b)]
    return int(sqrt(sum(d ** 2 for d in dist)))


def manhattan_distance(a: tuple[int, ...], b: tuple[int, ...]):
    return int(sum([abs(a_i - b_i) for a_i, b_i in zip(a, b)]))


def get_relative_beacon_dist(beacons: Union[tuple[tuple[int, ...], ...],
                                            set[tuple[int, ...]]]):
    relative_dist: defaultdict[tuple[int, ...], set[int]] = defaultdict(set)
    for a in beacons:
        for b in beacons:
            relative_dist[a].add(distance(a, b))
        relative_dist[a].remove(0)

    return relative_dist


def get_n_overlapping_beacons(rel_dist_scanner1: defaultdict[tuple[int, ...],
                                                             set[int]],
                              rel_dist_scanner2: defaultdict[tuple[int, ...],
                                                             set[int]]):
    return max([
        len(rel_dist_scanner1[a].intersection(rel_dist_scanner2[b]))
        for a in rel_dist_scanner1
        for b in rel_dist_scanner2
    ])


def align(rel_dist_scanner1: defaultdict[tuple[int, ...],
                                         set[int]],
          rel_dist_scanner2: defaultdict[tuple[int, ...],
                                         set[int]],
          min_matches: int):
    matches: dict[tuple[int, ...], tuple[int, ...]] = {}
    for a in rel_dist_scanner1:
        for b in rel_dist_scanner2:
            if (len(rel_dist_scanner1[a].intersection(rel_dist_scanner2[b])) >=
                    min_matches - 1):
                matches[a] = b

    dims = len(list(matches)[0])

    # both views of the same points will have the exact same center of mass
    com_1 = [sum(m[dim] for m in matches.keys()) / len(matches.keys())
             for dim in range(dims)]
    com_2 = [sum(m[dim] for m in matches.values()) / len(matches.values())
             for dim in range(dims)]

    a = list(matches.keys())[0]
    b = matches[a]

    a_mod = [round(a[d] - com_1[d]) for d in range(dims)]
    b_mod = [round(b[d] - com_2[d]) for d in range(dims)]

    rotation: dict[int, tuple[int, int]] = {}
    for i in range(dims):
        idx = [abs(v) for v in b_mod].index(abs(a_mod[i]))
        rotation[i] = (idx,  1 if a_mod[i] * b_mod[idx] >= 0 else -1)

    b_rot = [b[rotation[d][0]] * rotation[d][1] for d in range(dims)]

    translation = [int(a[d] - b_rot[d]) for d in range(dims)]

    return rotation, translation


def tranform_beacons(rotation: dict[int, tuple[int, int]],
                     translation: list[int],
                     beacons: tuple[tuple[int, ...], ...]):
    dims = len(list(translation))
    transformed_beacons: set[tuple[int, ...]] = set()
    for b in beacons:
        transformed_beacons.add(
            tuple(b[rotation[d][0]] * rotation[d][1] + translation[d]
                  for d in range(dims)))

    return transformed_beacons


def part_a(data: list[str]):
    scanners = get_scanners(data)
    grid = set(scanners.pop(0))

    rel_dist = {b: get_relative_beacon_dist(b) for b in scanners}

    while scanners:
        grid_rel_dist = get_relative_beacon_dist(grid)
        beacons_overlapping = [
            get_n_overlapping_beacons(grid_rel_dist, rel_dist[b])
            for b in scanners
        ]

        s = beacons_overlapping.index(max(beacons_overlapping))

        rotation, translation = align(grid_rel_dist, rel_dist[scanners[s]], 12)

        grid.update(tranform_beacons(rotation, translation, scanners[s]))

        del scanners[s]

    return len(grid)


def part_b(data: list[str]):
    scanners = get_scanners(data)
    grid = set(scanners.pop(0))

    rel_dist = {b: get_relative_beacon_dist(b) for b in scanners}

    rel_scanner_pos: list[tuple[int, ...]] = []
    while scanners:
        grid_rel_dist = get_relative_beacon_dist(grid)
        beacons_overlapping = [
            get_n_overlapping_beacons(grid_rel_dist, rel_dist[b])
            for b in scanners
        ]

        s = beacons_overlapping.index(max(beacons_overlapping))

        rotation, translation = align(grid_rel_dist, rel_dist[scanners[s]], 12)
        rel_scanner_pos.append(tuple(translation))

        grid.update(tranform_beacons(rotation, translation, scanners[s]))

        del scanners[s]

    max_scanner_dist = max([manhattan_distance(s1, s2)
                            for s1, s2 in combinations(rel_scanner_pos, 2)])

    return max_scanner_dist
