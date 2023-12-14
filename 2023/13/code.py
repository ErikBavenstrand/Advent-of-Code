# Advent of Code 2023 Day 13
# Author: Erik Båvenstrand
# URL: https://adventofcode.com/2023/day/13


from adventlib.utils.string import rotate_2d_list


def get_patterns(data: list[str]) -> list[list[str]]:
    """Get the patterns from the data.

    Args:
        data: Advent of Code challenge input.

    Returns:
        List of patterns.
    """
    patterns = []
    pattern = []
    for row in data + [""]:
        if row == "":
            patterns.append(pattern)
            pattern = []
        else:
            pattern.append(row)
    return patterns


def is_reflected_at(hashes: list[int], idx: int) -> bool:
    """Check if the hashes are reflected around the idx.

    Args:
        hashes: List of hashes.
        idx: Index to check around.

    Returns:
        True if the hashes are reflected, False otherwise.
    """
    i = idx
    j = idx + 1
    while i >= 0 and j < len(hashes):
        if hashes[i] != hashes[j]:
            return False
        i -= 1
        j += 1
    return True


def get_reflection_idx(pattern: list[str], ignore_idx: int | None = None) -> int | None:
    """Get the index of the reflection.

    Args:
        pattern: Pattern to check.
        ignore_idx: Index to ignore.

    Returns:
        The index of the reflection, None if no reflection exists.
    """
    hashes = []
    for row in pattern:
        hashes.append(hash(row))

    for idx in range(len(hashes) - 1):
        if hashes[idx] == hashes[idx + 1]:
            if is_reflected_at(hashes, idx) and idx + 1 != ignore_idx:
                return idx + 1
    return None


def get_pattern_variations(pattern: list[str]) -> list[list[str]]:
    """Get all variations of the pattern.

    Args:
        pattern: Pattern to get variations of.

    Returns:
        List of all variations of the pattern.
    """
    pattern_variations = []
    for y, row in enumerate(pattern):
        for x, char in enumerate(row):
            replacement_char = "." if char == "#" else "#"
            new_pattern = pattern.copy()
            new_pattern[y] = (
                new_pattern[y][:x] + replacement_char + new_pattern[y][x + 1 :]
            )
            pattern_variations.append(new_pattern)
    return pattern_variations


def part_a(data: list[str]) -> int | str | None:
    """Solution to part A.

    Args:
        data: Advent of Code challenge input.

    Returns:
        Solution to the challenge.
    """
    patterns = get_patterns(data)

    pattern_sum = 0
    for pattern in patterns:
        row_reflection_idx = get_reflection_idx(pattern)
        if row_reflection_idx:
            pattern_sum += row_reflection_idx * 100
            continue

        column_reflection_idx = get_reflection_idx(rotate_2d_list(pattern))
        if column_reflection_idx:
            pattern_sum += column_reflection_idx
            continue
    return pattern_sum


def part_b(data: list[str]) -> int | str | None:
    """Solution to part B.

    Args:
        data: Advent of Code challenge input.

    Returns:
        Solution to the challenge.
    """
    patterns = get_patterns(data)

    pattern_sum = 0
    for pattern in patterns:
        old_row_reflection_idx = get_reflection_idx(pattern)
        old_column_reflection_idx = get_reflection_idx(rotate_2d_list(pattern))
        for variation in get_pattern_variations(pattern):
            row_reflection_idx = get_reflection_idx(
                variation, ignore_idx=old_row_reflection_idx
            )
            if row_reflection_idx:
                pattern_sum += row_reflection_idx * 100
                break

            column_reflection_idx = get_reflection_idx(
                rotate_2d_list(variation), ignore_idx=old_column_reflection_idx
            )
            if column_reflection_idx:
                pattern_sum += column_reflection_idx
                break
    return pattern_sum
