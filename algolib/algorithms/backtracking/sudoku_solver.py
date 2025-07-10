"""Sudoku solver using backtracking.

The solver works on a standard 9×9 Sudoku puzzle, represented as a list of
lists (rows) of integers where 0 denotes an empty cell.

It exposes a single public method `solve(board)` which returns the solved board
or None if no solution exists.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Tuple

Board = List[List[int]]


@dataclass(slots=True)
class SudokuSolver:
    """Backtracking Sudoku solver (single responsibility)."""

    _SIZE: int = 9
    _SUBGRID: int = 3

    # Public API -----------------------------------------------------------

    def solve(self, board: Board) -> Board | None:
        """Solve Sudoku puzzle *board*.

        Args:
            board: 9×9 grid with 0 representing empty cells.

        Returns
        -------
            Solved board if a solution exists, None otherwise.
        """
        if not self._is_valid_board(board):
            raise ValueError("Invalid board shape; expected 9x9 grid")

        # Check if the board is already invalid (has duplicates)
        if not self._is_valid_partial_board(board):
            return None

        # Create a copy to avoid mutating the original
        board_copy = [row[:] for row in board]

        if self._solve_recursive(board_copy):
            return board_copy
        return None

    # ---------------------------------------------------------------------
    # Internal helpers
    # ---------------------------------------------------------------------

    def _solve_recursive(self, board: Board) -> bool:
        """Recursive helper to solve the Sudoku board."""
        empty = self._find_empty(board)
        if empty is None:
            return True  # Solved
        row, col = empty
        for num in range(1, 10):
            if self._is_safe(board, row, col, num):
                board[row][col] = num
                if self._solve_recursive(board):
                    return True
                board[row][col] = 0  # backtrack
        return False

    def _is_valid_board(self, board: Board) -> bool:  # pragma: no cover
        if len(board) != self._SIZE or any(len(row) != self._SIZE for row in board):
            return False
        # Check all values are in 0-9
        for row in board:
            for cell in row:
                if not (0 <= cell <= 9):
                    return False
        return True

    def _is_valid_partial_board(self, board: Board) -> bool:
        """Check if a partial board is valid (no duplicates in filled cells)."""
        return (
            self._check_rows_valid(board)
            and self._check_columns_valid(board)
            and self._check_subgrids_valid(board)
        )

    def _check_rows_valid(self, board: Board) -> bool:
        """Check if all rows are valid (no duplicates in filled cells)."""
        for row in board:
            filled = [cell for cell in row if cell != 0]
            if len(filled) != len(set(filled)):
                return False
        return True

    def _check_columns_valid(self, board: Board) -> bool:
        """Check if all columns are valid (no duplicates in filled cells)."""
        for col in range(self._SIZE):
            filled = [board[row][col] for row in range(self._SIZE) if board[row][col] != 0]
            if len(filled) != len(set(filled)):
                return False
        return True

    def _check_subgrids_valid(self, board: Board) -> bool:
        """Check if all 3x3 subgrids are valid (no duplicates in filled cells)."""
        for box_row in range(0, self._SIZE, self._SUBGRID):
            for box_col in range(0, self._SIZE, self._SUBGRID):
                filled = []
                for i in range(self._SUBGRID):
                    for j in range(self._SUBGRID):
                        cell = board[box_row + i][box_col + j]
                        if cell != 0:
                            filled.append(cell)
                if len(filled) != len(set(filled)):
                    return False
        return True

    def _find_empty(self, board: Board) -> Tuple[int, int] | None:
        for r in range(self._SIZE):
            for c in range(self._SIZE):
                if board[r][c] == 0:
                    return r, c
        return None

    def _is_safe(self, board: Board, row: int, col: int, num: int) -> bool:
        # Row & column check
        if any(board[row][c] == num for c in range(self._SIZE)):
            return False
        if any(board[r][col] == num for r in range(self._SIZE)):
            return False
        # Subgrid check
        start_row = (row // self._SUBGRID) * self._SUBGRID
        start_col = (col // self._SUBGRID) * self._SUBGRID
        for r in range(start_row, start_row + self._SUBGRID):
            for c in range(start_col, start_col + self._SUBGRID):
                if board[r][c] == num:
                    return False
        return True

    def __repr__(self) -> str:  # pragma: no cover
        return f"{self.__class__.__name__}()"
