# Advent of Code 2023 Day 20
# Author: Erik Båvenstrand
# URL: https://adventofcode.com/2023/day/20

from abc import ABC
from collections import deque
from enum import Enum
from math import gcd


class ModuleType(Enum):
    """Module types."""

    FLIP_FLOP = "%"
    CONJUNCTION = "&"
    BROADCASTER = "broadcaster"


class PulseType(Enum):
    """Pulse types."""

    LOW = 0
    HIGH = 1


class Module(ABC):
    """Abstract module."""

    name: str
    type: ModuleType
    destinations: list[str]
    memory: bool | dict[str, PulseType]


class MemoryModule(Module, ABC):
    """Abstract memory module."""

    memory: dict[str, PulseType]


class BroadcasterModule(MemoryModule):
    """Broadcaster module."""

    def __init__(self, name: str, destinations: list[str]) -> None:
        """Initialize broadcaster module.

        Args:
            name: Name of module.
            destinations: Destinations of module.
        """
        self.name = name
        self.type = ModuleType.BROADCASTER
        self.destinations = destinations
        self.memory = {}


class ConjunctionModule(MemoryModule):
    """Conjunction module."""

    def __init__(self, name: str, destinations: list[str]) -> None:
        """Initialize conjunction module.

        Args:
            name: Name of module.
            destinations: Destinations of module.
        """
        self.name = name
        self.type = ModuleType.CONJUNCTION
        self.destinations = destinations
        self.memory = {}


class FlipFlopModule(Module):
    """Flip-flop module."""

    memory: bool

    def __init__(self, name: str, destinations: list[str]) -> None:
        """Initialize flip-flop module.

        Args:
            name: Name of module.
            destinations: Destinations of module.
        """
        self.name = name
        self.type = ModuleType.FLIP_FLOP
        self.destinations = destinations
        self.memory = False


def get_modules(data: list[str]) -> dict[str, Module]:
    """Get modules.

    Args:
        data: Advent of Code challenge input.

    Returns:
        Modules.
    """
    modules: dict[str, Module] = {}
    for line in data:
        name, destinations = line.split(" -> ")
        destinations = destinations.split(", ")
        if name == "broadcaster":
            module = BroadcasterModule(name, destinations)
        elif name.startswith("%"):
            module = FlipFlopModule(name[1:], destinations)
        else:
            module = ConjunctionModule(name[1:], destinations)
        modules[module.name] = module

    for name, module in modules.items():
        for destination in module.destinations:
            dest_module = modules.get(destination, None)
            if dest_module is not None and isinstance(dest_module, MemoryModule):
                dest_module.memory[name] = PulseType.LOW

    return modules


def part_a(data: list[str]) -> int | str | None:
    """Solution to part A.

    Args:
        data: Advent of Code challenge input.

    Returns:
        Solution to the challenge.
    """
    modules = get_modules(data)

    low_pulses = 0
    high_pulses = 0
    for _ in range(1000):
        low_pulses += 1

        queue: deque[tuple[str, str, PulseType]] = deque(
            [
                ("broadcaster", x, PulseType.LOW)
                for x in modules["broadcaster"].destinations
            ]
        )

        while queue:
            source, destination, pulse = queue.popleft()

            if pulse == PulseType.LOW:
                low_pulses += 1
            else:
                high_pulses += 1

            if destination not in modules:
                continue

            module = modules[destination]

            if not isinstance(module, MemoryModule):
                if pulse == PulseType.LOW:
                    module.memory = module.memory is False
                    outgoing_pulse = PulseType.HIGH if module.memory else PulseType.LOW
                    for dest_name in module.destinations:
                        queue.append((module.name, dest_name, outgoing_pulse))

            else:
                module.memory[source] = pulse
                outgoing_pulse = (
                    PulseType.LOW
                    if all(pulse == PulseType.HIGH for pulse in module.memory.values())
                    else PulseType.HIGH
                )
                for dest in module.destinations:
                    queue.append((module.name, dest, outgoing_pulse))
    return low_pulses * high_pulses


def part_b(data: list[str]) -> int | str | None:  # noqa: C901
    """Solution to part B.

    Args:
        data: Advent of Code challenge input.

    Returns:
        Solution to the challenge.
    """
    modules = get_modules(data)
    rx_feeder = ""
    for module in modules.values():
        if "rx" in module.destinations:
            rx_feeder = module.name

    lengths = {}
    visited = {
        name: 0 for name, module in modules.items() if rx_feeder in module.destinations
    }
    count = 0

    while True:
        count += 1
        queue: deque[tuple[str, str, PulseType]] = deque(
            [
                ("broadcaster", x, PulseType.LOW)
                for x in modules["broadcaster"].destinations
            ]
        )

        while queue:
            source, destination, pulse = queue.popleft()

            if destination not in modules:
                continue

            module = modules[destination]

            if module.name == rx_feeder and pulse == PulseType.HIGH:
                visited[source] += 1

                if source not in lengths:
                    lengths[source] = count

                if all(visited.values()):
                    product = 1
                    for length in lengths.values():
                        product = product * length // gcd(product, length)
                    return product

            if not isinstance(module, MemoryModule):
                if pulse == PulseType.LOW:
                    module.memory = module.memory is False
                    outgoing_pulse = PulseType.HIGH if module.memory else PulseType.LOW
                    for dest in module.destinations:
                        queue.append((module.name, dest, outgoing_pulse))

            else:
                module.memory[source] = pulse
                outgoing_pulse = (
                    PulseType.LOW
                    if all(pulse == PulseType.HIGH for pulse in module.memory.values())
                    else PulseType.HIGH
                )
                for dest in module.destinations:
                    queue.append((module.name, dest, outgoing_pulse))
