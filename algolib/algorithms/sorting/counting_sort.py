"""Counting sort algorithm for integer arrays."""

from dataclasses import dataclass
from typing import MutableSequence

from algolib.algorithms.sorting.base import Sorter


@dataclass(slots=True, init=False)
class CountingSort(Sorter[int]):
    """Stable, linear-time counting sort (range dependent)."""

    _min_val: int
    _max_val: int

    def __init__(self, min_val: int = 0, max_val: int = 100) -> None:
        if min_val > max_val:
            raise ValueError("min_val must be <= max_val")
        self._min_val = min_val
        self._max_val = max_val

    def sort(self, data: MutableSequence[int]) -> MutableSequence[int]:
        if not data:
            return data

        for item in data:
            if item < self._min_val or item > self._max_val:
                raise ValueError(
                    f"Element {item} is outside range [{self._min_val}, {self._max_val}]"
                )

        range_size = self._max_val - self._min_val + 1
        count = [0] * range_size

        for item in data:
            count[item - self._min_val] += 1

        for i in range(1, range_size):
            count[i] += count[i - 1]

        sorted_data = [0] * len(data)
        for i in range(len(data) - 1, -1, -1):
            item = data[i]
            sorted_data[count[item - self._min_val] - 1] = item
            count[item - self._min_val] -= 1

        for i, item in enumerate(sorted_data):
            data[i] = item

        return data
