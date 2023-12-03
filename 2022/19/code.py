# Advent of Code 2022 Day 19
# Author: Erik Båvenstrand
# URL: https://adventofcode.com/2022/day/19

import functools
import re
from typing import Union


def calculate_max_geodes(
    ore_robot_ore_cost: int,
    clay_robot_ore_cost: int,
    obsidian_robot_ore_cost: int,
    obsidian_robot_clay_cost: int,
    geode_robot_ore_cost: int,
    geode_robot_obsidian_cost: int,
    minutes: int,
):
    @functools.cache
    def max_geodes(
        ores: int,
        clay: int,
        obsidian: int,
        ore_robots: int,
        clay_robots: int,
        obsidian_robots: int,
        minutes_left: int,
    ) -> int:
        if minutes_left <= 1:
            return 0

        min_ore_robots = (
            max(
                ore_robot_ore_cost,
                clay_robot_ore_cost,
                obsidian_robot_ore_cost,
                geode_robot_ore_cost,
            )
            * minutes_left
            - ores
        ) / minutes_left
        min_clay_robots = (
            obsidian_robot_clay_cost * minutes_left - clay
        ) / minutes_left
        min_obsidian_robots = (
            geode_robot_obsidian_cost * minutes_left - obsidian
        ) / minutes_left

        need_ores = ore_robots < min_ore_robots
        need_clay = clay_robots < min_clay_robots
        need_obsidian = obsidian_robots < min_obsidian_robots

        build_ore_robot = ores >= ore_robot_ore_cost and need_ores
        build_clay_robot = ores >= clay_robot_ore_cost and need_clay and need_obsidian
        build_obsidian_robot = (
            ores >= obsidian_robot_ore_cost
            and clay >= obsidian_robot_clay_cost
            and need_obsidian
        )
        build_geode_robot = (
            ores >= geode_robot_ore_cost and obsidian >= geode_robot_obsidian_cost
        )

        score = 0
        if build_geode_robot:
            score = max(
                score,
                max_geodes(
                    ores - geode_robot_ore_cost + ore_robots,
                    clay + clay_robots,
                    obsidian - geode_robot_obsidian_cost + obsidian_robots,
                    ore_robots,
                    clay_robots,
                    obsidian_robots,
                    minutes_left - 1,
                )
                + minutes_left
                - 1,
            )
        else:
            if build_obsidian_robot:
                score = max(
                    score,
                    max_geodes(
                        ores - obsidian_robot_ore_cost + ore_robots,
                        clay - obsidian_robot_clay_cost + clay_robots,
                        obsidian + obsidian_robots,
                        ore_robots,
                        clay_robots,
                        obsidian_robots + 1,
                        minutes_left - 1,
                    ),
                )
            if build_clay_robot:
                score = max(
                    score,
                    max_geodes(
                        ores - clay_robot_ore_cost + ore_robots,
                        clay + clay_robots,
                        obsidian + obsidian_robots,
                        ore_robots,
                        clay_robots + 1,
                        obsidian_robots,
                        minutes_left - 1,
                    ),
                )
            if build_ore_robot:
                score = max(
                    score,
                    max_geodes(
                        ores - ore_robot_ore_cost + ore_robots,
                        clay + clay_robots,
                        obsidian + obsidian_robots,
                        ore_robots + 1,
                        clay_robots,
                        obsidian_robots,
                        minutes_left - 1,
                    ),
                )
            if (
                not build_ore_robot
                or (clay_robots and need_obsidian)
                or obsidian_robots
            ):
                score = max(
                    score,
                    max_geodes(
                        ores + ore_robots,
                        clay + clay_robots,
                        obsidian + obsidian_robots,
                        ore_robots,
                        clay_robots,
                        obsidian_robots,
                        minutes_left - 1,
                    ),
                )
        return score

    return max_geodes(0, 0, 0, 1, 0, 0, minutes)


def part_a(data: list[str]) -> Union[int, str, None]:
    """Solution to part A.

    Args:
        data (list[str]): Advent of Code challenge input.

    Returns:
        Union[int, str, None]: Solution to the challenge.
    """
    quality_sum = 0
    for blueprint in data:
        (
            blueprint_idx,
            ore_robot_ore_cost,
            clay_robot_ore_cost,
            obsidian_robot_ore_cost,
            obsidian_robot_clay_cost,
            geode_robot_ore_cost,
            geode_robot_obsidian_cost,
        ) = [int(x) for x in re.findall("[0-9]+", blueprint)]
        quality_sum += blueprint_idx * calculate_max_geodes(
            ore_robot_ore_cost,
            clay_robot_ore_cost,
            obsidian_robot_ore_cost,
            obsidian_robot_clay_cost,
            geode_robot_ore_cost,
            geode_robot_obsidian_cost,
            24,
        )
    return quality_sum


def part_b(data: list[str]) -> Union[int, str, None]:
    """Solution to part B.

    Args:
        data (list[str]): Advent of Code challenge input.

    Returns:
        Union[int, str, None]: Solution to the challenge.
    """
    geode_prod = 1
    for blueprint in data[:3]:
        (
            ore_robot_ore_cost,
            clay_robot_ore_cost,
            obsidian_robot_ore_cost,
            obsidian_robot_clay_cost,
            geode_robot_ore_cost,
            geode_robot_obsidian_cost,
        ) = [int(x) for x in re.findall("[0-9]+", blueprint)][1:]
        geode_prod *= calculate_max_geodes(
            ore_robot_ore_cost,
            clay_robot_ore_cost,
            obsidian_robot_ore_cost,
            obsidian_robot_clay_cost,
            geode_robot_ore_cost,
            geode_robot_obsidian_cost,
            32,
        )
    return geode_prod
