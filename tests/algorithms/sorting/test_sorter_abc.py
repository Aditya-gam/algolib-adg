"""Tests for the Sorter abstract base class."""

import unittest
from typing import MutableSequence

import pytest

from algolib._typing import ComparableT
from algolib.algorithms.sorting.base import Sorter


def test_sorter_abc_enforcement() -> None:
    """Test that Sorter cannot be instantiated without implementing sort."""
    with pytest.raises(TypeError, match="Can't instantiate abstract class"):

        class IncompleteSorter(Sorter[int]):
            pass

        IncompleteSorter()  # type: ignore[abstract]


def test_sorter_subclass_must_implement_sort() -> None:
    """Ensure a concrete subclass of Sorter must implement the sort method."""

    class CompleteSorter(Sorter[int]):
        def sort(self, data: MutableSequence[int]) -> MutableSequence[int]:
            return sorted(data)

    instance = CompleteSorter()
    assert instance.sort([3, 1, 2]) == [1, 2, 3]


class MockSorter(Sorter[ComparableT]):
    def sort(self, data: MutableSequence[ComparableT]) -> MutableSequence[ComparableT]:
        return sorted(data)


class TestSorterABC(unittest.TestCase):
    def test_run_method(self) -> None:
        sorter: MockSorter[int] = MockSorter()
        data = [3, 1, 4, 1, 5, 9, 2, 6]
        self.assertEqual(sorter.run(data), sorted(data))
