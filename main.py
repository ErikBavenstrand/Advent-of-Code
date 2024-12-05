import datetime
import importlib
from pathlib import Path
from time import time
from typing import Literal

import aocd
import click
from jinja2 import Environment, FileSystemLoader

BASE_DIR = Path(__file__).resolve().parent
PROGRESS_MARKDOWN_FILE = BASE_DIR / "PROGRESS.md"
TEMPLATE_DIR = BASE_DIR / "templates"
SOLUTION_TEMPLATE_FILE = "solution_template.py.j2"
TESTS_TEMPLATE_FILE = "tests_template.py.j2"


CURRENT_DATE = datetime.date.today()
CURRENT_YEAR = CURRENT_DATE.year
CURRENT_DAY = CURRENT_DATE.day


@click.group()
def cli():
    """CLI for Advent of Code."""
    pass


@cli.command()
@click.argument("year", type=click.IntRange(2015, CURRENT_YEAR))
@click.argument("day", type=click.IntRange(1, 25))
@click.option("-a", "--author", default="Erik Båvenstrand", help="Author of the solution.")
def generate(year: int, day: int, author: str) -> None:
    """Generate a new solution file for a specific day of the Advent of Code challenge."""
    if year == CURRENT_YEAR and day > CURRENT_DAY:
        raise click.BadParameter(
            f"Day must be in the range [1, {CURRENT_DAY}] for the current year.",
            param_hint="day",
        )

    year_str = str(year)
    day_str = str(day).zfill(2)

    year_path = BASE_DIR / year_str
    day_path = year_path / day_str
    tests_path = day_path / "test_cases"
    Path(year_path).mkdir(parents=True, exist_ok=True)
    Path(day_path).mkdir(parents=True, exist_ok=True)
    Path(tests_path).mkdir(parents=True, exist_ok=True)

    solution_file = day_path / "solution.py"
    tests_file = day_path / "tests.py"

    env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))

    init_file = day_path / "__init__.py"
    if not init_file.exists():
        init_file.touch()

    if not solution_file.exists():
        template = env.get_template(SOLUTION_TEMPLATE_FILE)
        with open(solution_file, "w+") as f:
            f.write(template.render(year=year, day=day, author=author))

    if not tests_file.exists():
        template = env.get_template(TESTS_TEMPLATE_FILE)
        with open(tests_file, "w+") as f:
            f.write(template.render(year=year, day=day))

    update_readme_table()
    click.echo(f"Generated files for Year {year}, Day {day}.")


@cli.command()
@click.argument("year", type=click.IntRange(2015, CURRENT_YEAR))
@click.argument("day", type=click.IntRange(1, 25))
@click.argument("part", type=click.Choice(["a", "b"]))
@click.option(
    "-c",
    "--case-id",
    type=int,
    help="Test case ID to modify (skip if adding a new test case).",
)
def manage_test_case(year: int, day: int, part: Literal["a", "b"], case_id: int | None) -> None:
    """Manage test cases for a specific day of the Advent of Code challenge."""
    if year == CURRENT_YEAR and day > CURRENT_DAY:
        raise click.BadParameter(f"Day must be in the range [1, {CURRENT_DAY}] for the current year.")

    year_str = str(year)
    day_str = str(day).zfill(2)

    solution_file = BASE_DIR / year_str / day_str / "solution.py"
    if not solution_file.exists():
        raise click.ClickException(
            f"Solution file for year {year}, day {day} does not exist. Please generate it first."
        )

    test_cases_path = BASE_DIR / year_str / day_str / "test_cases"
    Path(test_cases_path).mkdir(parents=True, exist_ok=True)

    if case_id is None:
        existing_files = sorted(test_cases_path.glob("input_*.txt"))
        case_id = len(existing_files) + 1

    input_file = test_cases_path / f"input_{case_id}.txt"
    output_a_file = test_cases_path / f"output_{case_id}_a.txt" if part != "b" else None
    output_b_file = test_cases_path / f"output_{case_id}_b.txt" if part != "a" else None

    if not input_file.exists():
        click.echo(f"Input for test case {case_id} is missing. Please enter the input data.")
        input_data = click.edit(require_save=True)

        if input_data is None:
            raise click.ClickException("No input data entered. Aborting.")

        input_data = input_data.strip()
        input_file.write_text(input_data)

    if part == "a":
        if output_a_file is not None and not output_a_file.exists():
            expected_a = click.prompt("Enter the expected output for part A", type=str)
            output_a_file.write_text(expected_a)

    if part == "b":
        if output_b_file is not None and not output_b_file.exists():
            expected_b = click.prompt("Enter the expected output for part B", type=str)
            output_b_file.write_text(expected_b)

    test_code_path = BASE_DIR / year_str / day_str / "tests.py"
    with test_code_path.open("a") as f:
        f.write(f"""

def test_part_{part}_{case_id}() -> None:
    {"input_data, expected_a, _" if part == "a" else "input_data, _, expected_b"} = load_test_case({case_id})
{"    assert str(part_a(input_data.splitlines())) == expected_a" if part == "a" else ""}
{"    assert str(part_b(input_data.splitlines())) == expected_b" if part == "b" else ""}""")

    click.echo(f"Test case {case_id} {'modified' if case_id else 'added'} for part {part}, day {day}, year {year}.")


