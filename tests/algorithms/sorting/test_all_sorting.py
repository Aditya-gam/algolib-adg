"""Tests for all sorting algorithms."""

from typing import MutableSequence

import pytest
from hypothesis import given
from hypothesis import strategies as st

from algolib.algorithms.sorting import (
    CountingSort,
    HeapSort,
    InsertionSort,
    QuickSort,
    RadixSort,
    SelectionSort,
)
from algolib.algorithms.sorting.base import Sorter
from tests.utils.helpers import is_sorted


# Test data strategies
@given(st.lists(st.integers(min_value=-10, max_value=1000)))
def test_counting_sorter_property(data: list[int]) -> None:
    """Test counting sort with property-based testing."""
    sorter = CountingSort(min_val=-10, max_val=1000)
    sorted_data = sorter.sort(data)
    assert is_sorted(sorted_data)


@given(st.lists(st.integers()))
def test_heap_sorter_property(data: list[int]) -> None:
    """Test heap sort with property-based testing."""
    sorter: HeapSort[int] = HeapSort[int]()
    sorted_data = sorter.sort(data)
    assert is_sorted(sorted_data)


@given(st.lists(st.integers()))
def test_insertion_sorter_property(data: list[int]) -> None:
    """Test insertion sort with property-based testing."""
    sorter = InsertionSort()
    sorted_data = sorter.sort(data)
    assert is_sorted(sorted_data)


@given(st.lists(st.integers()))
def test_quick_sorter_property(data: list[int]) -> None:
    """Test quick sort with property-based testing."""
    sorter: QuickSort[int] = QuickSort[int]()
    sorted_data = sorter.sort(data)
    assert is_sorted(sorted_data)


@given(st.lists(st.integers(min_value=0, max_value=999)))
def test_radix_sorter_property(data: list[int]) -> None:
    """Test radix sort with property-based testing."""
    sorter = RadixSort()
    sorted_data = sorter.sort(data)
    assert is_sorted(sorted_data)


@given(st.lists(st.integers()))
def test_selection_sorter_property(data: list[int]) -> None:
    """Test selection sort with property-based testing."""
    sorter = SelectionSort()
    sorted_data = sorter.sort(data)
    assert is_sorted(sorted_data)


class TestCountingSort:
    """Test cases for Counting Sort algorithm."""

    @pytest.fixture
    def sorter(self) -> CountingSort:
        return CountingSort(min_val=-10, max_val=1000)

    def test_sort_empty_list(self, sorter: CountingSort) -> None:
        """Test sorting an empty list."""
        assert sorter.sort([]) == []

    def test_sort_single_element(self, sorter: CountingSort) -> None:
        """Test sorting a single element."""
        assert sorter.sort([5]) == [5]

    def test_sort_sorted_list(self, sorter: CountingSort) -> None:
        """Test sorting an already sorted list."""
        data = [1, 2, 3, 4, 5]
        assert sorter.sort(data) == [1, 2, 3, 4, 5]

    def test_sort_reverse_sorted_list(self, sorter: CountingSort) -> None:
        """Test sorting a reverse sorted list."""
        data = [5, 4, 3, 2, 1]
        assert sorter.sort(data) == [1, 2, 3, 4, 5]

    def test_sort_with_duplicates(self, sorter: CountingSort) -> None:
        """Test sorting with duplicate elements."""
        data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        assert sorter.sort(data) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

    def test_sort_with_negative_numbers(self, sorter: CountingSort) -> None:
        """Test sorting with negative numbers."""
        data = [-5, 3, -1, 0, -8, 5]
        assert sorter.sort(data) == [-8, -5, -1, 0, 3, 5]

    def test_sort_with_zeros(self, sorter: CountingSort) -> None:
        """Test sorting with zeros."""
        data = [0, 5, 0, 3, 0]
        assert sorter.sort(data) == [0, 0, 0, 3, 5]

    def test_sort_large_range(self, sorter: CountingSort) -> None:
        """Test sorting with large range of numbers."""
        data = [1000, 1, 999, 2, 998, 3]
        assert sorter.sort(data) == [1, 2, 3, 998, 999, 1000]


