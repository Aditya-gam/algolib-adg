"""Queue data structure implementation."""

from collections import deque
from dataclasses import dataclass, field
from typing import Deque, Generic, TypeVar

T = TypeVar("T")


@dataclass(slots=True)
class Queue(Generic[T]):
    """Queue data structure - FIFO (First-In-First-Out) container.

    A queue is a linear data structure that follows the First-In-First-Out (FIFO) principle.
    Elements are added at the rear (enqueue) and removed from the front (dequeue).

    Time Complexities:
        - enqueue: O(1) - constant time insertion at rear
        - dequeue: O(1) - constant time removal from front
        - peek: O(1) - constant time access to front element
        - is_empty: O(1) - constant time check
        - size: O(1) - constant time size query

    Space Complexity: O(n) - where n is the number of elements in the queue

    Common use cases:
        - Process scheduling in operating systems
        - Breadth-first search (BFS) traversal
        - Handling requests in web servers
        - Print queue management
        - Buffer for data streams

    Example:
        >>> queue = Queue[int]()
        >>> queue.enqueue(1)
        >>> queue.enqueue(2)
        >>> queue.enqueue(3)
        >>> print(queue.peek())    # Output: 1
        >>> print(queue.dequeue()) # Output: 1
        >>> print(queue.size())    # Output: 2
    """

    _container: Deque[T] = field(default_factory=deque, init=False, repr=False)

    def enqueue(self, item: T) -> None:
        """Add an item to the rear of the queue.

        Args:
            item: The item to add to the queue

        Example:
            >>> queue = Queue[str]()
            >>> queue.enqueue("first")
            >>> queue.enqueue("second")
            >>> print(queue.size())  # Output: 2
        """
        self._container.append(item)

    def dequeue(self) -> T:
        """Remove and return the item at the front of the queue.

        Returns:
            The item that was at the front of the queue

        Raises:
            IndexError: If the queue is empty

        Example:
            >>> queue = Queue[int]()
            >>> queue.enqueue(42)
            >>> item = queue.dequeue()
            >>> print(item)  # Output: 42
        """
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._container.popleft()

    def peek(self) -> T:
        """Return the item at the front of the queue without removing it.

        Returns:
            The item at the front of the queue

        Raises:
            IndexError: If the queue is empty

        Example:
            >>> queue = Queue[str]()
            >>> queue.enqueue("hello")
            >>> front = queue.peek()
            >>> print(front)  # Output: "hello"
            >>> print(queue.size())  # Output: 1 (item still in queue)
        """
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self._container[0]

    def is_empty(self) -> bool:
        """Check if the queue is empty.

        Returns:
            True if the queue contains no elements, False otherwise

        Example:
            >>> queue = Queue[int]()
            >>> print(queue.is_empty())  # Output: True
            >>> queue.enqueue(1)
            >>> print(queue.is_empty())  # Output: False
        """
        return len(self._container) == 0

    def size(self) -> int:
        """Return the number of items in the queue.

        Returns:
            The number of elements currently in the queue

        Example:
            >>> queue = Queue[int]()
            >>> print(queue.size())  # Output: 0
            >>> queue.enqueue(1)
            >>> queue.enqueue(2)
            >>> print(queue.size())  # Output: 2
        """
        return len(self._container)

    def __len__(self) -> int:
        """Return the number of items in the queue (supports len() function)."""
        return len(self._container)

    def __repr__(self) -> str:
        """Return string representation of the Queue instance."""
        return f"{self.__class__.__name__}()"

    def __str__(self) -> str:
        """Return string representation of the Queue contents."""
        return str(list(self._container))
