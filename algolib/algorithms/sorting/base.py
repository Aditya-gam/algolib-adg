"""Abstract base classes for sorting algorithms."""

from abc import ABC, abstractmethod
from typing import Generic, MutableSequence

from algolib._typing import ComparableT


class Sorter(Generic[ComparableT], ABC):
    """Abstract base class for sorting algorithms."""

    @abstractmethod
    def sort(self, data: MutableSequence[ComparableT]) -> MutableSequence[ComparableT]:
        """
        Sorts a mutable sequence.

        Args:
            data (MutableSequence[ComparableT]): The sequence to sort.

        Returns:
            MutableSequence[ComparableT]: A new sequence containing the sorted elements.
        """
        ...
