"""Insertion Sort algorithm implementation."""

from dataclasses import dataclass
from typing import List, MutableSequence

from algolib._typing import ComparableT
from algolib.algorithms.sorting.base import Sorter


@dataclass(slots=True)
class InsertionSort(Sorter[ComparableT]):
    """Insertion Sort algorithm - O(n²) time complexity, O(1) space complexity.

    Insertion sort is a simple sorting algorithm that builds the final sorted array
    one element at a time. It works by taking elements from the unsorted portion
    and inserting them into their correct position in the sorted portion.

    Time Complexity:
        - Best Case: O(n) - when the array is already sorted
        - Average Case: O(n²) - random order
        - Worst Case: O(n²) - when the array is sorted in reverse order

    Space Complexity: O(1) - constant space usage (in-place sorting)

    Characteristics:
        - Stable: Equal elements maintain their relative order
        - In-place: Sorts the array without using extra space
        - Adaptive: Performs better on partially sorted arrays
        - Online: Can sort a list as it receives it

    Advantages:
        - Simple implementation
        - Efficient for small datasets
        - Stable sorting algorithm
        - Adaptive (performs well on nearly sorted arrays)
        - Online (can sort data as it's received)
        - No additional memory space needed

    Disadvantages:
        - Poor performance on large datasets
        - More writes compared to selection sort
        - Not as efficient as advanced algorithms for large datasets

    Common use cases:
        - Small datasets where simplicity is preferred
        - Nearly sorted arrays (performs very well)
        - As a subroutine in hybrid algorithms (like Timsort)
        - When stability is required and dataset is small
        - Real-time applications where data arrives incrementally

    Example:
        >>> sorter = InsertionSort()
        >>> result = sorter.sort([64, 34, 25, 12, 22, 11, 90])
        >>> print(result)  # Output: [11, 12, 22, 25, 34, 64, 90]
        >>> result = sorter.sort([5, 2, 4, 6, 1, 3])
        >>> print(result)  # Output: [1, 2, 3, 4, 5, 6]
    """

    def sort(self, data: MutableSequence[ComparableT]) -> List[ComparableT]:
        """Sort a sequence using the insertion sort algorithm.

        Creates a copy of the input data and sorts it using insertion sort.
        Each element is inserted into its correct position in the sorted portion.

        Args:
            data: The sequence to sort (list, tuple, or any mutable sequence)

        Returns:
            A new sorted list containing the elements from the input sequence

        Example:
            >>> sorter = InsertionSort()
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

        # Perform insertion sort
        for i in range(1, n):
            key = result[i]
            j = i - 1

            # Move elements greater than key one position ahead
            while j >= 0 and result[j] > key:
                result[j + 1] = result[j]
                j -= 1

            # Place key at its correct position
            result[j + 1] = key

        return result

    def sort_in_place(self, data: MutableSequence[ComparableT]) -> None:
        """Sort a mutable sequence in-place using insertion sort.

        Modifies the original sequence directly without creating a copy.

        Args:
            data: The mutable sequence to sort in-place

        Example:
            >>> sorter = InsertionSort()
            >>> numbers = [64, 34, 25, 12, 22, 11, 90]
            >>> sorter.sort_in_place(numbers)
            >>> print(numbers)  # Output: [11, 12, 22, 25, 34, 64, 90]
        """
        if not data:
            return

        n = len(data)

        # Perform insertion sort
        for i in range(1, n):
            key = data[i]
            j = i - 1

            # Move elements greater than key one position ahead
            while j >= 0 and data[j] > key:
                data[j + 1] = data[j]
                j -= 1

            # Place key at its correct position
            data[j + 1] = key

    def binary_insertion_sort(self, data: MutableSequence[ComparableT]) -> List[ComparableT]:
        """Sort using insertion sort with binary search for finding insertion position.

        Uses binary search to find the correct position for insertion, reducing
        the number of comparisons from O(n) to O(log n) per element.

        Args:
            data: The sequence to sort

        Returns:
            A new sorted list containing the elements from the input sequence

        Example:
            >>> sorter = InsertionSort()
            >>> sorter.binary_insertion_sort([5, 2, 8, 1, 9])
            [1, 2, 5, 8, 9]
        """
        if not data:
            return []

        # Create a copy to avoid modifying the original
        result = list(data)
        n = len(result)

        # Perform binary insertion sort
        for i in range(1, n):
            key = result[i]
            # Find the correct position using binary search
            left, right = 0, i

            while left < right:
                mid = (left + right) // 2
                if result[mid] < key or result[mid] == key:
                    left = mid + 1
                else:
                    right = mid

            # Shift elements to make room for key
            for j in range(i, left, -1):
                result[j] = result[j - 1]

            # Insert key at the correct position
            result[left] = key

        return result

    def is_sorted(self, data: MutableSequence[ComparableT]) -> bool:
        """Check if a sequence is already sorted in ascending order.

        Args:
            data: The sequence to check

        Returns:
            True if the sequence is sorted, False otherwise

        Example:
            >>> sorter = InsertionSort()
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

    def count_inversions(self, data: MutableSequence[ComparableT]) -> int:
        """Count the number of inversions in the sequence.

        An inversion is a pair of indices (i, j) such that i < j but data[i] > data[j].
        This gives an indication of how far the array is from being sorted.

        Args:
            data: The sequence to analyze

        Returns:
            The number of inversions in the sequence

        Example:
            >>> sorter = InsertionSort()
            >>> sorter.count_inversions([2, 3, 8, 6, 1])
            5  # Number of inversions
            >>> sorter.count_inversions([1, 2, 3, 4, 5])
            0  # Already sorted
        """
        if len(data) <= 1:
            return 0

        inversions = 0
        n = len(data)

        for i in range(n - 1):
            for j in range(i + 1, n):
                if data[i] > data[j]:
                    inversions += 1

        return inversions

    def sort_with_stats(
        self, data: MutableSequence[ComparableT]
    ) -> tuple[List[ComparableT], int, int]:
        """Sort the sequence and return statistics about the sorting process.

        Args:
            data: The sequence to sort

        Returns:
            A tuple containing:
            - The sorted list
            - Number of comparisons made
            - Number of shifts (movements) made

        Example:
            >>> sorter = InsertionSort()
            >>> sorted_list, comparisons, shifts = sorter.sort_with_stats([5, 2, 8, 1, 9])
            >>> print(f"Sorted: {sorted_list}")
            >>> print(f"Comparisons: {comparisons}, Shifts: {shifts}")
        """
        if not data:
            return [], 0, 0

        # Create a copy to avoid modifying the original
        result = list(data)
        n = len(result)
        comparisons = 0
        shifts = 0

        # Perform insertion sort with statistics
        for i in range(1, n):
            key = result[i]
            j = i - 1

            # Move elements greater than key one position ahead
            while j >= 0:
                comparisons += 1
                if result[j] > key:
                    result[j + 1] = result[j]
                    shifts += 1
                    j -= 1
                else:
                    break

            # Place key at its correct position
            if j + 1 != i:
                result[j + 1] = key
                shifts += 1

        return result, comparisons, shifts

    def __repr__(self) -> str:
        """Return string representation of the InsertionSort instance."""
        return f"{self.__class__.__name__}()"
