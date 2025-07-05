"""Bubble sort algorithm implementation."""

from typing import MutableSequence

from algolib._typing import ComparableT
from algolib.algorithms.sorting.base import Sorter


class BubbleSorter(Sorter[ComparableT]):
    """Bubble sort implementation.

    This is a simple, stable sorting algorithm that repeatedly steps through the list,
    compares adjacent elements and swaps them if they are in the wrong order.
    The pass through the list is repeated until the list is sorted.
    """

    def sort(self, data: MutableSequence[ComparableT]) -> MutableSequence[ComparableT]:
        """Sorts a mutable sequence using the bubble sort algorithm.

        This implementation includes an optimization to exit early if the list becomes
        sorted before all passes are complete. It creates a new list to avoid
        modifying the original data.

        Args:
            data: The sequence to sort.

        Returns:
            A new list containing the sorted elements.
        """
        if not data:
            return []

        result = list(data)
        n = len(result)
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                if result[j] > result[j + 1]:
                    result[j], result[j + 1] = result[j + 1], result[j]
                    swapped = True
            if not swapped:
                break
        return result
