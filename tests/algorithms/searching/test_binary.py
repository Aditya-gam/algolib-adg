"""Tests for the binary search algorithm."""

import pytest
from hypothesis import given
from hypothesis import strategies as st

from algolib.algorithms.searching.binary import BinarySearcher


@given(st.lists(st.integers()), st.integers())
def test_binary_search_property(data: list[int], value_to_find: int) -> None:
    searcher = BinarySearcher[int]()
    sorted_data = sorted(list(set(data)))  # Ensure data is sorted and unique

    result = searcher.search(sorted_data, value_to_find)

    if value_to_find in sorted_data:
        assert result is not None
        assert sorted_data[result] == value_to_find
    else:
        assert result is None


@pytest.fixture
def searcher() -> BinarySearcher[int]:
    """Fixture for a BinarySearcher instance."""
    return BinarySearcher()


def test_search_empty_list(searcher: BinarySearcher[int]) -> None:
    """Test searching in an empty list."""
    assert searcher.search([], 5) is None


def test_search_target_present_odd_length(searcher: BinarySearcher[int]) -> None:
    """Test searching for a target that is present in a list of odd length."""
    assert searcher.search([1, 2, 3, 4, 5], 3) == 2


def test_search_target_present_even_length(searcher: BinarySearcher[int]) -> None:
    """Test searching for a target that is present in a list of even length."""
    assert searcher.search([1, 2, 3, 4, 5, 6], 4) == 3


def test_search_target_not_present(searcher: BinarySearcher[int]) -> None:
    """Test searching for a target that is not present in the list."""
    assert searcher.search([1, 2, 3, 4, 5], 6) is None


def test_search_target_is_first_element(searcher: BinarySearcher[int]) -> None:
    """Test searching for a target that is the first element of the list."""
    assert searcher.search([1, 2, 3, 4, 5], 1) == 0


def test_search_target_is_last_element(searcher: BinarySearcher[int]) -> None:
    """Test searching for a target that is the last element of the list."""
    assert searcher.search([1, 2, 3, 4, 5], 5) == 4


def test_search_target_smaller_than_all(searcher: BinarySearcher[int]) -> None:
    """Test searching for a target smaller than all elements."""
    assert searcher.search([10, 20, 30, 40, 50], 5) is None


def test_search_target_larger_than_all(searcher: BinarySearcher[int]) -> None:
    """Test searching for a target larger than all elements."""
    assert searcher.search([10, 20, 30, 40, 50], 60) is None


def test_search_with_duplicates(searcher: BinarySearcher[int]) -> None:
    """Test searching in a list with duplicate elements."""
    # Binary search might return any of the indices for duplicates.
    # The simplest iterative implementation usually finds the first one from the left
    # after the array is conceptually split.
    result = searcher.search([1, 2, 2, 2, 3], 2)
    assert result in [1, 2, 3]


def test_search_single_element_list_found(searcher: BinarySearcher[int]) -> None:
    """Test searching in a single element list where the target is found."""
    assert searcher.search([5], 5) == 0


def test_search_single_element_list_not_found(searcher: BinarySearcher[int]) -> None:
    """Test searching in a single element list where the target is not found."""
    assert searcher.search([5], 4) is None


def test_search_with_non_integer_values(searcher: BinarySearcher[str]) -> None:
    """Test searching with non-integer values."""
    searcher_str = BinarySearcher[str]()
    assert searcher_str.search(["apple", "banana", "cherry"], "banana") == 1
    assert searcher_str.search(["apple", "banana", "cherry"], "durian") is None


def test_search_two_elements_found_first(searcher: BinarySearcher[int]) -> None:
    """Test a two-element list where the target is the first element."""
    assert searcher.search([10, 20], 10) == 0


def test_search_two_elements_found_second(searcher: BinarySearcher[int]) -> None:
    """Test a two-element list where the target is the second element."""
    assert searcher.search([10, 20], 20) == 1


def test_search_two_elements_not_found(searcher: BinarySearcher[int]) -> None:
    """Test a two-element list where the target is not present."""
    assert searcher.search([10, 20], 15) is None


def test_search_with_negative_numbers(searcher: BinarySearcher[int]) -> None:
    """Test searching in a list containing negative numbers."""
    assert searcher.search([-5, -2, 0, 3, 7], -2) == 1
    assert searcher.search([-10, -5, 0, 5, 10], 2) is None


def test_search_with_floats(searcher: BinarySearcher[float]) -> None:
    """Test searching in a list of floating-point numbers."""
    searcher_float = BinarySearcher[float]()
    assert searcher_float.search([1.1, 2.2, 3.3, 4.4, 5.5], 3.3) == 2
    assert searcher_float.search([1.1, 2.2, 3.3, 4.4], 3.35) is None


def test_search_in_large_list(searcher: BinarySearcher[int]) -> None:
    """Test searching in a large list."""
    large_list = list(range(10_000))
    assert searcher.search(large_list, 7777) == 7777
    assert searcher.search(large_list, 10000) is None
