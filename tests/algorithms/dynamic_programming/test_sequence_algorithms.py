"""Unit tests for sequence algorithms (LCS and LIS)."""

from typing import List

import pytest

from algolib.algorithms.dynamic_programming import LCS, LIS


class TestLCS:
    """Test cases for Longest Common Subsequence (LCS) algorithm."""

    @pytest.fixture
    def lcs_solver(self) -> LCS:
        """Provide LCS solver instance."""
        return LCS()

    def test_basic_cases(self, lcs_solver: LCS) -> None:
        """Test basic LCS cases."""
        assert lcs_solver.compute("ABC", "AC") == 2
        assert lcs_solver.sequence("ABC", "AC") == "AC"

        assert lcs_solver.compute("AGGTAB", "GXTXAYB") == 4
        assert lcs_solver.sequence("AGGTAB", "GXTXAYB") in {"GTAB"}  # any valid LCS

    def test_empty_strings(self, lcs_solver: LCS) -> None:
        """Test LCS with empty strings."""
        assert lcs_solver.compute("", "") == 0
        assert lcs_solver.sequence("", "") == ""
        assert lcs_solver.compute("ABCDE", "") == 0
        assert lcs_solver.compute("", "ABCDE") == 0

    def test_single_characters(self, lcs_solver: LCS) -> None:
        """Test LCS with single characters."""
        assert lcs_solver.compute("A", "A") == 1
        assert lcs_solver.sequence("A", "A") == "A"
        assert lcs_solver.compute("A", "B") == 0
        assert lcs_solver.sequence("A", "B") == ""

    def test_identical_strings(self, lcs_solver: LCS) -> None:
        """Test LCS with identical strings."""
        s = "ABCDEFGH"
        assert lcs_solver.compute(s, s) == len(s)
        assert lcs_solver.sequence(s, s) == s

    def test_no_common_subsequence(self, lcs_solver: LCS) -> None:
        """Test LCS with no common subsequence."""
        assert lcs_solver.compute("ABC", "XYZ") == 0
        assert lcs_solver.sequence("ABC", "XYZ") == ""

    def test_multiple_lcs_possibilities(self, lcs_solver: LCS) -> None:
        """Test LCS with multiple possible solutions."""
        lcs_solver.compute("ABC", "ACB")  # Build the table first
        result = lcs_solver.sequence("ABC", "ACB")
        assert len(result) == 2
        assert result in ["AC", "BC", "AB"]

    def test_unicode_strings(self, lcs_solver: LCS) -> None:
        """Test LCS with unicode strings."""
        s1 = "αβγδε"
        s2 = "αδεζη"
        assert lcs_solver.compute(s1, s2) == 3
        result = lcs_solver.sequence(s1, s2)
        assert len(result) == 3
        assert all(c in s1 and c in s2 for c in result)

    def test_large_strings(self, lcs_solver: LCS) -> None:
        """Test LCS with larger strings."""
        s1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        s2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        assert lcs_solver.compute(s1, s2) == 26
        assert lcs_solver.sequence(s1, s2) == s1

    def test_repeated_characters(self, lcs_solver: LCS) -> None:
        """Test LCS with repeated characters."""
        s1 = "AABBCC"
        s2 = "ABCABC"
        assert lcs_solver.compute(s1, s2) == 4  # "ABCC" or similar
        result = lcs_solver.sequence(s1, s2)
        assert len(result) == 4

    def test_mixed_case_strings(self, lcs_solver: LCS) -> None:
        """Test LCS with mixed case strings."""
        s1 = "HelloWorld"
        s2 = "HELLOWORLD"
        assert lcs_solver.compute(s1, s2) == 2  # "HW" or similar
        result = lcs_solver.sequence(s1, s2)
        assert len(result) == 2


