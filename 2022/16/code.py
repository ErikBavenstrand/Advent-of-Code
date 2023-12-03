# Advent of Code 2022 Day 16
# Author: Erik Båvenstrand
# URL: https://adventofcode.com/2022/day/16

import functools
from typing import Literal, TypedDict, Union


class Valve(TypedDict):
    flow: int
    valves: list[str]


GraphType = dict[str, Valve]


@functools.cache
def traverse_graph(
    current_valve: str,
    time_remaining: int,
    opened_valves: frozenset[str],
    is_part_1: bool = True,
):
    if time_remaining <= 0:
        return 0 if is_part_1 else traverse_graph("AA", 26, opened_valves, True)

    global graph
    best = 0
    state = graph[current_valve]
    for valve in state["valves"]:
        best = max(
            best, traverse_graph(valve, time_remaining - 1, opened_valves, is_part_1)
        )

    if current_valve not in opened_valves and state["flow"] > 0 and time_remaining > 0:
        opened_valves_set = set(opened_valves)
        opened_valves_set.add(current_valve)
        time_remaining -= 1
        new_sum = time_remaining * state["flow"]

        for valve in state["valves"]:
            best = max(
                best,
                new_sum
                + traverse_graph(
                    valve, time_remaining - 1, frozenset(opened_valves_set), is_part_1
                ),
            )
    return best


graph: GraphType = {}

def solve_valve_issue(data: list[str], part: Union[Literal["A"], Literal["B"]]):
    

def part_a(data: list[str]) -> Union[int, str, None]:
    """Solution to part A.

    Args:
        data (list[str]): Advent of Code challenge input.

    Returns:
        Union[int, str, None]: Solution to the challenge.
    """
    global graph
    for line in data:
        line = line.strip().replace(",", "").split(" ")
        valve = line[1]
        flow = int(line[4].split("=")[-1].split(";")[0])
        valves = line[9:]
        graph[valve] = {"flow": flow, "valves": valves}
    return traverse_graph("AA", 30, frozenset())


def part_b(data: list[str]) -> Union[int, str, None]:
    """Solution to part B.

    Args:
        data (list[str]): Advent of Code challenge input.

    Returns:
        Union[int, str, None]: Solution to the challenge.
    """
    global graph
    for line in data:
        line = line.strip().replace(",", "").split(" ")
        valve = line[1]
        flow = int(line[4].split("=")[-1].split(";")[0])
        valves = line[9:]
        graph[valve] = {"flow": flow, "valves": valves}
    return traverse_graph("AA", 26, frozenset(), False)
