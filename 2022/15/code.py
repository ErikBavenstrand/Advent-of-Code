# Advent of Code 2022 Day 15
# Author: Erik Båvenstrand
# URL: https://adventofcode.com/2022/day/15

from typing import Union

from adventlib.point import Point2D
from adventlib.utils.number import clamp


def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    """Merge a list of ranges accounting for overlaps and spreads.

    Args:
        intervals: A list of ranges.

    Returns:
        A merged list of ranges.
    """
    if len(intervals) == 0:
        return []
    intervals.sort(key=lambda x: x[0])
    stack = []
    stack.append(intervals[0])
    for i in range(1, len(intervals)):
        last_element = stack[-1]
        if last_element[1] + 1 >= intervals[i][0]:
            last_element[1] = max(intervals[i][1], last_element[1])
            stack.pop()
            stack.append(last_element)
        else:
            stack.append(intervals[i])
    return stack


def part_a(data: list[str]) -> Union[int, str, None]:
    """Solution to part A.

    Args:
        data (list[str]): Advent of Code challenge input.

    Returns:
        Union[int, str, None]: Solution to the challenge.
    """
    sensors_intervals: list[list[int]] = []
    level = 2000000
    for line in data:
        sx, sy, bx, by = [
            int(pos)
            for pos in line.replace("Sensor at ", "")
            .replace(",", "")
            .replace("x=", "")
            .replace("y=", "")
            .replace(": closest beacon is at", "")
            .split()
        ]
        sensor, beacon = Point2D(sx, sy), Point2D(bx, by)
        left = int(
            sensor.x
            - (Point2D.manhattan_distance(sensor, beacon) - abs(level - sensor.y))
        )
        right = int(
            sensor.x
            + (Point2D.manhattan_distance(sensor, beacon) - abs(level - sensor.y))
        )
        if left <= right:
            if beacon.y == level and beacon.x == left:
                sensors_intervals.append([left + 1, right])
            elif beacon.y == level and beacon.x == right:
                sensors_intervals.append([left, right - 1])
            else:
                sensors_intervals.append([left, right])
    return sum(
        [
            abs(sensor_range[1] - sensor_range[0] + 1)
            for sensor_range in merge_intervals(sensors_intervals)
        ]
    )


def part_b(data: list[str]) -> Union[int, str, None]:
    """Solution to part B.

    Args:
        data (list[str]): Advent of Code challenge input.

    Returns:
        Union[int, str, None]: Solution to the challenge.
    """
    sensors_intervals: list[list[int]] = []
    sensor_beacon: list[tuple[Point2D, Point2D]] = []
    max_range = 4000000
    for line in data:
        sx, sy, bx, by = [
            int(pos)
            for pos in line.replace("Sensor at ", "")
            .replace(",", "")
            .replace("x=", "")
            .replace("y=", "")
            .replace(": closest beacon is at", "")
            .split()
        ]
        sensor, beacon = Point2D(sx, sy), Point2D(bx, by)
        sensor_beacon.append((sensor, beacon))

    for level in reversed(range(max_range)):
        sensors_intervals = []
        for sensor, beacon in sensor_beacon:
            left = int(
                sensor.x
                - (Point2D.manhattan_distance(sensor, beacon) - abs(level - sensor.y))
            )
            right = int(
                sensor.x
                + (Point2D.manhattan_distance(sensor, beacon) - abs(level - sensor.y))
            )
            left = clamp(left, 0, max_range)
            right = clamp(right, 0, max_range)
            if left <= right:
                sensors_intervals.append([left, right])
        merged_intervals = merge_intervals(sensors_intervals)
        if len(merged_intervals) > 1:
            return ((merged_intervals[0][1] + 1) * 4000000) + level
