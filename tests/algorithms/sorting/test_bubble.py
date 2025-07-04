"""Tests for the bubble sort algorithm."""

from dataclasses import dataclass

import pytest

from algolib.algorithms.sorting.bubble import BubbleSorter


@dataclass
class _ComparableItem:
    key: int
    value: str

    def __lt__(self, other: "_ComparableItem") -> bool:
        return self.key < other.key


@pytest.fixture
def sorter() -> BubbleSorter[int]:
    """Fixture for a BubbleSorter instance with integers."""
    return BubbleSorter()


@pytest.fixture
def stability_sorter() -> BubbleSorter[_ComparableItem]:
    """Fixture for a BubbleSorter instance with a custom comparable object."""
    return BubbleSorter()


def test_sort_empty_list(sorter: BubbleSorter[int]) -> None:
    """Test sorting an empty list."""
    assert sorter.sort([]) == []


def test_sort_sorted_list(sorter: BubbleSorter[int]) -> None:
    """Test sorting a list that is already sorted."""
    data = [1, 2, 3, 4, 5]
    sorted_data = sorter.sort(data)
    assert sorted_data == [1, 2, 3, 4, 5]
    assert id(data) != id(sorted_data)  # Ensure a new list is returned


def test_sort_reverse_sorted_list(sorter: BubbleSorter[int]) -> None:
    """Test sorting a list that is sorted in reverse order."""
    data = [5, 4, 3, 2, 1]
    sorted_data = sorter.sort(data)
    assert sorted_data == [1, 2, 3, 4, 5]
    assert id(data) != id(sorted_data)


def test_sort_list_with_duplicates(sorter: BubbleSorter[int]) -> None:
    """Test sorting a list with duplicate elements."""
    data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    sorted_data = sorter.sort(data)
    assert sorted_data == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
    assert id(data) != id(sorted_data)


def test_sort_single_element_list(sorter: BubbleSorter[int]) -> None:
    """Test sorting a list with a single element."""
    data = [42]
    sorted_data = sorter.sort(data)
    assert sorted_data == [42]
    assert id(data) != id(sorted_data)


def test_bubble_sort_is_stable(stability_sorter: BubbleSorter[_ComparableItem]) -> None:
    """Test that the bubble sort implementation is stable."""
    item1 = _ComparableItem(key=2, value="a")
    item2 = _ComparableItem(key=1, value="b")
    item3 = _ComparableItem(key=2, value="c")

    data = [item1, item2, item3]
    sorted_data = stability_sorter.sort(data)

    assert sorted_data[0].key == 1
    assert sorted_data[1].key == 2
    assert sorted_data[2].key == 2

    # Check that item1 ('a') comes before item3 ('c')
    assert sorted_data[1].value == "a"
    assert sorted_data[2].value == "c"
    assert id(data) != id(sorted_data)


def test_sort_two_elements_sorted(sorter: BubbleSorter[int]) -> None:
    """Test sorting a two-element list that is already sorted."""
    data = [10, 20]
    sorted_data = sorter.sort(data)
    assert sorted_data == [10, 20]
    assert id(data) != id(sorted_data)


def test_sort_two_elements_unsorted(sorter: BubbleSorter[int]) -> None:
    """Test sorting a two-element list that is unsorted."""
    data = [20, 10]
    sorted_data = sorter.sort(data)
    assert sorted_data == [10, 20]
    assert id(data) != id(sorted_data)


def test_sort_all_elements_the_same(sorter: BubbleSorter[int]) -> None:
    """Test sorting a list where all elements are the same."""
    data = [5, 5, 5, 5, 5]
    sorted_data = sorter.sort(data)
    assert sorted_data == [5, 5, 5, 5, 5]
    assert id(data) != id(sorted_data)


def test_sort_with_negative_numbers(sorter: BubbleSorter[int]) -> None:
    """Test sorting a list containing negative numbers."""
    data = [-5, 3, -1, 0, -8, 5]
    sorted_data = sorter.sort(data)
    assert sorted_data == [-8, -5, -1, 0, 3, 5]
    assert id(data) != id(sorted_data)


def test_sort_with_floats(sorter: BubbleSorter[float]) -> None:
    """Test sorting a list of floating-point numbers."""
    sorter_float = BubbleSorter[float]()
    data = [3.3, 1.1, 4.4, 2.2]
    sorted_data = sorter_float.sort(data)
    assert sorted_data == [1.1, 2.2, 3.3, 4.4]
    assert id(data) != id(sorted_data)


def test_sort_mixed_positive_and_negative(sorter: BubbleSorter[int]) -> None:
    """Test sorting a list with mixed positive and negative numbers."""
    data = [4, -2, -8, 0, 5, -1]
    sorted_data = sorter.sort(data)
    assert sorted_data == [-8, -2, -1, 0, 4, 5]
    assert id(data) != id(sorted_data)


def test_sort_strings(sorter: BubbleSorter[str]) -> None:
    """Test sorting a list of strings."""
    sorter_str = BubbleSorter[str]()
    data = ["cherry", "apple", "banana"]
    sorted_data = sorter_str.sort(data)
    assert sorted_data == ["apple", "banana", "cherry"]
    assert id(data) != id(sorted_data)


def test_early_exit_optimization(sorter: BubbleSorter[int]) -> None:
    """Test that the early-exit optimization works for a nearly sorted list."""
    data = [1, 2, 4, 3, 5]
    sorted_data = sorter.sort(data)
    assert sorted_data == [1, 2, 3, 4, 5]
    assert id(data) != id(sorted_data)


def test_sort_list_with_zero(sorter: BubbleSorter[int]) -> None:
    """Test sorting a list that includes zero."""
    data = [5, -2, 0, -5, 2]
    sorted_data = sorter.sort(data)
    assert sorted_data == [-5, -2, 0, 2, 5]
    assert id(data) != id(sorted_data)
