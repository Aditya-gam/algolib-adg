"""Heap sort implementation using a max-heap."""

from dataclasses import dataclass
from typing import Any, Callable, List, MutableSequence, Optional

from algolib._typing import T
from algolib.algorithms.sorting.base import Sorter
from algolib.data_structures.heap import MaxHeap


@dataclass(slots=True, init=False)
class HeapSort(Sorter[T]):
    """In-place O(n log n) heap-sort algorithm."""

    _key_func: Optional[Callable[[T], Any]]

    def __init__(self, key: Optional[Callable[[T], Any]] = None) -> None:
        self._key_func = key

    def sort(self, data: MutableSequence[T]) -> MutableSequence[T]:
        if len(data) <= 1:
            return data

        heap = MaxHeap(key=self._key_func)
        heap.build_heap(list(data))

        sorted_data: List[T] = []
        while not heap.is_empty():
            sorted_data.append(heap.extract_max())

        sorted_data.reverse()

        for i, item in enumerate(sorted_data):
            data[i] = item

        return data
