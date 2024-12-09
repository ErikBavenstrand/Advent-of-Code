# Advent of Code 2024 Day 07
# Author: Erik Båvenstrand
# URL: https://adventofcode.com/2024/day/7


from itertools import product


def calculate(a: int, b: int, op: str) -> int:
    """Calculate the result of an operation.

    Args:
        a: The first operand.
        b: The second operand.
        op: The operator.

    Returns:
        The result of the operation.
    """
    if op == "+":
        return a + b
    elif op == "*":
        return a * b
    elif op == "||":
        return int(f"{a}{b}")
    else:
        raise ValueError(f"Invalid operator: {op}")


def part_a(data: list[str]) -> int | str | None:
    """Solution to part A.

    Args:
        data: Advent of Code challenge input.

    Returns:
        Solution to the challenge.
    """
    calibration_result = 0
    for line in data:
        res, values = line.split(": ")
        expected_result = int(res)
        values = [int(v) for v in values.split(" ")]
        operator_combinations = product(["+", "*"], repeat=len(values) - 1)

        for operators in operator_combinations:
            result = values[0]
            for i, op in enumerate(operators, start=1):
                result = calculate(result, values[i], op)
            if result == expected_result:
                calibration_result += result
                break
    return calibration_result


def part_b(data: list[str]) -> int | str | None:
    """Solution to part B.

    Args:
        data: Advent of Code challenge input.

    Returns:
        Solution to the challenge.
    """
    calibration_result = 0
    for line in data:
        res, values = line.split(": ")
        expected_result = int(res)
        values = [int(v) for v in values.split(" ")]
        operator_combinations = product(["+", "*", "||"], repeat=len(values) - 1)

        for operators in operator_combinations:
            result = values[0]
            for i, op in enumerate(operators, start=1):
                result = calculate(result, values[i], op)
            if result == expected_result:
                calibration_result += result
                break
    return calibration_result
