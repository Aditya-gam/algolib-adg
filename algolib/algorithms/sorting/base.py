"""Abstract base classes for sorting algorithms."""

from abc import ABC, abstractmethod
from typing import Generic, MutableSequence

from algolib._typing import ComparableT


class Sorter(Generic[ComparableT], ABC):
    """Abstract base class for sorting algorithms."""

    @abstractmethod
    def sort(self, data: MutableSequence[ComparableT]) -> MutableSequence[ComparableT]:
        """Sorts a mutable sequence in place.

        Args:
            data: The mutable sequence to be sorted.

        Returns:
            The sorted mutable sequence.
        """
        ...
