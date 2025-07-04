"""Tests for the merge sort algorithm."""

from dataclasses import dataclass

import pytest

from algolib.algorithms.sorting.merge import MergeSorter


@dataclass
class _ComparableItem:
    key: int
    value: str

    def __lt__(self, other: "_ComparableItem") -> bool:
        return self.key < other.key

    def __le__(self, other: "_ComparableItem") -> bool:
        return self.key <= other.key


@pytest.fixture
def sorter() -> MergeSorter[int]:
    """Fixture for a MergeSorter instance with integers."""
    return MergeSorter()


@pytest.fixture
def stability_sorter() -> MergeSorter[_ComparableItem]:
    """Fixture for a MergeSorter instance with a custom comparable object."""
    return MergeSorter()


def test_sort_empty_list(sorter: MergeSorter[int]) -> None:
    """Test sorting an empty list."""
    assert sorter.sort([]) == []


def test_sort_sorted_list(sorter: MergeSorter[int]) -> None:
    """Test sorting a list that is already sorted."""
    data = [1, 2, 3, 4, 5]
    sorted_data = sorter.sort(data)
    assert sorted_data == [1, 2, 3, 4, 5]
    assert id(data) != id(sorted_data)


def test_sort_reverse_sorted_list(sorter: MergeSorter[int]) -> None:
    """Test sorting a list that is sorted in reverse order."""
    data = [5, 4, 3, 2, 1]
    sorted_data = sorter.sort(data)
    assert sorted_data == [1, 2, 3, 4, 5]
    assert id(data) != id(sorted_data)


def test_sort_list_with_duplicates(sorter: MergeSorter[int]) -> None:
    """Test sorting a list with duplicate elements."""
    data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    sorted_data = sorter.sort(data)
    assert sorted_data == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
    assert id(data) != id(sorted_data)


def test_sort_single_element_list(sorter: MergeSorter[int]) -> None:
    """Test sorting a list with a single element."""
    data = [42]
    sorted_data = sorter.sort(data)
    assert sorted_data == [42]
    assert id(data) != id(sorted_data)


def test_sort_odd_length_list(sorter: MergeSorter[int]) -> None:
    """Test sorting a list with an odd number of elements."""
    data = [3, 1, 4, 1, 5]
    sorted_data = sorter.sort(data)
    assert sorted_data == [1, 1, 3, 4, 5]
    assert id(data) != id(sorted_data)


def test_merge_sort_is_stable(stability_sorter: MergeSorter[_ComparableItem]) -> None:
    """Test that the merge sort implementation is stable."""
    item1 = _ComparableItem(key=2, value="a")
    item2 = _ComparableItem(key=1, value="b")
    item3 = _ComparableItem(key=2, value="c")

    data = [item1, item2, item3]
    sorted_data = stability_sorter.sort(data)

    assert sorted_data[0].key == 1
    assert sorted_data[1].key == 2
    assert sorted_data[2].key == 2

    # Check that item1 ('a') comes before item3 ('c') because of stability
    assert sorted_data[1].value == "a"
    assert sorted_data[2].value == "c"
    assert id(data) != id(sorted_data)


def test_sort_two_elements_sorted(sorter: MergeSorter[int]) -> None:
    """Test sorting a two-element list that is already sorted."""
    data = [10, 20]
    sorted_data = sorter.sort(data)
    assert sorted_data == [10, 20]
    assert id(data) != id(sorted_data)


def test_sort_two_elements_unsorted(sorter: MergeSorter[int]) -> None:
    """Test sorting a two-element list that is unsorted."""
    data = [20, 10]
    sorted_data = sorter.sort(data)
    assert sorted_data == [10, 20]
    assert id(data) != id(sorted_data)


def test_sort_all_elements_the_same(sorter: MergeSorter[int]) -> None:
    """Test sorting a list where all elements are the same."""
    data = [5, 5, 5, 5, 5]
    sorted_data = sorter.sort(data)
    assert sorted_data == [5, 5, 5, 5, 5]
    assert id(data) != id(sorted_data)


def test_sort_with_negative_numbers(sorter: MergeSorter[int]) -> None:
    """Test sorting a list containing negative numbers."""
    data = [-5, 3, -1, 0, -8, 5]
    sorted_data = sorter.sort(data)
    assert sorted_data == [-8, -5, -1, 0, 3, 5]
    assert id(data) != id(sorted_data)


def test_sort_with_floats(sorter: MergeSorter[float]) -> None:
    """Test sorting a list of floating-point numbers."""
    sorter_float = MergeSorter[float]()
    data = [3.3, 1.1, 4.4, 2.2]
    sorted_data = sorter_float.sort(data)
    assert sorted_data == [1.1, 2.2, 3.3, 4.4]
    assert id(data) != id(sorted_data)


def test_sort_strings(sorter: MergeSorter[str]) -> None:
    """Test sorting a list of strings."""
    sorter_str = MergeSorter[str]()
    data = ["cherry", "apple", "banana"]
    sorted_data = sorter_str.sort(data)
    assert sorted_data == ["apple", "banana", "cherry"]
    assert id(data) != id(sorted_data)


def test_sort_list_with_zero(sorter: MergeSorter[int]) -> None:
    """Test sorting a list that includes zero."""
    data = [5, -2, 0, -5, 2]
    sorted_data = sorter.sort(data)
    assert sorted_data == [-5, -2, 0, 2, 5]
    assert id(data) != id(sorted_data)


def test_sort_large_list(sorter: MergeSorter[int]) -> None:
    """Test sorting a large list."""
    large_list = list(range(1000, 0, -1))
    sorted_list = sorter.sort(large_list)
    assert sorted_list == list(range(1, 1001))
    assert id(large_list) != id(sorted_list)
