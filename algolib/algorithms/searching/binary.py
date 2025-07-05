"""Binary search algorithm implementation."""

from typing import Sequence

from algolib._typing import ComparableT
from algolib.algorithms.searching.base import Searcher


class BinarySearcher(Searcher[ComparableT]):
    """Binary search implementation.

    This algorithm finds the position of a target value within a sorted array.
    It works by repeatedly dividing the search interval in half.
    """

    def search(self, data: Sequence[ComparableT], target: ComparableT) -> int | None:
        """Performs an iterative binary search for a target in a sorted sequence.

        Args:
            data: The sorted sequence to search in.
            target: The value to search for.

        Returns:
            The index of the target, or None if not found.
        """
        low = 0
        high = len(data) - 1

        while low <= high:
            mid = (low + high) // 2
            mid_val = data[mid]

            if mid_val < target:
                low = mid + 1
            elif mid_val > target:
                high = mid - 1
            else:
                return mid

        return None
