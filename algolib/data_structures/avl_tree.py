"""AVL Tree (self-balancing BST) implementation."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Generic, Iterator, Optional

from algolib._typing import ComparableT

from ._rotation_mixin import RotationMixin


@dataclass(slots=True)
class _AVLNode(Generic[ComparableT]):
    key: ComparableT
    height: int = 1
    left: Optional["_AVLNode[ComparableT]"] = field(default=None, repr=False)
    right: Optional["_AVLNode[ComparableT]"] = field(default=None, repr=False)


class AVLTree(Generic[ComparableT], RotationMixin[_AVLNode[ComparableT]]):
    """Self-balancing AVL Tree supporting insertion & search."""

    _root: Optional[_AVLNode[ComparableT]]

    def __init__(self) -> None:
        self._root = None

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def insert(self, key: ComparableT) -> None:
        self._root = self._insert(self._root, key)

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
        if not self.contains(key):
            return False
        self._root = self._delete(self._root, key)
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

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    def _insert(
        self, node: Optional[_AVLNode[ComparableT]], key: ComparableT
    ) -> _AVLNode[ComparableT]:
        if node is None:
            return _AVLNode(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        else:
            return node  # duplicates ignored

        node.height = 1 + max(self._height(node.left), self._height(node.right))
        balance = self._balance_factor(node)

        # Left heavy
        if balance > 1:
            if node.left and key < node.left.key:  # Left ‑ Left
                return self._rotate_right(node)
            else:  # Left ‑ Right
                if node.left:
                    node.left = self._rotate_left(node.left)
                return self._rotate_right(node)
        # Right heavy
        if balance < -1:
            if node.right and key > node.right.key:  # Right ‑ Right
                return self._rotate_left(node)
            else:  # Right ‑ Left
                if node.right:
                    node.right = self._rotate_right(node.right)
                return self._rotate_left(node)
        return node

    def _height(self, node: Optional[_AVLNode[ComparableT]]) -> int:
        return node.height if node else 0

    def _balance_factor(self, node: Optional[_AVLNode[ComparableT]]) -> int:
        if node is None:
            return 0
        return self._height(node.left) - self._height(node.right)

    def _search(
        self, node: Optional[_AVLNode[ComparableT]], key: ComparableT
    ) -> Optional[_AVLNode[ComparableT]]:
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search(node.left, key)
        return self._search(node.right, key)

    def _inorder(self, node: Optional[_AVLNode[ComparableT]]) -> Iterator[ComparableT]:
        if node is not None:
            yield from self._inorder(node.left)
            yield node.key
            yield from self._inorder(node.right)

    def _preorder(self, node: Optional[_AVLNode[ComparableT]]) -> Iterator[ComparableT]:
        if node is not None:
            yield node.key
            yield from self._preorder(node.left)
            yield from self._preorder(node.right)

    def _postorder(self, node: Optional[_AVLNode[ComparableT]]) -> Iterator[ComparableT]:
        if node is not None:
            yield from self._postorder(node.left)
            yield from self._postorder(node.right)
            yield node.key

    def _delete(
        self, node: Optional[_AVLNode[ComparableT]], key: ComparableT
    ) -> Optional[_AVLNode[ComparableT]]:
        if node is None:
            return None

        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            # Node to be deleted found
            node = self._remove_node(node)

        if node is None:
            return None

        return self._rebalance_after_deletion(node)

    def _remove_node(self, node: _AVLNode[ComparableT]) -> Optional[_AVLNode[ComparableT]]:
        """Remove a node and return the replacement node."""
        if node.left is None:
            return node.right
        elif node.right is None:
            return node.left
        else:
            # Node has two children
            successor = self._find_min(node.right)
            node.key = successor.key
            node.right = self._delete(node.right, successor.key)
            return node

    def _rebalance_after_deletion(self, node: _AVLNode[ComparableT]) -> _AVLNode[ComparableT]:
        """Rebalance the tree after deletion."""
        # Update height and balance
        node.height = 1 + max(self._height(node.left), self._height(node.right))
        balance = self._balance_factor(node)

        # Left heavy
        if balance > 1:
            return self._handle_left_heavy_deletion(node)
        # Right heavy
        if balance < -1:
            return self._handle_right_heavy_deletion(node)
        return node

    def _handle_left_heavy_deletion(self, node: _AVLNode[ComparableT]) -> _AVLNode[ComparableT]:
        """Handle left-heavy case after deletion."""
        if self._balance_factor(node.left) >= 0:  # Left-Left
            return self._rotate_right(node)
        else:  # Left-Right
            if node.left:
                node.left = self._rotate_left(node.left)
            return self._rotate_right(node)

    def _handle_right_heavy_deletion(self, node: _AVLNode[ComparableT]) -> _AVLNode[ComparableT]:
        """Handle right-heavy case after deletion."""
        if self._balance_factor(node.right) <= 0:  # Right-Right
            return self._rotate_left(node)
        else:  # Right-Left
            if node.right:
                node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

    def _find_min(self, node: _AVLNode[ComparableT]) -> _AVLNode[ComparableT]:
        while node.left is not None:
            node = node.left
        return node

    def _find_max(self, node: _AVLNode[ComparableT]) -> _AVLNode[ComparableT]:
        while node.right is not None:
            node = node.right
        return node

    # Update rotations to also refresh heights --------------------------------

    def _rotate_left(self, z: _AVLNode[ComparableT]) -> _AVLNode[ComparableT]:
        y = super()._rotate_left(z)
        z.height = 1 + max(self._height(z.left), self._height(z.right))
        y.height = 1 + max(self._height(y.left), self._height(y.right))
        return y

    def _rotate_right(self, y: _AVLNode[ComparableT]) -> _AVLNode[ComparableT]:
        x = super()._rotate_right(y)
        y.height = 1 + max(self._height(y.left), self._height(y.right))
        x.height = 1 + max(self._height(x.left), self._height(x.right))
        return x

    # ------------------------------------------------------------------

    def __len__(self) -> int:  # pragma: no cover simplistic
        return sum(1 for _ in self.inorder())

    def __contains__(self, item: object) -> bool:  # pragma: no cover
        if not isinstance(item, (int, str, float)):  # A bit of a hack for ComparableT
            return False
        return self.contains(item)  # type: ignore[arg-type]

    def __repr__(self) -> str:  # pragma: no cover
        return f"AVLTree(size={len(self)})"
