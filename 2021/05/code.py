# Advent of Code 2021 Day 05
# Author: Erik Båvenstrand
# URL: https://adventofcode.com/2021/day/5

from collections import defaultdict


def part_a(data: list[str]):
    def get_coords_range(x1: str, y1: str, x2: str, y2: str) -> list[str]:
        coords = []

        dx = int(x2) - int(x1)
        dy = int(y2) - int(y1)
        if int(x1) == int(x2):
            if dy > 0:
                dy += 1
                for v in range(dy):
                    coords.append(f"{int(x1)}, {int(y1) + v}")
            else:
                dy -= 1
                for v in range(dy, 0):
                    coords.append(f"{int(x1)}, {int(y1) + v}")
        elif int(y1) == int(y2):
            if dx > 0:
                dx += 1
                for v in range(dx):
                    coords.append(f"{int(x1) + v}, {int(y1)}")
            else:
                dx -= 1
                for v in range(dx, 0):
                    coords.append(f"{int(x1) + v}, {int(y1)}")
        return coords

    vents = defaultdict(lambda: 0)

    for line in data:
        coords = line.split(" -> ")
        from_coord = coords[0].split(",")
        to_coord = coords[1].split(",")
        coords = get_coords_range(
            from_coord[0], from_coord[1], to_coord[0], to_coord[1])
        for c in coords:
            vents[c] += 1

    vents_list = vents.items()
    vent_numbers = map(lambda v: v[1], vents_list)

    return sum(v > 1 for v in list(vent_numbers))


def part_b(data: list[str]):
    def get_range(v: int):
        if v > 0:
            return range(v + 1)
        elif v < 0:
            return range(v, 1)
        return range(0)

    def get_coords_range_diag(x1: str, y1: str, x2: str, y2: str) -> list[str]:
        coords = []

        dx = int(x2) - int(x1)
        dy = int(y2) - int(y1)
        if int(x1) == int(x2):
            for v in get_range(dy):
                coords.append(f"{int(x1)}, {int(y1) + v}")
        elif int(y1) == int(y2):
            for v in get_range(dx):
                coords.append(f"{int(x1) + v}, {int(y1)}")
        else:
            dx_range = get_range(dx)
            dy_range = get_range(dy)

            if dx > 0 and dy < 0:
                dy_range = reversed(dy_range)
            elif dx < 0 and dy > 0:
                dx_range = reversed(dx_range)

            for (vx, vy) in zip(dx_range, dy_range):
                coords.append(f"{int(x1) + vx}, {int(y1) + vy}")
        return coords

    vents = defaultdict(lambda: 0)

    for line in data:
        coords = line.split(" -> ")
        from_coord = coords[0].split(",")
        to_coord = coords[1].split(",")
        coords = get_coords_range_diag(
            from_coord[0], from_coord[1], to_coord[0], to_coord[1])
        for c in coords:
            vents[c] += 1

    vents_list = vents.items()
    vent_numbers = map(lambda v: v[1], vents_list)

    return sum(v > 1 for v in list(vent_numbers))
