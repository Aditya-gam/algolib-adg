"""Unit tests for greedy algorithms."""

import pytest

from algolib.algorithms.greedy import ActivitySelection, FractionalKnapsack, HuffmanCoding
from algolib.algorithms.greedy.activity_selection import Activity
from algolib.algorithms.greedy.fractional_knapsack import Item
from algolib.algorithms.greedy.huffman_coding import HuffmanNode


class TestActivitySelection:
    """Test cases for Activity Selection algorithm."""

    @pytest.fixture
    def activity_selector(self) -> ActivitySelection:
        """Provide ActivitySelection instance."""
        return ActivitySelection()

    def test_basic_activity_selection(self, activity_selector: ActivitySelection) -> None:
        """Test basic activity selection."""
        activities = [
            Activity(1, 4),
            Activity(3, 5),
            Activity(0, 6),
            Activity(5, 7),
            Activity(3, 8),
            Activity(5, 9),
            Activity(6, 10),
            Activity(8, 11),
        ]
        result = activity_selector.select(activities)
        # Greedy algorithm should select activities with earliest finish times
        # Expected: (1,4), (5,7), (8,11) - 3 activities
        assert len(result) == 3
        assert result[0] == Activity(1, 4)
        assert result[1] == Activity(5, 7)
        assert result[2] == Activity(8, 11)

    def test_empty_activities(self, activity_selector: ActivitySelection) -> None:
        """Test activity selection with empty list."""
        with pytest.raises(ValueError, match="Activities list cannot be empty"):
            activity_selector.select([])

    def test_single_activity(self, activity_selector: ActivitySelection) -> None:
        """Test activity selection with single activity."""
        activities = [Activity(1, 4)]
        result = activity_selector.select(activities)
        assert result == [Activity(1, 4)]

    def test_two_compatible_activities(self, activity_selector: ActivitySelection) -> None:
        """Test activity selection with two compatible activities."""
        activities = [Activity(1, 4), Activity(5, 7)]
        result = activity_selector.select(activities)
        assert result == [Activity(1, 4), Activity(5, 7)]

    def test_two_overlapping_activities(self, activity_selector: ActivitySelection) -> None:
        """Test activity selection with two overlapping activities."""
        activities = [Activity(1, 4), Activity(3, 6)]
        result = activity_selector.select(activities)
        # Should select the one with earlier finish time
        assert result == [Activity(1, 4)]

    def test_multiple_overlapping_activities(self, activity_selector: ActivitySelection) -> None:
        """Test activity selection with multiple overlapping activities."""
        activities = [Activity(1, 4), Activity(2, 6), Activity(4, 7), Activity(6, 8)]
        result = activity_selector.select(activities)
        # Should select (1,4), (4,7) - 2 activities
        # (6,8) is not selected because start=6 < last_finish=7
        assert len(result) == 2
        assert result[0] == Activity(1, 4)
        assert result[1] == Activity(4, 7)

    def test_activities_sorted_by_start_time(self, activity_selector: ActivitySelection) -> None:
        """Test that activities are sorted by start time if needed."""
        activities = [Activity(3, 5), Activity(1, 4), Activity(0, 6), Activity(5, 7)]
        result = activity_selector.select(activities)
        # Should select (1,4), (5,7) - 2 activities
        assert len(result) == 2
        assert result[0] == Activity(1, 4)
        assert result[1] == Activity(5, 7)

    def test_activities_with_same_start_time(self, activity_selector: ActivitySelection) -> None:
        """Test activities with same start time."""
        activities = [Activity(1, 4), Activity(1, 3), Activity(1, 5)]
        result = activity_selector.select(activities)
        # Should select the one with earliest finish time
        assert result == [Activity(1, 3)]

    def test_activities_with_same_end_time(self, activity_selector: ActivitySelection) -> None:
        """Test activities with same end time."""
        activities = [Activity(1, 4), Activity(2, 4), Activity(3, 4)]
        result = activity_selector.select(activities)
        # Should select the first one (1,4)
        assert result == [Activity(1, 4)]

    def test_activities_with_zero_duration(self, activity_selector: ActivitySelection) -> None:
        """Test activities with zero duration."""
        activities = [Activity(1, 1), Activity(2, 2), Activity(3, 3)]
        result = activity_selector.select(activities)
        assert result == [Activity(1, 1), Activity(2, 2), Activity(3, 3)]

    def test_activities_with_negative_times(self, activity_selector: ActivitySelection) -> None:
        """Test activities with negative times."""
        activities = [Activity(-2, 1), Activity(-1, 2), Activity(0, 3)]
        result = activity_selector.select(activities)
        # Activities overlap: (-2,1), (-1,2), (0,3)
        # Algorithm selects the one with earliest finish time
        assert len(result) == 1
        assert result[0] in [Activity(-2, 1), Activity(-1, 2), Activity(0, 3)]

    def test_large_number_of_activities(self, activity_selector: ActivitySelection) -> None:
        """Test activity selection with large number of activities."""
        activities = [Activity(i, i + 1) for i in range(100)]
        result = activity_selector.select(activities)
        assert len(result) == 100  # All activities should be selected

    def test_optimal_selection(self, activity_selector: ActivitySelection) -> None:
        """Test that the selection is optimal."""
        activities = [
            Activity(1, 4, "A"),
            Activity(2, 6, "B"),
            Activity(4, 7, "C"),
            Activity(6, 9, "D"),
        ]
        selected = activity_selector.select(activities)
        # Should select A and C (greedy choice: earliest finish time)
        assert len(selected) == 2
        assert selected[0].name == "A"
        assert selected[1].name == "C"

    def test_count_activities_method(self, activity_selector: ActivitySelection) -> None:
        """Test the count_activities method."""
        activities = [
            Activity(1, 4, "A"),
            Activity(2, 6, "B"),
            Activity(4, 7, "C"),
        ]
        count = activity_selector.count_activities(activities)
        assert count == 2  # A and C can be selected

    def test_total_time_method(self, activity_selector: ActivitySelection) -> None:
        """Test the total_time method."""
        activities = [
            Activity(1, 4, "A"),  # duration: 3
            Activity(2, 6, "B"),  # duration: 4
            Activity(4, 7, "C"),  # duration: 3
        ]
        total_time = activity_selector.total_time(activities)
        # Should select A and C: 3 + 3 = 6
        assert total_time == 6


