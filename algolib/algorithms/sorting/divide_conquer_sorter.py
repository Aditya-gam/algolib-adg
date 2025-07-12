"""Abstract base class for divide-and-conquer sorting algorithms."""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, Callable, MutableSequence, Optional

from algolib._typing import ComparableT
from algolib.algorithms.sorting.base import Sorter


@dataclass(slots=True, init=False)
class DivideConquerSorter(Sorter[ComparableT], ABC):
    """Abstract base class implementing the Template Method skeleton for
    divide-and-conquer sorting algorithms."""

    _key_func: Optional[Callable[[ComparableT], Any]]

    def __init__(self, key: Optional[Callable[[ComparableT], Any]] = None) -> None:
        self._key_func = key

    def sort(self, data: MutableSequence[ComparableT]) -> MutableSequence[ComparableT]:
        if len(data) <= 1:
            return data
        self._divide_and_conquer(data, 0, len(data) - 1)
        return data

    @abstractmethod
    def _divide_and_conquer(
        self, data: MutableSequence[ComparableT], left: int, right: int
    ) -> None:  # pragma: no cover
        ...

    def _compare(self, a: ComparableT, b: ComparableT) -> bool:
        if self._key_func is None:
            return a <= b
        key_a = self._key_func(a)
        key_b = self._key_func(b)
        return key_a <= key_b  # type: ignore[no-any-return]
