"""Stack data structure implementation."""

from dataclasses import dataclass, field
from typing import Generic, List, TypeVar

T = TypeVar("T")


@dataclass(slots=True)
class Stack(Generic[T]):
    """Stack data structure - LIFO (Last-In-First-Out) container.

    A stack is a linear data structure that follows the Last-In-First-Out (LIFO) principle.
    Elements are added and removed from the same end, called the "top" of the stack.

    Time Complexities:
        - push: O(1) - constant time insertion
        - pop: O(1) - constant time removal
        - peek: O(1) - constant time access to top element
        - is_empty: O(1) - constant time check
        - size: O(1) - constant time size query

    Space Complexity: O(n) - where n is the number of elements in the stack

    Common use cases:
        - Function call management (call stack)
        - Expression evaluation and syntax parsing
        - Backtracking algorithms
        - Undo operations in applications
        - Browser history navigation

    Example:
        >>> stack = Stack[int]()
        >>> stack.push(1)
        >>> stack.push(2)
        >>> stack.push(3)
        >>> print(stack.peek())  # Output: 3
        >>> print(stack.pop())   # Output: 3
        >>> print(stack.size())  # Output: 2
    """

    _container: List[T] = field(default_factory=list, init=False, repr=False)

    def push(self, item: T) -> None:
        """Add an item to the top of the stack.

        Args:
            item: The item to add to the stack

        Example:
            >>> stack = Stack[str]()
            >>> stack.push("first")
            >>> stack.push("second")
            >>> print(stack.size())  # Output: 2
        """
        self._container.append(item)

    def pop(self) -> T:
        """Remove and return the item at the top of the stack.

        Returns:
            The item that was at the top of the stack

        Raises:
            IndexError: If the stack is empty

        Example:
            >>> stack = Stack[int]()
            >>> stack.push(42)
            >>> item = stack.pop()
            >>> print(item)  # Output: 42
        """
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._container.pop()

    def peek(self) -> T:
        """Return the item at the top of the stack without removing it.

        Returns:
            The item at the top of the stack

        Raises:
            IndexError: If the stack is empty

        Example:
            >>> stack = Stack[str]()
            >>> stack.push("hello")
            >>> top = stack.peek()
            >>> print(top)  # Output: "hello"
            >>> print(stack.size())  # Output: 1 (item still in stack)
        """
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._container[-1]

    def is_empty(self) -> bool:
        """Check if the stack is empty.

        Returns:
            True if the stack contains no elements, False otherwise

        Example:
            >>> stack = Stack[int]()
            >>> print(stack.is_empty())  # Output: True
            >>> stack.push(1)
            >>> print(stack.is_empty())  # Output: False
        """
        return len(self._container) == 0

    def size(self) -> int:
        """Return the number of items in the stack.

        Returns:
            The number of elements currently in the stack

        Example:
            >>> stack = Stack[int]()
            >>> print(stack.size())  # Output: 0
            >>> stack.push(1)
            >>> stack.push(2)
            >>> print(stack.size())  # Output: 2
        """
        return len(self._container)

    def __len__(self) -> int:
        """Return the number of items in the stack (supports len() function)."""
        return len(self._container)

    def __repr__(self) -> str:
        """Return string representation of the Stack instance."""
        return f"{self.__class__.__name__}()"

    def __str__(self) -> str:
        """Return string representation of the Stack contents."""
        return str(self._container)
