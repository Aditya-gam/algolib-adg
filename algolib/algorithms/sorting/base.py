"""Abstract base classes for sorting algorithms."""

from abc import ABC, abstractmethod
from typing import Any, MutableSequence, cast

from algolib._typing import T
from algolib.interfaces import Sorter as SorterProtocol


class Sorter(SorterProtocol[T], ABC):
    """Abstract base class for sorting algorithms."""

    @abstractmethod
    def sort(self, data: MutableSequence[T]) -> MutableSequence[T]:
        """Sorts a mutable sequence in place.

        Args:
            data: The mutable sequence to be sorted.

        Returns:
            The sorted mutable sequence.
        """
        ...

    def run(self, data: Any) -> Any:
        """Run the sorting algorithm."""
        return self.sort(cast(MutableSequence[T], data))
