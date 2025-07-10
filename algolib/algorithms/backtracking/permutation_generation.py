"""Permutation Generation algorithm using backtracking and swapping.

This module defines the `PermutationFinder` class that generates all
permutations of a given list of elements. It encapsulates the backtracking
logic to respect SRP and can be reused across the codebase.

Time Complexity: O(n × n!), where n is the number of elements.
Space Complexity: O(n) for recursion depth (excluding output storage).
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Generic, List, Sequence, TypeVar, Union, cast

T = TypeVar("T")

HashableType = Union[str, int, float, bool, tuple[Any, ...], None]


def _make_hashable(x: Any) -> HashableType:
    """Convert a value to a hashable type for deduplication."""
    if isinstance(x, list):
        return tuple(_make_hashable(i) for i in x)
    if isinstance(x, dict):
        return tuple(sorted((k, _make_hashable(v)) for k, v in x.items()))
    if isinstance(x, set):
        return tuple(sorted(_make_hashable(i) for i in x))
    return cast(HashableType, x)


@dataclass(slots=True, init=False)
class PermutationFinder(Generic[T]):
    """Generate all permutations of a sequence via recursive backtracking.

    Example
    -------
    >>> pf = PermutationFinder[int]()
    >>> pf.permute([1, 2, 3])
    [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 2, 1], [3, 1, 2]]
    """

    _result: List[List[T]] = field(default_factory=list, init=False, repr=False)

    def permute(self, nums: Sequence[T]) -> List[List[T]]:
        """Return all unique permutations of *nums* as a list of lists."""
        self._result = []
        nums_list: List[T] = list(nums)
        self._backtrack(nums_list, 0)
        # Remove duplicates while preserving order

        seen = set()
        unique_result = []
        for perm in self._result:
            perm_tuple = tuple(_make_hashable(i) for i in perm)
            if perm_tuple not in seen:
                seen.add(perm_tuple)
                unique_result.append(perm)
        return unique_result

    # ---------------------------------------------------------------------
    # Internal helpers
    # ---------------------------------------------------------------------

    def _backtrack(self, arr: List[T], index: int) -> None:
        if index == len(arr):
            # Append a copy of the current arrangement
            self._result.append(arr.copy())
            return
        for i in range(index, len(arr)):
            arr[index], arr[i] = arr[i], arr[index]  # swap
            self._backtrack(arr, index + 1)
            arr[index], arr[i] = arr[i], arr[index]  # backtrack swap

    # Convenience alias -----------------------------------------------------

    def generate(self, nums: Sequence[T]) -> List[List[T]]:  # pragma: no cover
        """Alias to `permute` for semantic symmetry with `SubsetGeneration`."""
        return self.permute(nums)

    def __repr__(self) -> str:  # pragma: no cover
        return f"{self.__class__.__name__}()"
