from typing import Any, Callable, TypeVar

R = TypeVar("R")


def split_string(
    string: str, parts: int, func: Callable[[Any], R] = lambda x: x
) -> list[R]:
    """Splits a string into N parts.

    Will discard any elements in last part if string is not evenly divisible.

    Args:
        string (str): String to be split.
        parts (int): Number of equal sized parts.
        func (_type_, optional): Function to be applied to each part.
            Defaults to lambdax:x.

    Returns:
        list[R]: List of string divided into equal parts.
    """
    return [
        func("".join(sub_string))
        for sub_string in zip(*[iter(string)] * (len(string) // parts))
    ]