class TestFractionalKnapsack:
    """Test cases for Fractional Knapsack algorithm."""

    @pytest.fixture
    def knapsack_solver(self) -> FractionalKnapsack:
        """Provide FractionalKnapsack instance."""
        return FractionalKnapsack()

    def test_basic_fractional_knapsack(self, knapsack_solver: FractionalKnapsack) -> None:
        """Test basic fractional knapsack."""
        items = [Item(10, 60), Item(20, 100), Item(30, 120)]
        capacity = 50
        total_value, selection = knapsack_solver.solve(items, capacity)
        assert total_value > 0
        total_weight = sum(item.weight * fraction for item, fraction in selection)
        assert total_weight <= capacity

    def test_empty_items(self, knapsack_solver: FractionalKnapsack) -> None:
        """Test with empty items list."""
        with pytest.raises(ValueError, match="Items list cannot be empty"):
            knapsack_solver.solve([], 50)

    def test_zero_capacity(self, knapsack_solver: FractionalKnapsack) -> None:
        """Test with zero capacity."""
        items = [Item(10, 60), Item(20, 100)]
        total_value, selection = knapsack_solver.solve(items, 0)
        assert total_value == 0
        total_weight = sum(item.weight * fraction for item, fraction in selection)
        assert total_weight == 0

    def test_single_item_fits(self, knapsack_solver: FractionalKnapsack) -> None:
        """Test with single item that fits."""
        items = [Item(10, 60)]
        total_value, selection = knapsack_solver.solve(items, 15)
        assert total_value == 60
        total_weight = sum(item.weight * fraction for item, fraction in selection)
        assert total_weight == 10

    def test_single_item_partial_fit(self, knapsack_solver: FractionalKnapsack) -> None:
        """Test with single item that partially fits."""
        items = [Item(20, 100)]
        total_value, selection = knapsack_solver.solve(items, 10)
        assert total_value == 50  # Half of 100
        total_weight = sum(item.weight * fraction for item, fraction in selection)
        assert total_weight == 10

    def test_all_items_fit(self, knapsack_solver: FractionalKnapsack) -> None:
        """Test when all items fit."""
        items = [Item(10, 60), Item(20, 100), Item(30, 120)]
        total_value, selection = knapsack_solver.solve(items, 100)
        assert total_value == 280
        total_weight = sum(item.weight * fraction for item, fraction in selection)
        assert total_weight == 60

    def test_no_items_fit(self, knapsack_solver: FractionalKnapsack) -> None:
        """Test when no items fit completely."""
        items = [Item(20, 100), Item(30, 120)]
        total_value, selection = knapsack_solver.solve(items, 10)
        assert total_value == 50  # Half of 100
        total_weight = sum(item.weight * fraction for item, fraction in selection)
        assert total_weight == 10

    def test_items_with_same_density(self, knapsack_solver: FractionalKnapsack) -> None:
        """Test items with same value density."""
        items = [Item(10, 50), Item(20, 100), Item(30, 150)]
        total_value, selection = knapsack_solver.solve(items, 40)
        assert total_value == 200
        total_weight = sum(item.weight * fraction for item, fraction in selection)
        assert total_weight == 40

    def test_items_with_different_densities(self, knapsack_solver: FractionalKnapsack) -> None:
        """Test items with different value densities."""
        items = [Item(10, 60), Item(20, 100), Item(30, 120)]  # Densities: 6, 5, 4
        total_value, selection = knapsack_solver.solve(items, 25)
        # Should take 10 units of item 1 (60) + 15 units of item 2 (75)
        assert total_value == 135
        total_weight = sum(item.weight * fraction for item, fraction in selection)
        assert total_weight == 25

    def test_negative_capacity_raises_error(self, knapsack_solver: FractionalKnapsack) -> None:
        """Test that negative capacity raises error."""
        items = [Item(10, 60)]
        with pytest.raises(ValueError, match="Capacity cannot be negative"):
            knapsack_solver.solve(items, -10)

    def test_items_with_negative_weight_raises_error(
        self, knapsack_solver: FractionalKnapsack
    ) -> None:
        """Test that items with negative weight raise error."""
        items = [Item(-10, 60)]
        with pytest.raises(ValueError, match="Item weight and value must be non-negative"):
            knapsack_solver.solve(items, 50)

    def test_items_with_negative_value_raises_error(
        self, knapsack_solver: FractionalKnapsack
    ) -> None:
        """Test that items with negative value raise error."""
        items = [Item(10, -60)]
        with pytest.raises(ValueError, match="Item weight and value must be non-negative"):
            knapsack_solver.solve(items, 50)

    def test_items_with_zero_weight(self, knapsack_solver: FractionalKnapsack) -> None:
        """Test items with zero weight."""
        items = [Item(0, 60), Item(10, 100)]
        total_value, selection = knapsack_solver.solve(items, 10)
        # Zero weight items with positive value should be included fully
        assert total_value == 160  # 60 + 100
        assert len(selection) == 2
        assert selection[0][0] == Item(0, 60)
        assert selection[0][1] == 1.0
        assert selection[1][0] == Item(10, 100)
        assert selection[1][1] == 1.0

    def test_items_with_zero_value(self, knapsack_solver: FractionalKnapsack) -> None:
        """Test items with zero value."""
        items = [Item(10, 0), Item(10, 100)]
        total_value, selection = knapsack_solver.solve(items, 15)
        assert total_value == 100
        # Should only take the valuable item fully, and may take zero-value item partially
        assert any(item.value == 100 and fraction == 1.0 for item, fraction in selection)
        assert sum(item.weight * fraction for item, fraction in selection) == 15

    def test_float_weights_and_values(self, knapsack_solver: FractionalKnapsack) -> None:
        """Test with float weights and values."""
        items = [Item(10.5, 60.0), Item(20.0, 100.5), Item(30.5, 120.0)]
        total_value, selection = knapsack_solver.solve(items, 25.0)
        assert total_value > 0
        total_weight = sum(item.weight * fraction for item, fraction in selection)
        assert total_weight <= 25.0

    def test_large_capacity(self, knapsack_solver: FractionalKnapsack) -> None:
        """Test with large capacity."""
        items = [Item(100, 1000), Item(200, 2000), Item(300, 3000)]
        total_value, selection = knapsack_solver.solve(items, 1000)
        assert total_value == 6000
        total_weight = sum(item.weight * fraction for item, fraction in selection)
        assert total_weight == 600

    def test_optimal_selection(self, knapsack_solver: FractionalKnapsack) -> None:
        """Test that the selection is optimal."""
        items = [Item(10, 60), Item(20, 100), Item(30, 120)]  # Densities: 6, 5, 4
        total_value, _ = knapsack_solver.solve(items, 40)
        # Should take all of item 1 (10, 60) + all of item 2 (20, 100) + 10/30 of item 3 (40)
        expected_value = 60 + 100 + (120 * 10 / 30)
        assert abs(total_value - expected_value) < 0.01

    def test_zero_weight_item_with_zero_value(self, knapsack_solver: FractionalKnapsack) -> None:
        """Test items with zero weight and zero value."""
        items = [Item(0, 0), Item(10, 100)]
        total_value, selection = knapsack_solver.solve(items, 10)
        assert total_value == 100
        # Should only take the valuable item
        assert len(selection) == 1
        assert selection[0][0] == Item(10, 100)
        assert selection[0][1] == 1.0

    def test_calculate_ratio_method(self, knapsack_solver: FractionalKnapsack) -> None:
        """Test the calculate_ratio method."""
        item = Item(10, 60)
        ratio = knapsack_solver.calculate_ratio(item)
        assert ratio == 6.0

    def test_calculate_ratio_zero_weight_raises_error(
        self, knapsack_solver: FractionalKnapsack
    ) -> None:
        """Test calculate_ratio with zero weight item raises error."""
        item = Item(0, 60)
        with pytest.raises(ValueError, match="Cannot calculate ratio for zero weight item"):
            knapsack_solver.calculate_ratio(item)


