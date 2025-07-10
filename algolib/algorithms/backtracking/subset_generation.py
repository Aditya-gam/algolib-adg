"""Subset Generation algorithm implementation using backtracking."""

from dataclasses import dataclass, field
from typing import Generic, List, Sequence, TypeVar

T = TypeVar("T")


@dataclass(slots=True)
class SubsetGeneration(Generic[T]):
    """Subset Generation using backtracking - O(2^n) time complexity, O(n) space complexity.

    This algorithm generates all possible subsets (the power set) of a given set
    using backtracking. For each element, there are two choices: include it in
    the current subset or exclude it.

    Time Complexity: O(2^n) - where n is the number of elements
    Space Complexity: O(n) - for recursion stack depth

    The power set of a set with n elements contains 2^n subsets, including
    the empty set and the set itself.

    Characteristics:
        - Backtracking: Uses recursive exploration with choice undoing
        - Complete: Generates all possible subsets
        - Systematic: Explores all combinations in a structured way
        - Memory efficient: Uses minimal additional space during generation

    Advantages:
        - Generates all subsets systematically
        - Uses minimal extra space during generation
        - Clear recursive structure
        - Can be easily modified for constrained subset problems

    Disadvantages:
        - Exponential time complexity
        - Not suitable for large sets (n > 20-25)
        - Generates large number of results

    Common use cases:
        - Combinatorial problems
        - Optimization problems with subset constraints
        - Algorithm competitions
        - Mathematical analysis of sets
        - Feature selection in machine learning

    Example:
        >>> generator = SubsetGeneration()
        >>> result = generator.generate([1, 2, 3])
        >>> print(result)  # Output: [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
        >>> result = generator.generate(['a', 'b'])
        >>> print(result)  # Output: [[], ['a'], ['b'], ['a', 'b']]
    """

    _current_subset: List[T] = field(default_factory=list, init=False, repr=False)
    _all_subsets: List[List[T]] = field(default_factory=list, init=False, repr=False)

    def generate(self, elements: Sequence[T]) -> List[List[T]]:
        """Generate all subsets of the given elements using backtracking.

        Args:
            elements: The sequence of elements to generate subsets from

        Returns:
            A list of all possible subsets (including empty set)

        Example:
            >>> generator = SubsetGeneration()
            >>> generator.generate([1, 2, 3])
            [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
            >>> generator.generate(['x', 'y'])
            [[], ['x'], ['y'], ['x', 'y']]
            >>> generator.generate([])
            [[]]
        """
        # Reset state for fresh generation
        self._current_subset = []
        self._all_subsets = []

        # Convert to list for easier indexing
        elements_list = list(elements)

        # Start backtracking from index 0
        self._backtrack(elements_list, 0)

        return self._all_subsets

    def _backtrack(self, elements: List[T], index: int) -> None:
        """Recursive backtracking helper method.

        Args:
            elements: The list of elements
            index: Current index being considered
        """
        # Base case: processed all elements
        if index == len(elements):
            # Add current subset to results (make a copy)
            self._all_subsets.append(self._current_subset.copy())
            return

        # Choice 1: Exclude current element
        self._backtrack(elements, index + 1)

        # Choice 2: Include current element
        self._current_subset.append(elements[index])
        self._backtrack(elements, index + 1)

        # Backtrack: remove the element for next iteration
        self._current_subset.pop()

    def generate_iterative(self, elements: Sequence[T]) -> List[List[T]]:
        """Generate all subsets using iterative bit manipulation approach.

        Uses the fact that for n elements, there are 2^n subsets, and each
        subset can be represented by a binary number where bit i indicates
        whether element i is included.

        Args:
            elements: The sequence of elements to generate subsets from

        Returns:
            A list of all possible subsets

        Example:
            >>> generator = SubsetGeneration()
            >>> generator.generate_iterative([1, 2, 3])
            [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
        """
        elements_list = list(elements)
        n = len(elements_list)
        subsets = []

        # Generate all possible combinations using bit manipulation
        for i in range(2**n):
            subset = []
            for j in range(n):
                # Check if jth bit is set in i
                if i & (1 << j):
                    subset.append(elements_list[j])
            subsets.append(subset)

        return subsets

    def generate_with_size(self, elements: Sequence[T], size: int) -> List[List[T]]:
        """Generate all subsets of a specific size.

        Args:
            elements: The sequence of elements to generate subsets from
            size: The desired size of each subset

        Returns:
            A list of all subsets with the specified size

        Raises:
            ValueError: If size is negative or larger than the number of elements

        Example:
            >>> generator = SubsetGeneration()
            >>> generator.generate_with_size([1, 2, 3, 4], 2)
            [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
            >>> generator.generate_with_size(['a', 'b', 'c'], 0)
            [[]]
        """
        elements_list = list(elements)
        n = len(elements_list)

        if size < 0:
            raise ValueError("Size cannot be negative")
        if size > n:
            raise ValueError("Size cannot be larger than the number of elements")

        # Reset state
        self._current_subset = []
        self._all_subsets = []

        # Start backtracking with size constraint
        self._backtrack_with_size(elements_list, 0, size)

        return self._all_subsets

    def _backtrack_with_size(self, elements: List[T], index: int, remaining_size: int) -> None:
        """Recursive backtracking helper for specific size subsets.

        Args:
            elements: The list of elements
            index: Current index being considered
            remaining_size: Number of elements still needed for the subset
        """
        # Base case: found a subset of the desired size
        if remaining_size == 0:
            self._all_subsets.append(self._current_subset.copy())
            return

        # Pruning: not enough elements left to form a subset of desired size
        if index >= len(elements) or remaining_size > len(elements) - index:
            return

        # Choice 1: Include current element
        self._current_subset.append(elements[index])
        self._backtrack_with_size(elements, index + 1, remaining_size - 1)
        self._current_subset.pop()  # Backtrack

        # Choice 2: Exclude current element
        self._backtrack_with_size(elements, index + 1, remaining_size)

    def count_subsets(self, elements: Sequence[T]) -> int:
        """Count the total number of subsets without generating them.

        Args:
            elements: The sequence of elements

        Returns:
            The total number of subsets (always 2^n)

        Example:
            >>> generator = SubsetGeneration()
            >>> generator.count_subsets([1, 2, 3])
            8
            >>> generator.count_subsets(['a', 'b', 'c', 'd'])
            16
        """
        return int(2 ** len(elements))

    def count_subsets_with_size(self, elements: Sequence[T], size: int) -> int:
        """Count the number of subsets of a specific size.

        Uses the binomial coefficient formula: C(n, k) = n! / (k! * (n-k)!)

        Args:
            elements: The sequence of elements
            size: The desired size of subsets

        Returns:
            The number of subsets with the specified size

        Raises:
            ValueError: If size is negative or larger than the number of elements

        Example:
            >>> generator = SubsetGeneration()
            >>> generator.count_subsets_with_size([1, 2, 3, 4], 2)
            6
            >>> generator.count_subsets_with_size(['a', 'b', 'c'], 0)
            1
        """
        n = len(elements)

        if size < 0:
            raise ValueError("Size cannot be negative")
        if size > n:
            raise ValueError("Size cannot be larger than the number of elements")

        # Calculate binomial coefficient C(n, k)
        return self._binomial_coefficient(n, size)

    def _binomial_coefficient(self, n: int, k: int) -> int:
        """Calculate binomial coefficient C(n, k) = n! / (k! * (n-k)!)

        Uses an optimized approach to avoid computing large factorials.
        """
        if k > n - k:  # Take advantage of symmetry
            k = n - k

        result = 1
        for i in range(k):
            result = int(result * (n - i) // (i + 1))

        return result

    def is_subset(self, subset: Sequence[T], superset: Sequence[T]) -> bool:
        """Check if one sequence is a subset of another.

        Args:
            subset: The potential subset
            superset: The potential superset

        Returns:
            True if subset is a subset of superset, False otherwise

        Example:
            >>> generator = SubsetGeneration()
            >>> generator.is_subset([1, 2], [1, 2, 3, 4])
            True
            >>> generator.is_subset([1, 5], [1, 2, 3, 4])
            False
            >>> generator.is_subset([], [1, 2, 3])
            True
        """
        subset_set = set(subset)
        superset_set = set(superset)
        return subset_set.issubset(superset_set)

    def __repr__(self) -> str:
        """Return string representation of the SubsetGeneration instance."""
        return f"{self.__class__.__name__}()"
