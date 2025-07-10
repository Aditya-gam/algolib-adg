"""Trie (prefix tree) implementation for efficient string storage & lookup."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List


@dataclass(slots=True)
class _TrieNode:
    children: Dict[str, "_TrieNode"] = field(default_factory=dict)
    is_end_of_word: bool = False


@dataclass(slots=True)
class Trie:
    """Trie with insert, search and prefix checking operations."""

    _root: _TrieNode = field(default_factory=_TrieNode, repr=False)

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def insert(self, word: str) -> None:
        """Insert *word* into the trie."""
        node = self._root
        for ch in word:
            node = node.children.setdefault(ch, _TrieNode())
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        """Return True if *word* exists in the trie."""
        node = self._traverse(word)
        return node.is_end_of_word if node else False

    def starts_with(self, prefix: str) -> bool:
        """Return True if any word in the trie starts with *prefix*."""
        return self._traverse(prefix) is not None

    def words_with_prefix(self, prefix: str) -> List[str]:  # pragma: no cover
        """Return all words beginning with *prefix* (for debugging)."""
        node = self._traverse(prefix)
        results: List[str] = []
        if node:
            self._collect(node, prefix, results)
        return results

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    def _traverse(self, s: str) -> _TrieNode | None:
        node = self._root
        for ch in s:
            if ch not in node.children:
                return None
            node = node.children[ch]
        return node

    def _collect(self, node: _TrieNode, prefix: str, output: List[str]) -> None:
        if node.is_end_of_word:
            output.append(prefix)
        for ch, child in node.children.items():
            self._collect(child, prefix + ch, output)

    def __contains__(self, word: object) -> bool:  # pragma: no cover
        if not isinstance(word, str):
            return False
        return self.search(word)

    def __repr__(self) -> str:  # pragma: no cover
        return f"Trie(size={len(self._root.children)})"
