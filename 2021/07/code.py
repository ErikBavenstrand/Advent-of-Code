# Advent of Code 2021 Day 7
# Author: Erik Båvenstrand
# URL: https://adventofcode.com/2021/day/7

import argparse
import os.path
import statistics

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
    data = get_data(day=7, year=2021).splitlines()

###############################################################################
# ██████╗  █████╗ ██████╗ ████████╗     ██╗                                   #
# ██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝    ███║                                   #
# ██████╔╝███████║██████╔╝   ██║       ╚██║                                   #
# ██╔═══╝ ██╔══██║██╔══██╗   ██║        ██║                                   #
# ██║     ██║  ██║██║  ██║   ██║        ██║                                   #
# ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝        ╚═╝                                   #
###############################################################################

data_a = [int(d) for d in data[0].split(",")]
target = int(statistics.median(data_a))

fuel = 0
for c in data_a:
    fuel += abs(c - target)

answer_a = fuel
print("Part a: " + str(answer_a))
if args.submit and not args.testcase and answer_a:
    submit(answer=answer_a, part="a", day=7, year=2021)
###############################################################################
# ██████╗  █████╗ ██████╗ ████████╗    ██████╗                                #
# ██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝    ╚════██╗                               #
# ██████╔╝███████║██████╔╝   ██║        █████╔╝                               #
# ██╔═══╝ ██╔══██║██╔══██╗   ██║       ██╔═══╝                                #
# ██║     ██║  ██║██║  ██║   ██║       ███████╗                               #
# ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝       ╚══════╝                               #
###############################################################################

data_b = [int(d) for d in data[0].split(",")]
targetFloor = int(statistics.mean(data_b))
targetCeil = targetFloor + 1

fuelFloor = 0
fuelCeil = 0
for c in data_b:
    lenFloor = abs(c - targetFloor)
    lenCeil = abs(c - targetCeil)
    fuelFloor += (lenFloor * (1 + lenFloor)) / 2
    fuelCeil += (lenCeil * (1 + lenCeil)) / 2

answer_b = int(fuelFloor) if fuelFloor < fuelCeil else int(fuelCeil)
print("Part b: " + str(answer_b))
if args.submit and not args.testcase and answer_b:
    submit(answer=answer_b, part="b", day=7, year=2021)
