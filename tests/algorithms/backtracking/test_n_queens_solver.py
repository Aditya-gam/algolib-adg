"""Unit tests for N-Queens solver."""

from typing import List

import pytest

from algolib.algorithms.backtracking import NQueensSolver


class TestNQueensSolver:
    """Test cases for N-Queens solver."""

    def test_solve_4_queens(self, n_queens_solver: NQueensSolver) -> None:
        """Test solving 4-queens problem."""
        solutions = n_queens_solver.solve(4)
        assert len(solutions) == 2
        for solution in solutions:
            assert self._is_valid_solution(solution, 4)

    def test_solve_8_queens(self, n_queens_solver: NQueensSolver) -> None:
        """Test solving 8-queens problem."""
        solutions = n_queens_solver.solve(8)
        assert len(solutions) == 92
        for solution in solutions:
            assert self._is_valid_solution(solution, 8)

    def test_solve_1_queen(self, n_queens_solver: NQueensSolver) -> None:
        """Test solving 1-queen problem."""
        solutions = n_queens_solver.solve(1)
        assert len(solutions) == 1
        assert solutions[0] == [0]
        assert self._is_valid_solution(solutions[0], 1)

    def test_solve_2_queens(self, n_queens_solver: NQueensSolver) -> None:
        """Test solving 2-queens problem (no solution)."""
        solutions = n_queens_solver.solve(2)
        assert len(solutions) == 0

    def test_solve_3_queens(self, n_queens_solver: NQueensSolver) -> None:
        """Test solving 3-queens problem (no solution)."""
        solutions = n_queens_solver.solve(3)
        assert len(solutions) == 0

    def test_solve_5_queens(self, n_queens_solver: NQueensSolver) -> None:
        """Test solving 5-queens problem."""
        solutions = n_queens_solver.solve(5)
        assert len(solutions) == 10
        for solution in solutions:
            assert self._is_valid_solution(solution, 5)

    def test_solve_6_queens(self, n_queens_solver: NQueensSolver) -> None:
        """Test solving 6-queens problem."""
        solutions = n_queens_solver.solve(6)
        assert len(solutions) == 4
        for solution in solutions:
            assert self._is_valid_solution(solution, 6)

    def test_solve_7_queens(self, n_queens_solver: NQueensSolver) -> None:
        """Test solving 7-queens problem."""
        solutions = n_queens_solver.solve(7)
        assert len(solutions) == 40
        for solution in solutions:
            assert self._is_valid_solution(solution, 7)

    def test_solve_9_queens(self, n_queens_solver: NQueensSolver) -> None:
        """Test solving 9-queens problem."""
        solutions = n_queens_solver.solve(9)
        assert len(solutions) == 352
        for solution in solutions:
            assert self._is_valid_solution(solution, 9)

    def test_solve_10_queens(self, n_queens_solver: NQueensSolver) -> None:
        """Test solving 10-queens problem."""
        solutions = n_queens_solver.solve(10)
        assert len(solutions) == 724
        for solution in solutions:
            assert self._is_valid_solution(solution, 10)

    def test_invalid_board_size_zero(self, n_queens_solver: NQueensSolver) -> None:
        """Test that zero board size raises ValueError."""
        with pytest.raises(ValueError, match="n must be positive"):
            n_queens_solver.solve(0)

    def test_invalid_board_size_negative(self, n_queens_solver: NQueensSolver) -> None:
        """Test that negative board size raises ValueError."""
        with pytest.raises(ValueError, match="n must be positive"):
            n_queens_solver.solve(-1)

    def test_invalid_board_size_large(self, n_queens_solver: NQueensSolver) -> None:
        """Test that very large board size raises ValueError."""
        with pytest.raises(ValueError, match="Board size too large"):
            n_queens_solver.solve(100)

    def test_solution_uniqueness(self, n_queens_solver: NQueensSolver) -> None:
        """Test that all solutions are unique."""
        solutions = n_queens_solver.solve(8)
        unique_solutions = set(tuple(solution) for solution in solutions)
        assert len(unique_solutions) == len(solutions)

    def test_solution_format(self, n_queens_solver: NQueensSolver) -> None:
        """Test that solutions have correct format."""
        solutions = n_queens_solver.solve(4)
        for solution in solutions:
            assert isinstance(solution, list)
            assert len(solution) == 4
            assert all(isinstance(pos, int) for pos in solution)
            assert all(0 <= pos < 4 for pos in solution)

    def test_multiple_calls_same_instance(self, n_queens_solver: NQueensSolver) -> None:
        """Test that multiple calls work correctly on the same instance."""
        solutions1 = n_queens_solver.solve(4)
        solutions2 = n_queens_solver.solve(4)
        assert solutions1 == solutions2

    def test_solution_queens_not_in_same_row(self, n_queens_solver: NQueensSolver) -> None:
        """Test that no two queens are in the same row."""
        solutions = n_queens_solver.solve(8)
        for solution in solutions:
            assert len(set(solution)) == 8  # All positions are unique

    def test_solution_queens_not_in_same_diagonal(self, n_queens_solver: NQueensSolver) -> None:
        """Test that no two queens are in the same diagonal."""
        solutions = n_queens_solver.solve(8)
        for solution in solutions:
            # Check main diagonal
            for i in range(len(solution)):
                for j in range(i + 1, len(solution)):
                    # Queens at (i, solution[i]) and (j, solution[j])
                    # Check if they're on the same diagonal
                    row_diff = j - i
                    col_diff = solution[j] - solution[i]
                    assert abs(row_diff) != abs(col_diff)

    def test_performance_small_board(self, n_queens_solver: NQueensSolver) -> None:
        """Test performance for small board."""
        import time

        start_time = time.time()
        solutions = n_queens_solver.solve(8)
        end_time = time.time()
        assert end_time - start_time < 1.0  # Should complete within 1 second
        assert len(solutions) == 92

    def test_performance_medium_board(self, n_queens_solver: NQueensSolver) -> None:
        """Test performance for medium board."""
        import time

        start_time = time.time()
        solutions = n_queens_solver.solve(10)
        end_time = time.time()
        assert end_time - start_time < 5.0  # Should complete within 5 seconds
        assert len(solutions) == 724

    def test_edge_case_single_queen_position(self, n_queens_solver: NQueensSolver) -> None:
        """Test edge case with single queen position."""
        solutions = n_queens_solver.solve(1)
        assert solutions == [[0]]

    def test_edge_case_no_solution(self, n_queens_solver: NQueensSolver) -> None:
        """Test edge case with no solution."""
        solutions = n_queens_solver.solve(2)
        assert solutions == []

    def test_solution_queens_not_in_same_column(self, n_queens_solver: NQueensSolver) -> None:
        """Test that no two queens are in the same column (implicitly tested by row check)."""
        solutions = n_queens_solver.solve(8)
        for solution in solutions:
            # Since each queen is in a different row, and positions are unique,
            # no two queens can be in the same column
            assert len(set(solution)) == 8

    def _is_valid_solution(self, solution: List[int], board_size: int) -> bool:
        """Check if a solution is valid for the N-queens problem."""
        if len(solution) != board_size:
            return False

        # Check that all positions are within bounds
        if not all(0 <= pos < board_size for pos in solution):
            return False

        # Check that no two queens are in the same row (implicitly satisfied by solution format)
        if len(set(solution)) != board_size:
            return False

        # Check that no two queens are in the same diagonal
        for i in range(len(solution)):
            for j in range(i + 1, len(solution)):
                row_diff = j - i
                col_diff = solution[j] - solution[i]
                if abs(row_diff) == abs(col_diff):
                    return False

        return True
