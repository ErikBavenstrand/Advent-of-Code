def get_neighbors(x: int, y: int) -> list[tuple[int, int]]:
    """Gets the neighbors of a coordinate.

    Args:
        x: X-coordinate.
        y: Y-coordinate.

    Returns:
        A list of the coordinates neighbors.
    """
    return [
        (x - 1, y - 1),
        (x, y - 1),
        (x + 1, y - 1),
        (x - 1, y),
        (x + 1, y),
        (x - 1, y + 1),
        (x, y + 1),
        (x + 1, y + 1),
    ]
