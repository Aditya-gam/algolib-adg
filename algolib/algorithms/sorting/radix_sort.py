"""Radix sort algorithm for non-negative integers."""

from dataclasses import dataclass
from typing import MutableSequence

from algolib.algorithms.sorting.base import Sorter


@dataclass(slots=True, init=False)
class RadixSort(Sorter[int]):
    """Stable, digit-by-digit radix sort."""

    _base: int

    def __init__(self, base: int = 10) -> None:
        if base < 2:
            raise ValueError("Base must be at least 2")
        self._base = base

    def sort(self, data: MutableSequence[int]) -> MutableSequence[int]:
        if not data:
            return data

        for item in data:
            if item < 0:
                raise ValueError("RadixSort only supports non-negative integers")

        max_val = max(data)
        exp = 1
        while max_val // exp > 0:
            self._counting_sort_by_digit(data, exp)
            exp *= self._base

        return data

    def _counting_sort_by_digit(self, data: MutableSequence[int], exp: int) -> None:
        n = len(data)
        output = [0] * n
        count = [0] * self._base

        for item in data:
            digit = (item // exp) % self._base
            count[digit] += 1

        for i in range(1, self._base):
            count[i] += count[i - 1]

        for i in range(n - 1, -1, -1):
            digit = (data[i] // exp) % self._base
            output[count[digit] - 1] = data[i]
            count[digit] -= 1

        for i in range(n):
            data[i] = output[i]
