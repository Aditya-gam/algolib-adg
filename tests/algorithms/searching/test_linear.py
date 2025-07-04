"""Tests for the linear search algorithm."""

from typing import Any, List

import pytest

from algolib.algorithms.searching.linear import LinearSearcher


class _ComparableNone:
    def __eq__(self, other: Any) -> bool:
        return isinstance(other, _ComparableNone)

    def __lt__(self, other: Any) -> bool:
        return False


@pytest.fixture()
def searcher() -> LinearSearcher[int]:
    """Fixture for a LinearSearcher instance."""
    return LinearSearcher()


def test_search_empty_list(searcher: LinearSearcher[int]) -> None:
    """Test searching in an empty list."""
    assert searcher.search([], 5) is None


def test_search_target_present(searcher: LinearSearcher[int]) -> None:
    """Test searching for a target that is present in the list."""
    assert searcher.search([1, 2, 3, 4, 5], 3) == 2


def test_search_target_not_present(searcher: LinearSearcher[int]) -> None:
    """Test searching for a target that is not present in the list."""
    assert searcher.search([1, 2, 3, 4, 5], 6) is None


def test_search_target_is_first_element(searcher: LinearSearcher[int]) -> None:
    """Test searching for a target that is the first element of the list."""
    assert searcher.search([1, 2, 3, 4, 5], 1) == 0


def test_search_target_is_last_element(searcher: LinearSearcher[int]) -> None:
    """Test searching for a target that is the last element of the list."""
    assert searcher.search([1, 2, 3, 4, 5], 5) == 4


def test_search_with_duplicates(searcher: LinearSearcher[int]) -> None:
    """Test searching in a list with duplicate elements."""
    assert searcher.search([1, 2, 3, 2, 1], 2) == 1


def test_search_with_non_integer_values(searcher: LinearSearcher[str]) -> None:
    """Test searching with non-integer values."""
    searcher_str = LinearSearcher[str]()
    assert searcher_str.search(["apple", "banana", "cherry"], "banana") == 1
    assert searcher_str.search(["apple", "banana", "cherry"], "durian") is None


def test_search_single_element_list_found(searcher: LinearSearcher[int]) -> None:
    """Test searching a single-element list where the target is present."""
    assert searcher.search([5], 5) == 0


def test_search_single_element_list_not_found(searcher: LinearSearcher[int]) -> None:
    """Test searching a single-element list where the target is not present."""
    assert searcher.search([5], 4) is None


def test_search_all_elements_are_the_same_found(searcher: LinearSearcher[int]) -> None:
    """Test searching in a list where all elements are the same as the target."""
    assert searcher.search([3, 3, 3, 3, 3], 3) == 0


def test_search_all_elements_are_the_same_not_found(
    searcher: LinearSearcher[int],
) -> None:
    """Test searching in a list of identical elements for a different target."""
    assert searcher.search([3, 3, 3, 3, 3], 5) is None


def test_search_with_floats(searcher: LinearSearcher[float]) -> None:
    """Test searching in a list of floating-point numbers."""
    searcher_float = LinearSearcher[float]()
    assert searcher_float.search([1.1, 2.2, 3.3, 4.4], 3.3) == 2
    assert searcher_float.search([1.1, 2.2, 3.3, 4.4], 3.35) is None


def test_search_for_none() -> None:
    """Test searching for None in a list that contains it."""
    searcher_none = LinearSearcher[_ComparableNone]()
    none_equivalent = _ComparableNone()
    search_list: List[Any] = [
        _ComparableNone(),
        _ComparableNone(),
        none_equivalent,
        _ComparableNone(),
    ]
    assert searcher_none.search(search_list, none_equivalent) == 2


def test_search_for_item_not_in_list_with_none() -> None:
    """Test searching for a target in a list that contains None but not the target."""
    searcher_none = LinearSearcher[_ComparableNone]()
    none_equivalent = _ComparableNone()
    search_list: List[Any] = [
        _ComparableNone(),
        _ComparableNone(),
        none_equivalent,
        _ComparableNone(),
    ]
    assert searcher_none.search(search_list, _ComparableNone()) is None


def test_search_in_large_list(searcher: LinearSearcher[int]) -> None:
    """Test searching in a large list."""
    large_list = list(range(10_000))
    assert searcher.search(large_list, 9999) == 9999
    assert searcher.search(large_list, 10000) is None
