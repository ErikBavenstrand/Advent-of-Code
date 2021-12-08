# Advent of Code 2021 Day 8
# Author: Erik Båvenstrand
# URL: https://adventofcode.com/2021/day/8

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
    data = get_data(day=8, year=2021).splitlines()

###############################################################################
# ██████╗  █████╗ ██████╗ ████████╗     ██╗                                   #
# ██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝    ███║                                   #
# ██████╔╝███████║██████╔╝   ██║       ╚██║                                   #
# ██╔═══╝ ██╔══██║██╔══██╗   ██║        ██║                                   #
# ██║     ██║  ██║██║  ██║   ██║        ██║                                   #
# ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝        ╚═╝                                   #
###############################################################################

count = 0
for line in data:
    line = line.split("|")[1]
    for val in line.split(" "):
        if len(val) in [7, 4, 3, 2]:
            count += 1

answer_a = count
print("Part a: " + str(answer_a))
if args.submit and not args.testcase and answer_a:
    submit(answer=answer_a, part="a", day=8, year=2021)
###############################################################################
# ██████╗  █████╗ ██████╗ ████████╗    ██████╗                                #
# ██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝    ╚════██╗                               #
# ██████╔╝███████║██████╔╝   ██║        █████╔╝                               #
# ██╔═══╝ ██╔══██║██╔══██╗   ██║       ██╔═══╝                                #
# ██║     ██║  ██║██║  ██║   ██║       ███████╗                               #
# ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝       ╚══════╝                               #
###############################################################################

total = 0
for patterns, outputs in [line.split("|") for line in data]:
    line = {len(pattern): set(pattern) for pattern in patterns.split()}

    num = ''
    for output in map(set, outputs.split()):
        # https://imgur.com/a/LIS2zZr use sets and pattern match
        match len(output), len(output & line[3]), len(output & line[4]):
            case 2, _, _: num += '1'
            case 3, _, _: num += '7'
            case 4, _, _: num += '4'
            case 7, _, _: num += '8'
            case 5, 3, _: num += '3'
            case 5, _, 3: num += '5'
            case 5, _, _: num += '2'
            case 6, _, 4: num += '9'
            case 6, 3, _: num += '0'
            case 6, _, _: num += '6'
    total += int(num)

answer_b = total
print("Part b: " + str(answer_b))
if args.submit and not args.testcase and answer_b:
    submit(answer=answer_b, part="b", day=8, year=2021)
