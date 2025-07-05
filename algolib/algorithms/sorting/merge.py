"""Merge sort algorithm implementation."""

from typing import List, MutableSequence

from algolib._typing import ComparableT
from algolib.algorithms.sorting.base import Sorter


class MergeSorter(Sorter[ComparableT]):
    """Merge sort implementation.

    This is a stable, comparison-based sorting algorithm that uses a divide and
    conquer strategy. It divides the list into two halves, recursively sorts them,
    and then merges the sorted halves.
    """

    def sort(self, data: MutableSequence[ComparableT]) -> MutableSequence[ComparableT]:
        """Sorts a mutable sequence using the merge sort algorithm.

        This implementation is recursive and creates new lists for the sorted output,
        leaving the original data unmodified.

        Args:
            data: The sequence to sort.

        Returns:
            A new list containing the sorted elements.
        """
        if len(data) <= 1:
            return list(data)

        mid = len(data) // 2
        left_half = self.sort(data[:mid])
        right_half = self.sort(data[mid:])

        return self._merge(left_half, right_half)

    def _merge(
        self, left: MutableSequence[ComparableT], right: MutableSequence[ComparableT]
    ) -> List[ComparableT]:
        """Merges two sorted sequences into a single sorted list.

        Args:
            left: The left sorted sequence.
            right: The right sorted sequence.

        Returns:
            A new sorted list containing all elements from left and right.
        """
        result: List[ComparableT] = []
        i = j = 0

        while i < len(left) and j < len(right):
            if not right[j] < left[i]:  # noqa: SIM103
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])
        return result
