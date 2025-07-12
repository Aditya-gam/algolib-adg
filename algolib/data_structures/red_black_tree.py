"""Red-Black Tree implementation (insertion only)."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum, auto
from typing import Generic, Iterator, Optional

from algolib._typing import ComparableT

from ._rotation_mixin import RotationMixin


class Color(Enum):
    RED = auto()
    BLACK = auto()


@dataclass(slots=True)
class _RBNode(Generic[ComparableT]):
    key: ComparableT
    color: Color = Color.RED
    left: Optional["_RBNode[ComparableT]"] = field(default=None, repr=False)
    right: Optional["_RBNode[ComparableT]"] = field(default=None, repr=False)
    parent: Optional["_RBNode[ComparableT]"] = field(default=None, repr=False)


class RedBlackTree(Generic[ComparableT], RotationMixin[_RBNode[ComparableT]]):
    """Red-Black Tree with insert and search operations."""

    _root: Optional[_RBNode[ComparableT]]

    def __init__(self) -> None:
        self._root = None

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def insert(self, key: ComparableT) -> None:
        new_node = _RBNode(key)
        self._bst_insert(new_node)
        self._fix_insert(new_node)

    def contains(self, key: ComparableT) -> bool:
        return self._search(self._root, key) is not None

    def inorder(self) -> Iterator[ComparableT]:
        yield from self._inorder(self._root)

    def preorder(self) -> Iterator[ComparableT]:
        yield from self._preorder(self._root)

    def postorder(self) -> Iterator[ComparableT]:
        yield from self._postorder(self._root)

    def search(self, key: ComparableT) -> bool:
        return self.contains(key)

    def delete(self, key: ComparableT) -> bool:
        # Basic deletion - not fully implemented for Red-Black Tree
        # This is a simplified version that just removes the node
        if not self.contains(key):
            return False
        # For now, implement a basic BST deletion without rebalancing
        self._root = self._delete_basic(self._root, key)
        return True

    def find_min(self) -> ComparableT:
        if self._root is None:
            raise ValueError("Tree is empty")
        return self._find_min(self._root).key

    def find_max(self) -> ComparableT:
        if self._root is None:
            raise ValueError("Tree is empty")
        return self._find_max(self._root).key

    def height(self) -> int:
        return self._height(self._root)

    def size(self) -> int:
        return len(self)

    def is_empty(self) -> bool:
        return self._root is None

    def clear(self) -> None:
        self._root = None

    def _delete_basic(
        self, node: Optional[_RBNode[ComparableT]], key: ComparableT
    ) -> Optional[_RBNode[ComparableT]]:
        """Basic BST deletion without Red-Black rebalancing."""
        if node is None:
            return None

        if key < node.key:
            node.left = self._delete_basic(node.left, key)
        elif key > node.key:
            node.right = self._delete_basic(node.right, key)
        else:
            # Node to be deleted found
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                # Node has two children
                successor = self._find_min(node.right)
                node.key = successor.key
                node.right = self._delete_basic(node.right, successor.key)

        return node

    # ------------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------------

    def _bst_insert(self, node: _RBNode[ComparableT]) -> None:
        y: Optional[_RBNode[ComparableT]] = None
        x = self._root
        while x is not None:
            y = x
            if node.key < x.key:
                x = x.left
            elif node.key > x.key:
                x = x.right
            else:
                return  # duplicate keys ignored
        node.parent = y
        if y is None:
            self._root = node
        elif node.key < y.key:
            y.left = node
        else:
            y.right = node

    # Fix violations after insertion ------------------------------------

    def _fix_insert(self, z: _RBNode[ComparableT]) -> None:
        while z.parent and z.parent.color == Color.RED:
            if z.parent.parent is None:
                break  # Should not happen if root is properly colored black

            if z.parent == z.parent.parent.left:
                z = self._handle_red_parent_left_case(z)
            else:  # z.parent is the right child
                z = self._handle_red_parent_right_case(z)

        if self._root:
            self._root.color = Color.BLACK

    def _handle_red_parent_left_case(self, z: _RBNode[ComparableT]) -> _RBNode[ComparableT]:
        """Fix Red-Black Tree violations when parent of z is a left child."""
        assert z.parent is not None
        parent = z.parent
        assert parent.parent is not None
        grandparent = parent.parent
        uncle = grandparent.right
        if uncle and uncle.color == Color.RED:
            parent.color = Color.BLACK
            uncle.color = Color.BLACK
            grandparent.color = Color.RED
            z = grandparent
        else:
            if z == parent.right:
                z = parent
                self._rotate_left(z)
                if z.parent is not None:
                    parent = z.parent
            if z.parent is not None:
                parent = z.parent
                parent.color = Color.BLACK
                if parent.parent is not None:
                    grandparent = parent.parent
                    grandparent.color = Color.RED
                    self._rotate_right(grandparent)
        return z

    def _handle_red_parent_right_case(self, z: _RBNode[ComparableT]) -> _RBNode[ComparableT]:
        """Fix Red-Black Tree violations when parent of z is a right child."""
        assert z.parent is not None
        parent = z.parent
        assert parent.parent is not None
        grandparent = parent.parent
        uncle = grandparent.left
        if uncle and uncle.color == Color.RED:
            parent.color = Color.BLACK
            uncle.color = Color.BLACK
            grandparent.color = Color.RED
            z = grandparent
        else:
            if z == parent.left:
                z = parent
                self._rotate_right(z)
                if z.parent is not None:
                    parent = z.parent
            if z.parent is not None:
                parent = z.parent
                parent.color = Color.BLACK
                if parent.parent is not None:
                    grandparent = parent.parent
                    grandparent.color = Color.RED
                    self._rotate_left(grandparent)
        return z

    # Override rotations to maintain parent links -----------------------

    def _rotate_left(self, x: _RBNode[ComparableT]) -> _RBNode[ComparableT]:
        y = super()._rotate_left(x)
        # If rotation didn't happen (y is the same as x), return x
        if y is x:
            return x
        parent = x.parent
        y.parent = parent
        x.parent = y
        if x.right:
            x.right.parent = x
        if parent is None:
            self._root = y
        else:
            if parent.left == x:
                parent.left = y
            else:
                parent.right = y
        return y

    def _rotate_right(self, y: _RBNode[ComparableT]) -> _RBNode[ComparableT]:
        x = super()._rotate_right(y)
        # If rotation didn't happen (x is the same as y), return y
        if x is y:
            return y
        parent = y.parent
        x.parent = parent
        y.parent = x
        if y.left:
            y.left.parent = y
        if parent is None:
            self._root = x
        else:
            if parent.left == y:
                parent.left = x
            else:
                parent.right = x
        return x

    def _search(
        self, node: Optional[_RBNode[ComparableT]], key: ComparableT
    ) -> Optional[_RBNode[ComparableT]]:
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search(node.left, key)
        return self._search(node.right, key)

    def _inorder(self, node: Optional[_RBNode[ComparableT]]) -> Iterator[ComparableT]:
        if node is not None:
            yield from self._inorder(node.left)
            yield node.key
            yield from self._inorder(node.right)

    def _preorder(self, node: Optional[_RBNode[ComparableT]]) -> Iterator[ComparableT]:
        if node is not None:
            yield node.key
            yield from self._preorder(node.left)
            yield from self._preorder(node.right)

    def _postorder(self, node: Optional[_RBNode[ComparableT]]) -> Iterator[ComparableT]:
        if node is not None:
            yield from self._postorder(node.left)
            yield from self._postorder(node.right)
            yield node.key

    def _find_min(self, node: _RBNode[ComparableT]) -> _RBNode[ComparableT]:
        while node.left is not None:
            node = node.left
        return node

    def _find_max(self, node: _RBNode[ComparableT]) -> _RBNode[ComparableT]:
        while node.right is not None:
            node = node.right
        return node

    def _height(self, node: Optional[_RBNode[ComparableT]]) -> int:
        if node is None:
            return 0
        return 1 + max(self._height(node.left), self._height(node.right))

    # ------------------------------------------------------------------

    def __len__(self) -> int:  # pragma: no cover
        return sum(1 for _ in self.inorder())

    def __repr__(self) -> str:  # pragma: no cover
        return f"RedBlackTree(size={len(self)})"
