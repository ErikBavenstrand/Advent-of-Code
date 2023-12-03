# Advent of Code 2022 Day 20
# Author: Erik Båvenstrand
# URL: https://adventofcode.com/2022/day/20

from typing import Union


def decrypt(encrypted: list[int], cycles: int = 1) -> list[int]:
    """Decrypts the encrypted list of ints.

    Args:
        encrypted: Encrypted list of ints.
        cycles: Number of cycles to run unmixing. Defaults to 1.

    Returns:
        Decrypts a list of ints.
    """
    length = len(encrypted)
    indices = list(range(length))
    for _ in range(cycles):
        for i, value in enumerate(encrypted):
            if value == 0:
                continue
            j = indices.index(i)
            x = indices.pop(j)
            k = (j + value) % (length - 1)
            indices.insert(k, x)
    return [encrypted[i] for i in indices]


def get_coordinates(decryped: list[int]) -> int:
    """Get coordinates from decrypted list of ints.

    Args:
        decryped: Decrypted list of ints.

    Returns:
        Coordinates.
    """
    return sum(
        decryped[i]
        for i in ((decryped.index(0) + m) % len(decryped) for m in [1000, 2000, 3000])
    )


def part_a(data: list[str]) -> Union[int, str, None]:
    """Solution to part A.

    Args:
        data (list[str]): Advent of Code challenge input.

    Returns:
        Union[int, str, None]: Solution to the challenge.
    """
    encrypted: list[int] = []
    for val in data:
        encrypted.append(int(val))
    return get_coordinates(decrypt(encrypted))


def part_b(data: list[str]) -> Union[int, str, None]:
    """Solution to part B.

    Args:
        data (list[str]): Advent of Code challenge input.

    Returns:
        Union[int, str, None]: Solution to the challenge.
    """
    decryption_key = 811589153
    encrypted: list[int] = []
    for val in data:
        encrypted.append(int(val) * decryption_key)
    return get_coordinates(decrypt(encrypted, cycles=10))
