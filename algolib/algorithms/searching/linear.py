"""Linear search algorithm implementation."""

from typing import Sequence

from algolib._typing import ComparableT
from algolib.algorithms.searching.base import Searcher


class LinearSearcher(Searcher[ComparableT]):
    """Linear search implementation.

    This algorithm iterates through the sequence to find the target.
    """

    def search(self, data: Sequence[ComparableT], target: ComparableT) -> int | None:
        """Performs a linear search for a target value in a sequence.

        Args:
            data: The sequence to search in.
            target: The value to search for.

        Returns:
            The index of the first occurrence of the target, or None if not found.
        """
        for i, item in enumerate(data):
            if item == target:
                return i
        return None
