# Advent of Code 2021 Day 03
# Author: Erik Båvenstrand
# URL: https://adventofcode.com/2021/day/3

class Node:
    def __init__(self, data: str, parent=None) -> None:
        self.zero = None
        self.one = None
        self.parent = parent
        self.val = data
        self.count = 0

    def insert(self, data: list) -> None:
        self.count += 1
        if len(data) == 0:
            return
        if data[0] == "0":
            if not self.zero:
                self.zero = Node("0", self)
            self.zero.insert(data[1:])
        elif data[0] == "1":
            if not self.one:
                self.one = Node("1", self)
            self.one.insert(data[1:])

    def __str__(self) -> str:
        tree_str = ""
        tree_str += f"({str(self.val)}, {str(self.count)})"
        if self.zero:
            tree_str += str(self.zero)
        if self.one:
            tree_str += str(self.one)
        return tree_str


def part_a(data: list[str]):
    acc = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    total = 0
    for line in data:
        for (i, v) in enumerate(list(line)):
            acc[i] += int(v)
        total += 1

    val = ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"]
    inv = ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"]
    for (i, v) in enumerate(acc):
        val[i] = str(1 if v > total / 2 else 0)
        inv[i] = str(1 if int(val[i]) == 0 else 0)

    return int("".join(val), 2) * int("".join(inv), 2)


def part_b(data: list[str]):
    root_node = Node("root")
    for bin in data:
        bin = bin.strip("\n")
        root_node.insert(list(bin))

    def most_freq(node: Node) -> Node:
        if node.one and node.zero:
            if node.one.count >= node.zero.count:
                return most_freq(node.one)
            else:
                return most_freq(node.zero)
        elif not node.one and node.zero:
            return most_freq(node.zero)
        elif node.one and not node.zero:
            return most_freq(node.one)
        else:
            return node

    def least_freq(node: Node) -> Node:
        if node.one and node.zero:
            if node.zero.count <= node.one.count:
                return least_freq(node.zero)
            else:
                return least_freq(node.one)
        elif not node.one and node.zero:
            return least_freq(node.zero)
        elif node.one and not node.zero:
            return least_freq(node.one)
        else:
            return node

    def get_str(node: Node) -> str:
        if not node.parent:
            return ""
        return get_str(node.parent) + node.val

    m = most_freq(root_node)
    le = least_freq(root_node)

    return int(get_str(m), 2) * int(get_str(le), 2)
