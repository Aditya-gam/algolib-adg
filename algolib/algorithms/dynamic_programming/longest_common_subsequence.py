"""Longest Common Subsequence (LCS) dynamic-programming algorithm implementation.

This module defines the `LCS` class that computes the length (and option-ally the actual
subsequence) shared by two input strings.

Time complexity: O(n × m) where n = len(str1) and m = len(str2).
Space complexity: O(n × m) for full DP table.

The implementation hides the DP table to preserve encapsulation and keeps
all logic inside a single responsibility class, in line with SOLID
principles.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import List


@dataclass(slots=True, init=False)
class LCS:
    """Compute the *Longest Common Subsequence* between two strings.

    Example
    -------
    >>> lcs = LCS()
    >>> lcs.compute("AGGTAB", "GXTXAYB")
    4
    >>> lcs.sequence("AGGTAB", "GXTXAYB")
    'GTAB'
    """

    _table: List[List[int]] = field(default_factory=list, init=False, repr=False)
    _last_a: str = field(default="", init=False, repr=False)
    _last_b: str = field(default="", init=False, repr=False)

    def _build_table(self, a: str, b: str) -> None:
        """Populate the internal DP table for inputs *a* and *b*."""
        n, m = len(a), len(b)
        # (n+1) x (m+1) zero-initialised matrix
        self._table = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if a[i - 1] == b[j - 1]:
                    self._table[i][j] = self._table[i - 1][j - 1] + 1
                else:
                    self._table[i][j] = max(self._table[i - 1][j], self._table[i][j - 1])

        self._last_a = a
        self._last_b = b

    # Public API -----------------------------------------------------------------

    def compute(self, a: str, b: str) -> int:
        """Return length of the longest common subsequence between *a* and *b*."""
        self._build_table(a, b)
        return self._table[len(a)][len(b)]

    def sequence(self, a: str, b: str) -> str:
        """Reconstruct one *actual* longest common subsequence after `compute`."""
        if (
            not self._table
            or self._last_a != a
            or self._last_b != b
            or len(self._table) != len(a) + 1
            or len(self._table[0]) != len(b) + 1
        ):
            # Build table if not already built or if inputs changed
            self._build_table(a, b)

        i, j = len(a), len(b)
        lcs_chars: List[str] = []
        while i > 0 and j > 0:
            if a[i - 1] == b[j - 1]:
                lcs_chars.append(a[i - 1])
                i -= 1
                j -= 1
            elif self._table[i - 1][j] >= self._table[i][j - 1]:
                i -= 1
            else:
                j -= 1

        return "".join(reversed(lcs_chars))
