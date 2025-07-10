"""Rotation mixin providing reusable left/right rotation helpers for BST variants."""

from __future__ import annotations

from typing import Generic, Optional, TypeVar

TNode = TypeVar("TNode")


class RotationMixin(Generic[TNode]):
    """Mixin with `_rotate_left` and `_rotate_right` utilities.

    Assumes the *node* objects have ``left`` and ``right`` attributes referencing
    child nodes (or ``None``) and (optionally) "parent". Subclasses are
    responsible for updating heights/colors as needed after rotation.
    """

    # pylint: disable=attribute-defined-outside-init

    def _rotate_left(self, z: TNode) -> TNode:
        y: Optional[TNode] = z.right  # type: ignore[attr-defined]
        if y is None:
            return z
        z.right = y.left  # type: ignore[attr-defined]
        y.left = z  # type: ignore[attr-defined]
        return y

    def _rotate_right(self, y: TNode) -> TNode:
        x: Optional[TNode] = y.left  # type: ignore[attr-defined]
        if x is None:
            return y
        y.left = x.right  # type: ignore[attr-defined]
        x.right = y  # type: ignore[attr-defined]
        return x
