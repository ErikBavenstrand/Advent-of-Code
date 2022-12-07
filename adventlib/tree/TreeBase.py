from abc import ABC


class Tree(ABC):
    def __init__(self):
        self.children: list[Tree] = []
