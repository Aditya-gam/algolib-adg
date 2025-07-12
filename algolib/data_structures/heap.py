"""Max Heap implementation for HeapSort and other algorithms."""

from dataclasses import dataclass
from typing import Callable, Generic, List, Optional, TypeVar

from algolib._typing import T

_T = TypeVar("_T")


@dataclass(slots=True, init=False)
class MaxHeap(Generic[T]):
    """A max heap implementation supporting custom comparison functions.

    This max heap uses a list-based representation where for any node at index i:
    - Left child is at index 2*i + 1
    - Right child is at index 2*i + 2
    - Parent is at index (i-1)//2

    Time Complexity:
        - insert: O(log n)
        - extract_max: O(log n)
        - peek: O(1)
        - build_heap: O(n)

    Space Complexity: O(n)

    Attributes:
        _heap: The internal list representation of the heap
        _key_func: Optional function to extract comparison key from elements
    """

    _heap: List[T]
    _key_func: Optional[Callable[[T], object]]

    def __init__(self, key: Optional[Callable[[T], object]] = None) -> None:
        """Initialize an empty max heap.

        Args:
            key: Optional function to extract comparison key from elements.
                If None, elements are compared directly.
        """
        self._heap = []
        self._key_func = key

    def _compare(self, a: T, b: T) -> bool:
        """Compare two elements using the key function if provided.

        Args:
            a: First element
            b: Second element

        Returns:
            True if a >= b according to the comparison criteria
        """
        if self._key_func is None:
            return a >= b  # type: ignore[operator, no-any-return]
        key_a = self._key_func(a)
        key_b = self._key_func(b)
        return key_a >= key_b  # type: ignore[operator, no-any-return]

    def _parent_index(self, index: int) -> int:
        """Get the parent index of a given index.

        Args:
            index: The child index

        Returns:
            The parent index
        """
        return (index - 1) // 2

    def _left_child_index(self, index: int) -> int:
        """Get the left child index of a given index.

        Args:
            index: The parent index

        Returns:
            The left child index
        """
        return 2 * index + 1

    def _right_child_index(self, index: int) -> int:
        """Get the right child index of a given index.

        Args:
            index: The parent index

        Returns:
            The right child index
        """
        return 2 * index + 2

    def _heapify_up(self, index: int) -> None:
        """Restore heap property by moving element up.

        Args:
            index: Starting index to heapify upward
        """
        while index > 0:
            parent_idx = self._parent_index(index)
            if self._compare(self._heap[index], self._heap[parent_idx]):
                self._heap[index], self._heap[parent_idx] = (
                    self._heap[parent_idx],
                    self._heap[index],
                )
                index = parent_idx
            else:
                break

    def _heapify_down(self, index: int) -> None:
        """Restore heap property by moving element down.

        Args:
            index: Starting index to heapify downward
        """
        while True:
            largest = index
            left_idx = self._left_child_index(index)
            right_idx = self._right_child_index(index)

            # Compare with left child
            if left_idx < len(self._heap) and self._compare(
                self._heap[left_idx], self._heap[largest]
            ):
                largest = left_idx

            # Compare with right child
            if right_idx < len(self._heap) and self._compare(
                self._heap[right_idx], self._heap[largest]
            ):
                largest = right_idx

            if largest != index:
                self._heap[index], self._heap[largest] = (self._heap[largest], self._heap[index])
                index = largest
            else:
                break

    def insert(self, item: T) -> None:
        """Insert an item into the heap.

        Args:
            item: The item to insert
        """
        self._heap.append(item)
        self._heapify_up(len(self._heap) - 1)

    def extract_max(self) -> T:
        """Remove and return the maximum element from the heap.

        Returns:
            The maximum element

        Raises:
            IndexError: If the heap is empty
        """
        if not self._heap:
            raise IndexError("extract_max from empty heap")

        if len(self._heap) == 1:
            return self._heap.pop()

        max_item = self._heap[0]
        self._heap[0] = self._heap.pop()
        self._heapify_down(0)

        return max_item

    def peek(self) -> T:
        """Return the maximum element without removing it.

        Returns:
            The maximum element

        Raises:
            IndexError: If the heap is empty
        """
        if not self._heap:
            raise IndexError("peek from empty heap")
        return self._heap[0]

    def build_heap(self, items: List[T]) -> None:
        """Build a heap from a list of items in O(n) time.

        Args:
            items: List of items to build the heap from
        """
        self._heap = items.copy()

        # Start from the last non-leaf node and heapify down
        for i in range(len(self._heap) // 2 - 1, -1, -1):
            self._heapify_down(i)

    def is_empty(self) -> bool:
        """Check if the heap is empty.

        Returns:
            True if the heap is empty, False otherwise
        """
        return len(self._heap) == 0

    def size(self) -> int:
        """Get the number of items in the heap.

        Returns:
            The number of items in the heap
        """
        return len(self._heap)

    def __len__(self) -> int:
        """Return the number of items in the heap."""
        return len(self._heap)

    def __bool__(self) -> bool:
        """Return True if the heap is not empty."""
        return bool(self._heap)

    def __repr__(self) -> str:
        """Return string representation of the heap."""
        return f"MaxHeap({self._heap})"
