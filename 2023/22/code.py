# Advent of Code 2023 Day 22
# Author: Erik Båvenstrand
# URL: https://adventofcode.com/2023/day/22
from __future__ import annotations

from collections import defaultdict, deque
from dataclasses import dataclass
from typing import Literal

import numpy as np


AxisType = Literal["x", "y", "z"]
AXIS_TO_INDEX: dict[AxisType, int] = {"x": 0, "y": 1, "z": 2}


@dataclass(frozen=True)
class Brick:
    """Brick class."""

    corner_1: tuple[int, int, int]
    corner_2: tuple[int, int, int]

    def __lt__(self, other: Brick):
        """Less than operator.

        Args:
            other: Other brick.

        Returns:
            True if self is less than other.
        """
        return self.min(axis="z") < other.min(axis="z")

    def min(self, axis: AxisType) -> int:
        """Returns the minimum value of the brick along the given axis.

        Args:
            axis: Axis to check.

        Returns:
            Minimum value of the brick along the given axis.
        """
        return min(
            self.corner_1[AXIS_TO_INDEX[axis]], self.corner_2[AXIS_TO_INDEX[axis]]
        )

    def max(self, axis: AxisType) -> int:
        """Returns the maximum value of the brick along the given axis.

        Args:
            axis: Axis to check.

        Returns:
            Maximum value of the brick along the given axis.
        """
        return max(
            self.corner_1[AXIS_TO_INDEX[axis]], self.corner_2[AXIS_TO_INDEX[axis]]
        )

    def xy_bounds(self) -> tuple[tuple[int, int], tuple[int, int]]:
        """Returns the minimum and maximum x and y values of the brick.

        Returns:
            Tuple of the minimum and maximum x and y values of the brick.
        """
        return (
            (self.min(axis="x"), self.min(axis="y")),
            (self.max(axis="x"), self.max(axis="y")),
        )

    def update_z(self, base_z: int) -> Brick:
        """Updates the z values of the brick.

        Args:
            base_z: New z value.

        Returns:
            Updated brick.
        """
        delta_z = self.min(axis="z") - base_z
        return Brick(
            (self.corner_1[0], self.corner_1[1], self.corner_1[2] - delta_z),
            (self.corner_2[0], self.corner_2[1], self.corner_2[2] - delta_z),
        )

    def height(self) -> int:
        """Returns the height of the brick.

        Returns:
            Height of the brick.
        """
        return self.max(axis="z") - self.min(axis="z") + 1

    def area_intersects(self, other: Brick) -> bool:
        """Checks if the area of the brick intersects with the area of another brick.

        Args:
            other: Other brick.

        Returns:
            True if the area of the brick intersects with the area of another brick.
        """
        (x1, y1), (x2, y2) = self.xy_bounds()
        (other_x1, other_y1), (other_x2, other_y2) = other.xy_bounds()
        if x2 < other_x1 or other_x2 < x1 or y2 < other_y1 or other_y2 < y1:
            return False
        return True


def parse_bricks(data: list[str]) -> list[Brick]:
    """Parses the challenge input into a list of bricks.

    Args:
        data: Advent of Code challenge input.

    Returns:
        List of bricks.
    """
    bricks = []
    for line in data:
        (x1, y1, z1), (x2, y2, z2) = [
            (int(v) for v in corner.split(",")) for corner in line.split("~")
        ]
        bricks.append(Brick((x1, y1, z1), (x2, y2, z2)))
    return bricks


def get_bricks_xy_bounds(
    bricks: list[Brick],
) -> tuple[tuple[int, int], tuple[int, int]]:
    """Returns the minimum and maximum x and y values of the bricks.

    Args:
        bricks: List of bricks.

    Returns:
        Tuple of the minimum and maximum x and y values of the bricks.
    """
    x_min = x_max = 0
    y_min = y_max = 0
    for brick in bricks:
        x_min, x_max = min(brick.min(axis="x"), x_min), max(brick.max(axis="x"), x_max)
        y_min, y_max = min(brick.min(axis="y"), y_min), max(brick.max(axis="y"), y_max)
    return (x_min, x_max), (y_min, y_max)


def drop_bricks(
    bricks: list[Brick],
) -> dict[Brick, set[Brick]]:
    """Drops the bricks to the lowest possible z value.

    Args:
        bricks: List of bricks.

    Returns:
        Dictionary of bricks to the bricks they are directly resting on.
    """
    (x_min, x_max), (y_min, y_max) = get_bricks_xy_bounds(bricks)
    bricks_at_level: dict[int, set[Brick]] = defaultdict(set)
    bricks_supporting: dict[Brick, set[Brick]] = defaultdict(set)

    height_map = np.zeros((y_max - y_min + 1, x_max - x_min + 1), dtype=np.int32)
    for brick in bricks:
        (x1, y1), (x2, y2) = brick.xy_bounds()
        old_max_height = int(np.max(height_map[y1 : y2 + 1, x1 : x2 + 1]))
        brick.update_z(old_max_height + 1)
        new_max_height = old_max_height + brick.height()
        height_map[y1 : y2 + 1, x1 : x2 + 1] = new_max_height
        bricks_at_level[new_max_height].add(brick)
        bricks_supporting[brick].update(
            [
                base_brick
                for base_brick in bricks_at_level[old_max_height]
                if base_brick.area_intersects(brick)
            ]
        )

    return bricks_supporting


def get_brick_data(
    data: list[str],
) -> tuple[int, dict[Brick, set[Brick]], dict[Brick, set[Brick]]]:
    """Get required datastructures for part A and B.

    Args:
        data: Advent of Code challenge input.

    Returns:
        Tuple of number of safe bricks, upper to base bricks, and base to upper bricks.
    """
    bricks = parse_bricks(data)
    bricks.sort()

    bricks_supporting = drop_bricks(bricks)

    critical_bricks = set()
    bricks_resting_on = defaultdict(set)
    for brick in bricks:
        if len(bricks_supporting[brick]) == 1:
            (base_brick,) = bricks_supporting[brick]
            critical_bricks.add(base_brick)

        for base_brick in bricks_supporting[brick]:
            bricks_resting_on[base_brick].add(brick)

    n_safe_bricks = len(bricks) - len(critical_bricks)
    return n_safe_bricks, bricks_supporting, bricks_resting_on


def part_a(data: list[str]) -> int | str | None:
    """Solution to part A.

    Args:
        data: Advent of Code challenge input.

    Returns:
        Solution to the challenge.
    """
    n_safe_bricks, _, _ = get_brick_data(data)
    return n_safe_bricks


def part_b(data: list[str]) -> int | str | None:
    """Solution to part B.

    Args:
        data: Advent of Code challenge input.

    Returns:
        Solution to the challenge.
    """
    _, bricks_supporting, bricks_resting_on = get_brick_data(data)
    total = 0
    for brick in bricks_supporting:
        queue = deque(
            upper
            for upper in bricks_resting_on[brick]
            if len(bricks_supporting[upper]) == 1
        )
        falling = set(queue)
        falling.add(brick)

        while queue:
            upper = queue.popleft()
            for base in bricks_resting_on[upper] - falling:
                if bricks_supporting[base] < falling:
                    queue.append(base)
                    falling.add(base)

        total += len(falling) - 1
    return total