class TestHuffmanCoding:
    """Test cases for Huffman Coding algorithm."""

    @pytest.fixture
    def huffman_coder(self) -> HuffmanCoding:
        """Provide HuffmanCoding instance."""
        return HuffmanCoding()

    def test_basic_huffman_coding(self, huffman_coder: HuffmanCoding) -> None:
        """Test basic Huffman coding."""
        text = "hello world"
        encoded, codes, tree = huffman_coder.compress(text)
        assert encoded is not None
        assert len(codes) > 0
        assert tree is not None

    def test_empty_text(self, huffman_coder: HuffmanCoding) -> None:
        """Test with empty text."""
        with pytest.raises(ValueError, match="Text cannot be empty"):
            huffman_coder.compress("")

    def test_single_character(self, huffman_coder: HuffmanCoding) -> None:
        """Test with single character."""
        encoded, codes, tree = huffman_coder.compress("a")
        assert encoded is not None
        assert len(codes) == 1
        assert tree is not None

    def test_repeated_characters(self, huffman_coder: HuffmanCoding) -> None:
        """Test with repeated characters."""
        text = "aaaa"
        encoded, codes, tree = huffman_coder.compress(text)
        assert encoded is not None
        assert len(codes) == 1
        assert tree is not None

    def test_all_different_characters(self, huffman_coder: HuffmanCoding) -> None:
        """Test with all different characters."""
        text = "abcdef"
        encoded, codes, tree = huffman_coder.compress(text)
        assert encoded is not None
        assert len(codes) == 6
        assert tree is not None

    def test_mixed_frequency_characters(self, huffman_coder: HuffmanCoding) -> None:
        """Test with mixed frequency characters."""
        text = "aaabbbcccc"
        encoded, codes, tree = huffman_coder.compress(text)
        assert encoded is not None
        assert len(codes) == 3
        assert tree is not None

    def test_unicode_characters(self, huffman_coder: HuffmanCoding) -> None:
        """Test with unicode characters."""
        text = "αβγδε"
        encoded, codes, tree = huffman_coder.compress(text)
        assert encoded is not None
        assert len(codes) == 5
        assert tree is not None

    def test_numbers_and_symbols(self, huffman_coder: HuffmanCoding) -> None:
        """Test with numbers and symbols."""
        text = "hello123!@#"
        encoded, codes, tree = huffman_coder.compress(text)
        assert encoded is not None
        assert len(codes) == len(set(text))
        assert tree is not None

    def test_whitespace_characters(self, huffman_coder: HuffmanCoding) -> None:
        """Test with whitespace characters."""
        text = "hello world\n\t"
        encoded, codes, tree = huffman_coder.compress(text)
        assert encoded is not None
        assert len(codes) == len(set(text))
        assert tree is not None

    def test_large_text(self, huffman_coder: HuffmanCoding) -> None:
        """Test with large text."""
        text = "hello world " * 1000
        encoded, codes, tree = huffman_coder.compress(text)
        assert encoded is not None
        assert len(codes) == len(set(text))
        assert tree is not None

    def test_compression_ratio_property(self, huffman_coder: HuffmanCoding) -> None:
        """Test that compression ratio is reasonable."""
        text = "hello world"
        encoded, codes, tree = huffman_coder.compress(text)
        ratio = huffman_coder.calculate_compression_ratio(text, encoded)
        assert 0 <= ratio <= 1

    def test_encoding_table_property(self, huffman_coder: HuffmanCoding) -> None:
        """Test that encoding table contains all unique characters."""
        text = "hello world"
        encoded, codes, tree = huffman_coder.compress(text)
        unique_chars = set(text)
        assert set(codes.keys()) == unique_chars

    def test_encoded_text_length(self, huffman_coder: HuffmanCoding) -> None:
        """Test that encoded text length is reasonable."""
        text = "hello world"
        encoded, codes, tree = huffman_coder.compress(text)
        if encoded:
            assert len(encoded) > 0

    def test_frequency_analysis(self, huffman_coder: HuffmanCoding) -> None:
        """Test that more frequent characters get shorter codes."""
        text = "aaabbbcccc"
        encoded, codes, tree = huffman_coder.compress(text)
        # 'c' should have shorter code than 'a' or 'b'
        if codes:
            c_code = codes.get("c", "")
            a_code = codes.get("a", "")
            b_code = codes.get("b", "")
            assert len(c_code) <= len(a_code)
            assert len(c_code) <= len(b_code)

    def test_decode_functionality(self, huffman_coder: HuffmanCoding) -> None:
        """Test decode functionality."""
        text = "hello world"
        encoded, codes, tree = huffman_coder.compress(text)
        # Build frequency map for decode
        freq_map: dict[str, int] = {}
        for ch in text:
            freq_map[ch] = freq_map.get(ch, 0) + 1
        decoded = huffman_coder.decode(encoded, tree, freq_map)
        assert decoded == text

    def test_special_characters_only(self, huffman_coder: HuffmanCoding) -> None:
        """Test with only special characters."""
        text = "!@#$%^&*()"
        encoded, codes, tree = huffman_coder.compress(text)
        assert encoded is not None
        assert len(codes) == len(set(text))
        assert tree is not None

    def test_mixed_case_characters(self, huffman_coder: HuffmanCoding) -> None:
        """Test with mixed case characters."""
        text = "HelloWorld"
        encoded, codes, tree = huffman_coder.compress(text)
        assert encoded is not None
        assert len(codes) == len(set(text))
        assert tree is not None

    def test_encode_character_not_in_codes(self, huffman_coder: HuffmanCoding) -> None:
        """Test encoding with character not in codes raises error."""
        codes = {"a": "0", "b": "1"}
        with pytest.raises(ValueError, match="Character 'c' not found in codes"):
            huffman_coder.encode("abc", codes)

    def test_traverse_huffman_tree_invalid_bit(self, huffman_coder: HuffmanCoding) -> None:
        """Test traverse_huffman_tree with invalid bit raises error."""
        # Create a simple tree
        node = HuffmanNode("a", 1)
        with pytest.raises(ValueError, match="Invalid bit '2' in encoded string"):
            huffman_coder._traverse_huffman_tree("2", node)

    def test_traverse_huffman_tree_path_leads_to_none(self, huffman_coder: HuffmanCoding) -> None:
        """Test traverse_huffman_tree when path leads to None raises error."""
        # Create a tree where a path leads to None
        root = HuffmanNode(None, 2)
        root.left = HuffmanNode("a", 1)
        root.right = None  # This path leads to None

        with pytest.raises(ValueError, match="Invalid encoded string: path leads to None"):
            huffman_coder._traverse_huffman_tree("1", root)

    def test_decode_with_none_tree(self, huffman_coder: HuffmanCoding) -> None:
        """Test decode with None tree raises error."""
        freq_map = {"a": 1}
        with pytest.raises(ValueError, match="Cannot decode with None tree"):
            huffman_coder.decode("0", None, freq_map)

    def test_decode_empty_encoded_string(self, huffman_coder: HuffmanCoding) -> None:
        """Test decode with empty encoded string."""
        root = HuffmanNode("a", 1)
        freq_map = {"a": 1}
        result = huffman_coder.decode("", root, freq_map)
        assert result == ""

    def test_decode_single_node_tree(self, huffman_coder: HuffmanCoding) -> None:
        """Test decode with single node tree."""
        root = HuffmanNode("a", 1)
        freq_map = {"a": 1}
        result = huffman_coder.decode("000", root, freq_map)
        assert result == "aaa"

    def test_decode_incomplete_encoded_string(self, huffman_coder: HuffmanCoding) -> None:
        """Test decode with incomplete encoded string raises error."""
        # Create a tree where traversing the encoded string leaves us at a non-leaf node
        #      *
        #     / \
        #    a   *
        #       / \
        #      b   c
        root = HuffmanNode(None, 5)
        root.left = HuffmanNode("a", 2)
        right = HuffmanNode(None, 3)
        right.left = HuffmanNode("b", 1)
        right.right = HuffmanNode("c", 2)
        root.right = right
        freq_map = {"a": 2, "b": 1, "c": 2}
        # Encoded string '1' leaves us at the right internal node (not a leaf)
        with pytest.raises(ValueError, match="Incomplete encoded string"):
            huffman_coder.decode("1", root, freq_map)

    def test_decode_incomplete_encoded_string_single_char_freq_map(
        self, huffman_coder: HuffmanCoding
    ) -> None:
        """Test decode with incomplete string but single char freq map (should not raise error)."""
        root = HuffmanNode("a", 1)
        freq_map = {"a": 1}  # Single character frequency map
        # This should not raise an error because len(freq_map) == 1
        result = huffman_coder.decode("0", root, freq_map)
        assert result == "a"

    def test_calculate_compression_ratio_empty_original(self, huffman_coder: HuffmanCoding) -> None:
        """Test compression ratio calculation with empty original string."""
        ratio = huffman_coder.calculate_compression_ratio("", "0")
        assert ratio == 0.0

    def test_huffman_node_comparison(self) -> None:
        """Test HuffmanNode comparison for heap operations."""
        node1 = HuffmanNode("a", 1)
        node2 = HuffmanNode("b", 2)
        assert node1 < node2
        assert not node2 < node1

    def test_huffman_node_repr(self) -> None:
        """Test HuffmanNode string representation."""
        node = HuffmanNode("a", 5)
        assert repr(node) == "HuffmanNode(char=a, freq=5)"

    def test_build_tree_empty_text_raises_error(self, huffman_coder: HuffmanCoding) -> None:
        """Test build_tree with empty text raises error."""
        with pytest.raises(ValueError, match="Text cannot be empty"):
            huffman_coder.build_tree("", {"a": 1})

    def test_build_tree_single_character(self, huffman_coder: HuffmanCoding) -> None:
        """Test build_tree with single character text."""
        text = "a"
        freq_map = {"a": 1}
        tree = huffman_coder.build_tree(text, freq_map)
        assert tree is not None
        assert tree.char == "a"
        assert tree.freq == 1

    def test_generate_codes_with_none_root(self, huffman_coder: HuffmanCoding) -> None:
        """Test generate_codes with None root."""
        codes = huffman_coder.generate_codes(None)
        assert codes == {}