@cli.command()
@click.argument("year", type=click.IntRange(2015, CURRENT_YEAR))
@click.argument("day", type=click.IntRange(1, 25))
@click.option("-s", "--submit", is_flag=True, help="Submit the answer to Advent of Code.")
def solve(year: int, day: int, submit: bool) -> None:
    """Solve a specific day of the Advent of Code challenge."""
    if year == CURRENT_YEAR and day > CURRENT_DAY:
        raise click.BadParameter(f"Day must be in the range [1, {CURRENT_DAY}] for the current year.")

    year_str = str(year)
    day_str = str(day).zfill(2)

    try:
        solution = importlib.import_module(f"{year_str}.{day_str}.solution")
    except ModuleNotFoundError:
        click.echo(
            f"Solution module not found for Year {year}, Day {day}. Ensure you have generated it.",
            err=True,
        )
        return

    data = aocd.get_data(day=day, year=year).splitlines()
    submission_success = {"a": False, "b": False}
    results = {}

    def output_answer(part: Literal["a", "b"], answer: int | str | None, elapsed: float | None):
        if answer is not None and elapsed is not None:
            click.echo(f"({elapsed:.6f}s) Part {part}: {answer}")
        if submit and answer is not None:
            try:
                aocd.submit(answer=answer, part=part, day=day, year=year)  # type: ignore
                submission_success[part] = True
                results[part] = answer
            except aocd.AocdError as e:
                click.echo(f"Submission failed for Part {part}: {e}", err=True)

    start_time_a = time()
    res_part_a = solution.part_a(data.copy())
    elapsed_a = time() - start_time_a if res_part_a is not None else None
    output_answer("a", res_part_a, elapsed_a)

    start_time_b = time()
    res_part_b = solution.part_b(data.copy())
    elapsed_b = time() - start_time_b if res_part_b is not None else None
    output_answer("b", res_part_b, elapsed_b)

    document_submission(year, day, elapsed_a, elapsed_b)


def update_readme_table():
    """Update the PROGRESS.md file with missing days."""
    if not PROGRESS_MARKDOWN_FILE.exists():
        with open(PROGRESS_MARKDOWN_FILE, "w") as f:
            f.write("# Advent of Code Progress\n\n")
            f.write("| Year | Day | Status | Part A | Part B | Submission Time |\n")
            f.write("| ---- | --- | ------ | ------ | ------ | --------------- |\n")

    with open(PROGRESS_MARKDOWN_FILE, "r+") as f:
        lines = f.readlines()
        header, rows = lines[:4], lines[4:]
        existing_dates = [(year.strip(), day.strip()) for (year, day) in [row.split("|")[1:3] for row in rows]]
        missing_dates = [
            f"| {year} | {str(day).zfill(2)} | ❌ | | | |\n"
            for year in range(2015, CURRENT_YEAR + 1)
            for day in range(1, 26)
            if (str(year), str(day).zfill(2)) not in existing_dates and (year < CURRENT_YEAR or day <= CURRENT_DAY)
        ]
        rows.extend(missing_dates)
        rows.sort(reverse=True)
        f.seek(0)
        f.truncate()
        f.writelines(header + rows)


def document_submission(year: int, day: int, elapsed_a: float | None, elapsed_b: float | None):
    """Document the submission in the PROGRESS.md file.

    Args:
        year: The year of the submission.
        day: The day of the submission.
        elapsed_a: The time taken to solve part A.
        elapsed_b: The time taken to solve part B.
    """
    update_readme_table()
    submission_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    elapsed_a_str = f"{elapsed_a:.6f}s" if elapsed_a is not None else ""
    elapsed_b_str = f"{elapsed_b:.6f}s" if elapsed_b is not None else ""
    status_icon = "✅" if elapsed_a is not None and elapsed_b is not None else "🔄"
    entry = (
        f"| {year} | {str(day).zfill(2)} | {status_icon} | {elapsed_a_str} | {elapsed_b_str} | {submission_time} |\n"
    )

    with open(PROGRESS_MARKDOWN_FILE, "r+") as f:
        lines = f.readlines()
        header, rows = lines[:4], lines[4:]
        rows = [row for row in rows if not row.startswith(f"| {year} | {str(day).zfill(2)} |")]
        rows.append(entry)
        rows.sort(reverse=True)
        f.seek(0)
        f.truncate()
        f.writelines(header + rows)


if __name__ == "__main__":
    cli()
