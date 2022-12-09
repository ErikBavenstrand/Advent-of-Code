from __future__ import annotations

from abc import ABC
from typing import Iterable, Union

from adventlib.tree.errors import CircularTreeError, TreeError


class NodeMixin(ABC):
    def __init__(self) -> None:
        self.__parent: Union[NodeMixin, None] = None
        self.__children: list[NodeMixin] = []

    @property
    def parent(self) -> Union[NodeMixin, None]:
        """Get parent of Node.

        Returns:
            Parent of Node.
        """
        return self.__parent

    @parent.setter
    def parent(self, new_parent: Union[NodeMixin, None]) -> None:
        if new_parent is not None and not isinstance(new_parent, NodeMixin):
            raise TreeError(
                f"Parent node {repr(new_parent)} is not subclass of type 'NodeMixin'."
            )

        parent = self.__parent
        if parent is not new_parent:
            self.__check_loop(new_parent)
            self.__detach_parent()
            self.__attach_parent(new_parent)

    @property
    def children(self) -> tuple[NodeMixin, ...]:
        """Get children of Node.

        Returns:
            Children of Node.
        """
        return tuple(self.__children)

    @children.setter
    def children(self, children: list[NodeMixin]):
        children_tuple = tuple(children)
        NodeMixin.__check_children(children_tuple)
        old_children = self.__children
        del self.children
        try:
            self._pre_attach_children(children_tuple)
            for child in children_tuple:
                child.parent = self
            self._post_attach_children(children_tuple)
        except Exception:
            self.children = old_children
            raise

    @children.deleter
    def children(self):
        children = self.children
        self._pre_detach_children(children)
        for child in children:
            child.parent = None
        assert len(self.children) == 0
        self._post_detach_children(children)

    def __check_loop(self, node: Union[NodeMixin, None]) -> None:
        if node is not None:
            if node is self:
                raise CircularTreeError(
                    f"Cannot set parent. {repr(self)} cannot be parent of itself."
                )
            if any(parent is self for parent in node.__iter_path_reverse()):
                raise CircularTreeError(
                    f"Cannot set parent. {repr(self)} is parent of {repr(node)}"
                )

    def __detach_parent(self) -> None:
        parent = self.__parent
        if parent is not None:
            self._pre_detach_parent(parent)
            children = parent.__children
            assert any(child is self for child in children), "Tree is corrupt."
            parent.__children = [child for child in children if child is not self]
            self.__parent = None
            self._post_detach_parent(parent)

    def __attach_parent(self, parent: Union[NodeMixin, None]) -> None:
        if parent is not None:
            self._pre_attach_parent(parent)
            children = parent.__children
            assert not any(child is self for child in children), "Tree is corrupt."
            children.append(self)
            self.__parent = parent
            self._post_attach_parent(parent)

    def __iter_path_reverse(self) -> Iterable[NodeMixin]:
        node = self
        while node is not None:
            yield node
            node = node.parent

    def _pre_detach_parent(self, parent: NodeMixin) -> None:
        pass

    def _post_detach_parent(self, parent: NodeMixin) -> None:
        pass

    def _pre_attach_parent(self, parent: NodeMixin) -> None:
        pass

    def _post_attach_parent(self, parent: NodeMixin) -> None:
        pass

    def _pre_detach_children(self, children: tuple[NodeMixin, ...]) -> None:
        pass

    def _post_detach_children(self, children: tuple[NodeMixin, ...]) -> None:
        pass

    def _pre_attach_children(self, children: tuple[NodeMixin, ...]) -> None:
        pass

    def _post_attach_children(self, children: tuple[NodeMixin, ...]) -> None:
        pass

    @staticmethod
    def __check_children(children: tuple[NodeMixin, ...]):
        seen = set()
        for child in children:
            if not isinstance(child, NodeMixin):
                raise TreeError(
                    f"Cannot add non-node object {repr(child)}. It is not a subclass of 'NodeMixin'."
                )
            child_id = id(child)
            if child_id not in seen:
                seen.add(child_id)
            else:
                raise TreeError(
                    f"Cannot add node {repr(child)} multiple times as child."
                )
