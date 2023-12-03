# Advent of Code 2023 Day 02
# Author: Erik Båvenstrand
# URL: https://adventofcode.com/2023/day/2


def get_hand_cube_counts(hand: str) -> tuple[int, int, int]:
    """Get the number of red, green and blue cubes in a hand.

    Args:
        hand: A string representing a hand of cubes.

    Returns:
        A tuple containing the number of red, green and blue cubes.
    """
    red = 0
    green = 0
    blue = 0

    for cube in hand.split(", "):
        cube_number, cube_color = cube.split(" ")
        if cube_color == "red":
            red += int(cube_number)
        elif cube_color == "green":
            green += int(cube_number)
        elif cube_color == "blue":
            blue += int(cube_number)

    return red, green, blue


def get_max_cube_counts(game: str) -> tuple[int, int, int]:
    """Get the maximum number of red, green and blue cubes in a game.

    Args:
        game: A string representing a game of hands.

    Returns:
        A tuple containing the maximum number of red, green and blue cubes.
    """
    max_red = 0
    max_green = 0
    max_blue = 0

    for hand in game.split(": ")[1].split("; "):
        red, green, blue = get_hand_cube_counts(hand)
        max_red = max(max_red, red)
        max_green = max(max_green, green)
        max_blue = max(max_blue, blue)

    return max_red, max_green, max_blue


def part_a(data: list[str]) -> int | str | None:
    """Solution to part A.

    Args:
        data: Advent of Code challenge input.

    Returns:
        Solution to the challenge.
    """
    max_red = 12
    max_green = 13
    max_blue = 14

    valid_hands = []
    for i, game in enumerate(data):
        id = i + 1
        red, green, blue = get_max_cube_counts(game)
        if red <= max_red and green <= max_green and blue <= max_blue:
            valid_hands.append(id)

    return sum(valid_hands)


def part_b(data: list[str]) -> int | str | None:
    """Solution to part B.

    Args:
        data: Advent of Code challenge input.

    Returns:
        Solution to the challenge.
    """
    powers = []
    for game in data:
        red, green, blue = get_max_cube_counts(game)
        powers.append(red * green * blue)
    return sum(powers)
