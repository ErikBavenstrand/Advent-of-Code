import argparse
import logging
import os
from datetime import date
from importlib import import_module

from aocd import get_data, submit

logger = logging.getLogger(__name__)

curr_date = date.today()
curr_year = curr_date.year
curr_day = curr_date.day


def year(x: str) -> int:
    n = int(x)
    if n < 2015 or n > curr_year:
        raise argparse.ArgumentTypeError(
            f"Year must be in the range [2015, {curr_year}]")
    return n


def day(x: str) -> int:
    n = int(x)
    if n < 1 or n > 25:
        raise argparse.ArgumentTypeError(
            "Day must be in the range [1, 25]")
    return n


parser = argparse.ArgumentParser()
parser.add_argument("year",
                    help="the command to be executed",
                    type=year,
                    )
parser.add_argument("day",
                    help="the command to be executed",
                    type=day,
                    )
group = parser.add_mutually_exclusive_group()
group.add_argument("-t, --testcase", dest="testcase",
                   action="store_true", default=False)
group.add_argument("-s, --submit", dest="submit",
                   action="store_true", default=False)
group.add_argument("-g, --generate", dest="generate",
                   action="store_true", default=False)
args = parser.parse_args()

# Sanity check the date
if args.year == curr_year and args.day > curr_day:
    raise argparse.ArgumentTypeError(
        f"Day must be in the range [1, {curr_day}] for the current year")


def submit_answer(part: str, answer):
    print(f"Part {part}: " + str(answer))
    if args.submit and not args.testcase and answer:
        submit(answer=answer, part=part, day=args.day, year=args.year)


# Generate files for day
if args.generate:
    BASE_DIR = "./"
    AUTHOR = "Erik Båvenstrand"

    def mkdir_if_not_exist(path: str):
        if not os.path.exists(path):
            os.mkdir(path)
        return path

    print("Generating directories and files for Advent of Code.")
    mkdir_if_not_exist(BASE_DIR)

    print(f"Year: {str(args.year)}, Day: {str(args.day).zfill(2)}")
    year_path = mkdir_if_not_exist(os.path.join(BASE_DIR, str(args.year)))
    day_path = mkdir_if_not_exist(
        os.path.join(year_path, str(args.day).zfill(2)))
    if not os.path.exists(os.path.join(day_path, "code.py")):
        with open(os.path.join(day_path, "code.py"), "w+") as f:
            f.write(f"""# Advent of Code {str(args.year)} Day {str(args.day).zfill(2)}
# Author: {AUTHOR}
# URL: https://adventofcode.com/{str(args.year)}/day/{str(args.day)}

def part_a(data: list[str]):
    return None


def part_b(data: list[str]):
    return None
""")
    if not os.path.exists(os.path.join(day_path, "testcase.txt")):
        with open(os.path.join(day_path, "testcase.txt"), "w+") as f:
            pass

else:
    # Import code of the day
    code = import_module(f"{str(args.year)}.{str(args.day).zfill(2)}.code")

    # Import data of the day
    data = ""
    if args.testcase:
        with open((os.path.join(str(args.year), str(args.day).zfill(2),
                                "testcase.txt")), "r") as f:
            data = f.read().splitlines()
    else:
        data = get_data(day=args.day, year=args.year).splitlines()

    res = code.part_a(data.copy())
    if type(res) == tuple:
        submit_answer("a", res[0])
        submit_answer("b", code.part_b(data.copy(), *res[1:]))
    else:
        submit_answer("a", res)
        submit_answer("b", code.part_b(data.copy()))
