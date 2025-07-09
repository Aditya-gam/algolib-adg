from dataclasses import dataclass, field
from typing import Generic, Iterator, Optional

from algolib._typing import T


@dataclass(slots=True)
class _Node(Generic[T]):
    data: T
    next: Optional["_Node[T]"] = field(default=None, repr=False)


@dataclass(slots=True, init=False)
class LinkedList(Generic[T]):
    """A singly linked list."""

    _head: Optional[_Node[T]]
    _tail: Optional[_Node[T]]
    _size: int

    def __init__(self) -> None:
        self._head = None
        self._tail = None
        self._size = 0

    def append(self, item: T) -> None:
        """Adds an item to the end of the list."""
        new_node = _Node(item)
        if self._tail is None:
            self._head = self._tail = new_node
        else:
            self._tail.next = new_node
            self._tail = new_node
        self._size += 1

    def prepend(self, item: T) -> None:
        """Adds an item to the beginning of the list."""
        new_node = _Node(item)
        if self._head is None:
            self._head = self._tail = new_node
        else:
            new_node.next = self._head
            self._head = new_node
        self._size += 1

    def is_empty(self) -> bool:
        """Returns True if the list is empty, False otherwise."""
        return self._head is None

    def __iter__(self) -> Iterator[T]:
        """Returns an iterator for the list."""
        current = self._head
        while current:
            yield current.data
            current = current.next

    def __len__(self) -> int:
        """Returns the number of items in the list."""
        return self._size

    def __str__(self) -> str:
        if self.is_empty():
            return "LinkedList()"
        return f"LinkedList({' -> '.join(map(str, self))})"
