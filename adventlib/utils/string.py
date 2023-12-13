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


def transpose_list(list_: list[list[Any]] | list[str]) -> list[Any]:
    """Transpose a list of lists.

    If the list is a list of strings, the result will be a list of strings. Otherwise,
    the result will be a list of lists.

    Args:
        list_: List of lists.

    Returns:
        Transposed list.
    """
    if isinstance(list_[0], str):
        return list(map("".join, zip(*list_)))
    else:
        return list(map(list, zip(*list_)))
