import datetime
import json
from pathlib import Path
from typing import Literal, TypedDict

PROGRESS_JSON_FILE = Path("progress.json")
PROGRESS_MARKDOWN_FILE = Path("PROGRESS.md")

CURRENT_DATE = datetime.date.today()
CURRENT_YEAR = CURRENT_DATE.year
CURRENT_DAY = CURRENT_DATE.day


class SolutionProgress(TypedDict):
    """A dictionary containing the progress of a solution."""

    status: Literal["✅", "🔄", "❌"]
    """The status of the solution."""
    elapsed_a: float | None
    """The time it took to solve part A."""
    elapsed_b: float | None
    """The time it took to solve part B."""
    submission_time: str | None
    """The time the solution was submitted."""


ProgressDataType = dict[str, dict[str, SolutionProgress]]
"""A dictionary containing the progress of all solutions."""


def load_progress() -> ProgressDataType:
    """Load the progress of all solutions.

    Returns:
        A dictionary containing the progress of all solutions.
    """
    if not PROGRESS_JSON_FILE.exists():
        return {}

    with PROGRESS_JSON_FILE.open("r") as f:
        return json.load(f)


def save_progress(progress: ProgressDataType) -> None:
    """Save the progress of all solutions.

    Args:
        progress: A dictionary containing the progress of all solutions.
    """
    with PROGRESS_JSON_FILE.open("w") as f:
        json.dump(progress, f, indent=4)


def update_progress_json() -> None:
    """Update the progress JSON file with all days from 2015 to the current day."""
    progress = load_progress()
    for year in range(2015, CURRENT_YEAR + 1):
        for day in range(1, 26):
            if year == CURRENT_YEAR and day > CURRENT_DAY:
                break

            year_str = str(year)
            day_str = str(day).zfill(2)
            if year_str not in progress:
                progress[year_str] = {}
            if day_str not in progress[year_str]:
                progress[year_str][day_str] = {
                    "status": "❌",
                    "elapsed_a": None,
                    "elapsed_b": None,
                    "submission_time": None,
                }
    save_progress(progress)


def update_progress_markdown() -> None:
    """Update the PROGRESS.md file with a table of the progress of all solutions."""
    progress = load_progress()

    table_header = (
        "# Advent of Code Progress\n\n"
        "| Year | Day | Status | Part A | Part B | Submission Time |\n"
        "| ---- | --- | ------ | ------ | ------ | --------------- |\n"
    )

    table_rows: list[str] = []
    for year in sorted(progress.keys(), reverse=True):
        for day in sorted(progress[year].keys(), reverse=True):
            day_progress = progress[year][day]
            status_str = day_progress["status"]
            elapsed_a_str = f"{day_progress['elapsed_a']:.6f}s" if day_progress["elapsed_a"] is not None else ""
            elapsed_b_str = f"{day_progress['elapsed_b']:.6f}s" if day_progress["elapsed_b"] is not None else ""
            submission_time = day_progress["submission_time"] or ""
            table_rows.append(
                f"| {year} | {day} | {status_str} | {elapsed_a_str} | {elapsed_b_str} | {submission_time} |\n"
            )

        table_rows.append("| | | | | | |\n")

    with PROGRESS_MARKDOWN_FILE.open("w") as f:
        f.write(table_header)
        f.writelines(table_rows)


def document_solution(year: int, day: int, elapsed_a: float | None, elapsed_b: float | None) -> None:
    """Document the progress of a solution.

    Args:
        year: The year of the solution.
        day: The day of the solution.
        elapsed_a: The time it took to solve part A.
        elapsed_b: The time it took to solve part B.
    """
    update_progress_json()

    submission_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    status_icon = "✅" if elapsed_a is not None and elapsed_b is not None else "🔄"

    progress = load_progress()
    year_str = str(year)
    day_str = str(day).zfill(2)

    progress[year_str][day_str] = {
        "status": status_icon,
        "elapsed_a": elapsed_a,
        "elapsed_b": elapsed_b,
        "submission_time": submission_time,
    }

    save_progress(progress)
    update_progress_markdown()


__all__ = ["document_solution"]
