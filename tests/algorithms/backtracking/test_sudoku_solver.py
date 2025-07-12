"""Unit tests for Sudoku solver."""

from typing import List

import pytest

from algolib.algorithms.backtracking import SudokuSolver


class TestSudokuSolver:
    """Test cases for Sudoku solver."""

    def test_solve_valid_board(
        self, sudoku_solver: SudokuSolver, valid_sudoku_board: List[List[int]]
    ) -> None:
        """Test solving a valid Sudoku board."""
        result = sudoku_solver.solve(valid_sudoku_board)
        assert result is not None
        assert self._is_valid_solution(result)

    def test_solve_already_solved_board(
        self, sudoku_solver: SudokuSolver, solved_sudoku_board: List[List[int]]
    ) -> None:
        """Test solving an already solved board."""
        result = sudoku_solver.solve(solved_sudoku_board)
        assert result is not None
        assert result == solved_sudoku_board
        assert self._is_valid_solution(result)

    def test_solve_unsolvable_board(
        self, sudoku_solver: SudokuSolver, unsolvable_sudoku_board: List[List[int]]
    ) -> None:
        """Test solving an unsolvable board."""
        result = sudoku_solver.solve(unsolvable_sudoku_board)
        assert result is None

    def test_solve_empty_board(self, sudoku_solver: SudokuSolver) -> None:
        """Test solving an empty board."""
        empty_board = [[0] * 9 for _ in range(9)]
        result = sudoku_solver.solve(empty_board)
        assert result is not None
        assert self._is_valid_solution(result)

    def test_solve_board_with_one_empty_cell(self, sudoku_solver: SudokuSolver) -> None:
        """Test solving a board with only one empty cell."""
        board = [
            [5, 3, 4, 6, 7, 8, 9, 1, 2],
            [6, 7, 2, 1, 9, 5, 3, 4, 8],
            [1, 9, 8, 3, 4, 2, 5, 6, 7],
            [8, 5, 9, 7, 6, 1, 4, 2, 3],
            [4, 2, 6, 8, 5, 3, 7, 9, 1],
            [7, 1, 3, 9, 2, 4, 8, 5, 6],
            [9, 6, 1, 5, 3, 7, 2, 8, 4],
            [2, 8, 7, 4, 1, 9, 6, 3, 5],
            [3, 4, 5, 2, 8, 6, 1, 7, 0],  # Only one empty cell
        ]
        result = sudoku_solver.solve(board)
        assert result is not None
        assert self._is_valid_solution(result)

    def test_solve_board_with_minimal_clues(self, sudoku_solver: SudokuSolver) -> None:
        """Test solving a board with minimal clues."""
        board = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0],  # Only one clue
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
        result = sudoku_solver.solve(board)
        assert result is not None
        assert self._is_valid_solution(result)

    def test_solve_board_with_duplicate_in_row(self, sudoku_solver: SudokuSolver) -> None:
        """Test solving a board with duplicate numbers in a row."""
        board = [
            [1, 1, 0, 0, 0, 0, 0, 0, 0],  # Invalid: two 1s in first row
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
        result = sudoku_solver.solve(board)
        assert result is None

    def test_solve_board_with_duplicate_in_column(self, sudoku_solver: SudokuSolver) -> None:
        """Test solving a board with duplicate numbers in a column."""
        board = [
            [1, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 0],  # Invalid: two 1s in first column
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
        result = sudoku_solver.solve(board)
        assert result is None

    def test_solve_board_with_duplicate_in_box(self, sudoku_solver: SudokuSolver) -> None:
        """Test solving a board with duplicate numbers in a 3x3 box."""
        board = [
            [1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0, 0],  # Invalid: two 1s in first 3x3 box
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
        result = sudoku_solver.solve(board)
        assert result is None

    def test_solve_invalid_board_shape_raises_error(self, sudoku_solver: SudokuSolver) -> None:
        """Test that invalid board shape raises ValueError."""
        invalid_board = [[1, 2, 3], [4, 5, 6]]  # Not 9x9
        with pytest.raises(ValueError, match="Invalid board shape"):
            sudoku_solver.solve(invalid_board)

    def test_solve_board_with_invalid_values_raises_error(
        self, sudoku_solver: SudokuSolver
    ) -> None:
        """Test that board with invalid values raises ValueError."""
        invalid_board = [
            [10, 0, 0, 0, 0, 0, 0, 0, 0],  # Invalid: 10 is not 0-9
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
        with pytest.raises(ValueError, match="Invalid board shape"):
            sudoku_solver.solve(invalid_board)

    def test_multiple_calls_same_instance(
        self, sudoku_solver: SudokuSolver, valid_sudoku_board: List[List[int]]
    ) -> None:
        """Test that multiple calls work correctly on the same instance."""
        board1 = [row[:] for row in valid_sudoku_board]
        board2 = [row[:] for row in valid_sudoku_board]

        result1 = sudoku_solver.solve(board1)
        result2 = sudoku_solver.solve(board2)

        assert result1 is not None
        assert result2 is not None
        assert self._is_valid_solution(result1)
        assert self._is_valid_solution(result2)

    def test_solve_board_with_all_nines(self, sudoku_solver: SudokuSolver) -> None:
        """Test solving a board with all cells filled with 9s (invalid)."""
        board = [[9] * 9 for _ in range(9)]
        result = sudoku_solver.solve(board)
        assert result is None

    def test_solve_board_with_alternating_pattern(self, sudoku_solver: SudokuSolver) -> None:
        """Test solving a board with an alternating pattern."""
        board = [
            [1, 2, 3, 0, 0, 0, 0, 0, 0],
            [4, 5, 6, 0, 0, 0, 0, 0, 0],
            [7, 8, 9, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 2, 3, 0, 0, 0],
            [0, 0, 0, 4, 5, 6, 0, 0, 0],
            [0, 0, 0, 7, 8, 9, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 2, 3],
            [0, 0, 0, 0, 0, 0, 4, 5, 6],
            [0, 0, 0, 0, 0, 0, 7, 8, 0],
        ]
        result = sudoku_solver.solve(board)
        assert result is not None
        assert self._is_valid_solution(result)

    def test_solve_board_with_single_clue_in_each_box(self, sudoku_solver: SudokuSolver) -> None:
        """Test solving a board with one clue in each 3x3 box."""
        board = [
            [1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 2, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 3, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
        result = sudoku_solver.solve(board)
        assert result is not None
        assert self._is_valid_solution(result)

    def test_solve_board_with_cross_pattern(self, sudoku_solver: SudokuSolver) -> None:
        """Test solving a board with a cross pattern of clues."""
        board = [
            [1, 0, 0, 0, 2, 0, 0, 0, 3],
            [0, 4, 0, 0, 0, 0, 0, 5, 0],
            [0, 0, 6, 0, 0, 0, 7, 0, 0],
            [0, 0, 0, 8, 0, 9, 0, 0, 0],
            [2, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 9, 0, 8, 0, 0, 0],
            [0, 0, 7, 0, 0, 0, 6, 0, 0],
            [0, 5, 0, 0, 0, 0, 0, 4, 0],
            [3, 0, 0, 0, 2, 0, 0, 0, 1],
        ]
        result = sudoku_solver.solve(board)
        assert result is None  # Board is unsolvable

    def test_solve_board_with_diagonal_pattern(self, sudoku_solver: SudokuSolver) -> None:
        """Test solving a board with a diagonal pattern of clues."""
        board = [
            [1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 2, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 3, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 4, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 5, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 6, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 7, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 8, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 9],
        ]
        result = sudoku_solver.solve(board)
        assert result is not None
        assert self._is_valid_solution(result)

    def test_solve_board_with_sparse_clues(self, sudoku_solver: SudokuSolver) -> None:
        """Test solving a board with very sparse clues."""
        board = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0],  # Only one clue in center
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
        result = sudoku_solver.solve(board)
        assert result is not None
        assert self._is_valid_solution(result)

    def test_solve_board_with_almost_complete(self, sudoku_solver: SudokuSolver) -> None:
        """Test solving a board that is almost complete."""
        board = [
            [5, 3, 4, 6, 7, 8, 9, 1, 2],
            [6, 7, 2, 1, 9, 5, 3, 4, 8],
            [1, 9, 8, 3, 4, 2, 5, 6, 7],
            [8, 5, 9, 7, 6, 1, 4, 2, 3],
            [4, 2, 6, 8, 5, 3, 7, 9, 1],
            [7, 1, 3, 9, 2, 4, 8, 5, 6],
            [9, 6, 1, 5, 3, 7, 2, 8, 4],
            [2, 8, 7, 4, 1, 9, 6, 3, 5],
            [3, 4, 5, 2, 8, 6, 1, 7, 0],  # Only one missing
        ]
        result = sudoku_solver.solve(board)
        assert result is not None
        assert self._is_valid_solution(result)
        assert result[8][8] == 9  # Should fill the missing cell

    def test_solve_board_with_multiple_solutions(self, sudoku_solver: SudokuSolver) -> None:
        """Test solving a board that might have multiple solutions."""
        board = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0],  # Only one clue
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
        result = sudoku_solver.solve(board)
        assert result is not None
        assert self._is_valid_solution(result)

    def test_solve_board_with_symmetrical_pattern(self, sudoku_solver: SudokuSolver) -> None:
        """Test solving a board with a symmetrical pattern."""
        board = [
            [1, 0, 0, 0, 0, 0, 0, 0, 1],
            [0, 2, 0, 0, 0, 0, 0, 2, 0],
            [0, 0, 3, 0, 0, 0, 3, 0, 0],
            [0, 0, 0, 4, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 5, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 4, 0, 0, 0],
            [0, 0, 3, 0, 0, 0, 3, 0, 0],
            [0, 2, 0, 0, 0, 0, 0, 2, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 1],
        ]
        result = sudoku_solver.solve(board)
        assert result is None  # Board is unsolvable

    def _is_valid_solution(self, board: List[List[int]]) -> bool:
        """Check if a Sudoku solution is valid."""
        if not self._is_valid_board_shape(board):
            return False

        return (
            self._are_rows_valid(board)
            and self._are_columns_valid(board)
            and self._are_boxes_valid(board)
        )

    def _is_valid_board_shape(self, board: List[List[int]]) -> bool:
        """Check if the board has the correct shape."""
        return len(board) == 9 and all(len(row) == 9 for row in board)

    def _are_rows_valid(self, board: List[List[int]]) -> bool:
        """Check if all rows are valid."""
        for row in board:
            if not self._is_valid_group(row):
                return False
        return True

    def _are_columns_valid(self, board: List[List[int]]) -> bool:
        """Check if all columns are valid."""
        for col in range(9):
            column = [board[row][col] for row in range(9)]
            if not self._is_valid_group(column):
                return False
        return True

    def _are_boxes_valid(self, board: List[List[int]]) -> bool:
        """Check if all 3x3 boxes are valid."""
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                box = []
                for i in range(3):
                    for j in range(3):
                        box.append(board[box_row + i][box_col + j])
                if not self._is_valid_group(box):
                    return False
        return True

    def _is_valid_group(self, group: List[int]) -> bool:
        """Check if a group (row, column, or box) is valid."""
        # Check that all numbers are 1-9
        if not all(1 <= num <= 9 for num in group):
            return False

        # Check that all numbers are unique
        return len(set(group)) == 9
