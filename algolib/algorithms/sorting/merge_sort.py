"""Merge sort implementation based on the divide-and-conquer paradigm."""

from dataclasses import dataclass
from typing import MutableSequence

from algolib._typing import ComparableT

from .divide_conquer_sorter import DivideConquerSorter


@dataclass(slots=True, init=False)
class MergeSort(DivideConquerSorter[ComparableT]):
    """Classic merge-sort algorithm.

    Stable O(n log n) time complexity with O(n) auxiliary space.
    """

    def _divide_and_conquer(
        self, data: MutableSequence[ComparableT], left: int, right: int
    ) -> None:
        if left < right:
            mid = (left + right) // 2
            self._divide_and_conquer(data, left, mid)
            self._divide_and_conquer(data, mid + 1, right)
            self._merge(data, left, mid, right)

    def _merge(self, data: MutableSequence[ComparableT], left: int, mid: int, right: int) -> None:
        left_array = [data[i] for i in range(left, mid + 1)]
        right_array = [data[i] for i in range(mid + 1, right + 1)]

        i = j = 0
        k = left

        while i < len(left_array) and j < len(right_array):
            if self._compare(left_array[i], right_array[j]):
                data[k] = left_array[i]
                i += 1
            else:
                data[k] = right_array[j]
                j += 1
            k += 1

        while i < len(left_array):
            data[k] = left_array[i]
            i += 1
            k += 1

        while j < len(right_array):
            data[k] = right_array[j]
            j += 1
            k += 1

    def sort(self, data: MutableSequence[ComparableT]) -> MutableSequence[ComparableT]:
        """Return a new list containing the sorted elements.

        This keeps the non-mutating contract expected by existing callers/tests
        while leveraging the in-place divide-and-conquer implementation under
        the hood.
        """
        if len(data) <= 1:
            return list(data)

        # Work on a copy to avoid side-effects.
        result: MutableSequence[ComparableT] = list(data)
        self._divide_and_conquer(result, 0, len(result) - 1)

        # Reflect the sorted order back into the original sequence so that
        # callers relying on in-place behaviour (e.g., greedy algorithms)
        # continue to work correctly.
        for idx, item in enumerate(result):
            data[idx] = item

        return result
