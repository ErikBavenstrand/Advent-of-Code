# Advent of Code 2021 Day 5
# Author: Erik Båvenstrand
# URL: https://adventofcode.com/2021/day/5

import argparse
import os.path
from collections import defaultdict

from aocd import get_data, submit

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
group.add_argument("-t, --testcase", dest="testcase", action="store_true")
group.add_argument("-s, --submit", dest="submit", action="store_true")
parser.set_defaults(testcase=False, submit=False)
args = parser.parse_args()

data = ""
if args.testcase:
    with open((os.path.join(os.path.dirname(__file__),
                            "testcase.txt")), "r") as f:
        data = f.read().splitlines()
else:
    data = get_data(day=5, year=2021).splitlines()

###############################################################################
# ██████╗  █████╗ ██████╗ ████████╗     ██╗                                   #
# ██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝    ███║                                   #
# ██████╔╝███████║██████╔╝   ██║       ╚██║                                   #
# ██╔═══╝ ██╔══██║██╔══██╗   ██║        ██║                                   #
# ██║     ██║  ██║██║  ██║   ██║        ██║                                   #
# ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝        ╚═╝                                   #
###############################################################################


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
a = sum(v > 1 for v in list(vent_numbers))

answer_a = a
print("Part a: " + str(answer_a))
if args.submit and not args.testcase and answer_a:
    submit(answer=answer_a, part="a", day=5, year=2021)
###############################################################################
# ██████╗  █████╗ ██████╗ ████████╗    ██████╗                                #
# ██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝    ╚════██╗                               #
# ██████╔╝███████║██████╔╝   ██║        █████╔╝                               #
# ██╔═══╝ ██╔══██║██╔══██╗   ██║       ██╔═══╝                                #
# ██║     ██║  ██║██║  ██║   ██║       ███████╗                               #
# ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝       ╚══════╝                               #
###############################################################################


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
b = sum(v > 1 for v in list(vent_numbers))

answer_b = b
print("Part b: " + str(answer_b))
if args.submit and not args.testcase and answer_b:
    submit(answer=answer_b, part="b", day=5, year=2021)