class TestLIS:
    """Test cases for Longest Increasing Subsequence (LIS) algorithm."""

    @pytest.fixture
    def lis_solver(self) -> LIS[int]:
        """Provide LIS solver instance."""
        return LIS[int]()

    def test_standard_example(self, lis_solver: LIS[int]) -> None:
        """Test standard LIS example."""
        seq = [10, 9, 2, 5, 3, 7, 101, 18]
        assert lis_solver.length(seq) == 4  # [2, 3, 7, 101]

    def test_already_sorted(self, lis_solver: LIS[int]) -> None:
        """Test LIS with already sorted sequence."""
        seq = [1, 2, 3, 4, 5]
        assert lis_solver.length(seq) == 5

    def test_reverse_sorted(self, lis_solver: LIS[int]) -> None:
        """Test LIS with reverse sorted sequence."""
        seq = [5, 4, 3, 2, 1]
        assert lis_solver.length(seq) == 1

    def test_with_duplicates(self, lis_solver: LIS[int]) -> None:
        """Test LIS with duplicate elements."""
        seq = [2, 2, 2, 2]
        assert lis_solver.length(seq) == 1

    def test_empty_sequence(self, lis_solver: LIS[int]) -> None:
        """Test LIS with empty sequence."""
        seq: List[int] = []
        assert lis_solver.length(seq) == 0

    def test_single_element(self, lis_solver: LIS[int]) -> None:
        """Test LIS with single element."""
        seq = [42]
        assert lis_solver.length(seq) == 1

    def test_negative_numbers(self, lis_solver: LIS[int]) -> None:
        """Test LIS with negative numbers."""
        seq = [-5, -3, -1, -2, -4]
        assert lis_solver.length(seq) == 3  # [-5, -3, -1]

    def test_mixed_positive_negative(self, lis_solver: LIS[int]) -> None:
        """Test LIS with mixed positive and negative numbers."""
        seq = [-3, 1, -2, 2, -1, 3]
        assert lis_solver.length(seq) == 4  # [-3, 1, 2, 3]

    def test_all_same_elements(self, lis_solver: LIS[int]) -> None:
        """Test LIS with all same elements."""
        seq = [5, 5, 5, 5, 5]
        assert lis_solver.length(seq) == 1

    def test_large_sequence(self, lis_solver: LIS[int]) -> None:
        """Test LIS with larger sequence."""
        seq = [10, 22, 9, 33, 21, 50, 41, 60, 80]
        assert lis_solver.length(seq) == 6  # [10, 22, 33, 50, 60, 80]

    def test_float_sequence(self) -> None:
        """Test LIS with float sequence."""
        lis_solver = LIS[float]()
        seq = [1.1, 2.2, 1.5, 3.3, 2.8, 4.4]
        assert lis_solver.length(seq) == 4  # [1.1, 2.2, 3.3, 4.4]

    def test_string_sequence(self) -> None:
        """Test LIS with string sequence."""
        lis_solver = LIS[str]()
        seq = ["apple", "banana", "cherry", "date", "elderberry"]
        assert lis_solver.length(seq) == 5

    def test_complex_sequence(self, lis_solver: LIS[int]) -> None:
        """Test LIS with complex sequence."""
        seq = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6]
        result = lis_solver.length(seq)
        assert result >= 6  # Should find a reasonable LIS

    def test_sequence_with_zeros(self, lis_solver: LIS[int]) -> None:
        """Test LIS with sequence containing zeros."""
        seq = [0, 1, 0, 2, 0, 3]
        assert lis_solver.length(seq) == 4  # [0, 1, 2, 3]

    def test_sequence_with_large_numbers(self, lis_solver: LIS[int]) -> None:
        """Test LIS with large numbers."""
        seq = [1000000, 999999, 1000001, 999998, 1000002]
        assert lis_solver.length(seq) == 3  # [999999, 1000001, 1000002]

    def test_sequence_with_repeated_patterns(self, lis_solver: LIS[int]) -> None:
        """Test LIS with repeated patterns."""
        seq = [1, 2, 3, 1, 2, 3, 1, 2, 3]
        assert lis_solver.length(seq) == 3  # [1, 2, 3]

    def test_sequence_with_alternating_pattern(self, lis_solver: LIS[int]) -> None:
        """Test LIS with alternating pattern."""
        seq = [1, 3, 2, 4, 3, 5, 4, 6]
        assert lis_solver.length(seq) == 5  # [1, 3, 4, 5, 6] or similar

    def test_sequence_with_multiple_peaks(self, lis_solver: LIS[int]) -> None:
        """Test LIS with sequence having multiple peaks."""
        seq = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7]
        assert lis_solver.length(seq) == 6  # [1, 3, 4, 5, 6, 7] or similar
