from __future__ import annotations

from abc import ABC
from typing import Any, Optional, Union


class BinaryNode(ABC):
    def __init__(self, data: Any = None, parent: Optional[BinaryNode] = None):
        self.left: Union[BinaryNode, None] = None
        self.right: Union[BinaryNode, None] = None
        self.parent: Union[BinaryNode, None] = parent
        self.value: Any = None
        self.insert(data)

    def insert(self, data: Any):
        if isinstance(data, list):
            self.left = BinaryNode(data[0], self)
            self.right = BinaryNode(data[1], self)
        elif isinstance(data, int):
            self.value = int(data)

    def __str__(self):
        lines, *_ = self._display_aux()
        return lines

    def _display_aux(self: BinaryNode):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = "%s" % self.value
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        elif self.right is None and self.left:
            lines, n, p, x = self.left._display_aux()
            s = "%s" % self.value
            u = len(s)
            first_line = (x + 1) * " " + (n - x - 1) * "_" + s
            second_line = x * " " + "/" + (n - x - 1 + u) * " "
            shifted_lines = [line + u * " " for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None and self.right:
            lines, n, p, x = self.right._display_aux()
            s = "%s" % self.value
            u = len(s)
            first_line = s + x * "_" + (n - x) * " "
            second_line = (u + x) * " " + "\\" + (n - x - 1) * " "
            shifted_lines = [u * " " + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        if self.left and self.right:
            left, n, p, x = self.left._display_aux()
            right, m, q, y = self.right._display_aux()
            s = "%s" % self.value
            u = len(s)
            first_line = (x + 1) * " " + (n - x - 1) * "_" + s + y * "_" + (m - y) * " "
            second_line = (
                x * " " + "/" + (n - x - 1 + u + y) * " " + "\\" + (m - y - 1) * " "
            )
            if p < q:
                left += [n * " "] * (q - p)
            elif q < p:
                right += [m * " "] * (p - q)
            zipped_lines = zip(left, right)
            lines = [first_line, second_line] + [
                a + u * " " + b for a, b in zipped_lines
            ]
            return lines, n + m + u, max(p, q) + 2, n + u // 2
