"""Tests for searching base classes."""

from typing import Sequence

import pytest

from algolib.algorithms.searching.base import Searcher


class MockSearcher(Searcher[int]):
    """Mock searcher for testing base class functionality."""

    def search(self, data: Sequence[int], item: int) -> int | None:
        """Mock search implementation."""
        try:
            return data.index(item)
        except ValueError:
            return None


class TestSearcherBase:
    """Test the Searcher base class."""

    def test_run_with_valid_tuple(self) -> None:
        """Test run method with valid tuple input."""
        searcher = MockSearcher()
        result = searcher.run(([1, 2, 3, 4, 5], 3))
        assert result == 2

    def test_run_with_invalid_input_type(self) -> None:
        """Test run method with invalid input type."""
        searcher = MockSearcher()
        with pytest.raises(TypeError, match="Expected a tuple \\(sequence, item\\) for searching."):
            searcher.run([1, 2, 3])  # Not a tuple

    def test_run_with_wrong_tuple_length(self) -> None:
        """Test run method with tuple of wrong length."""
        searcher = MockSearcher()
        with pytest.raises(TypeError, match="Expected a tuple \\(sequence, item\\) for searching."):
            searcher.run(([1, 2, 3],))  # Only one element

    def test_run_with_too_many_elements(self) -> None:
        """Test run method with tuple with too many elements."""
        searcher = MockSearcher()
        with pytest.raises(TypeError, match="Expected a tuple \\(sequence, item\\) for searching."):
            searcher.run(([1, 2, 3], 2, "extra"))  # Three elements

    def test_run_with_none_input(self) -> None:
        """Test run method with None input."""
        searcher = MockSearcher()
        with pytest.raises(TypeError, match="Expected a tuple \\(sequence, item\\) for searching."):
            searcher.run(None)

    def test_run_with_string_input(self) -> None:
        """Test run method with string input."""
        searcher = MockSearcher()
        with pytest.raises(TypeError, match="Expected a tuple \\(sequence, item\\) for searching."):
            searcher.run("not a tuple")

    def test_run_with_empty_tuple(self) -> None:
        """Test run method with empty tuple."""
        searcher = MockSearcher()
        with pytest.raises(TypeError, match="Expected a tuple \\(sequence, item\\) for searching."):
            searcher.run(())
