QUEEN_DIRECTIONS_2D = [
    (-1, -1),  # Up Left
    (0, -1),  # Up
    (1, -1),  # Up Right
    (-1, 0),  # Left
    (1, 0),  # Right
    (-1, 1),  # Down Left
    (0, 1),  # Down
    (1, 1),  # Down Right
]
"""Directions (x, y) for a 2D grid, including diagonals."""


def get_neighbors(x: int, y: int) -> list[tuple[int, int]]:
    """Gets the neighbors of a coordinate.

    Args:
        x: X-coordinate.
        y: Y-coordinate.

    Returns:
        A list of the coordinates neighbors.
    """
    return [(x + dx, y + dy) for dx, dy in QUEEN_DIRECTIONS_2D]
