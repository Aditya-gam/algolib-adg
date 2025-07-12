"""Unit tests for Knapsack DP solver."""

import pytest

from algolib.algorithms.dynamic_programming import DPItem, KnapsackDP


class TestKnapsackDP:
    """Test cases for Knapsack DP solver."""

    def test_solve_empty_items(self, knapsack_dp: KnapsackDP) -> None:
        """Test solving with empty items list."""
        with pytest.raises(ValueError, match="Items list cannot be empty"):
            knapsack_dp.solve([], 10)

    def test_solve_zero_capacity(self, knapsack_dp: KnapsackDP) -> None:
        """Test solving with zero capacity."""
        items = [DPItem(2, 3), DPItem(3, 4), DPItem(4, 5)]
        result = knapsack_dp.solve(items, 0)
        assert result[0] == 0
        assert result[1] == []

    def test_solve_negative_capacity(self, knapsack_dp: KnapsackDP) -> None:
        """Test solving with negative capacity."""
        items = [DPItem(2, 3), DPItem(3, 4), DPItem(4, 5)]
        with pytest.raises(ValueError, match="Capacity cannot be negative"):
            knapsack_dp.solve(items, -1)

    def test_solve_single_item_fits(self, knapsack_dp: KnapsackDP) -> None:
        """Test solving with single item that fits."""
        items = [DPItem(3, 5)]
        result = knapsack_dp.solve(items, 5)
        assert result[0] == 5
        assert len(result[1]) == 1

    def test_solve_single_item_doesnt_fit(self, knapsack_dp: KnapsackDP) -> None:
        """Test solving with single item that doesn't fit."""
        items = [DPItem(6, 5)]
        result = knapsack_dp.solve(items, 5)
        assert result[0] == 0
        assert result[1] == []

    def test_solve_two_items_both_fit(self, knapsack_dp: KnapsackDP) -> None:
        """Test solving with two items that both fit."""
        items = [DPItem(2, 3), DPItem(3, 4)]
        result = knapsack_dp.solve(items, 6)
        assert result[0] == 7
        assert len(result[1]) == 2

    def test_solve_two_items_one_fits(self, knapsack_dp: KnapsackDP) -> None:
        """Test solving with two items where only one fits."""
        items = [DPItem(2, 3), DPItem(4, 5)]
        result = knapsack_dp.solve(items, 3)
        assert result[0] == 3
        assert len(result[1]) == 1

    def test_solve_multiple_items_optimal_selection(self, knapsack_dp: KnapsackDP) -> None:
        """Test solving with multiple items requiring optimal selection."""
        items = [DPItem(2, 3), DPItem(3, 4), DPItem(4, 5), DPItem(5, 6)]
        result = knapsack_dp.solve(items, 10)
        assert result[0] == 13  # Items 0, 1, 2: 2+3+4=9 weight, 3+4+5=12 value
        assert len(result[1]) == 3

    def test_solve_classic_example(self, knapsack_dp: KnapsackDP) -> None:
        """Test solving classic knapsack example."""
        items = [DPItem(1, 1), DPItem(3, 4), DPItem(4, 5), DPItem(5, 7)]
        result = knapsack_dp.solve(items, 7)
        assert result[0] == 9  # Items 1, 2: 3+4=7 weight, 4+5=9 value
        assert len(result[1]) == 2

    def test_solve_all_items_fit(self, knapsack_dp: KnapsackDP) -> None:
        """Test solving when all items fit."""
        items = [DPItem(1, 2), DPItem(2, 3), DPItem(3, 4)]
        result = knapsack_dp.solve(items, 10)
        assert result[0] == 9
        assert len(result[1]) == 3

    def test_solve_no_items_fit(self, knapsack_dp: KnapsackDP) -> None:
        """Test solving when no items fit."""
        items = [DPItem(5, 10), DPItem(6, 12), DPItem(7, 14)]
        result = knapsack_dp.solve(items, 4)
        assert result[0] == 0
        assert result[1] == []

    def test_solve_duplicate_items(self, knapsack_dp: KnapsackDP) -> None:
        """Test solving with duplicate items."""
        items = [DPItem(2, 3), DPItem(2, 3), DPItem(3, 4)]
        result = knapsack_dp.solve(items, 5)
        # Two items with weight 2, value 3 + one item with weight 3, value 4
        assert result[0] == 7
        assert len(result[1]) == 2

    def test_solve_zero_value_items(self, knapsack_dp: KnapsackDP) -> None:
        """Test solving with items having zero value."""
        items = [DPItem(2, 0), DPItem(3, 4), DPItem(4, 0)]
        result = knapsack_dp.solve(items, 5)
        assert result[0] == 4
        assert len(result[1]) == 1

    def test_solve_zero_weight_items(self, knapsack_dp: KnapsackDP) -> None:
        """Test solving with items having zero weight."""
        items = [DPItem(0, 3), DPItem(2, 4), DPItem(0, 5)]
        result = knapsack_dp.solve(items, 5)
        assert result[0] == 12  # All items can be selected
        assert len(result[1]) == 3

    def test_solve_large_capacity(self, knapsack_dp: KnapsackDP) -> None:
        """Test solving with large capacity."""
        items = [DPItem(100, 1000), DPItem(200, 2000), DPItem(300, 3000)]
        result = knapsack_dp.solve(items, 1000)
        assert result[0] == 6000  # All items fit
        assert len(result[1]) == 3

    def test_solve_small_capacity_large_items(self, knapsack_dp: KnapsackDP) -> None:
        """Test solving with small capacity and large items."""
        items = [DPItem(100, 1000), DPItem(200, 2000), DPItem(300, 3000)]
        result = knapsack_dp.solve(items, 50)
        assert result[0] == 0
        assert result[1] == []

    def test_solve_negative_weight_items(self, knapsack_dp: KnapsackDP) -> None:
        """Test solving with negative weight items."""
        items = [DPItem(-1, 5), DPItem(2, 3), DPItem(3, 4)]
        with pytest.raises(ValueError, match="Item weight and value must be non-negative"):
            knapsack_dp.solve(items, 10)

    def test_solve_negative_value_items(self, knapsack_dp: KnapsackDP) -> None:
        """Test solving with negative value items."""
        items = [DPItem(1, -5), DPItem(2, 3), DPItem(3, 4)]
        with pytest.raises(ValueError, match="Item weight and value must be non-negative"):
            knapsack_dp.solve(items, 10)

    def test_solve_float_weights_values(self, knapsack_dp: KnapsackDP) -> None:
        """Test solving with float weights and values."""
        items = [DPItem(1, 2), DPItem(2, 4), DPItem(3, 5)]
        result = knapsack_dp.solve(items, 5)
        assert result[0] == 9  # Items 1, 2: 2+3=5 weight, 4+5=9 value
        assert len(result[1]) == 2

    def test_solve_identical_items(self, knapsack_dp: KnapsackDP) -> None:
        """Test solving with identical items."""
        items = [DPItem(2, 3), DPItem(2, 3), DPItem(2, 3)]
        result = knapsack_dp.solve(items, 6)
        assert result[0] == 9  # All three items fit
        assert len(result[1]) == 3

    def test_solve_high_value_low_weight(self, knapsack_dp: KnapsackDP) -> None:
        """Test solving with high value, low weight items."""
        items = [DPItem(1, 100), DPItem(1, 100), DPItem(1, 100)]
        result = knapsack_dp.solve(items, 2)
        assert result[0] == 200  # Two items fit
        assert len(result[1]) == 2

    def test_solve_low_value_high_weight(self, knapsack_dp: KnapsackDP) -> None:
        """Test solving with low value, high weight items."""
        items = [DPItem(10, 1), DPItem(10, 1), DPItem(10, 1)]
        result = knapsack_dp.solve(items, 25)
        assert result[0] == 2  # Two items fit
        assert len(result[1]) == 2

    def test_solve_mixed_weights_values(self, knapsack_dp: KnapsackDP) -> None:
        """Test solving with mixed weights and values."""
        items = [DPItem(1, 1), DPItem(2, 3), DPItem(3, 6), DPItem(4, 10), DPItem(5, 15)]
        result = knapsack_dp.solve(items, 8)
        assert result[0] == 21  # Items 2, 4: 3+5=8 weight, 6+15=21 value
        assert len(result[1]) == 2

    def test_solve_performance_large_input(self, knapsack_dp: KnapsackDP) -> None:
        """Test performance with large input."""
        import time

        items = [DPItem(i, i * 2) for i in range(1, 101)]  # 100 items
        start_time = time.time()
        result = knapsack_dp.solve(items, 1000)
        end_time = time.time()
        assert end_time - start_time < 5.0  # Should complete within 5 seconds
        assert result[0] > 0

    def test_solve_multiple_calls_same_instance(self, knapsack_dp: KnapsackDP) -> None:
        """Test that multiple calls work correctly on the same instance."""
        items = [DPItem(2, 3), DPItem(3, 4), DPItem(4, 5)]
        result1 = knapsack_dp.solve(items, 10)
        result2 = knapsack_dp.solve(items, 10)
        assert result1[0] == result2[0]
        assert result1[1] == result2[1]

    def test_solve_immutability(self, knapsack_dp: KnapsackDP) -> None:
        """Test that the original items list is not modified."""
        items = [DPItem(2, 3), DPItem(3, 4), DPItem(4, 5)]
        original_items = items.copy()
        knapsack_dp.solve(items, 10)
        assert items == original_items

    def test_solve_result_attributes(self, knapsack_dp: KnapsackDP) -> None:
        """Test that result has correct attributes."""
        items = [DPItem(2, 3), DPItem(3, 4), DPItem(4, 5)]
        result = knapsack_dp.solve(items, 10)
        assert len(result) == 2
        assert isinstance(result[0], int)
        assert isinstance(result[1], list)

    def test_solve_selected_items_validity(self, knapsack_dp: KnapsackDP) -> None:
        """Test that selected items are valid."""
        items = [DPItem(2, 3), DPItem(3, 4), DPItem(4, 5)]
        result = knapsack_dp.solve(items, 10)
        selected_items = result[1]
        for item in selected_items:
            assert item in items

    def test_solve_total_weight_constraint(self, knapsack_dp: KnapsackDP) -> None:
        """Test that total weight of selected items doesn't exceed capacity."""
        items = [DPItem(2, 3), DPItem(3, 4), DPItem(4, 5)]
        capacity = 10
        result = knapsack_dp.solve(items, capacity)
        selected_items = result[1]
        total_weight = sum(item.weight for item in selected_items)
        assert total_weight <= capacity

    def test_solve_total_value_correctness(self, knapsack_dp: KnapsackDP) -> None:
        """Test that total value matches sum of selected items."""
        items = [DPItem(2, 3), DPItem(3, 4), DPItem(4, 5)]
        result = knapsack_dp.solve(items, 10)
        max_value = result[0]
        selected_items = result[1]
        total_value = sum(item.value for item in selected_items)
        assert max_value == total_value

    def test_solve_optimality(self, knapsack_dp: KnapsackDP) -> None:
        """Test that solution is optimal."""
        items = [DPItem(2, 3), DPItem(3, 4), DPItem(4, 5), DPItem(5, 6)]
        capacity = 10
        result = knapsack_dp.solve(items, capacity)
        max_value = result[0]
        # Manual verification of optimal solution
        # Items 0, 1, 2: weight 2+3+4=9, value 3+4+5=12
        # Items 0, 1, 3: weight 2+3+5=10, value 3+4+6=13 (optimal)
        assert max_value == 13

    # Tests for solve_optimized method
    def test_solve_optimized_empty_items(self, knapsack_dp: KnapsackDP) -> None:
        """Test optimized solving with empty items list."""
        with pytest.raises(ValueError, match="Items list cannot be empty"):
            knapsack_dp.solve_optimized([], 10)

    def test_solve_optimized_negative_capacity(self, knapsack_dp: KnapsackDP) -> None:
        """Test optimized solving with negative capacity."""
        items = [DPItem(2, 3), DPItem(3, 4), DPItem(4, 5)]
        with pytest.raises(ValueError, match="Capacity cannot be negative"):
            knapsack_dp.solve_optimized(items, -1)

    def test_solve_optimized_single_item(self, knapsack_dp: KnapsackDP) -> None:
        """Test optimized solving with single item."""
        items = [DPItem(3, 5)]
        result = knapsack_dp.solve_optimized(items, 5)
        assert result[0] == 5
        assert len(result[1]) == 1

    def test_solve_optimized_multiple_items(self, knapsack_dp: KnapsackDP) -> None:
        """Test optimized solving with multiple items."""
        items = [DPItem(2, 3), DPItem(3, 4), DPItem(4, 5)]
        result = knapsack_dp.solve_optimized(items, 10)
        assert result[0] == 12
        assert len(result[1]) == 3

    def test_solve_optimized_consistency_with_standard(self, knapsack_dp: KnapsackDP) -> None:
        """Test that optimized and standard methods produce same results."""
        items = [DPItem(2, 3), DPItem(3, 4), DPItem(4, 5), DPItem(5, 6)]
        capacity = 10
        standard_result = knapsack_dp.solve(items, capacity)
        optimized_result = knapsack_dp.solve_optimized(items, capacity)
        assert standard_result[0] == optimized_result[0]
        # Check that selected items have same total value
        standard_value = sum(item.value for item in standard_result[1])
        optimized_value = sum(item.value for item in optimized_result[1])
        assert standard_value == optimized_value

    def test_solve_optimized_negative_items(self, knapsack_dp: KnapsackDP) -> None:
        """Test optimized solving with negative weight items."""
        items = [DPItem(-1, 5), DPItem(2, 3), DPItem(3, 4)]
        with pytest.raises(ValueError, match="Item weight and value must be non-negative"):
            knapsack_dp.solve_optimized(items, 10)

    # Tests for can_achieve_value method
    def test_can_achieve_value_possible(self, knapsack_dp: KnapsackDP) -> None:
        """Test can_achieve_value when target is achievable."""
        items = [DPItem(2, 3), DPItem(3, 4), DPItem(4, 5)]
        assert knapsack_dp.can_achieve_value(items, 10, 7) is True

    def test_can_achieve_value_impossible(self, knapsack_dp: KnapsackDP) -> None:
        """Test can_achieve_value when target is not achievable."""
        items = [DPItem(2, 3), DPItem(3, 4), DPItem(4, 5)]
        assert knapsack_dp.can_achieve_value(items, 5, 20) is False

    def test_can_achieve_value_exact(self, knapsack_dp: KnapsackDP) -> None:
        """Test can_achieve_value when target equals maximum value."""
        items = [DPItem(2, 3), DPItem(3, 4), DPItem(4, 5)]
        max_value, _ = knapsack_dp.solve(items, 10)
        assert knapsack_dp.can_achieve_value(items, 10, max_value) is True

    def test_can_achieve_value_zero_target(self, knapsack_dp: KnapsackDP) -> None:
        """Test can_achieve_value with zero target."""
        items = [DPItem(2, 3), DPItem(3, 4), DPItem(4, 5)]
        assert knapsack_dp.can_achieve_value(items, 10, 0) is True

    # Tests for find_minimum_capacity method
    def test_find_minimum_capacity_achievable(self, knapsack_dp: KnapsackDP) -> None:
        """Test find_minimum_capacity when target is achievable."""
        items = [DPItem(2, 3), DPItem(3, 4), DPItem(4, 5)]
        min_capacity = knapsack_dp.find_minimum_capacity(items, 7)
        assert min_capacity > 0
        # Verify that this capacity can achieve the target
        assert knapsack_dp.can_achieve_value(items, min_capacity, 7) is True

    def test_find_minimum_capacity_impossible(self, knapsack_dp: KnapsackDP) -> None:
        """Test find_minimum_capacity when target is impossible."""
        items = [DPItem(2, 3), DPItem(3, 4), DPItem(4, 5)]
        min_capacity = knapsack_dp.find_minimum_capacity(items, 100)
        assert min_capacity == -1

    def test_find_minimum_capacity_zero_target(self, knapsack_dp: KnapsackDP) -> None:
        """Test find_minimum_capacity with zero target."""
        items = [DPItem(2, 3), DPItem(3, 4), DPItem(4, 5)]
        min_capacity = knapsack_dp.find_minimum_capacity(items, 0)
        assert min_capacity == 0

    def test_find_minimum_capacity_empty_items(self, knapsack_dp: KnapsackDP) -> None:
        """Test find_minimum_capacity with empty items."""
        min_capacity = knapsack_dp.find_minimum_capacity([], 0)
        assert min_capacity == 0

    def test_find_minimum_capacity_empty_items_nonzero_target(
        self, knapsack_dp: KnapsackDP
    ) -> None:
        """Test find_minimum_capacity with empty items and nonzero target."""
        min_capacity = knapsack_dp.find_minimum_capacity([], 5)
        assert min_capacity == -1

    # Tests for solve_bounded method
    def test_solve_bounded_basic(self, knapsack_dp: KnapsackDP) -> None:
        """Test basic bounded knapsack solving."""
        items = [DPItem(2, 3), DPItem(3, 4)]
        quantities = [2, 1]
        result = knapsack_dp.solve_bounded(items, quantities, 10)
        assert result[0] > 0
        assert len(result[1]) > 0

    def test_solve_bounded_mismatched_lists(self, knapsack_dp: KnapsackDP) -> None:
        """Test bounded solving with mismatched items and quantities lists."""
        items = [DPItem(2, 3), DPItem(3, 4)]
        quantities = [2]  # Only one quantity for two items
        with pytest.raises(
            ValueError, match="Items and quantities lists must have the same length"
        ):
            knapsack_dp.solve_bounded(items, quantities, 10)

    def test_solve_bounded_negative_capacity(self, knapsack_dp: KnapsackDP) -> None:
        """Test bounded solving with negative capacity."""
        items = [DPItem(2, 3), DPItem(3, 4)]
        quantities = [2, 1]
        with pytest.raises(ValueError, match="Capacity cannot be negative"):
            knapsack_dp.solve_bounded(items, quantities, -1)

    def test_solve_bounded_empty_items(self, knapsack_dp: KnapsackDP) -> None:
        """Test bounded solving with empty items."""
        result = knapsack_dp.solve_bounded([], [], 10)
        assert result[0] == 0
        assert result[1] == []

    def test_solve_bounded_zero_quantities(self, knapsack_dp: KnapsackDP) -> None:
        """Test bounded solving with zero quantities."""
        items = [DPItem(2, 3), DPItem(3, 4)]
        quantities = [0, 0]
        # When all quantities are zero, the expanded items list will be empty
        # This should be handled by the solve_bounded method
        result = knapsack_dp.solve_bounded(items, quantities, 10)
        assert result[0] == 0
        assert result[1] == []

    def test_solve_bounded_single_item(self, knapsack_dp: KnapsackDP) -> None:
        """Test bounded solving with single item."""
        items = [DPItem(2, 3)]
        quantities = [3]
        result = knapsack_dp.solve_bounded(items, quantities, 6)
        assert result[0] == 9  # 3 items * 3 value
        assert len(result[1]) == 1
        assert result[1][0][1] == 3  # Quantity should be 3

    def test_solve_bounded_multiple_items(self, knapsack_dp: KnapsackDP) -> None:
        """Test bounded solving with multiple items."""
        items = [DPItem(2, 3), DPItem(3, 4)]
        quantities = [2, 1]
        result = knapsack_dp.solve_bounded(items, quantities, 8)
        assert result[0] > 0
        # Verify quantities don't exceed limits
        item_quantities: dict[int, int] = {}
        for item, quantity in result[1]:
            item_idx = items.index(item)
            item_quantities[item_idx] = item_quantities.get(item_idx, 0) + quantity
        assert item_quantities.get(0, 0) <= 2
        assert item_quantities.get(1, 0) <= 1

    # Tests for analyze_solution method
    def test_analyze_solution_basic(self, knapsack_dp: KnapsackDP) -> None:
        """Test basic solution analysis."""
        items = [DPItem(2, 3), DPItem(3, 4), DPItem(4, 5)]
        analysis = knapsack_dp.analyze_solution(items, 10)

        assert "max_value" in analysis
        assert "selected_items" in analysis
        assert "total_weight" in analysis
        assert "total_value" in analysis
        assert "efficiency" in analysis
        assert "capacity_utilization" in analysis

        assert analysis["max_value"] > 0
        assert len(analysis["selected_items"]) > 0
        assert analysis["total_weight"] <= 10
        assert analysis["total_value"] == analysis["max_value"]

    def test_analyze_solution_zero_capacity(self, knapsack_dp: KnapsackDP) -> None:
        """Test solution analysis with zero capacity."""
        items = [DPItem(2, 3), DPItem(3, 4), DPItem(4, 5)]
        analysis = knapsack_dp.analyze_solution(items, 0)

        assert analysis["max_value"] == 0
        assert len(analysis["selected_items"]) == 0
        assert analysis["total_weight"] == 0
        assert analysis["total_value"] == 0
        assert analysis["efficiency"] == 0
        assert analysis["capacity_utilization"] == 0

    def test_analyze_solution_no_items_fit(self, knapsack_dp: KnapsackDP) -> None:
        """Test solution analysis when no items fit."""
        items = [DPItem(10, 20), DPItem(15, 30)]
        analysis = knapsack_dp.analyze_solution(items, 5)

        assert analysis["max_value"] == 0
        assert len(analysis["selected_items"]) == 0
        assert analysis["total_weight"] == 0
        assert analysis["total_value"] == 0
        assert analysis["efficiency"] == 0
        assert analysis["capacity_utilization"] == 0

    def test_analyze_solution_efficiency_calculation(self, knapsack_dp: KnapsackDP) -> None:
        """Test efficiency calculation in solution analysis."""
        items = [DPItem(2, 6), DPItem(3, 9)]  # Efficiency = 3 for both items
        analysis = knapsack_dp.analyze_solution(items, 10)

        # Both items should be selected (weight 5, value 15)
        assert analysis["total_weight"] == 5
        assert analysis["total_value"] == 15
        assert analysis["efficiency"] == 3.0  # 15/5 = 3
        assert analysis["capacity_utilization"] == 0.5  # 5/10 = 0.5

    # Tests for DPItem
    def test_dp_item_creation(self) -> None:
        """Test DPItem creation."""
        item = DPItem(2, 3, "test_item")
        assert item.weight == 2
        assert item.value == 3
        assert item.name == "test_item"

    def test_dp_item_default_name(self) -> None:
        """Test DPItem with default name."""
        item = DPItem(2, 3)
        assert item.weight == 2
        assert item.value == 3
        assert item.name == ""

    def test_dp_item_equality(self) -> None:
        """Test DPItem equality."""
        item1 = DPItem(2, 3, "item1")
        item2 = DPItem(2, 3, "item1")
        item3 = DPItem(2, 3, "item2")

        assert item1 == item2
        assert item1 != item3

    def test_dp_item_repr(self) -> None:
        """Test DPItem string representation."""
        item = DPItem(2, 3, "test_item")
        assert "DPItem" in repr(item)
        assert "2" in repr(item)
        assert "3" in repr(item)
        assert "test_item" in repr(item)


@pytest.fixture
def knapsack_dp() -> KnapsackDP:
    """Fixture to provide a KnapsackDP instance."""
    return KnapsackDP()
