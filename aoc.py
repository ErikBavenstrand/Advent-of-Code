import argparse
import datetime
import importlib
import os
from time import time
from typing import Union

import aocd

curr_date = datetime.date.today()
curr_year = curr_date.year
curr_day = curr_date.day


def type_year(x: str) -> int:
    """Validate and transform year in string format to integer format.

    Args:
        x (str): Year in string format.

    Raises:
        ArgumentTypeError: Raises error if year is outside of valid bounds.

    Returns:
        int: Year in integer format.
    """
    n = int(x)
    if n < 2015 or n > curr_year:
        raise argparse.ArgumentTypeError(
            f"Year must be in the range [2015, {curr_year}]"
        )
    return n


def type_day(x: str) -> int:
    """Validate and transform day in string format to integer format.

    Args:
        x (str): Day in string format.

    Raises:
        ArgumentTypeError: Raises error if day is outside of valid bounds.

    Returns:
        int: Day in integer format.
    """
    n = int(x)
    if n < 1 or n > 25:
        raise argparse.ArgumentTypeError("Day must be in the range [1, 25]")
    return n


parser = argparse.ArgumentParser()
parser.add_argument("year", help="the year of the challange", type=type_year)
parser.add_argument("day", help="the day of the challange", type=type_day)
subparsers = parser.add_subparsers(dest="action", required=True)
parser_generate = subparsers.add_parser("generate")
parser_generate.add_argument(
    "-a",
    "--author",
    help="the author of the challenge solution",
    default="Erik Båvenstrand",
)
parser_test = subparsers.add_parser("test")
parser_solve = subparsers.add_parser("solve")
parser_solve.add_argument(
    "-s",
    "--submit",
    help="submit the answer to Advent of Code",
    action="store_true",
    default=False,
)
args = parser.parse_args()

if args.year == curr_year and args.day > curr_day:
    raise argparse.ArgumentTypeError(
        f"Day must be in the range [1, {curr_day}] for the current year"
    )

year_str = str(args.year)
day_str = str(args.day).zfill(2)

if args.action == "generate":
    print("Generating directories and files for Advent of Code.")
    print(f"Year: {year_str}, Day: {day_str}")

    def mkdir_if_not_exist(path: str) -> str:
        """Creates directory if it does not currently exist.

        Args:
            path (str): Path of the directory.

        Returns:
            str: Path of the directory.
        """
        if not os.path.exists(path):
            os.mkdir(path)
        return path

    year_path = mkdir_if_not_exist(year_str)
    day_path = mkdir_if_not_exist(os.path.join(year_path, day_str))
    if not os.path.exists(os.path.join(day_path, "code.py")):
        with open(os.path.join(day_path, "code.py"), "w+") as f:
            f.write(
                f"""# Advent of Code {year_str} Day {day_str}
# Author: {args.author}
# URL: https://adventofcode.com/{args.year}/day/{args.day}


def part_a(data: list[str]) -> int | str | None:
    \"\"\"Solution to part A.

    Args:
        data: Advent of Code challenge input.

    Returns:
        Solution to the challenge.
    \"\"\"
    return None


def part_b(data: list[str]) -> int | str | None:
    \"\"\"Solution to part B.

    Args:
        data: Advent of Code challenge input.

    Returns:
        Solution to the challenge.
    \"\"\"
    return None
"""
            )
    if not os.path.exists(os.path.join(day_path, "testcase.txt")):
        with open(os.path.join(day_path, "testcase.txt"), "w+") as f:
            pass

else:
    module = importlib.import_module(f"{year_str}.{day_str}.code")
    data = ""

    if args.action == "test":
        with open((os.path.join(year_str, day_str, "testcase.txt")), "r") as f:
            data = f.read().splitlines()
    else:
        data = aocd.get_data(day=args.day, year=args.year).splitlines()

    def output_answer(part: str, answer: Union[int, str, None], time: float) -> None:
        """Output the answer for the part and potentially submit it to Advent of Code.

        Args:
            part (str): Either 'a' or 'b'.
            answer (Union[int, str, None]): The answer to the challenge.
            time (float): Seconds elapsed for the calculation.
        """
        print(f"({time:.6f}s) Part {part}: {str(answer)}")
        if args.action == "solve" and args.submit and answer is not None:
            aocd.submit(answer=answer, part=part, day=args.day, year=args.year)

    start_time_a = time()
    res_part_a: Union[int, str, None] = module.part_a(data.copy())
    time_a = time() - start_time_a
    output_answer("a", res_part_a, time_a)

    start_time_b = time()
    res_part_b: Union[int, str, None] = module.part_b(data.copy())
    time_b = time() - start_time_b
    output_answer("b", res_part_b, time_b)
