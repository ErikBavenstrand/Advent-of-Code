# Advent of Code 2015 Day 3
# Author: Erik Båvenstrand
# URL: https://adventofcode.com/2015/day/3

import argparse
import os.path

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
    data = get_data(day=3, year=2015).splitlines()

###############################################################################
# ██████╗  █████╗ ██████╗ ████████╗     ██╗                                   #
# ██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝    ███║                                   #
# ██████╔╝███████║██████╔╝   ██║       ╚██║                                   #
# ██╔═══╝ ██╔══██║██╔══██╗   ██║        ██║                                   #
# ██║     ██║  ██║██║  ██║   ██║        ██║                                   #
# ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝        ╚═╝                                   #
###############################################################################

houses = dict()
curr_x = 0
curr_y = 0
houses[f"{curr_x}, {curr_y}"] = 1
for inst in list(data[0]):
    if inst == "<":
        curr_x -= 1
    elif inst == ">":
        curr_x += 1
    elif inst == "^":
        curr_y += 1
    elif inst == "v":
        curr_y -= 1
    houses[f"{curr_x}, {curr_y}"] = 1

answer_a = len(houses.items())
print("Part a: " + str(answer_a))
if args.submit and not args.testcase and answer_a:
    submit(answer=answer_a, part="a", day=3, year=2015)
###############################################################################
# ██████╗  █████╗ ██████╗ ████████╗    ██████╗                                #
# ██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝    ╚════██╗                               #
# ██████╔╝███████║██████╔╝   ██║        █████╔╝                               #
# ██╔═══╝ ██╔══██║██╔══██╗   ██║       ██╔═══╝                                #
# ██║     ██║  ██║██║  ██║   ██║       ███████╗                               #
# ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝       ╚══════╝                               #
###############################################################################

houses = dict()
santa_x = 0
santa_y = 0

robo_x = 0
robo_y = 0

houses[f"{santa_x}, {santa_y}"] = 1
is_robo_santa = False
for inst in list(data[0]):
    if is_robo_santa:
        if inst == "<":
            robo_x -= 1
        elif inst == ">":
            robo_x += 1
        elif inst == "^":
            robo_y += 1
        elif inst == "v":
            robo_y -= 1
        houses[f"{robo_x}, {robo_y}"] = 1

    else:
        if inst == "<":
            santa_x -= 1
        elif inst == ">":
            santa_x += 1
        elif inst == "^":
            santa_y += 1
        elif inst == "v":
            santa_y -= 1
        houses[f"{santa_x}, {santa_y}"] = 1

    is_robo_santa = not is_robo_santa

answer_b = len(houses.items())
print("Part b: " + str(answer_b))
if args.submit and not args.testcase and answer_b:
    submit(answer=answer_b, part="b", day=3, year=2015)