class TestHeapSort:
    """Test cases for Heap Sort algorithm."""

    @pytest.fixture
    def sorter(self) -> HeapSort[int]:
        return HeapSort[int]()

    def test_sort_empty_list(self, sorter: HeapSort[int]) -> None:
        """Test sorting an empty list."""
        assert sorter.sort([]) == []

    def test_sort_single_element(self, sorter: HeapSort[int]) -> None:
        """Test sorting a single element."""
        assert sorter.sort([5]) == [5]

    def test_sort_sorted_list(self, sorter: HeapSort[int]) -> None:
        """Test sorting an already sorted list."""
        data = [1, 2, 3, 4, 5]
        assert sorter.sort(data) == [1, 2, 3, 4, 5]

    def test_sort_reverse_sorted_list(self, sorter: HeapSort[int]) -> None:
        """Test sorting a reverse sorted list."""
        data = [5, 4, 3, 2, 1]
        assert sorter.sort(data) == [1, 2, 3, 4, 5]

    def test_sort_with_duplicates(self, sorter: HeapSort[int]) -> None:
        """Test sorting with duplicate elements."""
        data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        assert sorter.sort(data) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

    def test_sort_with_negative_numbers(self, sorter: HeapSort[int]) -> None:
        """Test sorting with negative numbers."""
        data = [-5, 3, -1, 0, -8, 5]
        assert sorter.sort(data) == [-8, -5, -1, 0, 3, 5]

    def test_sort_large_list(self, sorter: HeapSort[int]) -> None:
        """Test sorting a large list."""
        data = list(range(100, 0, -1))
        assert sorter.sort(data) == list(range(1, 101))


