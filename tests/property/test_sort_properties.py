# ruff: noqa: D100,D101,D102,D103,D104,D105,D107
import collections
from typing import List, Type

import pytest
from hypothesis import given
from hypothesis import strategies as st

from algolib.algorithms.sorting.base import Sorter
from algolib.algorithms.sorting.bubble import BubbleSorter
from algolib.algorithms.sorting.merge import MergeSorter
from tests.property.strategies import random_int_list

# List of all Sorter implementations to be tested
ALL_SORTERS: List[Type[Sorter[int]]] = [BubbleSorter, MergeSorter]


def is_sorted(data: List[int]) -> bool:
    """Checks if a list is sorted in non-decreasing order."""
    return all(data[i] <= data[i + 1] for i in range(len(data) - 1))


@pytest.mark.property
@pytest.mark.parametrize("sorter_class", ALL_SORTERS)
@given(data=random_int_list)
def test_sort_properties(sorter_class: Type[Sorter[int]], data: List[int]) -> None:
    """
    Tests two properties of sorting algorithms:
    1. Idempotency: Applying the sort twice has the same result as applying it once.
    2. Correctness: The output is sorted and is a permutation of the input.
    """
    sorter = sorter_class()

    # Property 1: The output is sorted
    sorted_data = sorter.sort(data.copy())
    assert is_sorted(list(sorted_data))

    # Property 2: The output is a permutation of the input
    assert collections.Counter(data) == collections.Counter(sorted_data)


@pytest.mark.property
@pytest.mark.parametrize("sorter_class", ALL_SORTERS)
@given(data=st.lists(st.integers(), min_size=1, max_size=100))
def test_idempotency(sorter_class: Type[Sorter[int]], data: List[int]) -> None:
    """Tests that sorting an already sorted list does not change it."""
    sorter = sorter_class()

    # First sort
    sorted_once = sorter.sort(data.copy())
    assert is_sorted(list(sorted_once))

    # Sorting again should not change the list
    sorted_twice = sorter.sort(sorted_once[:])
    assert sorted_once == sorted_twice
