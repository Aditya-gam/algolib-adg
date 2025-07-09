"""Abstract base classes for searching algorithms."""

from abc import ABC, abstractmethod
from typing import Any, Generic, Sequence, cast

from algolib._typing import ComparableT
from algolib.interfaces import Searcher as SearcherProtocol


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

    def run(self, data: Any) -> Any:
        """Runs the searching algorithm."""
        if not isinstance(data, tuple) or len(data) != 2:
            raise TypeError("Expected a tuple (sequence, target) for searching.")

        sequence, target = data
        if not isinstance(sequence, Sequence) or isinstance(sequence, str):
            raise TypeError("First element of the tuple must be a non-string sequence.")

        return self.search(cast(Sequence[ComparableT], sequence), cast(ComparableT, target))


# Type assertion to ensure Searcher conforms to the protocol
_searcher_protocol_check: type[SearcherProtocol] = cast(type[SearcherProtocol], Searcher)
