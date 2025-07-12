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
            try:
                return a <= b
            except (RecursionError, TypeError):
                # Fallback to hash-based comparison for problematic objects
                try:
                    return hash(a) <= hash(b)
                except (TypeError, RecursionError):
                    # Final fallback: use object address
                    return str(a) <= str(b)
        key_a = self._key_func(a)
        key_b = self._key_func(b)
        try:
            return key_a <= key_b  # type: ignore[no-any-return]
        except (RecursionError, TypeError):
            # Fallback to hash-based comparison for problematic objects
            try:
                return hash(key_a) <= hash(key_b)
            except (TypeError, RecursionError):
                # Final fallback: use string representation
                return str(key_a) <= str(key_b)
