# Advent of Code 2021 Day 18
# Author: Erik Båvenstrand
# URL: https://adventofcode.com/2021/day/18

from __future__ import annotations

import ast
import itertools
import math
from typing import Union


class Node:
    def __init__(self, data=None, parent: Node = None):
        self.parent: Union[Node, None] = parent
        self.left = None
        self.right = None
        self.value = None
        self.insert(data)

    def insert(self, data):
        if isinstance(data, list):
            self.left = Node(data[0], self)
            self.right = Node(data[1], self)
        elif isinstance(data, int):
            self.value = int(data)

    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.value
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        elif self.right is None and self.left:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.value
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None and self.right:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.value
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        if self.left and self.right:
            left, n, p, x = self.left._display_aux()
            right, m, q, y = self.right._display_aux()
            s = '%s' % self.value
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * \
                '_' + s + y * '_' + (m - y) * ' '
            second_line = x * ' ' + '/' + \
                (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
            if p < q:
                left += [n * ' '] * (q - p)
            elif q < p:
                right += [m * ' '] * (p - q)
            zipped_lines = zip(left, right)
            lines = [first_line, second_line] + \
                [a + u * ' ' + b for a, b in zipped_lines]
            return lines, n + m + u, max(p, q) + 2, n + u // 2


def get_leftmost_child(node: Node) -> Node:
    if node.left is not None:
        return get_leftmost_child(node.left)
    else:
        return node


def get_rightmost_child(node: Node) -> Node:
    if node.right is not None:
        return get_rightmost_child(node.right)
    else:
        return node


def get_right_neighbor(node: Node) -> Union[None, Node]:
    if node.parent is not None:
        right = node.parent.right
        left = node.parent.left
        if right is not None and node != right:
            return get_leftmost_child(right)
        elif left is not None and node != left:
            return get_right_neighbor(node.parent)
    else:
        return None


def get_left_neighbor(node: Node) -> Union[None, Node]:
    if node.parent is not None:
        right = node.parent.right
        left = node.parent.left
        if right is not None and node != right:
            return get_left_neighbor(node.parent)
        elif left is not None and node != left:
            return get_rightmost_child(left)
    else:
        return None


def explode(node: Node, level: int = 0) -> bool:
    if level == 4:
        if node.left is not None and \
           node.right is not None and \
           node.left.value is not None and \
           node.right.value is not None:
            node.value = 0
            left = get_left_neighbor(node)
            if left is not None and left.value is not None:
                left.value += node.left.value
            right = get_right_neighbor(node)
            if right is not None and right.value is not None:
                right.value += node.right.value
            node.left = node.right = None
            return True
        return False
    else:
        left_exploded = right_exploded = False
        if node.left is not None:
            left_exploded = explode(node.left, level + 1)
        if node.right is not None:
            right_exploded = explode(node.right, level + 1)
        return left_exploded or right_exploded


def split(node: Node) -> bool:
    if node.value is not None and node.value >= 10:
        node.left = Node(math.floor(node.value / 2), node)
        node.right = Node(math.ceil(node.value / 2), node)
        node.value = None
        return True
    else:
        left_splutted = right_splutted = False
        if node.left is not None:
            left_splutted = split(node.left)
        if node.right is not None and not left_splutted:
            right_splutted = split(node.right)
        return left_splutted or right_splutted


def add(a: Node, b: Node):
    root = Node()
    root.left = a
    root.right = b
    root.left.parent = root
    root.right.parent = root
    changed = True
    while changed:
        exploded = explode(root)
        # root.display()
        splutted = split(root)
        # root.display()
        if not exploded and not splutted:
            changed = False
    return root


def magnitude(node: Node):
    sum = 0 if node.value is None else node.value
    if node.left:
        sum += 3 * magnitude(node.left)
    if node.right:
        sum += 2 * magnitude(node.right)
    return sum


def part_a(data: list[str]):
    root = Node(ast.literal_eval(data[0]))
    for i in range(1, len(data)):
        b = Node(ast.literal_eval(data[i]))
        root = add(root, b)
    return magnitude(root)


def part_b(data: list[str]):
    max = 0
    for a, b in itertools.permutations(data, 2):
        a = Node(ast.literal_eval(a))
        b = Node(ast.literal_eval(b))
        root = add(a, b)
        mag = magnitude(root)
        max = mag if mag > max else max
    return max
