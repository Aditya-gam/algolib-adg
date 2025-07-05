"""Abstract base classes for searching algorithms."""

from abc import ABC, abstractmethod
from typing import Generic, Sequence

from algolib._typing import ComparableT


class Searcher(Generic[ComparableT], ABC):
    """Abstract base class for searching algorithms."""

    @abstractmethod
    def search(self, data: Sequence[ComparableT], target: ComparableT) -> int | None:
        """Searches for a target value within a sequence.

        Args:
            data: The sequence to search in.
            target: The value to search for.

        Returns:
            The index of the target if found, otherwise None.
        """
        ...
