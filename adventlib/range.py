from typing import Optional


class Range:
    __slots__ = ("start", "end")

    def __init__(self, start: int, end: int) -> None:
        """Create a new range.

        Args:
            start: The start of the range.
            end: The end of the range.

        Raises:
            ValueError: If the start is greater than or equal to the end.
        """
        self.start = start
        self.end = end
        if self.start >= self.end:
            raise ValueError(f"{self.start=} must be < {self.end=}")

    def __repr__(self) -> str:
        """Get a string representation of the range.

        Returns:
            A string representation of the range.
        """
        return f"{self.__class__.__name__}({self.start}, {self.end})"

    def __eq__(self, other: object) -> bool:
        """Check if two ranges are equal.

        Args:
            other: The other range to compare to.

        Raises:
            NotImplementedError: If the other object is not a Range.

        Returns:
            True if the ranges are equal, False otherwise.
        """
        if not isinstance(other, Range):
            raise NotImplementedError(f"Cannot compare {self.__class__} to {other}")
        return self.start == other.start and self.end == other.end

    def __contains__(self, number: int) -> bool:
        """Check if a number is in the range.

        Args:
            number: The number to check.

        Returns:
            True if the number is in the range, False otherwise.
        """
        return self.start <= number < self.end

    def __len__(self) -> int:
        """Get the length of the range.

        Returns:
            The length of the range.
        """
        return self.end - self.start

    def __hash__(self) -> int:
        """Get a hash of the range.

        Returns:
            A hash of the range.
        """
        return hash((self.start, self.end))

    def has_intersection(self, other: "Range") -> bool:
        """Check if the range has an intersection with another range.

        Args:
            other: The other range to check.

        Returns:
            True if the ranges have an intersection, False otherwise.
        """
        return self.start < other.end and other.start < self.end

    def intersection(self, other: "Range") -> Optional["Range"]:
        """Get the intersection of the range with another range.

        Returns:
            The intersection of the ranges, or None if they do not intersect.
        """
        if not self.has_intersection(other):
            return None
        return Range(max(self.start, other.start), min(self.end, other.end))

    def remainder(self, other: "Range") -> list["Range"]:
        """Get the remainder of the range after removing the intersection with another range.

        Returns:
            A list of the remaining ranges after removing the intersection.
        """
        intersection = self.intersection(other)
        if intersection is None:
            return []

        result = []
        if self.start < intersection.start:
            result.append(Range(self.start, intersection.start))
        if intersection.end < self.end:
            result.append(Range(intersection.end, self.end))
        return result
