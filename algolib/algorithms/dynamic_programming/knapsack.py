"""Dynamic Programming algorithms implementation for intermediate algorithms."""

from dataclasses import dataclass
from typing import Any, Dict, List, NamedTuple, Tuple


class DPItem(NamedTuple):
    """Represents an item for dynamic programming problems."""

    weight: int
    value: int
    name: str = ""


@dataclass(slots=True, init=False)
class KnapsackDP:
    """0/1 Knapsack Dynamic Programming algorithm implementation.

    Solves the 0/1 knapsack problem using dynamic programming where each item
    can either be included completely or not at all (no fractions allowed).

    Time Complexity: O(n × W) - where n is items, W is capacity
    Space Complexity: O(n × W) - for the DP table

    Characteristics:
        - Dynamic Programming: Uses optimal substructure
        - 0/1 constraint: Items taken completely or not at all
        - Optimal: Guarantees optimal solution
        - Table-based: Uses 2D DP table

    Advantages:
        - Guarantees optimal solution
        - Handles discrete items naturally
        - Well-studied algorithm
        - Can be optimized for space

    Disadvantages:
        - Pseudo-polynomial time complexity
        - High space complexity
        - Not suitable for large weights
        - More complex than greedy approaches

    Example:
        >>> items = [
        ...     DPItem(10, 60, "item1"),
        ...     DPItem(20, 100, "item2"),
        ...     DPItem(30, 120, "item3")
        ... ]
        >>> knapsack = KnapsackDP()
        >>> value, selection = knapsack.solve(items, 50)
        >>> print(f"Maximum value: {value}")
    """

    # Error messages
    _CAPACITY_NEGATIVE_MSG = "Capacity cannot be negative"

    def solve(self, items: List[DPItem], capacity: int) -> Tuple[int, List[DPItem]]:
        """Solve the 0/1 knapsack problem using dynamic programming.

        Args:
            items: List of items with weight and value
            capacity: Maximum weight capacity of the knapsack

        Returns:
            Tuple of (maximum value, list of selected items)

        Raises:
            ValueError: If capacity is negative or items list is empty
        """
        if capacity < 0:
            raise ValueError(self._CAPACITY_NEGATIVE_MSG)

        if not items:
            raise ValueError("Items list cannot be empty")

        # Validate items
        for item in items:
            if item.weight < 0 or item.value < 0:
                raise ValueError("Item weight and value must be non-negative")

        n = len(items)

        # Create DP table: dp[i][w] = maximum value using items 0..i-1 with capacity w
        dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

        # Fill the DP table
        for i in range(1, n + 1):
            item = items[i - 1]
            for w in range(capacity + 1):
                # Option 1: Don't include the current item
                dp[i][w] = dp[i - 1][w]

                # Option 2: Include the current item (if it fits)
                if item.weight <= w:
                    include_value = dp[i - 1][w - item.weight] + item.value
                    dp[i][w] = max(dp[i][w], include_value)

        # Backtrack to find the selected items
        selected_items = self._backtrack(dp, items, capacity)

        return dp[n][capacity], selected_items

    def _backtrack(self, dp: List[List[int]], items: List[DPItem], capacity: int) -> List[DPItem]:
        """Backtrack through the DP table to find selected items.

        Args:
            dp: Filled DP table
            items: List of items
            capacity: Knapsack capacity

        Returns:
            List of selected items
        """
        selected: List[DPItem] = []
        i = len(items)
        w = capacity

        while i > 0 and w > 0:
            # If value differs from above, item was included
            if dp[i][w] != dp[i - 1][w]:
                item = items[i - 1]
                selected.append(item)
                w -= item.weight
            i -= 1

        return selected[::-1]  # Reverse to get original order

    def solve_optimized(self, items: List[DPItem], capacity: int) -> Tuple[int, List[DPItem]]:
        """Solve using space-optimized DP (O(W) space).

        Args:
            items: List of items with weight and value
            capacity: Maximum weight capacity of the knapsack

        Returns:
            Tuple of (maximum value, list of selected items)

        Note:
            This optimization reduces space complexity to O(W) but makes
            backtracking more complex, so we use the standard approach.
        """
        if capacity < 0:
            raise ValueError(self._CAPACITY_NEGATIVE_MSG)

        if not items:
            raise ValueError("Items list cannot be empty")

        # Validate items
        for item in items:
            if item.weight < 0 or item.value < 0:
                raise ValueError("Item weight and value must be non-negative")

        n = len(items)

        # Use two rows: previous and current
        prev = [0] * (capacity + 1)
        curr = [0] * (capacity + 1)

        # Keep track of which items are selected for each weight
        selected_items: List[List[DPItem]] = [[] for _ in range(capacity + 1)]

        for i in range(n):
            item = items[i]
            new_selected: List[List[DPItem]] = [[] for _ in range(capacity + 1)]

            self._process_item_for_capacity(
                item, capacity, prev, curr, selected_items, new_selected
            )

            # Swap rows
            prev, curr = curr, prev
            selected_items = new_selected

        return prev[capacity], selected_items[capacity]

    def _process_item_for_capacity(
        self,
        item: DPItem,
        capacity: int,
        prev: List[int],
        curr: List[int],
        selected_items: List[List[DPItem]],
        new_selected: List[List[DPItem]],
    ) -> None:
        """Process a single item for all capacity values in the optimized DP approach."""
        for w in range(capacity + 1):
            # Option 1: Don't include the current item
            curr[w] = prev[w]
            new_selected[w] = selected_items[w].copy()

            # Option 2: Include the current item (if it fits)
            if item.weight <= w:
                include_value = prev[w - item.weight] + item.value
                if include_value > curr[w]:
                    curr[w] = include_value
                    new_selected[w] = selected_items[w - item.weight].copy()
                    new_selected[w].append(item)

    def can_achieve_value(self, items: List[DPItem], capacity: int, target_value: int) -> bool:
        """Check if a target value can be achieved with given capacity.

        Args:
            items: List of items
            capacity: Knapsack capacity
            target_value: Target value to achieve

        Returns:
            True if target value can be achieved, False otherwise
        """
        max_value, _ = self.solve(items, capacity)
        return max_value >= target_value

    def find_minimum_capacity(self, items: List[DPItem], target_value: int) -> int:
        """Find minimum capacity needed to achieve target value.

        Args:
            items: List of items
            target_value: Target value to achieve

        Returns:
            Minimum capacity needed, or -1 if impossible
        """
        if not items:
            return -1 if target_value > 0 else 0

        max_possible_capacity = sum(item.weight for item in items)

        # Binary search on capacity
        left, right = 0, max_possible_capacity
        result = -1

        while left <= right:
            mid = (left + right) // 2
            max_value, _ = self.solve(items, mid)

            if max_value >= target_value:
                result = mid
                right = mid - 1
            else:
                left = mid + 1

        return result

    def solve_bounded(
        self, items: List[DPItem], quantities: List[int], capacity: int
    ) -> Tuple[int, List[Tuple[DPItem, int]]]:
        """Solve bounded knapsack where each item has a quantity limit."""
        if len(items) != len(quantities):
            raise ValueError("Items and quantities lists must have the same length")
        if capacity < 0:
            raise ValueError(self._CAPACITY_NEGATIVE_MSG)
        if not items:
            return 0, []

        expanded_items, item_mapping = self._expand_bounded_items(items, quantities)

        # If all quantities are zero, expanded_items will be empty
        if not expanded_items:
            return 0, []

        max_value, selected_expanded = self.solve(expanded_items, capacity)
        result_selection = self._reconstruct_bounded_solution(
            items, selected_expanded, expanded_items, item_mapping
        )

        return max_value, result_selection

    def _expand_bounded_items(
        self, items: List[DPItem], quantities: List[int]
    ) -> Tuple[List[DPItem], List[Tuple[int, int]]]:
        """Expand items with quantities into a list of 0/1 knapsack items."""
        expanded_items: List[DPItem] = []
        item_mapping: List[Tuple[int, int]] = []  # (original_index, quantity)

        for i, (item, quantity) in enumerate(zip(items, quantities, strict=True)):
            if quantity <= 0:
                continue

            k = 1
            remaining = quantity
            while k < remaining:
                expanded_item = DPItem(
                    weight=item.weight * k,
                    value=item.value * k,
                    name=f"{item.name}_{k}",
                )
                expanded_items.append(expanded_item)
                item_mapping.append((i, k))
                remaining -= k
                k *= 2

            if remaining > 0:
                expanded_item = DPItem(
                    weight=item.weight * remaining,
                    value=item.value * remaining,
                    name=f"{item.name}_{remaining}",
                )
                expanded_items.append(expanded_item)
                item_mapping.append((i, remaining))
        return expanded_items, item_mapping

    def _reconstruct_bounded_solution(
        self,
        original_items: List[DPItem],
        selected_expanded: List[DPItem],
        expanded_items: List[DPItem],
        item_mapping: List[Tuple[int, int]],
    ) -> List[Tuple[DPItem, int]]:
        """Reconstruct the bounded knapsack solution from the 0/1 solution."""
        item_quantities = [0] * len(original_items)
        # Create a mapping from expanded item object id to its index
        expanded_item_to_idx = {id(e): i for i, e in enumerate(expanded_items)}

        for expanded_item in selected_expanded:
            if id(expanded_item) in expanded_item_to_idx:
                idx = expanded_item_to_idx[id(expanded_item)]
                orig_idx, quantity = item_mapping[idx]
                item_quantities[orig_idx] += quantity

        result_selection = []
        for i, quantity in enumerate(item_quantities):
            if quantity > 0:
                result_selection.append((original_items[i], quantity))
        return result_selection

    def analyze_solution(self, items: List[DPItem], capacity: int) -> Dict[str, Any]:
        """Analyze the knapsack solution and provide detailed information.

        Args:
            items: List of items
            capacity: Knapsack capacity

        Returns:
            Dictionary with analysis results
        """

        max_value, selected_items = self.solve(items, capacity)

        total_weight = sum(item.weight for item in selected_items)
        total_value = sum(item.value for item in selected_items)

        efficiency = total_value / total_weight if total_weight > 0 else 0
        capacity_utilization = total_weight / capacity if capacity > 0 else 0

        # Calculate value density for each item
        item_densities = []
        for item in items:
            density = item.value / item.weight if item.weight > 0 else 0
            item_densities.append((item, density))

        item_densities.sort(key=lambda x: x[1], reverse=True)

        return {
            "max_value": max_value,
            "selected_items": selected_items,
            "total_weight": total_weight,
            "total_value": total_value,
            "efficiency": efficiency,
            "capacity_utilization": capacity_utilization,
            "items_by_density": item_densities,
            "selection_count": len(selected_items),
            "remaining_capacity": capacity - total_weight,
        }
