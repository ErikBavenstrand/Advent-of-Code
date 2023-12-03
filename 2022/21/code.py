# Advent of Code 2022 Day 21
# Author: Erik Båvenstrand
# URL: https://adventofcode.com/2022/day/21

from typing import Union


def get_monkey_value(name: str, monkeys: dict[str, Union[str, int]]) -> int:
    value = monkeys[name]
    if isinstance(value, int):
        return value
    else:
        m1, operator, m2 = value.split(" ")
        m1_value = get_monkey_value(m1, monkeys)
        m2_value = get_monkey_value(m2, monkeys)
        match operator:
            case "+":
                value = m1_value + m2_value
            case "-":
                value = m1_value - m2_value
            case "*":
                value = m1_value * m2_value
            case "/":
                value = m1_value / m2_value
        monkeys[name] = int(value)
        return int(value)


def get_root_diff(humn: int, monkeys: dict[str, Union[str, int]]) -> int:
    root_values = monkeys["root"]
    assert isinstance(root_values, str)
    m1, _, m2 = root_values.split(" ")
    monkeys["humn"] = humn
    monkey_dict_copy = monkeys.copy()
    return get_monkey_value(m1, monkey_dict_copy) - get_monkey_value(
        m2, monkey_dict_copy
    )


def gradient(humn: int, monkeys: dict[str, Union[str, int]]):
    x0 = humn
    v0 = get_root_diff(humn, monkeys)
    while (v1 := get_root_diff(humn, monkeys)) == v0:
        humn += 1
    return (v1 - v0) / (humn - x0)


def part_a(data: list[str]) -> Union[int, str, None]:
    """Solution to part A.

    Args:
        data (list[str]): Advent of Code challenge input.

    Returns:
        Union[int, str, None]: Solution to the challenge.
    """
    monkeys: dict[str, Union[str, int]] = {}
    for monkey in data:
        name, value = monkey.split(": ")
        monkeys[name] = int(value) if value.isnumeric() else value
    return get_monkey_value("root", monkeys)


def part_b(data: list[str]) -> Union[int, str, None]:
    """Solution to part B.

    Args:
        data (list[str]): Advent of Code challenge input.

    Returns:
        Union[int, str, None]: Solution to the challenge.
    """
    monkeys: dict[str, Union[str, int]] = {}
    for monkey in data:
        name, value = monkey.split(": ")
        monkeys[name] = int(value) if value.isnumeric() else value

    x: int = 0
    while True:
        y = get_root_diff(x, monkeys)
        if y == 0:
            break
        x -= int(y / gradient(x, monkeys))
    return x
