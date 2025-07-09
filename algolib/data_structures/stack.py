from dataclasses import dataclass, field
from typing import Generic, List

from algolib._typing import T


@dataclass(slots=True)
class Stack(Generic[T]):
    """A LIFO (Last-In, First-Out) stack."""

    _container: List[T] = field(default_factory=list, init=False, repr=False)

    def push(self, item: T) -> None:
        """Adds an item to the top of the stack."""
        self._container.append(item)

    def pop(self) -> T:
        """Removes and returns the item at the top of the stack."""
        if self.is_empty():
            raise IndexError("pop from an empty stack")
        return self._container.pop()

    def peek(self) -> T:
        """Returns the item at the top of the stack without removing it."""
        if self.is_empty():
            raise IndexError("peek from an empty stack")
        return self._container[-1]

    def is_empty(self) -> bool:
        """Returns True if the stack is empty, False otherwise."""
        return len(self._container) == 0

    def __len__(self) -> int:
        """Returns the number of items in the stack."""
        return len(self._container)

    def __repr__(self) -> str:
        """Returns a string representation of the stack."""
        return f"Stack({self._container})"
