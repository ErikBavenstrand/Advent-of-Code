from __future__ import annotations

import math
from typing import Tuple, Union

NumberType = Union[int, float]
PointTupleType = Tuple[NumberType, NumberType]


class Point2D:
    """Point2D."""

    def __init__(self, x: NumberType, y: NumberType) -> None:
        """Initialize a 2D point.

        Args:
            x: X coordinate.
            y: Y coordinate.
        """
        self.x: NumberType = x
        self.y: NumberType = y

    def __str__(self) -> str:
        """String representation of point.

        Returns:
            Point string representation.
        """
        return f"({self.x}, {self.y})"

    def __repr__(self) -> PointTupleType:
        """Representation of a point.

        Returns:
            Point representation.
        """
        return (self.x, self.y)

    def __add__(self, point: Union[Point2D, PointTupleType]) -> Point2D:
        """Vector addition of two specified points.

        Args:
            point: Point to add.

        Returns:
            Resulting point.
        """
        if isinstance(point, Point2D):
            return Point2D(self.x + point.x, self.y + point.y)
        elif isinstance(point, tuple) and len(point) == 2:
            return Point2D(self.x + point[0], self.y + point[1])
        return NotImplemented

    def __sub__(self, point: Union[Point2D, PointTupleType]) -> Point2D:
        """Vector subtraction of two points.

        Args:
            point: Point to subtract.

        Returns:
            Resulting point.
        """
        if isinstance(point, Point2D):
            return self.__add__((-point.x, -point.y))
        elif isinstance(point, tuple) and len(point) == 2:
            return self.__add__((-point[0], -point[1]))
        return NotImplemented

    def __eq__(self, point: Union[Point2D, PointTupleType]) -> bool:
        """Check if points are equal.

        Args:
            point: Point to compare with.

        Returns:
            True if points are equal.
        """
        if isinstance(point, Point2D):
            return (self.x == point.x) and (self.y == point.y)
        elif isinstance(point, tuple) and len(point) == 2:
            return (self.x == point[0]) and (self.y == point[1])
        else:
            return False

    def __hash__(self) -> int:
        """Hash function for point.

        Returns:
            Hashed value.
        """
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
