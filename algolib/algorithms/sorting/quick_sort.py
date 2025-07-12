"""Quick sort implementation based on the divide-and-conquer paradigm."""

from dataclasses import dataclass
from typing import MutableSequence

from algolib._typing import ComparableT

from .divide_conquer_sorter import DivideConquerSorter


@dataclass(slots=True, init=False)
class QuickSort(DivideConquerSorter[ComparableT]):
    """In-place, unstable quick-sort algorithm.

    Average O(n log n) time, worst-case O(n²), and O(log n) auxiliary space.
    """

    def _divide_and_conquer(
        self, data: MutableSequence[ComparableT], left: int, right: int
    ) -> None:
        if left < right:
            pivot_index = self._partition(data, left, right)
            self._divide_and_conquer(data, left, pivot_index - 1)
            self._divide_and_conquer(data, pivot_index + 1, right)

    def _partition(self, data: MutableSequence[ComparableT], left: int, right: int) -> int:
        pivot = data[right]
        i = left - 1

        for j in range(left, right):
            if self._compare(data[j], pivot):
                i += 1
                data[i], data[j] = data[j], data[i]

        data[i + 1], data[right] = data[right], data[i + 1]
        return i + 1
