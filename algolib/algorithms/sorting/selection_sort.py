"""Selection Sort algorithm implementation."""

from dataclasses import dataclass
from typing import List, MutableSequence

from algolib._typing import ComparableT
from algolib.algorithms.sorting.base import Sorter


@dataclass(slots=True)
class SelectionSort(Sorter[ComparableT]):
    """Selection Sort algorithm - O(n²) time complexity, O(1) space complexity.

    Selection sort is a simple sorting algorithm that works by repeatedly finding
    the minimum element from the unsorted portion of the array and placing it
    at the beginning of the sorted portion.

    Time Complexity:
        - Best Case: O(n²) - even when the array is already sorted
        - Average Case: O(n²) - random order
        - Worst Case: O(n²) - when the array is sorted in reverse order

    Space Complexity: O(1) - constant space usage (in-place sorting)

    Characteristics:
        - Unstable: Equal elements may not maintain their relative order
        - In-place: Sorts the array without using extra space
        - Not adaptive: Performance doesn't improve on partially sorted arrays
        - Simple: Easy to understand and implement

    Advantages:
        - Simple implementation
        - No additional memory space needed
        - Performs well on small datasets
        - Minimizes the number of swaps (O(n) swaps)

    Disadvantages:
        - Poor performance on large datasets
        - Not stable (relative order of equal elements may change)
        - Not adaptive (doesn't perform better on partially sorted arrays)
        - Always performs O(n²) comparisons

    Common use cases:
        - Educational purposes (learning sorting concepts)
        - Small datasets where simplicity is preferred
        - When memory is extremely limited
        - When the cost of swapping is high (minimizes swaps)

    Example:
        >>> sorter = SelectionSort()
        >>> result = sorter.sort([64, 25, 12, 22, 11])
        >>> print(result)  # Output: [11, 12, 22, 25, 64]
        >>> result = sorter.sort([3, 1, 4, 1, 5])
        >>> print(result)  # Output: [1, 1, 3, 4, 5]
    """

    def sort(self, data: MutableSequence[ComparableT]) -> List[ComparableT]:
        """Sort a sequence using the selection sort algorithm.

        Creates a copy of the input data and sorts it using selection sort.
        Repeatedly finds the minimum element and places it at the correct position.

        Args:
            data: The sequence to sort (list, tuple, or any mutable sequence)

        Returns:
            A new sorted list containing the elements from the input sequence

        Example:
            >>> sorter = SelectionSort()
            >>> sorter.sort([5, 2, 8, 1, 9])
            [1, 2, 5, 8, 9]
            >>> sorter.sort(['banana', 'apple', 'cherry'])
            ['apple', 'banana', 'cherry']
            >>> sorter.sort([])
            []
        """
        if not data:
            return []

        # Create a copy to avoid modifying the original
        result = list(data)
        n = len(result)

        # Perform selection sort
        for i in range(n - 1):
            # Find the minimum element in remaining unsorted array
            min_idx = i
            for j in range(i + 1, n):
                if result[j] < result[min_idx]:
                    min_idx = j

            # Swap the found minimum element with the first element
            if min_idx != i:
                result[i], result[min_idx] = result[min_idx], result[i]

        return result

    def sort_in_place(self, data: MutableSequence[ComparableT]) -> None:
        """Sort a mutable sequence in-place using selection sort.

        Modifies the original sequence directly without creating a copy.

        Args:
            data: The mutable sequence to sort in-place

        Example:
            >>> sorter = SelectionSort()
            >>> numbers = [64, 25, 12, 22, 11]
            >>> sorter.sort_in_place(numbers)
            >>> print(numbers)  # Output: [11, 12, 22, 25, 64]
        """
        if not data:
            return

        n = len(data)

        # Perform selection sort
        for i in range(n - 1):
            # Find the minimum element in remaining unsorted array
            min_idx = i
            for j in range(i + 1, n):
                if data[j] < data[min_idx]:
                    min_idx = j

            # Swap the found minimum element with the first element
            if min_idx != i:
                data[i], data[min_idx] = data[min_idx], data[i]

    def find_min_index(self, data: MutableSequence[ComparableT], start: int, end: int) -> int:
        """Find the index of the minimum element in a given range.

        Args:
            data: The sequence to search in
            start: Starting index (inclusive)
            end: Ending index (exclusive)

        Returns:
            The index of the minimum element in the range [start, end)

        Raises:
            ValueError: If start >= end or indices are out of bounds

        Example:
            >>> sorter = SelectionSort()
            >>> sorter.find_min_index([5, 2, 8, 1, 9], 1, 4)
            3  # Index of element 1
        """
        if start >= end or start < 0 or end > len(data):
            raise ValueError("Invalid range specified")

        min_idx = start
        for i in range(start + 1, end):
            if data[i] < data[min_idx]:
                min_idx = i

        return min_idx

    def is_sorted(self, data: MutableSequence[ComparableT]) -> bool:
        """Check if a sequence is already sorted in ascending order.

        Args:
            data: The sequence to check

        Returns:
            True if the sequence is sorted, False otherwise

        Example:
            >>> sorter = SelectionSort()
            >>> sorter.is_sorted([1, 2, 3, 4, 5])
            True
            >>> sorter.is_sorted([5, 2, 8, 1, 9])
            False
            >>> sorter.is_sorted([])
            True
        """
        if len(data) <= 1:
            return True

        for i in range(len(data) - 1):
            if data[i] > data[i + 1]:
                return False

        return True

    def count_swaps(self, data: MutableSequence[ComparableT]) -> int:
        """Count the number of swaps needed to sort the sequence.

        Args:
            data: The sequence to analyze

        Returns:
            The number of swaps required to sort the sequence

        Example:
            >>> sorter = SelectionSort()
            >>> sorter.count_swaps([5, 2, 8, 1, 9])
            3  # Number of swaps needed
        """
        if not data:
            return 0

        # Create a copy to avoid modifying the original
        result = list(data)
        n = len(result)
        swap_count = 0

        # Perform selection sort and count swaps
        for i in range(n - 1):
            # Find the minimum element in remaining unsorted array
            min_idx = i
            for j in range(i + 1, n):
                if result[j] < result[min_idx]:
                    min_idx = j

            # Swap the found minimum element with the first element
            if min_idx != i:
                result[i], result[min_idx] = result[min_idx], result[i]
                swap_count += 1

        return swap_count

    def __repr__(self) -> str:
        """Return string representation of the SelectionSort instance."""
        return f"{self.__class__.__name__}()"
