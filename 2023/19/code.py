# Advent of Code 2023 Day 19
# Author: Erik Båvenstrand
# URL: https://adventofcode.com/2023/day/19


def parse_workflow(
    rules_str: str,
) -> tuple[list[tuple[str, bool, int, str]], str]:
    """Parses the workflow into a list of tuples.

    Args:
        workflow_str: The workflow to parse.

    Returns:
        A list of tuples.
    """
    parsed_workflow: list[tuple[str, bool, int, str]] = []
    for rule in rules_str.split(",")[:-1]:
        condition, next_workflow_name = rule.split(":")
        category, operator, value = condition[0], condition[1], condition[2:]
        parsed_workflow.append(
            (category, operator == "<", int(value), next_workflow_name)
        )
    return parsed_workflow, rules_str.split(",")[-1]


def parse_part(part_str: str) -> dict[str, int]:
    """Parses a part string into a dict.

    Args:
        part_str: The part string to parse.

    Returns:
        A dict of the categories and their ratings for the part.
    """
    return {
        category: int(rating)
        for category, rating in map(
            lambda x: x.split("=", 1), part_str[1:-1].split(",")
        )
    }


def process_inputs(
    data: list[str],
) -> tuple[
    dict[str, tuple[list[tuple[str, bool, int, str]], str]], list[dict[str, int]]
]:
    """Get the workflows and parts from the data.

    Args:
        data: Advent of Code challenge input.

    Returns:
        A tuple of the workflows and parts.
    """
    workflows_str, parts_str = [
        text.split("\n") for text in "\n".join(data).split("\n\n")
    ]
    workflows: dict[str, tuple[list[tuple[str, bool, int, str]], str]] = {}
    for workflow_str in workflows_str:
        name, rules_str = workflow_str[:-1].split("{")
        workflows[name] = parse_workflow(rules_str)

    parts: list[dict[str, int]] = []
    for part_str in parts_str:
        parts.append(parse_part(part_str))

    return workflows, parts


def execute_workflow(
    workflow: tuple[list[tuple[str, bool, int, str]], str], part: dict[str, int]
) -> str:
    """Executes a workflow.

    Args:
        workflow: The workflow to execute.
        part: The part to execute the workflow on.

    Returns:
        The name of the next workflow.
    """
    rules, default = workflow
    for rule in rules:
        category, less_than, value, next_category = rule
        if less_than:
            if part[category] < value:
                return next_category
        else:
            if part[category] > value:
                return next_category
    return default


def propagate_ranged_parts_workflow(
    workflows: dict[str, tuple[list[tuple[str, bool, int, str]], str]],
    workflow_name: str,
    part: dict[str, tuple[int, int]],
) -> int:
    """Propagates the ranged parts workflow.

    Args:
        workflows: The workflow definitions.
        workflow_name: The name of the workflow to execute.
        part: The part to execute the instruction on.

    Returns:
        The number of combinations.
    """
    combinations = 0
    rules, default = workflows[workflow_name]
    for rule in rules:
        category, less_than, value, next_workflow_name = rule
        part_low, part_high = part[category]
        if (less_than and part_low < value and part_high < value) or (
            not less_than and part_low > value and part_high > value
        ):
            return combinations + calculate_combinations(
                workflows, next_workflow_name, part
            )

        if (less_than and part_low >= value and part_high >= value) or (
            not less_than and part_low <= value and part_high <= value
        ):
            continue

        splitted_part = part.copy()
        if less_than:
            splitted_part[category] = (part_low, value - 1)
            part[category] = (value, part_high)
        else:
            splitted_part[category] = (value + 1, part_high)
            part[category] = (part_low, value)

        combinations += calculate_combinations(
            workflows, next_workflow_name, splitted_part
        )
    return combinations + calculate_combinations(workflows, default, part)


def calculate_combinations(
    workflows: dict[str, tuple[list[tuple[str, bool, int, str]], str]],
    workflow_name: str,
    part: dict[str, tuple[int, int]],
) -> int:
    """Calculates the number of combinations for a part inside the ranges.

    Args:
        workflows: The workflow definitions.
        workflow_name: The name of the workflow to execute.
        part: The part to calculate the combinations for.

    Returns:
        The number of combinations.
    """
    match workflow_name:
        case "A":
            return (
                (part["x"][1] - part["x"][0] + 1)
                * (part["m"][1] - part["m"][0] + 1)
                * (part["a"][1] - part["a"][0] + 1)
                * (part["s"][1] - part["s"][0] + 1)
            )
        case "R":
            return 0
    return propagate_ranged_parts_workflow(workflows, workflow_name, part)


def part_a(data: list[str]) -> int | str | None:
    """Solution to part A.

    Args:
        data: Advent of Code challenge input.

    Returns:
        Solution to the challenge.
    """
    workflows, parts = process_inputs(data)
    part_sum = 0
    for part in parts:
        workflow = "in"
        while workflow not in ["A", "R"]:
            workflow = execute_workflow(workflows[workflow], part)
        part_sum += int(workflow == "A") * sum(part.values())
    return part_sum


def part_b(data: list[str]) -> int | str | None:
    """Solution to part B.

    Args:
        data: Advent of Code challenge input.

    Returns:
        Solution to the challenge.
    """
    workflows, _ = process_inputs(data)
    xmas: dict[str, tuple[int, int]] = {
        "x": (1, 4000),
        "m": (1, 4000),
        "a": (1, 4000),
        "s": (1, 4000),
    }
    return calculate_combinations(workflows, "in", xmas)
