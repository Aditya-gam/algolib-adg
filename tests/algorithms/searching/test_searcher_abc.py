"""Tests for the Searcher abstract base class."""

from typing import Sequence

import pytest

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
