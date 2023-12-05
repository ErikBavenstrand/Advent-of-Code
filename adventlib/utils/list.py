from typing import Any, Callable, Iterator, TypeVar

T = TypeVar("T")


def chunk_list(
    items: list,
    chunk_size: int,
    func: Callable[[Any], T] = lambda x: x,
    apply_to_chunk: bool = False,
) -> Iterator[T]:
    """Applies a function to each item or each chunk based on user preference.

    Args:
        items: List of items to be processed.
        chunk_size: Size of each chunk for processing.
        func: Optional mapping function to be applied to each item.
        apply_to_chunk: Boolean indicating whether to apply function to each chunk.

    Returns:
        Iterator of results after applying the function to each item or each chunk.
    """
    chunks = (items[idx : idx + chunk_size] for idx in range(0, len(items), chunk_size))

    if apply_to_chunk and func:
        return (func(chunk) for chunk in chunks)
    return (func(item) for chunk in chunks for item in chunk)
