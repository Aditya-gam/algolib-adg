"""Abstract base classes for sorting algorithms."""

from abc import ABC, abstractmethod
from typing import Any, Generic, MutableSequence, cast

from algolib._typing import ComparableT
from algolib.interfaces import Sorter as SorterProtocol


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

    def run(self, data: Any) -> Any:
        """Run the sorting algorithm."""
        return self.sort(cast(MutableSequence[ComparableT], data))


# Type assertion to ensure Sorter conforms to the protocol
_sorter_protocol_check: type[SorterProtocol] = cast(type[SorterProtocol], Sorter)
