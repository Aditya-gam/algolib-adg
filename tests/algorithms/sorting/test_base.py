"""Tests for sorting base classes."""

from typing import MutableSequence

from algolib.algorithms.sorting.base import Sorter


class MockSorter(Sorter[int]):
    """Mock sorter for testing base class functionality."""

    def sort(self, data: MutableSequence[int]) -> MutableSequence[int]:
        """Mock sort implementation."""
        # Only lists have sort method, so we need to handle this properly
        if isinstance(data, list):
            data.sort()
        else:
            # For other MutableSequence types, we need to sort manually
            sorted_data = sorted(data)
            data.clear()
            data.extend(sorted_data)
        return data


class TestSorterBase:
    """Test the Sorter base class."""

    def test_run_with_list(self) -> None:
        """Test run method with list input."""
        sorter = MockSorter()
        data: list[int] = [3, 1, 4, 1, 5]
        result = sorter.run(data)
        assert result == [1, 1, 3, 4, 5]
        assert data == [1, 1, 3, 4, 5]  # Should be modified in place

    def test_run_with_empty_list(self) -> None:
        """Test run method with empty list."""
        sorter = MockSorter()
        data: list[int] = []
        result = sorter.run(data)
        assert result == []
        assert data == []

    def test_run_with_single_element(self) -> None:
        """Test run method with single element list."""
        sorter = MockSorter()
        data = [42]
        result = sorter.run(data)
        assert result == [42]
        assert data == [42]

    def test_run_with_already_sorted_list(self) -> None:
        """Test run method with already sorted list."""
        sorter = MockSorter()
        data = [1, 2, 3, 4, 5]
        result = sorter.run(data)
        assert result == [1, 2, 3, 4, 5]
        assert data == [1, 2, 3, 4, 5]

    def test_run_with_reverse_sorted_list(self) -> None:
        """Test run method with reverse sorted list."""
        sorter = MockSorter()
        data = [5, 4, 3, 2, 1]
        result = sorter.run(data)
        assert result == [1, 2, 3, 4, 5]
        assert data == [1, 2, 3, 4, 5]

    def test_run_with_duplicate_elements(self) -> None:
        """Test run method with duplicate elements."""
        sorter = MockSorter()
        data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        result = sorter.run(data)
        assert result == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
        assert data == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

    def test_run_with_negative_numbers(self) -> None:
        """Test run method with negative numbers."""
        sorter = MockSorter()
        data = [-3, 1, -4, 1, -5]
        result = sorter.run(data)
        assert result == [-5, -4, -3, 1, 1]
        assert data == [-5, -4, -3, 1, 1]

    def test_run_with_zero(self) -> None:
        """Test run method with zero values."""
        sorter = MockSorter()
        data = [0, -1, 1, 0]
        result = sorter.run(data)
        assert result == [-1, 0, 0, 1]
        assert data == [-1, 0, 0, 1]
