"""N-Queens problem solver using backtracking.

The goal is to place N queens on an N×N chessboard such that no two queens
attack each other (no shared row, column or diagonal).

This module provides the `NQueensSolver` class with a `solve(n)` method that
returns all valid solutions, each represented as a list of column indices for
rows 0..n-1.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import List


@dataclass(slots=True, init=False)
class NQueensSolver:
    """Backtracking solver for the classic *N-Queens* puzzle."""

    _solutions: List[List[int]] = field(default_factory=list, init=False, repr=False)

    def solve(self, n: int) -> List[List[int]]:
        """Return a list of all solutions for an *n*×*n* board."""
        if n <= 0:
            raise ValueError("n must be positive")
        if n > 20:  # Prevent excessive computation
            raise ValueError("Board size too large")
        self._solutions = []
        cols = set()
        diag1 = set()  # r - c
        diag2 = set()  # r + c
        # current partial solution, index = row, value = col
        current: List[int] = []

        def place(row: int) -> None:
            if row == n:
                self._solutions.append(current.copy())
                return
            for col in range(n):
                if col in cols or (row - col) in diag1 or (row + col) in diag2:
                    continue
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)
                current.append(col)
                place(row + 1)
                current.pop()
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)

        place(0)
        return self._solutions.copy()

    # Convenience helpers -------------------------------------------------

    def count_solutions(self, n: int) -> int:  # pragma: no cover
        """Return the number of valid configurations for board size *n*."""
        return len(self.solve(n))

    def __repr__(self) -> str:  # pragma: no cover
        return f"{self.__class__.__name__}()"
