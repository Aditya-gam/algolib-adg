"""Fibonacci sequence implementation with Dynamic Programming (memoization)."""

from dataclasses import dataclass, field
from typing import Dict


@dataclass(slots=True)
class Fibonacci:
    """Fibonacci sequence with Dynamic Programming - O(n) time complexity, O(n) space complexity.

    The Fibonacci sequence is a series of numbers where each number is the sum
    of the two preceding ones, usually starting with 0 and 1.

    Sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...

    This implementation uses memoization (top-down dynamic programming) to cache
    previously computed values, avoiding exponential time complexity.

    Time Complexity:
        - compute: O(n) - linear time for first computation, O(1) for cached values
        - Without memoization: O(2^n) - exponential time complexity

    Space Complexity: O(n) - due to memoization cache storage

    Characteristics:
        - Memoized: Caches results to avoid redundant calculations
        - Efficient: Dramatically improves performance over naive recursion
        - Persistent: Cache is maintained across multiple calls
        - Scalable: Can handle large values efficiently

    Advantages:
        - Avoids exponential time complexity of naive recursion
        - Persistent cache improves performance for multiple queries
        - Clear and readable implementation
        - Handles edge cases properly

    Disadvantages:
        - Uses additional memory for caching
        - Cache grows with the largest computed value
        - Potential for integer overflow with very large numbers

    Common use cases:
        - Mathematical computations
        - Algorithm optimization examples
        - Dynamic programming tutorials
        - Sequence generation
        - Performance comparison studies

    Example:
        >>> fib = Fibonacci()
        >>> print(fib.compute(10))  # Output: 55
        >>> print(fib.compute(20))  # Output: 6765
        >>> print(fib.sequence(8))  # Output: [0, 1, 1, 2, 3, 5, 8, 13]
    """

    _memo: Dict[int, int] = field(default_factory=dict, init=False, repr=False)

    def compute(self, n: int) -> int:
        """Compute the nth Fibonacci number using memoization.

        Args:
            n: The position in the Fibonacci sequence (0-indexed)

        Returns:
            The nth Fibonacci number

        Raises:
            ValueError: If n is negative

        Example:
            >>> fib = Fibonacci()
            >>> fib.compute(0)
            0
            >>> fib.compute(1)
            1
            >>> fib.compute(10)
            55
            >>> fib.compute(20)
            6765
        """
        if n < 0:
            raise ValueError("Fibonacci sequence is not defined for negative numbers")

        # Base cases
        if n in {0, 1}:
            return n

        # Check if already computed
        if n in self._memo:
            return self._memo[n]

        # Compute and memoize
        result = self.compute(n - 1) + self.compute(n - 2)
        self._memo[n] = result
        return result

    def compute_iterative(self, n: int) -> int:
        """Compute the nth Fibonacci number iteratively (without recursion).

        This approach uses constant space and avoids potential stack overflow
        for large values of n.

        Args:
            n: The position in the Fibonacci sequence (0-indexed)

        Returns:
            The nth Fibonacci number

        Raises:
            ValueError: If n is negative

        Example:
            >>> fib = Fibonacci()
            >>> fib.compute_iterative(10)
            55
            >>> fib.compute_iterative(50)
            12586269025
        """
        if n < 0:
            raise ValueError("Fibonacci sequence is not defined for negative numbers")

        if n in {0, 1}:
            return n

        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b

        return b

    def sequence(self, count: int) -> list[int]:
        """Generate the first 'count' Fibonacci numbers.

        Args:
            count: Number of Fibonacci numbers to generate

        Returns:
            A list containing the first 'count' Fibonacci numbers

        Raises:
            ValueError: If count is negative

        Example:
            >>> fib = Fibonacci()
            >>> fib.sequence(8)
            [0, 1, 1, 2, 3, 5, 8, 13]
            >>> fib.sequence(0)
            []
            >>> fib.sequence(1)
            [0]
        """
        if count < 0:
            raise ValueError("Count cannot be negative")

        if count == 0:
            return []

        return [self.compute(i) for i in range(count)]

    def is_fibonacci(self, num: int) -> bool:
        """Check if a number is a Fibonacci number.

        Uses the mathematical property that a number is Fibonacci if and only if
        one of (5*n² + 4) or (5*n² - 4) is a perfect square.

        Args:
            num: The number to check

        Returns:
            True if the number is a Fibonacci number, False otherwise

        Example:
            >>> fib = Fibonacci()
            >>> fib.is_fibonacci(13)
            True
            >>> fib.is_fibonacci(14)
            False
            >>> fib.is_fibonacci(0)
            True
        """
        if num < 0:
            return False

        def is_perfect_square(n: int) -> bool:
            """Check if a number is a perfect square."""
            if n < 0:
                return False
            root = int(n**0.5)
            return root * root == n

        # A number is Fibonacci if one of (5*n² + 4) or (5*n² - 4) is a perfect square
        return is_perfect_square(5 * num * num + 4) or is_perfect_square(5 * num * num - 4)

    def find_index(self, target: int) -> int | None:
        """Find the index of a target value in the Fibonacci sequence.

        Args:
            target: The Fibonacci number to find the index of

        Returns:
            The index of the target in the sequence, or None if not found

        Example:
            >>> fib = Fibonacci()
            >>> fib.find_index(13)
            7
            >>> fib.find_index(14)
            None
            >>> fib.find_index(0)
            0
        """
        if target < 0:
            return None

        if target == 0:
            return 0

        a, b = 0, 1
        index = 1

        while b < target:
            a, b = b, a + b
            index += 1

        return index if b == target else None

    def clear_cache(self) -> None:
        """Clear the memoization cache.

        This can be useful to free memory or reset the computation state.

        Example:
            >>> fib = Fibonacci()
            >>> fib.compute(100)  # Populates cache
            >>> fib.cache_size()  # Returns some positive number
            99
            >>> fib.clear_cache()
            >>> fib.cache_size()  # Returns 0
            0
        """
        self._memo.clear()

    def cache_size(self) -> int:
        """Get the current size of the memoization cache.

        Returns:
            The number of cached Fibonacci values

        Example:
            >>> fib = Fibonacci()
            >>> fib.cache_size()
            0
            >>> fib.compute(10)
            55
            >>> fib.cache_size()
            9
        """
        return len(self._memo)

    def ratio(self, n: int) -> float:
        """Calculate the ratio of consecutive Fibonacci numbers.

        As n approaches infinity, this ratio approaches the golden ratio (φ ≈ 1.618).

        Args:
            n: The position to calculate the ratio at (must be > 0)

        Returns:
            The ratio of F(n) to F(n-1)

        Raises:
            ValueError: If n <= 0

        Example:
            >>> fib = Fibonacci()
            >>> fib.ratio(10)
            1.6181818181818182
            >>> fib.ratio(20)
            1.6180339631667064
        """
        if n <= 0:
            raise ValueError("Ratio calculation requires n > 0")

        if n == 1:
            return float("inf")  # F(1)/F(0) = 1/0

        return self.compute(n) / self.compute(n - 1)

    def __repr__(self) -> str:
        """Return string representation of the Fibonacci instance."""
        return f"{self.__class__.__name__}()"
