from typing import Any, Callable, TypeVar


T = TypeVar("T")


def split_string(
    string: str, parts: int, func: Callable[[Any], T] = lambda x: x
) -> list[T]:
    """Splits a string into N parts.

    Will discard any elements in last part if string is not evenly divisible.

    Args:
        string: String to be split.
        parts: Number of equal sized parts.
        func: Function to be applied to each part, defaults to identity.

    Returns:
        List of string divided into equal parts.
    """
    return [
        func("".join(sub_string))
        for sub_string in zip(*[iter(string)] * (len(string) // parts))
    ]


def rotate_2d_list(list_: list[T], steps: int = 1, clockwise: bool = False) -> list[T]:
    """Rotates a 2D list clockwise or counter-clockwise for N steps.

    Args:
        list_: 2D list to be rotated.
        steps: Number of steps to rotate.
        clockwise: Rotate clockwise if True, counter-clockwise if False.

    Returns:
        Rotated list.
    """

    def transpose(l: list[Any]) -> list[Any]:
        return [list(row) for row in zip(*l)]

    def reverse_rows(l: list[Any]) -> list[Any]:
        return [row[::-1] for row in l]

    def reverse_columns(l: list[Any]) -> list[Any]:
        return l[::-1]

    matrix = list_.copy()
    for _ in range(steps % 4):
        if clockwise:
            matrix = reverse_rows(transpose(matrix))
        else:
            matrix = reverse_columns(transpose(matrix))

    if all(isinstance(row, str) for row in list_):
        matrix = ["".join(row) for row in matrix]  # type: ignore
    return matrix
