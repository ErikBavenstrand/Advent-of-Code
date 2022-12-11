# Advent of Code 2022 Day 11
# Author: Erik Båvenstrand
# URL: https://adventofcode.com/2022/day/11

import math
from typing import Union


class Monkey:
    """Monkey."""

    def __init__(
        self,
        monkey_id: int,
        items: list[int],
        func_expr: str,
        divider: int,
        target_monkey_id: dict[bool, int],
        decay: int = 1,
    ) -> None:
        """Create monkey object.

        Args:
            monkey_id: Id of the monkey.
            items: List of items the monkey holds.
            func_expr: String description of item value change function.
            divider: Denominator of the conditional which is used to determine which
                monkey the item is passed to.
            target_monkey_id: Dict of ids given boolean outcome of condition.
            decay: Next item value decay. Defaults to 1.
        """
        self.monkey_id: int = monkey_id
        self.items: list[int] = items
        self.func_expr: str = func_expr
        self.divider: int = divider
        self.target_monkey_id: dict[bool, int] = target_monkey_id
        self.decay: int = decay

    def get_item_next_value(self) -> int:
        """Calculate next value for item in font of the stack and remove it from the monkey.

        Returns:
            New item value.
        """
        item = self.items.pop(0)
        return math.floor((lambda x: eval(self.func_expr))(item) / self.decay)

    def get_next_monkey_id(self, item: int) -> int:
        """Get the id of the target monkey.

        Args:
            item: Value of the item to be passed.

        Returns:
            Id of the target monkey.
        """
        return self.target_monkey_id[item % self.divider == 0]


def part_a(data: list[str]) -> Union[int, str, None]:
    """Solution to part A.

    Args:
        data (list[str]): Advent of Code challenge input.

    Returns:
        Union[int, str, None]: Solution to the challenge.
    """
    monkeys: list[Monkey] = []
    for monkey in "\n".join(data).split("\n\n"):
        monkey_info = monkey.split("\n")
        monkey_id = int(monkey_info[0].split()[1][:-1])
        monkey_items = [int(item) for item in monkey_info[1].split(": ")[1].split(", ")]
        monkey_func = monkey_info[2].split("new = ")[1].replace("old", "x")
        divider = int(monkey_info[3].split("divisible by ")[1])
        target_monkey_id: dict[bool, int] = {
            True: int(monkey_info[4].split("throw to monkey ")[1]),
            False: int(monkey_info[5].split("throw to monkey ")[1]),
        }
        monkeys.append(
            Monkey(monkey_id, monkey_items, monkey_func, divider, target_monkey_id, 3)
        )

    monkey_activity = [0 for _ in range(len(monkeys))]
    for _ in range(20):
        for monkey in monkeys:
            monkey_activity[monkey.monkey_id] += len(monkey.items)
            for _ in range(len(monkey.items)):
                item = monkey.get_item_next_value()
                target_id = monkey.get_next_monkey_id(item)
                monkeys[target_id].items.append(item)
    return math.prod(sorted(monkey_activity, reverse=True)[:2])


def part_b(data: list[str]) -> Union[int, str, None]:
    """Solution to part B.

    Args:
        data (list[str]): Advent of Code challenge input.

    Returns:
        Union[int, str, None]: Solution to the challenge.
    """
    monkeys: list[Monkey] = []
    common_denominator = 1
    for monkey in "\n".join(data).split("\n\n"):
        monkey_info = monkey.split("\n")
        monkey_id = int(monkey_info[0].split()[1][:-1])
        monkey_items = [int(item) for item in monkey_info[1].split(": ")[1].split(", ")]
        monkey_func = monkey_info[2].split("new = ")[1].replace("old", "x")
        divider = int(monkey_info[3].split("divisible by ")[1])
        target_monkey_id: dict[bool, int] = {
            True: int(monkey_info[4].split("throw to monkey ")[1]),
            False: int(monkey_info[5].split("throw to monkey ")[1]),
        }
        monkeys.append(
            Monkey(monkey_id, monkey_items, monkey_func, divider, target_monkey_id)
        )
        common_denominator *= divider

    monkey_activity = [0 for _ in range(len(monkeys))]
    for _ in range(10000):
        for monkey in monkeys:
            monkey_activity[monkey.monkey_id] += len(monkey.items)
            for _ in range(len(monkey.items)):
                item = monkey.get_item_next_value() % common_denominator
                target_id = monkey.get_next_monkey_id(item)
                monkeys[target_id].items.append(item)
    return math.prod(sorted(monkey_activity, reverse=True)[:2])
