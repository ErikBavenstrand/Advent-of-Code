# Advent of Code 2015 Day 1
# Author: Erik Båvenstrand
# URL: https://adventofcode.com/2015/day/1

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
    data = get_data(day=1, year=2015).splitlines()

###############################################################################
# ██████╗  █████╗ ██████╗ ████████╗     ██╗                                   #
# ██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝    ███║                                   #
# ██████╔╝███████║██████╔╝   ██║       ╚██║                                   #
# ██╔═══╝ ██╔══██║██╔══██╗   ██║        ██║                                   #
# ██║     ██║  ██║██║  ██║   ██║        ██║                                   #
# ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝        ╚═╝                                   #
###############################################################################

data_a = list(data[0])
floor = 0
for (i, d) in enumerate(data_a):
    if d == "(":
        floor += 1
    elif d == ")":
        floor -= 1


answer_a = floor
print("Part a: " + str(answer_a))
if args.submit and not args.testcase and answer_a:
    submit(answer=answer_a, part="a", day=1, year=2015)
###############################################################################
# ██████╗  █████╗ ██████╗ ████████╗    ██████╗                                #
# ██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝    ╚════██╗                               #
# ██████╔╝███████║██████╔╝   ██║        █████╔╝                               #
# ██╔═══╝ ██╔══██║██╔══██╗   ██║       ██╔═══╝                                #
# ██║     ██║  ██║██║  ██║   ██║       ███████╗                               #
# ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝       ╚══════╝                               #
###############################################################################

data_b = list(data[0])
floor = 0
first_basement = None
for (i, d) in enumerate(data_b):
    if d == "(":
        floor += 1
    elif d == ")":
        floor -= 1
    if first_basement is None and floor == -1:
        first_basement = i + 1

answer_b = first_basement
print("Part b: " + str(answer_b))
if args.submit and not args.testcase and answer_b:
    submit(answer=answer_b, part="b", day=1, year=2015)
