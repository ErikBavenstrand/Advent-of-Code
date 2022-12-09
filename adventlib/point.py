from __future__ import annotations

import math
from typing import Union


class Point2D:
    def __init__(self, x: Union[int, float], y: Union[int, float]) -> None:
        self.x: Union[int, float] = x
        self.y: Union[int, float] = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __add__(self, point):
        if isinstance(point, Point2D):
            return Point2D(self.x + point.x, self.y + point.y)
        elif isinstance(point, tuple) and len(point) == 2:
            return Point2D(self.x + point[0], self.y + point[1])
        return NotImplemented

    def __sub__(self, point: Union[Point2D, tuple[Union[]]]):
        if isinstance(point, Point2D):
            return self.__add__((-point.x, -point.y))
        elif isinstance(point, tuple) and len(point) == 2:
            return self.__add__((-point[0], -point[1]))
        return NotImplemented

    def __eq__(self, point):
        if type(point) is Point2D:
            return (self.x == point.x) and (self.y == point.y)
        else:
            return False

    def __hash__(self):
        return hash((self.x, self.y))

    @staticmethod
    def distance(p1: Point2D, p2: Point2D) -> float:
        """Calculate absolute distance between p1 and p2.

        Args:
            p1: Point 1.
            p2: Point 2.

        Returns:
            Absolute distance between the points.
        """
        return math.hypot(p1.x - p2.x, p1.y - p2.y)

    @staticmethod
    def distance_vector(
        p1: Point2D, p2: Point2D
    ) -> tuple[Union[int, float], Union[int, float]]:
        """Calculate the distance vector between p1 and p2.

        Args:
            p1: Point 1.
            p2: Point 2.

        Returns:
            Distance vector between the points.
        """
        return (p1.x - p2.x, p1.y - p2.y)
