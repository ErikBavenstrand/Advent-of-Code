from __future__ import annotations

import math
from typing import Generator, Tuple, Union

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

    def __repr__(self) -> str:
        """Representation of a point.

        Returns:
            Point representation.
        """
        return str(self)

    def __add__(self, other: Point2D | PointTupleType) -> Point2D:
        """Vector addition of two specified points.

        Args:
            other: Point to add.

        Returns:
            Resulting point.
        """
        if isinstance(other, Point2D):
            return Point2D(self.x + other.x, self.y + other.y)
        elif isinstance(other, tuple) and len(other) == 2:
            return Point2D(self.x + other[0], self.y + other[1])
        return NotImplemented

    def __sub__(self, other: Point2D | PointTupleType) -> Point2D:
        """Vector subtraction of two points.

        Args:
            other: Point to subtract.

        Returns:
            Resulting point.
        """
        if isinstance(other, Point2D):
            return self.__add__((-other.x, -other.y))
        elif isinstance(other, tuple) and len(other) == 2:
            return self.__add__((-other[0], -other[1]))
        return NotImplemented

    def __eq__(self, other: Point2D | PointTupleType) -> bool:
        """Check if points are equal.

        Args:
            other: Point to compare with.

        Returns:
            True if points are equal.
        """
        if isinstance(other, Point2D):
            return (self.x == other.x) and (self.y == other.y)
        elif isinstance(other, tuple) and len(other) == 2:
            return (self.x == other[0]) and (self.y == other[1])
        else:
            return False

    def __hash__(self) -> int:
        """Hash function for point.

        Returns:
            Hashed value.
        """
        return hash((self.x, self.y))

    def __(self) -> tuple[NumberType, NumberType]:
        """Iterate over the point.

        Returns:
            Tuple of coordinates.
        """
        return (self.x, self.y)

    def __iter__(self) -> Generator[NumberType, None, None]:
        """Iterate over the point.


        Yields:
            Coordinates.
        """
        yield self.x
        yield self.y

    def neighbors(
        self,
        min_x: NumberType | None = None,
        max_x: NumberType | None = None,
        min_y: NumberType | None = None,
        max_y: NumberType | None = None,
        diagonals: bool = True,
    ) -> list[Point2D]:
        """Get the neighbors of the point.

        Only works with integer coordinates.

        Args:
            min_x: Minimum x value.
            max_x: Maximum x value.
            min_y: Minimum y value.
            max_y: Maximum y value.
            diagonals: Whether to include diagonal neighbors.

        Returns:
            List of neighbors.
        """
        if not isinstance(self.x, int) or not isinstance(self.y, int):
            raise ValueError("neighbors() only works with integer coordinates")

        neighbors = [
            Point2D(self.x - 1, self.y),
            Point2D(self.x + 1, self.y),
            Point2D(self.x, self.y - 1),
            Point2D(self.x, self.y + 1),
        ]
        if diagonals:
            neighbors.extend(
                [
                    Point2D(self.x - 1, self.y - 1),
                    Point2D(self.x + 1, self.y - 1),
                    Point2D(self.x - 1, self.y + 1),
                    Point2D(self.x + 1, self.y + 1),
                ]
            )
        if min_x is not None:
            neighbors = [neighbor for neighbor in neighbors if neighbor.x >= min_x]
        if min_y is not None:
            neighbors = [neighbor for neighbor in neighbors if neighbor.y >= min_y]
        if max_x is not None:
            neighbors = [neighbor for neighbor in neighbors if neighbor.x <= max_x]
        if max_y is not None:
            neighbors = [neighbor for neighbor in neighbors if neighbor.y <= max_y]
        return neighbors

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
    def distance_vector(p1: Point2D, p2: Point2D) -> PointTupleType:
        """Calculate the distance vector between p1 and p2.

        Args:
            p1: Point 1.
            p2: Point 2.

        Returns:
            Distance vector between the points.
        """
        return (p1.x - p2.x, p1.y - p2.y)

    @staticmethod
    def manhattan_distance(p1: Point2D, p2: Point2D) -> NumberType:
        """Calculate the Manhattan distance between p1 and p2.

        The Manhattan distance is the sum of the absolute values of the differences of the
        coordinates.

        Args:
            p1: Point 1.
            p2: Point 2.

        Returns:
            Manhattan distance between the points.
        """
        return abs(p1.x - p2.x) + abs(p1.y - p2.y)


if __name__ == "__main__":
    print(Point2D(1, 1).neighbors(diagonals=True, min_x=0, min_y=0))
