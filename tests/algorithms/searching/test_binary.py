"""Tests for binary search algorithm."""

import unittest
from typing import Sequence

import pytest
from hypothesis import given
from hypothesis import strategies as st

from algolib._typing import ComparableT
from algolib.algorithms.searching.base import Searcher
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


def test_search_unsorted_list_raises_value_error(
    searcher: BinarySearcher[int],
) -> None:
    """Test that searching in an unsorted list raises a ValueError."""
    with pytest.raises(ValueError, match="Input data must be sorted for binary search."):
        searcher.search([1, 3, 2, 4], 2)


class MockSearcher(Searcher[ComparableT]):
    def search(self, data: Sequence[ComparableT], target: ComparableT) -> int | None:
        try:
            return list(data).index(target)
        except ValueError:
            return None


class TestSearcherABC(unittest.TestCase):
    def test_searcher_abc_enforcement(self) -> None:
        """Test that Searcher cannot be instantiated without implementing search."""
        with pytest.raises(TypeError, match="Can't instantiate abstract class"):

            class IncompleteSearcher(Searcher[int]):
                pass

            IncompleteSearcher()  # type: ignore[abstract]

    def test_searcher_subclass_must_implement_search(self) -> None:
        """Ensure a concrete subclass of Searcher must implement the search method."""

        class CompleteSearcher(Searcher[int]):
            def search(self, data: Sequence[int], target: int) -> int | None:
                return 42

        instance = CompleteSearcher()
        assert instance.search([], 0) == 42

    def test_search(self) -> None:
        searcher: MockSearcher[int] = MockSearcher()
        self.assertEqual(searcher.search([1, 2, 3], 2), 1)
        self.assertIsNone(searcher.search([1, 2, 3], 4))

    def test_run(self) -> None:
        searcher: MockSearcher[int] = MockSearcher()
        self.assertEqual(searcher.run(([1, 2, 3], 2)), 1)
        self.assertIsNone(searcher.run(([1, 2, 3], 4)))

    def test_run_with_invalid_data_type(self) -> None:
        searcher: MockSearcher[int] = MockSearcher()
        with self.assertRaises(TypeError):
            searcher.run("not a tuple")
        with self.assertRaises(TypeError):
            searcher.run((1, 2, 3))


class DummySearcher(Searcher[int]):
    def search(self, data: Sequence[int], item: int) -> int | None:
        try:
            return list(data).index(item)
        except ValueError:
            return None


def test_searcher_run_calls_search() -> None:
    searcher = DummySearcher()
    data = ([1, 2, 3], 2)
    assert searcher.run(data) == 1
    data = ([1, 2, 3], 4)
    assert searcher.run(data) is None


def test_searcher_run_type_error() -> None:
    searcher = DummySearcher()
    with pytest.raises(TypeError):
        searcher.run([1, 2, 3])
    with pytest.raises(TypeError):
        searcher.run((1, 2, 3))
