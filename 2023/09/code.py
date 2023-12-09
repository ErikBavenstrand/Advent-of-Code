# Advent of Code 2023 Day 09
# Author: Erik Båvenstrand
# URL: https://adventofcode.com/2023/day/9


def part_a(data: list[str]) -> int | str | None:
    """Solution to part A.

    Args:
        data: Advent of Code challenge input.

    Returns:
        Solution to the challenge.
    """
    predictions = []
    for line in data:
        values = [[int(v) for v in line.split(" ")]]

        step = 0
        while not all(v == 0 for v in values[-1]):
            values.append(
                [
                    values[step][i + 1] - values[step][i]
                    for i in range(len(values[step]) - 1)
                ]
            )
            step += 1
        predictions.append(sum(diff[-1] for diff in values))
    return sum(predictions)


def part_b(data: list[str]) -> int | str | None:
    """Solution to part B.

    Args:
        data: Advent of Code challenge input.

    Returns:
        Solution to the challenge.
    """
    predictions = []
    for line in data:
        values = [[int(v) for v in line.split(" ")]]

        step = 0
        while not all(v == 0 for v in values[-1]):
            values.append(
                [
                    values[step][i + 1] - values[step][i]
                    for i in range(len(values[step]) - 1)
                ]
            )
            step += 1

        result = values[-1][-1]
        for seq in reversed(values[:-1]):
            result = seq[0] - result
        predictions.append(result)
    return sum(predictions)
