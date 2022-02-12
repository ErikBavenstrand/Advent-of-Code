from abc import ABC


class Graph(ABC):

    def __init__(self):
        self._vertexdict: dict = dict()

    def add_node(self, node):
        node.name
