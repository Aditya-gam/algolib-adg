"""Linked List data structure implementation."""

from dataclasses import dataclass, field
from typing import Generic, Iterator, Optional, TypeVar

T = TypeVar("T")


@dataclass(slots=True)
class _Node(Generic[T]):
    """Internal node class for the linked list."""

    data: T
    next: Optional["_Node[T]"] = field(default=None, repr=False)


@dataclass(slots=True, init=False)
class LinkedList(Generic[T]):
    """Singly linked list data structure.

    A linked list is a linear data structure where elements are stored in nodes,
    and each node contains data and a reference to the next node in the sequence.

    Time Complexities:
        - append: O(1) - constant time insertion at end (with tail reference)
        - prepend: O(1) - constant time insertion at beginning
        - insert_at: O(n) - linear time insertion at specific position
        - remove: O(n) - linear time removal (search + removal)
        - search: O(n) - linear time search
        - size: O(1) - constant time size query

    Space Complexity: O(n) - where n is the number of elements in the list

    Advantages:
        - Dynamic size (grows/shrinks during runtime)
        - Efficient insertion/deletion at beginning (O(1))
        - No memory waste (allocates only what's needed)

    Disadvantages:
        - No random access (must traverse from head)
        - Extra memory overhead for storing pointers
        - Not cache-friendly due to non-contiguous memory layout

    Common use cases:
        - Implementation of other data structures (stacks, queues)
        - Undo functionality in applications
        - Music playlists and browser history
        - Dynamic memory allocation

    Example:
        >>> ll = LinkedList[int]()
        >>> ll.append(1)
        >>> ll.append(2)
        >>> ll.prepend(0)
        >>> print(list(ll))  # Output: [0, 1, 2]
        >>> print(ll.size())  # Output: 3
    """

    _head: Optional[_Node[T]]
    _tail: Optional[_Node[T]]
    _size: int

    def __init__(self) -> None:
        """Initialize an empty linked list."""
        self._head = None
        self._tail = None
        self._size = 0

    def append(self, item: T) -> None:
        """Add an item to the end of the linked list.

        Args:
            item: The item to add to the end of the list

        Example:
            >>> ll = LinkedList[str]()
            >>> ll.append("first")
            >>> ll.append("second")
            >>> print(ll.size())  # Output: 2
        """
        new_node = _Node(item)
        if self._tail is None:
            self._head = self._tail = new_node
        else:
            self._tail.next = new_node
            self._tail = new_node
        self._size += 1

    def prepend(self, item: T) -> None:
        """Add an item to the beginning of the linked list.

        Args:
            item: The item to add to the beginning of the list

        Example:
            >>> ll = LinkedList[int]()
            >>> ll.append(2)
            >>> ll.prepend(1)
            >>> print(list(ll))  # Output: [1, 2]
        """
        new_node = _Node(item)
        if self._head is None:
            self._head = self._tail = new_node
        else:
            new_node.next = self._head
            self._head = new_node
        self._size += 1

    def insert_at(self, index: int, item: T) -> None:
        """Insert an item at a specific index in the linked list.

        Args:
            index: The position where to insert the item (0-based indexing)
            item: The item to insert

        Raises:
            IndexError: If the index is out of bounds

        Example:
            >>> ll = LinkedList[int]()
            >>> ll.append(1)
            >>> ll.append(3)
            >>> ll.insert_at(1, 2)
            >>> print(list(ll))  # Output: [1, 2, 3]
        """
        if index < 0 or index > self._size:
            raise IndexError(f"Index {index} out of bounds for list of size {self._size}")

        if index == 0:
            self.prepend(item)
        elif index == self._size:
            self.append(item)
        else:
            new_node = _Node(item)
            current = self._head
            for _ in range(index - 1):
                current = current.next  # type: ignore
            new_node.next = current.next  # type: ignore
            current.next = new_node  # type: ignore
            self._size += 1

    def remove(self, item: T) -> bool:
        """Remove the first occurrence of an item from the linked list.

        Args:
            item: The item to remove

        Returns:
            True if the item was found and removed, False otherwise

        Example:
            >>> ll = LinkedList[int]()
            >>> ll.append(1)
            >>> ll.append(2)
            >>> ll.append(3)
            >>> success = ll.remove(2)
            >>> print(success)  # Output: True
            >>> print(list(ll))  # Output: [1, 3]
        """
        if self._head is None:
            return False

        if self._head.data == item:
            self._head = self._head.next
            if self._head is None:
                self._tail = None
            self._size -= 1
            return True

        current = self._head
        while current.next is not None:
            if current.next.data == item:
                if current.next == self._tail:
                    self._tail = current
                current.next = current.next.next
                self._size -= 1
                return True
            current = current.next

        return False

    def search(self, item: T) -> int | None:
        """Search for an item in the linked list.

        Args:
            item: The item to search for

        Returns:
            The index of the first occurrence of the item, or None if not found

        Example:
            >>> ll = LinkedList[str]()
            >>> ll.append("hello")
            >>> ll.append("world")
            >>> index = ll.search("world")
            >>> print(index)  # Output: 1
        """
        current = self._head
        index = 0
        while current is not None:
            if current.data == item:
                return index
            current = current.next
            index += 1
        return None

    def is_empty(self) -> bool:
        """Check if the linked list is empty.

        Returns:
            True if the list contains no elements, False otherwise

        Example:
            >>> ll = LinkedList[int]()
            >>> print(ll.is_empty())  # Output: True
            >>> ll.append(1)
            >>> print(ll.is_empty())  # Output: False
        """
        return self._head is None

    def size(self) -> int:
        """Return the number of items in the linked list.

        Returns:
            The number of elements currently in the list

        Example:
            >>> ll = LinkedList[int]()
            >>> print(ll.size())  # Output: 0
            >>> ll.append(1)
            >>> ll.append(2)
            >>> print(ll.size())  # Output: 2
        """
        return self._size

    def __len__(self) -> int:
        """Return the number of items in the linked list (supports len() function)."""
        return self._size

    def __iter__(self) -> Iterator[T]:
        """Return an iterator for the linked list."""
        current = self._head
        while current is not None:
            yield current.data
            current = current.next

    def __repr__(self) -> str:
        """Return string representation of the LinkedList instance."""
        return f"{self.__class__.__name__}()"

    def __str__(self) -> str:
        """Return string representation of the LinkedList contents."""
        return str(list(self))
