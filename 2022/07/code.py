# Advent of Code 2022 Day 07
# Author: Erik Båvenstrand
# URL: https://adventofcode.com/2022/day/7

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Optional, Union

import numpy as np


class AbstractTree(ABC):
    
    @abstractmethod
    def is_leaf


class Node(ABC):
    def __init__(self, size: int, name: str, parent: Optional[Node] = None):
        self.size: int = size
        self.name: str = name
        if parent:
            self.parent: Node = parent
        self.children: list[Node] = []

    def __str__(self, level=0):
        ret = "  " * level + repr(self) + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret

    def __repr__(self):
        return f"{self.name} - {self.size}"

    def add_child(self, child: Node):
        self.size += child.size
        self.propagate_update_size(child.size)
        self.children.append(child)

    def propagate_update_size(self, size: int):
        try:
            self.parent.size += size
            self.parent.propagate_update_size(size)
        except AttributeError:
            pass

    def get_child(self, child_name):
        for child in self.children:
            if child.name == child_name:
                return child
        new_child = Node(0, child_name, self)
        self.add_child(new_child)
        return new_child


def part_a(data: list[str]) -> Union[int, str, None]:
    """Solution to part A.

    Args:
        data (list[str]): Advent of Code challenge input.

    Returns:
        Union[int, str, None]: Solution to the challenge.
    """
    root = Node(0, "/")
    current_dir: Node = root
    dirs = [root]
    for line in data:
        line_parts = line.split(" ")

        match line_parts:
            case "$", "cd", "..":
                current_dir = current_dir.parent
            case "$", "cd", "/":
                current_dir = root
            case "$", "cd", dir:
                current_dir = current_dir.get_child(dir)
            case "$", "ls":
                pass
            case "dir", name:
                subdir = Node(0, name, current_dir)
                current_dir.add_child(subdir)
                dirs.append(subdir)
            case size, name:
                current_dir.add_child(Node(int(size), name, current_dir))

    dir_sizes = [directory.size for directory in dirs]
    dir_size_sum = 0
    for size in dir_sizes:
        if size <= 100000:
            dir_size_sum += size

    return dir_size_sum


def part_b(data: list[str]) -> Union[int, str, None]:
    """Solution to part B.

    Args:
        data (list[str]): Advent of Code challenge input.

    Returns:
        Union[int, str, None]: Solution to the challenge.
    """
    root = Node(0, "/")
    current_dir: Node = root
    dirs = [root]
    for line in data:
        line_parts = line.split(" ")

        match line_parts:
            case "$", "cd", "..":
                current_dir = current_dir.parent
            case "$", "cd", "/":
                current_dir = root
            case "$", "cd", dir:
                current_dir = current_dir.get_child(dir)
            case "$", "ls":
                pass
            case "dir", name:
                subdir = Node(0, name, current_dir)
                current_dir.add_child(subdir)
                dirs.append(subdir)
            case size, name:
                current_dir.add_child(Node(int(size), name, current_dir))

    print(root)
    dir_sizes = np.array(sorted([directory.size for directory in dirs]))
    min_viable_dir_size = dir_sizes[dir_sizes >= dir_sizes[-1] - 40000000][0]

    return min_viable_dir_size
