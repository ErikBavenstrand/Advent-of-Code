# Advent of Code 2021 Day 6
# Author: Erik Båvenstrand
# URL: https://adventofcode.com/2021/day/6

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
    data = get_data(day=6, year=2021).splitlines()

###############################################################################
# ██████╗  █████╗ ██████╗ ████████╗     ██╗                                   #
# ██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝    ███║                                   #
# ██████╔╝███████║██████╔╝   ██║       ╚██║                                   #
# ██╔═══╝ ██╔══██║██╔══██╗   ██║        ██║                                   #
# ██║     ██║  ██║██║  ██║   ██║        ██║                                   #
# ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝        ╚═╝                                   #
###############################################################################

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

answer_a = sum(n_fish)
print("Part a: " + str(answer_a))
if args.submit and not args.testcase and answer_a:
    submit(answer=answer_a, part="a", day=6, year=2021)
###############################################################################
# ██████╗  █████╗ ██████╗ ████████╗    ██████╗                                #
# ██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝    ╚════██╗                               #
# ██████╔╝███████║██████╔╝   ██║        █████╔╝                               #
# ██╔═══╝ ██╔══██║██╔══██╗   ██║       ██╔═══╝                                #
# ██║     ██║  ██║██║  ██║   ██║       ███████╗                               #
# ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝       ╚══════╝                               #
###############################################################################

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

answer_b = sum(n_fish)
print("Part b: " + str(answer_b))
if args.submit and not args.testcase and answer_b:
    submit(answer=answer_b, part="b", day=6, year=2021)