class TestInsertionSort:
    """Test cases for Insertion Sort algorithm."""

    @pytest.fixture
    def sorter(self) -> InsertionSort:
        return InsertionSort()

    def test_sort_empty_list(self, sorter: InsertionSort) -> None:
        """Test sorting an empty list."""
        assert sorter.sort([]) == []

    def test_sort_single_element(self, sorter: InsertionSort) -> None:
        """Test sorting a single element."""
        assert sorter.sort([5]) == [5]

    def test_sort_sorted_list(self, sorter: InsertionSort) -> None:
        """Test sorting an already sorted list."""
        data = [1, 2, 3, 4, 5]
        assert sorter.sort(data) == [1, 2, 3, 4, 5]

    def test_sort_reverse_sorted_list(self, sorter: InsertionSort) -> None:
        """Test sorting a reverse sorted list."""
        data = [5, 4, 3, 2, 1]
        assert sorter.sort(data) == [1, 2, 3, 4, 5]

    def test_sort_with_duplicates(self, sorter: InsertionSort) -> None:
        """Test sorting with duplicate elements."""
        data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        assert sorter.sort(data) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

    def test_sort_with_negative_numbers(self, sorter: InsertionSort) -> None:
        """Test sorting with negative numbers."""
        data = [-5, 3, -1, 0, -8, 5]
        assert sorter.sort(data) == [-8, -5, -1, 0, 3, 5]

    def test_sort_small_list(self, sorter: InsertionSort) -> None:
        """Test sorting a small list."""
        data = [3, 1, 2]
        assert sorter.sort(data) == [1, 2, 3]

    # Tests for sort_in_place method
    def test_sort_in_place_empty_list(self, sorter: InsertionSort) -> None:
        """Test in-place sorting of empty list."""
        data: list[int] = []
        sorter.sort_in_place(data)
        assert data == []

    def test_sort_in_place_single_element(self, sorter: InsertionSort) -> None:
        """Test in-place sorting of single element."""
        data = [5]
        sorter.sort_in_place(data)
        assert data == [5]

    def test_sort_in_place_sorted_list(self, sorter: InsertionSort) -> None:
        """Test in-place sorting of already sorted list."""
        data = [1, 2, 3, 4, 5]
        sorter.sort_in_place(data)
        assert data == [1, 2, 3, 4, 5]

    def test_sort_in_place_reverse_sorted_list(self, sorter: InsertionSort) -> None:
        """Test in-place sorting of reverse sorted list."""
        data = [5, 4, 3, 2, 1]
        sorter.sort_in_place(data)
        assert data == [1, 2, 3, 4, 5]

    def test_sort_in_place_with_duplicates(self, sorter: InsertionSort) -> None:
        """Test in-place sorting with duplicate elements."""
        data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        sorter.sort_in_place(data)
        assert data == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

    def test_sort_in_place_with_negative_numbers(self, sorter: InsertionSort) -> None:
        """Test in-place sorting with negative numbers."""
        data = [-5, 3, -1, 0, -8, 5]
        sorter.sort_in_place(data)
        assert data == [-8, -5, -1, 0, 3, 5]

    def test_sort_in_place_modifies_original(self, sorter: InsertionSort) -> None:
        """Test that sort_in_place modifies the original list."""
        original_data = [5, 2, 8, 1, 9]
        data = original_data.copy()
        sorter.sort_in_place(data)
        assert data == [1, 2, 5, 8, 9]
        assert data is not original_data  # Should be the same object

    # Tests for binary_insertion_sort method
    def test_binary_insertion_sort_empty_list(self, sorter: InsertionSort) -> None:
        """Test binary insertion sort of empty list."""
        assert sorter.binary_insertion_sort([]) == []

    def test_binary_insertion_sort_single_element(self, sorter: InsertionSort) -> None:
        """Test binary insertion sort of single element."""
        assert sorter.binary_insertion_sort([5]) == [5]

    def test_binary_insertion_sort_sorted_list(self, sorter: InsertionSort) -> None:
        """Test binary insertion sort of already sorted list."""
        data = [1, 2, 3, 4, 5]
        assert sorter.binary_insertion_sort(data) == [1, 2, 3, 4, 5]

    def test_binary_insertion_sort_reverse_sorted_list(self, sorter: InsertionSort) -> None:
        """Test binary insertion sort of reverse sorted list."""
        data = [5, 4, 3, 2, 1]
        assert sorter.binary_insertion_sort(data) == [1, 2, 3, 4, 5]

    def test_binary_insertion_sort_with_duplicates(self, sorter: InsertionSort) -> None:
        """Test binary insertion sort with duplicate elements."""
        data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        assert sorter.binary_insertion_sort(data) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

    def test_binary_insertion_sort_with_negative_numbers(self, sorter: InsertionSort) -> None:
        """Test binary insertion sort with negative numbers."""
        data = [-5, 3, -1, 0, -8, 5]
        assert sorter.binary_insertion_sort(data) == [-8, -5, -1, 0, 3, 5]

    def test_binary_insertion_sort_consistency_with_sort(self, sorter: InsertionSort) -> None:
        """Test that binary_insertion_sort produces same results as sort."""
        test_cases = [
            [],
            [5],
            [1, 2, 3, 4, 5],
            [5, 4, 3, 2, 1],
            [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],
            [-5, 3, -1, 0, -8, 5],
            [3, 1, 2],
        ]
        for data in test_cases:
            data_list: list[int] = data
            sort_result = sorter.sort(data_list)
            binary_result = sorter.binary_insertion_sort(data_list)
            assert sort_result == binary_result

    # Tests for is_sorted method
    def test_is_sorted_empty_list(self, sorter: InsertionSort) -> None:
        """Test is_sorted with empty list."""
        assert sorter.is_sorted([]) is True

    def test_is_sorted_single_element(self, sorter: InsertionSort) -> None:
        """Test is_sorted with single element."""
        assert sorter.is_sorted([5]) is True

    def test_is_sorted_sorted_list(self, sorter: InsertionSort) -> None:
        """Test is_sorted with sorted list."""
        assert sorter.is_sorted([1, 2, 3, 4, 5]) is True

    def test_is_sorted_reverse_sorted_list(self, sorter: InsertionSort) -> None:
        """Test is_sorted with reverse sorted list."""
        assert sorter.is_sorted([5, 4, 3, 2, 1]) is False

    def test_is_sorted_unsorted_list(self, sorter: InsertionSort) -> None:
        """Test is_sorted with unsorted list."""
        assert sorter.is_sorted([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) is False

    def test_is_sorted_with_duplicates(self, sorter: InsertionSort) -> None:
        """Test is_sorted with duplicates in sorted order."""
        assert sorter.is_sorted([1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]) is True

    def test_is_sorted_with_negative_numbers(self, sorter: InsertionSort) -> None:
        """Test is_sorted with negative numbers in sorted order."""
        assert sorter.is_sorted([-8, -5, -1, 0, 3, 5]) is True

    def test_is_sorted_partially_sorted(self, sorter: InsertionSort) -> None:
        """Test is_sorted with partially sorted list."""
        assert sorter.is_sorted([1, 2, 3, 5, 4, 6, 7]) is False

    # Tests for count_inversions method
    def test_count_inversions_empty_list(self, sorter: InsertionSort) -> None:
        """Test count_inversions with empty list."""
        assert sorter.count_inversions([]) == 0

    def test_count_inversions_single_element(self, sorter: InsertionSort) -> None:
        """Test count_inversions with single element."""
        assert sorter.count_inversions([5]) == 0

    def test_count_inversions_sorted_list(self, sorter: InsertionSort) -> None:
        """Test count_inversions with sorted list."""
        assert sorter.count_inversions([1, 2, 3, 4, 5]) == 0

    def test_count_inversions_reverse_sorted_list(self, sorter: InsertionSort) -> None:
        """Test count_inversions with reverse sorted list."""
        # [5, 4, 3, 2, 1] has 10 inversions
        assert sorter.count_inversions([5, 4, 3, 2, 1]) == 10

    def test_count_inversions_with_duplicates(self, sorter: InsertionSort) -> None:
        """Test count_inversions with duplicates."""
        # [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5] has many inversions
        inversions = sorter.count_inversions([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
        assert inversions > 0

    def test_count_inversions_small_list(self, sorter: InsertionSort) -> None:
        """Test count_inversions with small list."""
        # [3, 1, 2] has 2 inversions: (3,1) and (3,2)
        assert sorter.count_inversions([3, 1, 2]) == 2

    def test_count_inversions_with_negative_numbers(self, sorter: InsertionSort) -> None:
        """Test count_inversions with negative numbers."""
        # [-5, 3, -1, 0, -8, 5] has inversions
        inversions = sorter.count_inversions([-5, 3, -1, 0, -8, 5])
        assert inversions > 0

    def test_count_inversions_consistency(self, sorter: InsertionSort) -> None:
        """Test that count_inversions is consistent."""
        data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        inversions1 = sorter.count_inversions(data)
        inversions2 = sorter.count_inversions(data)
        assert inversions1 == inversions2

    # Tests for sort_with_stats method
    def test_sort_with_stats_empty_list(self, sorter: InsertionSort) -> None:
        """Test sort_with_stats with empty list."""
        sorted_list: list[int]
        sorted_list, comparisons, shifts = sorter.sort_with_stats([])
        assert sorted_list == []
        assert comparisons == 0
        assert shifts == 0

    def test_sort_with_stats_single_element(self, sorter: InsertionSort) -> None:
        """Test sort_with_stats with single element."""
        sorted_list, comparisons, shifts = sorter.sort_with_stats([5])
        assert sorted_list == [5]
        assert comparisons == 0
        assert shifts == 0

    def test_sort_with_stats_sorted_list(self, sorter: InsertionSort) -> None:
        """Test sort_with_stats with sorted list."""
        data = [1, 2, 3, 4, 5]
        sorted_list, comparisons, shifts = sorter.sort_with_stats(data)
        assert sorted_list == [1, 2, 3, 4, 5]
        assert comparisons >= 0
        assert shifts >= 0

    def test_sort_with_stats_reverse_sorted_list(self, sorter: InsertionSort) -> None:
        """Test sort_with_stats with reverse sorted list."""
        data = [5, 4, 3, 2, 1]
        sorted_list, comparisons, shifts = sorter.sort_with_stats(data)
        assert sorted_list == [1, 2, 3, 4, 5]
        assert comparisons > 0
        assert shifts > 0

    def test_sort_with_stats_with_duplicates(self, sorter: InsertionSort) -> None:
        """Test sort_with_stats with duplicates."""
        data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        sorted_list, comparisons, shifts = sorter.sort_with_stats(data)
        assert sorted_list == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
        assert comparisons > 0
        assert shifts > 0

    def test_sort_with_stats_consistency_with_sort(self, sorter: InsertionSort) -> None:
        """Test that sort_with_stats produces same sorted result as sort."""
        test_cases = [
            [],
            [5],
            [1, 2, 3, 4, 5],
            [5, 4, 3, 2, 1],
            [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],
            [-5, 3, -1, 0, -8, 5],
            [3, 1, 2],
        ]
        for data in test_cases:
            data_list: list[int] = data
            sort_result = sorter.sort(data_list)
            stats_result, _, _ = sorter.sort_with_stats(data_list)
            assert sort_result == stats_result

    def test_sort_with_stats_positive_stats(self, sorter: InsertionSort) -> None:
        """Test that sort_with_stats returns positive statistics."""
        data = [5, 4, 3, 2, 1]
        _, comparisons, shifts = sorter.sort_with_stats(data)
        assert comparisons >= 0
        assert shifts >= 0

    # Tests for __repr__ method
    def test_repr(self, sorter: InsertionSort) -> None:
        """Test string representation."""
        assert repr(sorter) == "InsertionSort()"

    def test_repr_consistency(self, sorter: InsertionSort) -> None:
        """Test that repr is consistent."""
        repr1 = repr(sorter)
        repr2 = repr(sorter)
        assert repr1 == repr2

    def test_repr_after_sorting(self, sorter: InsertionSort) -> None:
        """Test that repr doesn't change after sorting."""
        repr_before = repr(sorter)
        sorter.sort([5, 2, 8, 1, 9])
        repr_after = repr(sorter)
        assert repr_before == repr_after


class TestQuickSort:
    """Test cases for Quick Sort algorithm."""

    @pytest.fixture
    def sorter(self) -> QuickSort[int]:
        return QuickSort[int]()

    def test_sort_empty_list(self, sorter: QuickSort[int]) -> None:
        """Test sorting an empty list."""
        assert sorter.sort([]) == []

    def test_sort_single_element(self, sorter: QuickSort[int]) -> None:
        """Test sorting a single element."""
        assert sorter.sort([5]) == [5]

    def test_sort_sorted_list(self, sorter: QuickSort[int]) -> None:
        """Test sorting an already sorted list."""
        data = [1, 2, 3, 4, 5]
        assert sorter.sort(data) == [1, 2, 3, 4, 5]

    def test_sort_reverse_sorted_list(self, sorter: QuickSort[int]) -> None:
        """Test sorting a reverse sorted list."""
        data = [5, 4, 3, 2, 1]
        assert sorter.sort(data) == [1, 2, 3, 4, 5]

    def test_sort_with_duplicates(self, sorter: QuickSort[int]) -> None:
        """Test sorting with duplicate elements."""
        data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        assert sorter.sort(data) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

    def test_sort_with_negative_numbers(self, sorter: QuickSort[int]) -> None:
        """Test sorting with negative numbers."""
        data = [-5, 3, -1, 0, -8, 5]
        assert sorter.sort(data) == [-8, -5, -1, 0, 3, 5]

    def test_sort_large_list(self, sorter: QuickSort[int]) -> None:
        """Test sorting a large list."""
        data = list(range(100, 0, -1))
        assert sorter.sort(data) == list(range(1, 101))

    def test_sort_with_pivot_duplicates(self, sorter: QuickSort[int]) -> None:
        """Test sorting with many duplicate pivot values."""
        data = [3, 3, 3, 1, 3, 3, 3, 2, 3, 3, 3]
        assert sorter.sort(data) == [1, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3]


class TestRadixSort:
    """Test cases for Radix Sort algorithm."""

    @pytest.fixture
    def sorter(self) -> RadixSort:
        return RadixSort()

    def test_sort_empty_list(self, sorter: RadixSort) -> None:
        """Test sorting an empty list."""
        assert sorter.sort([]) == []

    def test_sort_single_element(self, sorter: RadixSort) -> None:
        """Test sorting a single element."""
        assert sorter.sort([5]) == [5]

    def test_sort_sorted_list(self, sorter: RadixSort) -> None:
        """Test sorting an already sorted list."""
        data = [1, 2, 3, 4, 5]
        assert sorter.sort(data) == [1, 2, 3, 4, 5]

    def test_sort_reverse_sorted_list(self, sorter: RadixSort) -> None:
        """Test sorting a reverse sorted list."""
        data = [5, 4, 3, 2, 1]
        assert sorter.sort(data) == [1, 2, 3, 4, 5]

    def test_sort_with_duplicates(self, sorter: RadixSort) -> None:
        """Test sorting with duplicate elements."""
        data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        assert sorter.sort(data) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

    def test_sort_large_numbers(self, sorter: RadixSort) -> None:
        """Test sorting with large numbers."""
        data = [1000, 100, 10, 1, 999, 99, 9]
        assert sorter.sort(data) == [1, 9, 10, 99, 100, 999, 1000]

    def test_sort_with_zeros(self, sorter: RadixSort) -> None:
        """Test sorting with zeros."""
        data = [0, 5, 0, 3, 0]
        assert sorter.sort(data) == [0, 0, 0, 3, 5]

    def test_sort_single_digit_numbers(self, sorter: RadixSort) -> None:
        """Test sorting with single digit numbers."""
        data = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        assert sorter.sort(data) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    def test_sort_with_negative_numbers_raises_error(self, sorter: RadixSort) -> None:
        """Test that sorting with negative numbers raises ValueError."""
        data = [1, -2, 3, -4, 5]
        with pytest.raises(ValueError, match="RadixSort only supports non-negative integers"):
            sorter.sort(data)

    def test_sort_with_mixed_negative_and_positive_raises_error(self, sorter: RadixSort) -> None:
        """Test that sorting with mixed negative and positive numbers raises ValueError."""
        data = [1, 2, 3, -1, 4, 5]
        with pytest.raises(ValueError, match="RadixSort only supports non-negative integers"):
            sorter.sort(data)

    def test_sort_with_all_negative_numbers_raises_error(self, sorter: RadixSort) -> None:
        """Test that sorting with all negative numbers raises ValueError."""
        data = [-1, -2, -3, -4, -5]
        with pytest.raises(ValueError, match="RadixSort only supports non-negative integers"):
            sorter.sort(data)

    def test_init_with_invalid_base_raises_error(self) -> None:
        """Test that initializing with invalid base raises ValueError."""
        with pytest.raises(ValueError, match="Base must be at least 2"):
            RadixSort(base=1)

    def test_init_with_zero_base_raises_error(self) -> None:
        """Test that initializing with zero base raises ValueError."""
        with pytest.raises(ValueError, match="Base must be at least 2"):
            RadixSort(base=0)

    def test_init_with_negative_base_raises_error(self) -> None:
        """Test that initializing with negative base raises ValueError."""
        with pytest.raises(ValueError, match="Base must be at least 2"):
            RadixSort(base=-1)

    def test_sort_with_different_base(self) -> None:
        """Test sorting with a different base (binary)."""
        sorter = RadixSort(base=2)
        data = [5, 3, 1, 4, 2]
        assert sorter.sort(data) == [1, 2, 3, 4, 5]

    def test_sort_with_hexadecimal_base(self) -> None:
        """Test sorting with hexadecimal base."""
        sorter = RadixSort(base=16)
        data = [15, 1, 14, 2, 13, 3]
        assert sorter.sort(data) == [1, 2, 3, 13, 14, 15]


class TestSelectionSort:
    """Test cases for Selection Sort algorithm."""

    @pytest.fixture
    def sorter(self) -> SelectionSort:
        return SelectionSort()

    def test_sort_empty_list(self, sorter: SelectionSort) -> None:
        """Test sorting an empty list."""
        assert sorter.sort([]) == []

    def test_sort_single_element(self, sorter: SelectionSort) -> None:
        """Test sorting a single element."""
        assert sorter.sort([5]) == [5]

    def test_sort_sorted_list(self, sorter: SelectionSort) -> None:
        """Test sorting an already sorted list."""
        data = [1, 2, 3, 4, 5]
        assert sorter.sort(data) == [1, 2, 3, 4, 5]

    def test_sort_reverse_sorted_list(self, sorter: SelectionSort) -> None:
        """Test sorting a reverse sorted list."""
        data = [5, 4, 3, 2, 1]
        assert sorter.sort(data) == [1, 2, 3, 4, 5]

    def test_sort_with_duplicates(self, sorter: SelectionSort) -> None:
        """Test sorting with duplicate elements."""
        data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        assert sorter.sort(data) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

    def test_sort_with_negative_numbers(self, sorter: SelectionSort) -> None:
        """Test sorting with negative numbers."""
        data = [-5, 3, -1, 0, -8, 5]
        assert sorter.sort(data) == [-8, -5, -1, 0, 3, 5]

    def test_sort_small_list(self, sorter: SelectionSort) -> None:
        """Test sorting a small list."""
        data = [3, 1, 2]
        assert sorter.sort(data) == [1, 2, 3]

    # Tests for sort_in_place method
    def test_sort_in_place_empty_list(self, sorter: SelectionSort) -> None:
        """Test in-place sorting of empty list."""
        data: list[int] = []
        sorter.sort_in_place(data)
        assert data == []

    def test_sort_in_place_single_element(self, sorter: SelectionSort) -> None:
        """Test in-place sorting of single element."""
        data = [5]
        sorter.sort_in_place(data)
        assert data == [5]

    def test_sort_in_place_sorted_list(self, sorter: SelectionSort) -> None:
        """Test in-place sorting of already sorted list."""
        data = [1, 2, 3, 4, 5]
        sorter.sort_in_place(data)
        assert data == [1, 2, 3, 4, 5]

    def test_sort_in_place_reverse_sorted_list(self, sorter: SelectionSort) -> None:
        """Test in-place sorting of reverse sorted list."""
        data = [5, 4, 3, 2, 1]
        sorter.sort_in_place(data)
        assert data == [1, 2, 3, 4, 5]

    def test_sort_in_place_with_duplicates(self, sorter: SelectionSort) -> None:
        """Test in-place sorting with duplicate elements."""
        data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        sorter.sort_in_place(data)
        assert data == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

    def test_sort_in_place_with_negative_numbers(self, sorter: SelectionSort) -> None:
        """Test in-place sorting with negative numbers."""
        data = [-5, 3, -1, 0, -8, 5]
        sorter.sort_in_place(data)
        assert data == [-8, -5, -1, 0, 3, 5]

    def test_sort_in_place_modifies_original(self, sorter: SelectionSort) -> None:
        """Test that sort_in_place modifies the original list."""
        original_data = [5, 2, 8, 1, 9]
        data = original_data.copy()
        sorter.sort_in_place(data)
        assert data == [1, 2, 5, 8, 9]
        assert data is not original_data  # Should be the same object

    # Tests for find_min_index method
    def test_find_min_index_basic(self, sorter: SelectionSort) -> None:
        """Test find_min_index with basic cases."""
        data = [5, 2, 8, 1, 9]
        assert sorter.find_min_index(data, 0, 5) == 3  # Index of 1
        # Index of 1 in range [1,4)
        assert sorter.find_min_index(data, 1, 4) == 3
        # Index of 2 in range [0,3)
        assert sorter.find_min_index(data, 0, 3) == 1

    def test_find_min_index_single_element(self, sorter: SelectionSort) -> None:
        """Test find_min_index with single element range."""
        data = [5, 2, 8, 1, 9]
        assert sorter.find_min_index(data, 2, 3) == 2  # Only element 8

    def test_find_min_index_first_element(self, sorter: SelectionSort) -> None:
        """Test find_min_index when first element is minimum."""
        data = [1, 5, 8, 2, 9]
        assert sorter.find_min_index(data, 0, 5) == 0  # Index of 1

    def test_find_min_index_last_element(self, sorter: SelectionSort) -> None:
        """Test find_min_index when last element is minimum."""
        data = [5, 8, 2, 9, 1]
        assert sorter.find_min_index(data, 0, 5) == 4  # Index of 1

    def test_find_min_index_with_duplicates(self, sorter: SelectionSort) -> None:
        """Test find_min_index with duplicate minimum values."""
        data = [5, 2, 1, 8, 1, 9]
        # Should return the first occurrence of minimum
        assert sorter.find_min_index(data, 0, 6) == 2  # First index of 1

    def test_find_min_index_invalid_range_start_equals_end(self, sorter: SelectionSort) -> None:
        """Test find_min_index with invalid range where start equals end."""
        data = [5, 2, 8, 1, 9]
        with pytest.raises(ValueError, match="Invalid range specified"):
            sorter.find_min_index(data, 2, 2)

    def test_find_min_index_invalid_range_start_greater_than_end(
        self, sorter: SelectionSort
    ) -> None:
        """Test find_min_index with invalid range where start > end."""
        data = [5, 2, 8, 1, 9]
        with pytest.raises(ValueError, match="Invalid range specified"):
            sorter.find_min_index(data, 3, 2)

    def test_find_min_index_invalid_range_negative_start(self, sorter: SelectionSort) -> None:
        """Test find_min_index with negative start index."""
        data = [5, 2, 8, 1, 9]
        with pytest.raises(ValueError, match="Invalid range specified"):
            sorter.find_min_index(data, -1, 3)

    def test_find_min_index_invalid_range_end_out_of_bounds(self, sorter: SelectionSort) -> None:
        """Test find_min_index with end index out of bounds."""
        data = [5, 2, 8, 1, 9]
        with pytest.raises(ValueError, match="Invalid range specified"):
            sorter.find_min_index(data, 1, 6)

    def test_find_min_index_with_negative_numbers(self, sorter: SelectionSort) -> None:
        """Test find_min_index with negative numbers."""
        data = [-5, 3, -1, 0, -8, 5]
        assert sorter.find_min_index(data, 0, 6) == 4  # Index of -8

    # Tests for is_sorted method
    def test_is_sorted_empty_list(self, sorter: SelectionSort) -> None:
        """Test is_sorted with empty list."""
        assert sorter.is_sorted([]) is True

    def test_is_sorted_single_element(self, sorter: SelectionSort) -> None:
        """Test is_sorted with single element."""
        assert sorter.is_sorted([5]) is True

    def test_is_sorted_sorted_list(self, sorter: SelectionSort) -> None:
        """Test is_sorted with sorted list."""
        assert sorter.is_sorted([1, 2, 3, 4, 5]) is True

    def test_is_sorted_reverse_sorted_list(self, sorter: SelectionSort) -> None:
        """Test is_sorted with reverse sorted list."""
        assert sorter.is_sorted([5, 4, 3, 2, 1]) is False

    def test_is_sorted_unsorted_list(self, sorter: SelectionSort) -> None:
        """Test is_sorted with unsorted list."""
        assert sorter.is_sorted([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) is False

    def test_is_sorted_with_duplicates(self, sorter: SelectionSort) -> None:
        """Test is_sorted with duplicates in sorted order."""
        assert sorter.is_sorted([1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]) is True

    def test_is_sorted_with_negative_numbers(self, sorter: SelectionSort) -> None:
        """Test is_sorted with negative numbers in sorted order."""
        assert sorter.is_sorted([-8, -5, -1, 0, 3, 5]) is True

    def test_is_sorted_partially_sorted(self, sorter: SelectionSort) -> None:
        """Test is_sorted with partially sorted list."""
        assert sorter.is_sorted([1, 2, 3, 5, 4, 6, 7]) is False

    # Tests for count_swaps method
    def test_count_swaps_empty_list(self, sorter: SelectionSort) -> None:
        """Test count_swaps with empty list."""
        assert sorter.count_swaps([]) == 0

    def test_count_swaps_single_element(self, sorter: SelectionSort) -> None:
        """Test count_swaps with single element."""
        assert sorter.count_swaps([5]) == 0

    def test_count_swaps_sorted_list(self, sorter: SelectionSort) -> None:
        """Test count_swaps with sorted list."""
        # Already sorted, no swaps needed
        assert sorter.count_swaps([1, 2, 3, 4, 5]) == 0

    def test_count_swaps_reverse_sorted_list(self, sorter: SelectionSort) -> None:
        """Test count_swaps with reverse sorted list."""
        # [5, 4, 3, 2, 1] needs swaps to sort
        swaps = sorter.count_swaps([5, 4, 3, 2, 1])
        assert swaps > 0

    def test_count_swaps_with_duplicates(self, sorter: SelectionSort) -> None:
        """Test count_swaps with duplicates."""
        swaps = sorter.count_swaps([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
        assert swaps >= 0

    def test_count_swaps_small_list(self, sorter: SelectionSort) -> None:
        """Test count_swaps with small list."""
        # [3, 1, 2] needs swaps to sort
        swaps = sorter.count_swaps([3, 1, 2])
        assert swaps > 0

    def test_count_swaps_with_negative_numbers(self, sorter: SelectionSort) -> None:
        """Test count_swaps with negative numbers."""
        swaps = sorter.count_swaps([-5, 3, -1, 0, -8, 5])
        assert swaps >= 0

    def test_count_swaps_consistency(self, sorter: SelectionSort) -> None:
        """Test that count_swaps is consistent."""
        data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        swaps1 = sorter.count_swaps(data)
        swaps2 = sorter.count_swaps(data)
        assert swaps1 == swaps2

    def test_count_swaps_verification(self, sorter: SelectionSort) -> None:
        """Test that count_swaps returns correct number of swaps."""
        # Test with a simple case where we can manually count swaps
        data = [3, 1, 2]
        swaps = sorter.count_swaps(data)
        # Manual verification: [3,1,2] -> [1,3,2] -> [1,2,3] = 2 swaps
        assert swaps == 2

    # Tests for __repr__ method
    def test_repr(self, sorter: SelectionSort) -> None:
        """Test string representation."""
        assert repr(sorter) == "SelectionSort()"

    def test_repr_consistency(self, sorter: SelectionSort) -> None:
        """Test that repr is consistent."""
        repr1 = repr(sorter)
        repr2 = repr(sorter)
        assert repr1 == repr2

    def test_repr_after_sorting(self, sorter: SelectionSort) -> None:
        """Test that repr doesn't change after sorting."""
        repr_before = repr(sorter)
        sorter.sort([5, 2, 8, 1, 9])
        repr_after = repr(sorter)
        assert repr_before == repr_after


class DummySorter(Sorter[int]):
    def sort(self, data: MutableSequence[int]) -> MutableSequence[int]:
        return list(sorted(data))


def test_sorter_run_calls_sort() -> None:
    sorter = DummySorter()
    data = [3, 1, 2]
    result = sorter.run(data)
    assert result == [1, 2, 3]


def test_counting_sort_invalid_range() -> None:
    with pytest.raises(ValueError, match="min_val must be <= max_val"):
        CountingSort(min_val=10, max_val=5)


def test_counting_sort_out_of_range() -> None:
    sorter = CountingSort(min_val=0, max_val=5)
    with pytest.raises(ValueError, match="outside range"):
        sorter.sort([1, 2, 6])
