# Advent of Code 2024 Day 05
# Author: Erik Båvenstrand
# URL: https://adventofcode.com/2024/day/5


from collections import defaultdict


def get_rule_mapping(rules: list[str]) -> dict[str, set[str]]:
    """Get a mapping of rule mappings for pages.

    Args:
        rules: A list of rules.

    Returns:
        A dictionary mapping pages to rules.
    """
    rule_mapping: dict[str, set[str]] = defaultdict(set)
    for rule in rules:
        before, after = rule.split("|")
        rule_mapping[before].add(after)
    return rule_mapping


def is_valid_manual(pages: list[str], rule_mapping: dict[str, set[str]]) -> tuple[bool, tuple[int, int]]:
    """Check if a manual is valid according to the rule mapping.

    Args:
        pages: List of pages in the manual.
        rule_mapping: Mapping of rules for pages.

    Returns:
        A tuple containing a boolean indicating if the manual is valid
        and a tuple containing the index of the invalid page and the
        index of the page that caused the invalidity.
    """
    seen_pages: set[str] = set()
    seen_pages_idx: dict[str, int] = {}
    for i, page in enumerate(pages):
        for prior in rule_mapping[page]:
            if prior in seen_pages:
                return False, (i, seen_pages_idx[prior])
        seen_pages_idx[page] = i
        seen_pages.add(page)
    return True, (-1, -1)


def part_a(data: list[str]) -> int | str | None:
    """Solution to part A.

    Args:
        data: Advent of Code challenge input.

    Returns:
        Solution to the challenge.
    """
    rules, manuals = [lines.splitlines() for lines in "\n".join(data).split("\n\n")]
    rule_mapping = get_rule_mapping(rules)

    result = 0
    for manual in manuals:
        pages = manual.split(",")
        is_valid, _ = is_valid_manual(pages, rule_mapping)
        if is_valid:
            result += int(pages[len(pages) // 2])
    return result


def part_b(data: list[str]) -> int | str | None:
    """Solution to part B.

    Args:
        data: Advent of Code challenge input.

    Returns:
        Solution to the challenge.
    """
    rules, manuals = [lines.splitlines() for lines in "\n".join(data).split("\n\n")]
    rule_mapping = get_rule_mapping(rules)

    result = 0
    for manual in manuals:
        pages = manual.split(",")
        is_valid, _ = is_valid_manual(pages, rule_mapping)
        if not is_valid:
            while not is_valid:
                is_valid, (i, j) = is_valid_manual(pages, rule_mapping)
                if not is_valid:
                    tmp = pages[i]
                    pages[i] = pages[j]
                    pages[j] = tmp
            result += int(pages[len(pages) // 2])
    return result
