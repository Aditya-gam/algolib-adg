"""Tests for the Searcher abstract base class."""

import unittest
from typing import Sequence

import pytest

from algolib._typing import ComparableT
from algolib.algorithms.searching.base import Searcher


def test_searcher_abc_enforcement() -> None:
    """Test that Searcher cannot be instantiated without implementing search."""
    with pytest.raises(TypeError, match="Can't instantiate abstract class"):

        class IncompleteSearcher(Searcher[int]):
            pass

        IncompleteSearcher()  # type: ignore[abstract]


def test_searcher_subclass_must_implement_search() -> None:
    """Ensure a concrete subclass of Searcher must implement the search method."""

    class CompleteSearcher(Searcher[int]):
        def search(self, data: Sequence[int], target: int) -> int | None:
            return 42

    instance = CompleteSearcher()
    assert instance.search([], 0) == 42


class MockSearcher(Searcher[ComparableT]):
    def search(self, data: Sequence[ComparableT], target: ComparableT) -> int | None:
        try:
            return list(data).index(target)
        except ValueError:
            return None


class TestSearcherABC(unittest.TestCase):
    def test_run_method(self) -> None:
        searcher: MockSearcher[int] = MockSearcher()
        data = [3, 1, 4, 1, 5, 9, 2, 6]
        self.assertEqual(searcher.run((data, 5)), 4)
        self.assertIsNone(searcher.run((data, 7)))

    def test_run_with_invalid_data_type(self) -> None:
        searcher: MockSearcher[int] = MockSearcher()
        with self.assertRaises(TypeError):
            searcher.run("not a tuple")
        with self.assertRaises(TypeError):
            searcher.run((1, 2, 3))
        with self.assertRaises(TypeError):
            searcher.run(("not a sequence", 2))
