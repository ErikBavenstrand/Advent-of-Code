import argparse
import os
from datetime import date

parser = argparse.ArgumentParser()
parser.add_argument('--start',
                    default=2015, type=int)
parser.add_argument('--end',
                    default=date.today().year, type=int)
args = parser.parse_args()

base_dir = "./"
AUTHOR = "Erik Båvenstrand"  # Name automatically put in the code templates.

# DATE SPECIFIC PARAMETERS
years = range(args.start, args.end + 1)
days = range(1, 26)
link = "https://adventofcode.com/"


def mkdir_if_not_exist(path: str):
    if not os.path.exists(path):
        os.mkdir(path)
    return path


print("Setup will create working directories and files for Advent of Code.")

# Create base dir if it doesn't exist
mkdir_if_not_exist(base_dir)

for y in years:
    print(f"Year: {str(y)}")
    year_path = mkdir_if_not_exist(base_dir + str(y))
    for d in days:
        if d < 10:
            d = f"0{d}"
        day_path = mkdir_if_not_exist(os.path.join(year_path, str(d)))

        if not os.path.exists(os.path.join(day_path, "code.py")):
            with open(os.path.join(day_path, "code.py"), "w+") as f:
                f.write(f"""# Advent of Code {str(y)} Day {str(int(d))}
# Author: {AUTHOR}
# URL: https://adventofcode.com/{str(y)}/day/{str(int(d))}

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
    data = get_data(day={str(int(d))}, year={str(y)}).splitlines()

###############################################################################
# ██████╗  █████╗ ██████╗ ████████╗     ██╗                                   #
# ██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝    ███║                                   #
# ██████╔╝███████║██████╔╝   ██║       ╚██║                                   #
# ██╔═══╝ ██╔══██║██╔══██╗   ██║        ██║                                   #
# ██║     ██║  ██║██║  ██║   ██║        ██║                                   #
# ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝        ╚═╝                                   #
###############################################################################


answer_a = None
print("Part a: " + str(answer_a))
if args.submit and not args.testcase and answer_a:
    submit(answer=answer_a, part="a", day={str(int(d))}, year={str(y)})
###############################################################################
# ██████╗  █████╗ ██████╗ ████████╗    ██████╗                                #
# ██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝    ╚════██╗                               #
# ██████╔╝███████║██████╔╝   ██║        █████╔╝                               #
# ██╔═══╝ ██╔══██║██╔══██╗   ██║       ██╔═══╝                                #
# ██║     ██║  ██║██║  ██║   ██║       ███████╗                               #
# ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝       ╚══════╝                               #
###############################################################################


answer_b = None
print("Part b: " + str(answer_b))
if args.submit and not args.testcase and answer_b:
    submit(answer=answer_b, part="b", day={str(int(d))}, year={str(y)})
""")

        if not os.path.exists(os.path.join(day_path, "testcase.txt")):
            with open(os.path.join(day_path, "testcase.txt"), "w+") as f:
                pass

print("Setup complete : Advent of Code working directories \
and files initialized with success.")
