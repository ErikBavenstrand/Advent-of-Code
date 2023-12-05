import argparse
import datetime
import importlib
import os
from pathlib import Path
from time import time

import aocd
import click
from aocd.examples import Example
from aocd.models import Puzzle
from click import Context, Parameter

current_date = datetime.date.today()
current_year = current_date.year
current_day = current_date.day


def validate_year(_ctx: Context, _param: Parameter, value: str) -> int:
    """Validate and transform year in string format to integer format.

    Args:
        _ctx: Context, not used.
        _param: Parameter, not used.
        value: Year in string format.

    Raises:
        click.BadParameter: Raises error if year is outside of valid bounds or not a valid integer.

    Returns:
        Year in integer format.
    """
    try:
        n = int(value)
        if not 2015 <= n <= current_year:
            raise click.BadParameter(
                f"Year must be in the range [2015, {current_year}]"
            )
        return n
    except ValueError:
        raise click.BadParameter("Year must be a valid integer")


def validate_day(_ctx: Context, _param: Parameter, value: str) -> int:
    """Validate and transform day in string format to integer format.

    Args:
        _ctx: Context, not used.
        _param: Parameter, not used.
        value: Day in string format.

    Raises:
        click.BadParameter: Raises error if day is outside of valid bounds or not a valid integer.

    Returns:
        Day in integer format.
    """
    try:
        n = int(value)
        if not 1 <= n <= 25:
            raise click.BadParameter("Day must be in the range [1, 25]")
        return n
    except ValueError:
        raise click.BadParameter("Day must be a valid integer")


@click.group()
def cli():
    pass


@cli.command()
@click.argument(
    "year",
    type=click.IntRange(2015, current_year),
)
@click.argument(
    "day",
    type=click.IntRange(1, 25),
)
@click.option(
    "-a", "--author", default="Erik Båvenstrand", help="Author of the solution"
)
def generate(year: int, day: int, author: str) -> None:
    year_str, day_str = str(year), str(day).zfill(2)
    year_path = Path(os.getcwd()) / year_str
    day_path = year_path / day_str
    code_file_path = day_path / "code.py"
    testcase_file_path = day_path / "testcase.txt"

    year_path.mkdir(parents=True, exist_ok=True)
    day_path.mkdir(parents=True, exist_ok=True)

    if not code_file_path.exists():
        with open(code_file_path, "w+") as f:
            f.write(
                f"""# Advent of Code {year_str} Day {day_str}
# Author: {author}
# URL: https://adventofcode.com/{year_str}/day/{day}


def part_a(data: list[str]) -> int | str | None:
    \"\"\"Solution to part A.\"\"\"
    return None


def part_b(data):
    \"\"\"Solution to part B.\"\"\"
    return None
"""
            )

    if not testcase_file_path.exists():
        with open(testcase_file_path, "w+") as f:
            pass

    examples: list[Example] = Puzzle(year=year, day=day).examples
    for example in examples:
        print(example.answer_a)


'''
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

if args.year == current_year and args.day > current_day:
    raise argparse.ArgumentTypeError(
        f"Day must be in the range [1, {current_day}] for the current year"
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
'''

if __name__ == "__main__":
    cli()
