from collections import deque
from typing import Deque, Generic

from algolib._typing import T


class Queue(Generic[T]):
    """A FIFO (First-In, First-Out) queue."""

    def __init__(self) -> None:
        self._container: Deque[T] = deque()

    def enqueue(self, item: T) -> None:
        """Adds an item to the end of the queue."""
        self._container.append(item)

    def dequeue(self) -> T:
        """Removes and returns the item at the front of the queue."""
        if self.is_empty():
            raise IndexError("dequeue from an empty queue")
        return self._container.popleft()

    def peek(self) -> T:
        """Returns the item at the front of the queue without removing it."""
        if self.is_empty():
            raise IndexError("peek from an empty queue")
        return self._container[0]

    def is_empty(self) -> bool:
        """Returns True if the queue is empty, False otherwise."""
        return len(self._container) == 0

    def __len__(self) -> int:
        """Returns the number of items in the queue."""
        return len(self._container)

    def __repr__(self) -> str:
        """Returns a string representation of the queue."""
        return f"Queue({list(self._container)})"
