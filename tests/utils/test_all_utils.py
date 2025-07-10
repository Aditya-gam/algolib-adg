"""Tests for utility modules and helper functions."""

from typing import Any, cast

import pytest

from algolib._typing import SupportsLessThan
from tests.utils.helpers import is_sorted


def test_supports_less_than_protocol() -> None:
    """Test the SupportsLessThan protocol."""

    class LessThanComparable:
        def __lt__(self, other: "LessThanComparable") -> bool:
            return True

    class NotLessThanComparable:
        pass

    assert isinstance(LessThanComparable(), SupportsLessThan)

    with pytest.raises(TypeError):
        # Cast to Any to bypass mypy type checking for this intentional error test
        _ = cast(Any, NotLessThanComparable()) < cast(Any, NotLessThanComparable())


def test_is_sorted_helper() -> None:
    """Test the is_sorted helper function."""
    assert is_sorted([1, 2, 3, 4, 5])
    assert is_sorted([1, 1, 2, 2, 3])
    assert is_sorted([1])
    assert is_sorted([])

    assert not is_sorted([1, 3, 2, 4])
    assert not is_sorted([5, 4, 3, 2, 1])
    assert not is_sorted([1, 2, 3, 2, 4])


def test_is_sorted_with_negative_numbers() -> None:
    """Test is_sorted with negative numbers."""
    assert is_sorted([-5, -3, -1, 0, 2, 4])
    assert is_sorted([-10, -5, 0, 5, 10])
    assert not is_sorted([0, -1, 1, -2, 2])


def test_is_sorted_with_floats() -> None:
    """Test is_sorted with floating point numbers."""
    assert is_sorted([1.1, 1.2, 1.3, 1.4])
    assert is_sorted([0.0, 0.5, 1.0, 1.5])
    assert not is_sorted([1.0, 0.5, 1.5, 0.0])


def test_is_sorted_with_strings() -> None:
    """Test is_sorted with strings."""
    assert is_sorted(["a", "b", "c", "d"])
    assert is_sorted(["apple", "banana", "cherry"])
    assert not is_sorted(["c", "a", "b", "d"])
