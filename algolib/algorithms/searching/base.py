"""Abstract base classes for searching algorithms."""

from abc import ABC, abstractmethod
from typing import Any, Sequence

from algolib._typing import T
from algolib.interfaces import Searcher as SearcherProtocol


class Searcher(SearcherProtocol[T], ABC):
    """Abstract base class for searching algorithms."""

    @abstractmethod
    def search(self, data: Sequence[T], item: T) -> int | None:
        """Searches for an item in a sequence.

        Args:
            data: The sequence to be searched.
            item: The item to search for.

        Returns:
            The index of the item if found, otherwise None.
        """
        ...

    def run(self, data: Any) -> Any:
        """Run the searching algorithm."""
        if not isinstance(data, tuple) or len(data) != 2:
            raise TypeError("Expected a tuple (sequence, item) for searching.")
        sequence, item = data
        return self.search(sequence, item)
