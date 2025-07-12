"""Unit tests for math algorithms."""

import pytest

from algolib.algorithms.math import Fibonacci


class TestFibonacci:
    """Test cases for Fibonacci algorithm."""

    @pytest.fixture
    def fibonacci_calculator(self) -> Fibonacci:
        """Provide Fibonacci calculator instance."""
        return Fibonacci()

    def test_fibonacci_sequence(self, fibonacci_calculator: Fibonacci) -> None:
        """Test basic Fibonacci sequence."""
        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
        for i, expected_value in enumerate(expected):
            assert fibonacci_calculator.compute(i) == expected_value

    def test_fibonacci_zero(self, fibonacci_calculator: Fibonacci) -> None:
        """Test Fibonacci(0)."""
        assert fibonacci_calculator.compute(0) == 0

    def test_fibonacci_one(self, fibonacci_calculator: Fibonacci) -> None:
        """Test Fibonacci(1)."""
        assert fibonacci_calculator.compute(1) == 1

    def test_fibonacci_two(self, fibonacci_calculator: Fibonacci) -> None:
        """Test Fibonacci(2)."""
        assert fibonacci_calculator.compute(2) == 1

    def test_fibonacci_three(self, fibonacci_calculator: Fibonacci) -> None:
        """Test Fibonacci(3)."""
        assert fibonacci_calculator.compute(3) == 2

    def test_fibonacci_four(self, fibonacci_calculator: Fibonacci) -> None:
        """Test Fibonacci(4)."""
        assert fibonacci_calculator.compute(4) == 3

    def test_fibonacci_five(self, fibonacci_calculator: Fibonacci) -> None:
        """Test Fibonacci(5)."""
        assert fibonacci_calculator.compute(5) == 5

    def test_fibonacci_six(self, fibonacci_calculator: Fibonacci) -> None:
        """Test Fibonacci(6)."""
        assert fibonacci_calculator.compute(6) == 8

    def test_fibonacci_seven(self, fibonacci_calculator: Fibonacci) -> None:
        """Test Fibonacci(7)."""
        assert fibonacci_calculator.compute(7) == 13

    def test_fibonacci_eight(self, fibonacci_calculator: Fibonacci) -> None:
        """Test Fibonacci(8)."""
        assert fibonacci_calculator.compute(8) == 21

    def test_fibonacci_nine(self, fibonacci_calculator: Fibonacci) -> None:
        """Test Fibonacci(9)."""
        assert fibonacci_calculator.compute(9) == 34

    def test_fibonacci_ten(self, fibonacci_calculator: Fibonacci) -> None:
        """Test Fibonacci(10)."""
        assert fibonacci_calculator.compute(10) == 55

    def test_fibonacci_large_number(self, fibonacci_calculator: Fibonacci) -> None:
        """Test Fibonacci with larger number."""
        # Test a larger number to ensure algorithm works
        result = fibonacci_calculator.compute(20)
        assert result == 6765

    def test_fibonacci_negative_raises_error(self, fibonacci_calculator: Fibonacci) -> None:
        """Test that negative input raises error."""
        with pytest.raises(
            ValueError, match="Fibonacci sequence is not defined for negative numbers"
        ):
            fibonacci_calculator.compute(-1)

    def test_fibonacci_negative_five_raises_error(self, fibonacci_calculator: Fibonacci) -> None:
        """Test that negative input raises error."""
        with pytest.raises(
            ValueError, match="Fibonacci sequence is not defined for negative numbers"
        ):
            fibonacci_calculator.compute(-5)

    def test_fibonacci_sequence_method(self, fibonacci_calculator: Fibonacci) -> None:
        """Test generating Fibonacci sequence."""
        sequence = fibonacci_calculator.sequence(10)
        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        assert sequence == expected

    def test_fibonacci_sequence_zero(self, fibonacci_calculator: Fibonacci) -> None:
        """Test generating Fibonacci sequence up to 0."""
        sequence = fibonacci_calculator.sequence(0)
        assert sequence == []

    def test_fibonacci_sequence_one(self, fibonacci_calculator: Fibonacci) -> None:
        """Test generating Fibonacci sequence up to 1."""
        sequence = fibonacci_calculator.sequence(1)
        assert sequence == [0]

    def test_fibonacci_sequence_two(self, fibonacci_calculator: Fibonacci) -> None:
        """Test generating Fibonacci sequence up to 2."""
        sequence = fibonacci_calculator.sequence(2)
        assert sequence == [0, 1]

    def test_fibonacci_sequence_negative_raises_error(
        self, fibonacci_calculator: Fibonacci
    ) -> None:
        """Test that negative input raises error for sequence."""
        with pytest.raises(ValueError, match="Count cannot be negative"):
            fibonacci_calculator.sequence(-1)

    def test_fibonacci_sequence_large_number(self, fibonacci_calculator: Fibonacci) -> None:
        """Test generating Fibonacci sequence for larger number."""
        sequence = fibonacci_calculator.sequence(15)
        assert len(sequence) == 15  # 0 to 14 inclusive
        assert sequence[0] == 0
        assert sequence[1] == 1
        assert sequence[14] == 377

    def test_fibonacci_sequence_property(self, fibonacci_calculator: Fibonacci) -> None:
        """Test that sequence follows Fibonacci property."""
        sequence = fibonacci_calculator.sequence(10)
        for i in range(2, len(sequence)):
            assert sequence[i] == sequence[i - 1] + sequence[i - 2]

    def test_fibonacci_memoization(self, fibonacci_calculator: Fibonacci) -> None:
        """Test that memoization works correctly."""
        # First call should compute
        result1 = fibonacci_calculator.compute(10)
        # Second call should use memoized result
        result2 = fibonacci_calculator.compute(10)
        assert result1 == result2

    def test_fibonacci_multiple_calls(self, fibonacci_calculator: Fibonacci) -> None:
        """Test multiple calls to Fibonacci calculator."""
        results = []
        for i in range(10):
            results.append(fibonacci_calculator.compute(i))

        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        assert results == expected

    def test_fibonacci_sequence_multiple_calls(self, fibonacci_calculator: Fibonacci) -> None:
        """Test multiple calls to sequence method."""
        sequence1 = fibonacci_calculator.sequence(5)
        sequence2 = fibonacci_calculator.sequence(5)
        assert sequence1 == sequence2

    def test_fibonacci_sequence_increasing(self, fibonacci_calculator: Fibonacci) -> None:
        """Test that Fibonacci sequence is non-decreasing."""
        sequence = fibonacci_calculator.sequence(20)
        for i in range(1, len(sequence)):
            assert sequence[i] >= sequence[i - 1]

    def test_fibonacci_sequence_positive_after_zero(self, fibonacci_calculator: Fibonacci) -> None:
        """Test that Fibonacci sequence is positive after index 0."""
        sequence = fibonacci_calculator.sequence(10)
        for i in range(1, len(sequence)):
            assert sequence[i] > 0

    def test_fibonacci_golden_ratio_approximation(self, fibonacci_calculator: Fibonacci) -> None:
        """Test that Fibonacci sequence approximates golden ratio."""
        sequence = fibonacci_calculator.sequence(20)
        golden_ratio = 1.618033988749895

        # Test that ratio of consecutive terms approaches golden ratio
        for i in range(10, len(sequence) - 1):
            ratio = sequence[i + 1] / sequence[i]
            # Allow some tolerance for approximation
            assert ratio == pytest.approx(golden_ratio, abs=0.1)

    def test_fibonacci_overflow_handling(self, fibonacci_calculator: Fibonacci) -> None:
        """Test that large Fibonacci numbers are handled correctly."""
        # Test that we can calculate reasonably large Fibonacci numbers
        # without overflow (assuming Python handles big integers)
        result = fibonacci_calculator.compute(50)
        assert result > 0
        assert isinstance(result, int)

    def test_fibonacci_sequence_length(self, fibonacci_calculator: Fibonacci) -> None:
        """Test that sequence has correct length."""
        for n in range(10):
            sequence = fibonacci_calculator.sequence(n)
            assert len(sequence) == n  # 0 to n-1 inclusive

    def test_fibonacci_sequence_last_element(self, fibonacci_calculator: Fibonacci) -> None:
        """Test that sequence last element matches compute result."""
        for n in range(1, 10):
            sequence = fibonacci_calculator.sequence(n)
            calculated = fibonacci_calculator.compute(n - 1)
            assert sequence[-1] == calculated

    def test_fibonacci_sequence_consistency(self, fibonacci_calculator: Fibonacci) -> None:
        """Test that sequence and compute methods are consistent."""
        for n in range(10):
            sequence = fibonacci_calculator.sequence(n)
            for i in range(n):
                assert sequence[i] == fibonacci_calculator.compute(i)

    def test_fibonacci_performance(self, fibonacci_calculator: Fibonacci) -> None:
        """Test performance of Fibonacci calculation."""
        import time

        start_time = time.time()
        result = fibonacci_calculator.compute(30)
        end_time = time.time()
        assert end_time - start_time < 1.0  # Should complete within 1 second
        assert result > 0

    def test_fibonacci_sequence_performance(self, fibonacci_calculator: Fibonacci) -> None:
        """Test performance of Fibonacci sequence generation."""
        import time

        start_time = time.time()
        sequence = fibonacci_calculator.sequence(30)
        end_time = time.time()
        assert end_time - start_time < 1.0  # Should complete within 1 second
        assert len(sequence) == 30

    # Tests for compute_iterative method
    def test_compute_iterative_basic(self, fibonacci_calculator: Fibonacci) -> None:
        """Test iterative computation of Fibonacci numbers."""
        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
        for i, expected_value in enumerate(expected):
            assert fibonacci_calculator.compute_iterative(i) == expected_value

    def test_compute_iterative_zero(self, fibonacci_calculator: Fibonacci) -> None:
        """Test iterative computation of Fibonacci(0)."""
        assert fibonacci_calculator.compute_iterative(0) == 0

    def test_compute_iterative_one(self, fibonacci_calculator: Fibonacci) -> None:
        """Test iterative computation of Fibonacci(1)."""
        assert fibonacci_calculator.compute_iterative(1) == 1

    def test_compute_iterative_large_number(self, fibonacci_calculator: Fibonacci) -> None:
        """Test iterative computation with large number."""
        result = fibonacci_calculator.compute_iterative(20)
        assert result == 6765

    def test_compute_iterative_negative_raises_error(self, fibonacci_calculator: Fibonacci) -> None:
        """Test that negative input raises error for iterative computation."""
        with pytest.raises(
            ValueError, match="Fibonacci sequence is not defined for negative numbers"
        ):
            fibonacci_calculator.compute_iterative(-1)

    def test_compute_iterative_consistency_with_compute(
        self, fibonacci_calculator: Fibonacci
    ) -> None:
        """Test that iterative and recursive methods produce same results."""
        for i in range(20):
            recursive_result = fibonacci_calculator.compute(i)
            iterative_result = fibonacci_calculator.compute_iterative(i)
            assert recursive_result == iterative_result

    def test_compute_iterative_performance(self, fibonacci_calculator: Fibonacci) -> None:
        """Test performance of iterative computation."""
        import time

        start_time = time.time()
        result = fibonacci_calculator.compute_iterative(50)
        end_time = time.time()
        assert end_time - start_time < 1.0  # Should complete within 1 second
        assert result > 0

    # Tests for is_fibonacci method
    def test_is_fibonacci_true_cases(self, fibonacci_calculator: Fibonacci) -> None:
        """Test is_fibonacci with known Fibonacci numbers."""
        fibonacci_numbers = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
        for num in fibonacci_numbers:
            assert fibonacci_calculator.is_fibonacci(num) is True

    def test_is_fibonacci_false_cases(self, fibonacci_calculator: Fibonacci) -> None:
        """Test is_fibonacci with non-Fibonacci numbers."""
        non_fibonacci_numbers = [4, 6, 7, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20]
        for num in non_fibonacci_numbers:
            assert fibonacci_calculator.is_fibonacci(num) is False

    def test_is_fibonacci_negative(self, fibonacci_calculator: Fibonacci) -> None:
        """Test is_fibonacci with negative numbers."""
        assert fibonacci_calculator.is_fibonacci(-1) is False
        assert fibonacci_calculator.is_fibonacci(-5) is False
        assert fibonacci_calculator.is_fibonacci(-100) is False

    def test_is_fibonacci_large_numbers(self, fibonacci_calculator: Fibonacci) -> None:
        """Test is_fibonacci with larger numbers."""
        # Test some larger Fibonacci numbers
        assert fibonacci_calculator.is_fibonacci(6765) is True  # F(20)
        assert fibonacci_calculator.is_fibonacci(6766) is False  # Not Fibonacci

    def test_is_fibonacci_perfect_square_edge_cases(self, fibonacci_calculator: Fibonacci) -> None:
        """Test is_fibonacci with edge cases around perfect squares."""
        # Test numbers that might be close to Fibonacci numbers
        assert fibonacci_calculator.is_fibonacci(0) is True
        assert fibonacci_calculator.is_fibonacci(1) is True
        assert fibonacci_calculator.is_fibonacci(2) is True

    # Tests for find_index method
    def test_find_index_fibonacci_numbers(self, fibonacci_calculator: Fibonacci) -> None:
        """Test find_index with known Fibonacci numbers."""
        test_cases = [
            (0, 0),  # F(0) = 0
            (1, 1),  # F(1) = 1
            (2, 3),  # F(3) = 2
            (3, 4),  # F(4) = 3
            (5, 5),  # F(5) = 5
            (8, 6),  # F(6) = 8
            (13, 7),  # F(7) = 13
            (21, 8),  # F(8) = 21
            (34, 9),  # F(9) = 34
            (55, 10),  # F(10) = 55
        ]
        for target, expected_index in test_cases:
            assert fibonacci_calculator.find_index(target) == expected_index

    def test_find_index_non_fibonacci_numbers(self, fibonacci_calculator: Fibonacci) -> None:
        """Test find_index with non-Fibonacci numbers."""
        non_fibonacci_numbers = [4, 6, 7, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20]
        for num in non_fibonacci_numbers:
            assert fibonacci_calculator.find_index(num) is None

    def test_find_index_negative(self, fibonacci_calculator: Fibonacci) -> None:
        """Test find_index with negative numbers."""
        assert fibonacci_calculator.find_index(-1) is None
        assert fibonacci_calculator.find_index(-5) is None
        assert fibonacci_calculator.find_index(-100) is None

    def test_find_index_large_numbers(self, fibonacci_calculator: Fibonacci) -> None:
        """Test find_index with larger numbers."""
        # Test with a larger Fibonacci number
        assert fibonacci_calculator.find_index(6765) == 20  # F(20)
        assert fibonacci_calculator.find_index(6766) is None  # Not Fibonacci

    def test_find_index_zero(self, fibonacci_calculator: Fibonacci) -> None:
        """Test find_index with zero."""
        assert fibonacci_calculator.find_index(0) == 0

    def test_find_index_not_found_case(self, fibonacci_calculator: Fibonacci) -> None:
        """Test find_index when target is not found (b != target case)."""
        # Test with a number that is not a Fibonacci number
        # This will trigger the else None branch
        assert fibonacci_calculator.find_index(4) is None
        assert fibonacci_calculator.find_index(6) is None
        assert fibonacci_calculator.find_index(7) is None

    # Tests for clear_cache method
    def test_clear_cache(self, fibonacci_calculator: Fibonacci) -> None:
        """Test clearing the memoization cache."""
        # Populate cache
        fibonacci_calculator.compute(10)
        assert fibonacci_calculator.cache_size() > 0

        # Clear cache
        fibonacci_calculator.clear_cache()
        assert fibonacci_calculator.cache_size() == 0

    def test_clear_cache_empty(self, fibonacci_calculator: Fibonacci) -> None:
        """Test clearing an empty cache."""
        assert fibonacci_calculator.cache_size() == 0
        fibonacci_calculator.clear_cache()
        assert fibonacci_calculator.cache_size() == 0

    def test_clear_cache_multiple_calls(self, fibonacci_calculator: Fibonacci) -> None:
        """Test multiple calls to clear_cache."""
        # Populate cache
        fibonacci_calculator.compute(10)
        fibonacci_calculator.compute(15)
        assert fibonacci_calculator.cache_size() > 0

        # Clear multiple times
        fibonacci_calculator.clear_cache()
        fibonacci_calculator.clear_cache()
        fibonacci_calculator.clear_cache()
        assert fibonacci_calculator.cache_size() == 0

    # Tests for cache_size method
    def test_cache_size_empty(self, fibonacci_calculator: Fibonacci) -> None:
        """Test cache size when cache is empty."""
        assert fibonacci_calculator.cache_size() == 0

    def test_cache_size_after_computation(self, fibonacci_calculator: Fibonacci) -> None:
        """Test cache size after computing Fibonacci numbers."""
        # Initial cache size should be 0
        assert fibonacci_calculator.cache_size() == 0

        # Compute F(5) - should cache F(2), F(3), F(4), F(5) (base cases 0,1 not cached)
        fibonacci_calculator.compute(5)
        assert fibonacci_calculator.cache_size() == 4

        # Compute F(10) - should add F(6), F(7), F(8), F(9), F(10)
        fibonacci_calculator.compute(10)
        assert fibonacci_calculator.cache_size() == 9

    def test_cache_size_after_clear(self, fibonacci_calculator: Fibonacci) -> None:
        """Test cache size after clearing cache."""
        fibonacci_calculator.compute(10)
        assert fibonacci_calculator.cache_size() > 0

        fibonacci_calculator.clear_cache()
        assert fibonacci_calculator.cache_size() == 0

    def test_cache_size_consistency(self, fibonacci_calculator: Fibonacci) -> None:
        """Test that cache size is consistent with actual cache contents."""
        fibonacci_calculator.compute(5)
        size_before = fibonacci_calculator.cache_size()

        # Compute same number again - should not change cache size
        fibonacci_calculator.compute(5)
        size_after = fibonacci_calculator.cache_size()
        assert size_before == size_after

    # Tests for ratio method
    def test_ratio_basic(self, fibonacci_calculator: Fibonacci) -> None:
        """Test ratio calculation for basic cases."""
        # F(2)/F(1) = 1/1 = 1.0
        assert fibonacci_calculator.ratio(2) == pytest.approx(1.0)

        # F(3)/F(2) = 2/1 = 2.0
        assert fibonacci_calculator.ratio(3) == pytest.approx(2.0)

        # F(4)/F(3) = 3/2 = 1.5
        assert fibonacci_calculator.ratio(4) == pytest.approx(1.5)

    def test_ratio_golden_ratio_approximation(self, fibonacci_calculator: Fibonacci) -> None:
        """Test that ratio approaches golden ratio."""
        golden_ratio = 1.618033988749895

        # Test that ratio approaches golden ratio for larger n
        ratio_10 = fibonacci_calculator.ratio(10)
        ratio_15 = fibonacci_calculator.ratio(15)
        ratio_20 = fibonacci_calculator.ratio(20)

        # Ratios should get closer to golden ratio as n increases
        assert abs(ratio_20 - golden_ratio) < abs(ratio_15 - golden_ratio)
        assert abs(ratio_15 - golden_ratio) < abs(ratio_10 - golden_ratio)

        # All ratios should be close to golden ratio
        assert ratio_10 == pytest.approx(golden_ratio, abs=0.1)
        assert ratio_15 == pytest.approx(golden_ratio, abs=0.01)
        assert ratio_20 == pytest.approx(golden_ratio, abs=0.001)

    def test_ratio_zero_raises_error(self, fibonacci_calculator: Fibonacci) -> None:
        """Test that ratio with zero raises error."""
        with pytest.raises(ValueError, match="Ratio calculation requires n > 0"):
            fibonacci_calculator.ratio(0)

    def test_ratio_negative_raises_error(self, fibonacci_calculator: Fibonacci) -> None:
        """Test that ratio with negative number raises error."""
        with pytest.raises(ValueError, match="Ratio calculation requires n > 0"):
            fibonacci_calculator.ratio(-1)

    def test_ratio_one_returns_infinity(self, fibonacci_calculator: Fibonacci) -> None:
        """Test that ratio(1) returns infinity."""
        result = fibonacci_calculator.ratio(1)
        assert result == float("inf")

    def test_ratio_large_number(self, fibonacci_calculator: Fibonacci) -> None:
        """Test ratio calculation with larger number."""
        ratio = fibonacci_calculator.ratio(25)
        golden_ratio = 1.618033988749895
        assert ratio == pytest.approx(golden_ratio, abs=0.0001)

    # Tests for __repr__ method
    def test_repr(self, fibonacci_calculator: Fibonacci) -> None:
        """Test string representation."""
        assert repr(fibonacci_calculator) == "Fibonacci()"

    def test_repr_consistency(self, fibonacci_calculator: Fibonacci) -> None:
        """Test that repr is consistent."""
        repr1 = repr(fibonacci_calculator)
        repr2 = repr(fibonacci_calculator)
        assert repr1 == repr2

    def test_repr_after_computation(self, fibonacci_calculator: Fibonacci) -> None:
        """Test that repr doesn't change after computation."""
        repr_before = repr(fibonacci_calculator)
        fibonacci_calculator.compute(10)
        repr_after = repr(fibonacci_calculator)
        assert repr_before == repr_after
