from typing import Any, Callable, Iterator, TypeVar

R = TypeVar("R")


def chunk_list(
    items: list, chunk_size: int, func: Callable[[Any], R] = lambda x: x
) -> Iterator[list[R]]:
    """Divides a list in chunks of specified size.

    Args:
        items (list): List of items to be chunked.
        chunk_size (int): Size of each chunk.
        func (Callable): Mapping function to be applied to each list in chunk.

    Returns:
        Iterator[list]: Chunked Iterator of list.
    """
    return (
        list(map(func, items[idx : idx + chunk_size]))
        for idx in range(0, len(items), chunk_size)
    )
