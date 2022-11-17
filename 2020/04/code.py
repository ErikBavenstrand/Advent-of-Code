# Advent of Code 2020 Day 04
# Author: Erik Båvenstrand
# URL: https://adventofcode.com/2020/day/4

import re
from typing import Union


def year_valid(yr: str, min_yr: int, max_yr: int) -> bool:
    """Validate year to be in range [min, max].

    Args:
        yr (str): Year.
        min_yr (int): Minimum valid year.
        max_yr (int): Maximum valid year.

    Returns:
        bool: True if birth year is four digits and in range [min, max].
    """
    year = int(yr)
    return len(yr) == 4 and year >= min_yr and year <= max_yr


def height_valid(hgt: str) -> bool:
    """Validate height unit and length.

    Args:
        hgt (str): The height either in cm or in.

    Returns:
        bool: True if cm in [150, 193] or in in [59, 76]
    """
    unit = hgt[-2:]
    if unit not in ["cm", "in"] or not hgt[:-2].isnumeric():
        return False

    height = int(hgt[:-2])
    min_height, max_height = 150, 193
    if unit == "in":
        min_height, max_height = 59, 76
    return height >= min_height and height <= max_height


def hair_color_valid(hcl: str) -> bool:
    """Validates that the hair color is of correct HEX format.

    Args:
        hcl (str): HEX format color.

    Returns:
        bool: True if hair color is valid HEX color format.
    """
    return bool(re.match(r"^#(?:[0-9a-f]{2}){3}", hcl))


def eye_color_valid(ecl: str) -> bool:
    """Validates the eye color.

    Args:
        ecl (str): Eye color.

    Returns:
        bool: True if eye color is valid.
    """
    return ecl in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


def passport_id_valid(pid: str) -> bool:
    """Validates the passport ID.

    Args:
        pid (str): Passport ID.

    Returns:
        bool: True if the passport ID has 9 digits and is a number.
    """
    return len(pid) == 9 and pid.isnumeric()


def part_a(data: list[str]) -> Union[int, str, None]:
    """Solution to part A.

    Args:
        data (list[str]): Advent of Code challenge input.

    Returns:
        Union[int, str, None]: Solution to the challenge.
    """
    valid_passports = 0
    required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    for passport in " ".join(data).split("  "):
        passport_it = iter(passport.replace(":", " ").split(" "))
        passport_dict = dict(zip(passport_it, passport_it))

        if all(field in passport_dict for field in required_fields):
            valid_passports += 1
    return valid_passports


def part_b(data: list[str]) -> Union[int, str, None]:
    """Solution to part B.

    Args:
        data (list[str]): Advent of Code challenge input.

    Returns:
        Union[int, str, None]: Solution to the challenge.
    """
    valid_passports = 0
    required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    for passport in " ".join(data).split("  "):
        passport_it = iter(passport.replace(":", " ").split(" "))
        passport_dict = dict(zip(passport_it, passport_it))

        if (
            all(field in passport_dict for field in required_fields)
            and year_valid(passport_dict["byr"], 1920, 2002)
            and year_valid(passport_dict["iyr"], 2010, 2020)
            and year_valid(passport_dict["eyr"], 2020, 2030)
            and height_valid(passport_dict["hgt"])
            and hair_color_valid(passport_dict["hcl"])
            and eye_color_valid(passport_dict["ecl"])
            and passport_id_valid(passport_dict["pid"])
        ):
            valid_passports += 1
    return valid_passports
