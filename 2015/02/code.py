# Advent of Code 2015 Day 2
# Author: Erik Båvenstrand
# URL: https://adventofcode.com/2015/day/2

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
    data = get_data(day=2, year=2015).splitlines()

###############################################################################
# ██████╗  █████╗ ██████╗ ████████╗     ██╗                                   #
# ██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝    ███║                                   #
# ██████╔╝███████║██████╔╝   ██║       ╚██║                                   #
# ██╔═══╝ ██╔══██║██╔══██╗   ██║        ██║                                   #
# ██║     ██║  ██║██║  ██║   ██║        ██║                                   #
# ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝        ╚═╝                                   #
###############################################################################

total_length = 0
for present in data:
    dims = sorted([int(d) for d in present.split("x")])
    total_length += (3 * dims[0] * dims[1]) + \
        (2 * dims[1] * dims[2]) + (2 * dims[0] * dims[2])

answer_a = total_length
print("Part a: " + str(answer_a))
if args.submit and not args.testcase and answer_a:
    submit(answer=answer_a, part="a", day=2, year=2015)
###############################################################################
# ██████╗  █████╗ ██████╗ ████████╗    ██████╗                                #
# ██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝    ╚════██╗                               #
# ██████╔╝███████║██████╔╝   ██║        █████╔╝                               #
# ██╔═══╝ ██╔══██║██╔══██╗   ██║       ██╔═══╝                                #
# ██║     ██║  ██║██║  ██║   ██║       ███████╗                               #
# ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝       ╚══════╝                               #
###############################################################################

total_length = 0
for present in data:
    dims = sorted([int(d) for d in present.split("x")])
    total_length += (2 * dims[0]) + (2 * dims[1]) + \
        (dims[0] * dims[1] * dims[2])

answer_b = total_length
print("Part b: " + str(answer_b))
if args.submit and not args.testcase and answer_b:
    submit(answer=answer_b, part="b", day=2, year=2015)
