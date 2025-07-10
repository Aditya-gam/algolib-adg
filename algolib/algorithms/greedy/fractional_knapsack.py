"""Fractional Knapsack greedy algorithm implementation.

Solves the fractional knapsack problem by selecting items based on their
value-to-weight ratio. Items can be taken in fractions.
"""

from dataclasses import dataclass
from typing import List, NamedTuple, Tuple

from algolib.algorithms.sorting.merge_sort import MergeSort


class Item(NamedTuple):
    """Represents an item with weight and value."""

    weight: float
    value: float
    name: str = ""


@dataclass(slots=True, init=False)
class FractionalKnapsack:
    """Greedy solution for the fractional knapsack problem."""

    _sorter: MergeSort[Item]

    def __init__(self) -> None:
        # Sort by value/weight ratio descending (higher ratio first)
        # Zero weight items with positive value get infinite ratio (sorted first)
        def get_ratio(item: Item) -> float:
            if item.weight == 0:
                return float("-inf") if item.value > 0 else 0.0
            return -item.value / item.weight

        self._sorter = MergeSort(key=get_ratio)

    def solve(self, items: List[Item], capacity: float) -> Tuple[float, List[Tuple[Item, float]]]:
        """Return maximum value achievable and the selected item fractions."""
        if capacity < 0:
            raise ValueError("Capacity cannot be negative")
        if not items:
            raise ValueError("Items list cannot be empty")
        for item in items:
            if item.weight < 0 or item.value < 0:
                raise ValueError("Item weight and value must be non-negative")

        sorted_items = list(items)
        self._sorter.sort(sorted_items)

        total_value = 0.0
        remaining_capacity = capacity
        selection: List[Tuple[Item, float]] = []

        for item in sorted_items:
            if remaining_capacity <= 0:
                break
            if item.weight == 0:
                if item.value > 0:
                    selection.append((item, 1.0))
                    total_value += item.value
                continue
            if item.weight <= remaining_capacity:
                selection.append((item, 1.0))
                total_value += item.value
                remaining_capacity -= item.weight
            else:
                fraction = remaining_capacity / item.weight
                selection.append((item, fraction))
                total_value += item.value * fraction
                remaining_capacity = 0
        return total_value, selection

    def calculate_ratio(self, item: Item) -> float:
        """Return value-to-weight ratio for a given item."""
        if item.weight == 0:
            raise ValueError("Cannot calculate ratio for zero weight item")
        return item.value / item.weight
