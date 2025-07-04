"""Test helper utilities."""

from typing import Sequence

from algolib._typing import ComparableT


def is_sorted(data: Sequence[ComparableT]) -> bool:
    """
    Checks if a sequence is sorted in non-decreasing order.

    Args:
        data: The sequence to check.

    Returns:
        True if the sequence is sorted, False otherwise.
    """
    return all(not (data[i + 1] < data[i]) for i in range(len(data) - 1))
