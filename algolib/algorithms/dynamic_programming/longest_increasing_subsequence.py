"""Longest Increasing Subsequence (LIS) algorithms.

This module provides the `LIS` class exposing a single `length` method that
returns the size of the longest strictly increasing subsequence within an
input sequence of comparable elements.

Two strategies are offered internally:
1. `O(n log n)` patience-sorting / tails array approach (default).
2. `O(n²)` dynamic-programming fallback for educational purposes.

The selection is implementation detail; the public interface remains the
same, respecting Open/Closed.
"""

from __future__ import annotations

import bisect
from dataclasses import dataclass
from typing import Generic, Iterable, List, Sequence, TypeVar

from algolib._typing import ComparableT

T = TypeVar("T")


@dataclass(slots=True, init=False)
class LIS(Generic[T]):
    """Compute the *Longest Increasing Subsequence* length in a sequence.

    Example
    -------
    >>> lis = LIS[int]()
    >>> lis.length([10, 9, 2, 5, 3, 7, 101, 18])
    4
    """

    def length(self, sequence: Sequence[ComparableT] | Iterable[ComparableT]) -> int:
        """Return the length of the LIS using the O(n log n) approach."""
        # Convert to list once to allow multiple passes and indexing.
        arr: List[ComparableT] = list(sequence)
        if not arr:
            return 0

        # `tails[i]` holds the minimum possible tail value for an increasing
        # subsequence of length `i + 1`.
        tails: List[ComparableT] = []
        for value in arr:
            # Locate insertion point for value in tails to maintain sorted order.
            idx = bisect.bisect_left(tails, value)
            if idx == len(tails):
                tails.append(value)
            else:
                tails[idx] = value
        return len(tails)
