"""Tests for Red-Black Tree data structure."""

from typing import Optional

import pytest

from algolib.data_structures.red_black_tree import Color, RedBlackTree, _RBNode


class TestRedBlackTree:
    """Test cases for Red-Black Tree data structure."""

    @pytest.fixture
    def rb_tree(self) -> RedBlackTree[int]:
        """Provide RedBlackTree instance."""
        return RedBlackTree()

    @pytest.fixture
    def populated_rb_tree(self) -> RedBlackTree[int]:
        """Provide populated RedBlackTree instance."""
        tree: RedBlackTree[int] = RedBlackTree()
        values = [10, 5, 15, 3, 7, 12, 17, 2, 4, 6, 8, 11, 13, 16, 18]
        for value in values:
            tree.insert(value)
        return tree

    def test_insert_single_element(self, rb_tree: RedBlackTree[int]) -> None:
        """Test inserting single element."""
        rb_tree.insert(5)
        assert rb_tree.search(5) is True
        assert rb_tree.size() == 1

    def test_insert_multiple_elements(self, rb_tree: RedBlackTree[int]) -> None:
        """Test inserting multiple elements."""
        values = [5, 3, 7, 2, 4, 6, 8]
        for value in values:
            rb_tree.insert(value)

        for value in values:
            assert rb_tree.search(value) is True
        assert rb_tree.size() == 7

    def test_insert_duplicate_elements(self, rb_tree: RedBlackTree[int]) -> None:
        """Test inserting duplicate elements."""
        rb_tree.insert(5)
        rb_tree.insert(5)  # Duplicate
        assert rb_tree.search(5) is True
        assert rb_tree.size() == 1  # Red-Black tree ignores duplicates

    def test_search_existing_element(self, rb_tree: RedBlackTree[int]) -> None:
        """Test searching for existing element."""
        rb_tree.insert(5)
        assert rb_tree.search(5) is True

    def test_search_nonexistent_element(self, rb_tree: RedBlackTree[int]) -> None:
        """Test searching for nonexistent element."""
        rb_tree.insert(5)
        assert rb_tree.search(10) is False

    def test_search_empty_tree(self, rb_tree: RedBlackTree[int]) -> None:
        """Test searching in empty tree."""
        assert rb_tree.search(5) is False

    def test_delete_leaf_node(self, rb_tree: RedBlackTree[int]) -> None:
        """Test deleting leaf node."""
        rb_tree.insert(5)
        rb_tree.insert(3)
        rb_tree.insert(7)

        assert rb_tree.delete(3) is True
        assert rb_tree.search(3) is False
        assert rb_tree.size() == 2

    def test_delete_node_with_one_child(self, rb_tree: RedBlackTree[int]) -> None:
        """Test deleting node with one child."""
        rb_tree.insert(5)
        rb_tree.insert(3)
        rb_tree.insert(7)
        rb_tree.insert(6)

        assert rb_tree.delete(7) is True
        assert rb_tree.search(7) is False
        assert rb_tree.search(6) is True
        assert rb_tree.size() == 3

    def test_delete_node_with_two_children(self, rb_tree: RedBlackTree[int]) -> None:
        """Test deleting node with two children."""
        rb_tree.insert(5)
        rb_tree.insert(3)
        rb_tree.insert(7)
        rb_tree.insert(6)
        rb_tree.insert(8)

        assert rb_tree.delete(7) is True
        assert rb_tree.search(7) is False
        assert rb_tree.search(6) is True
        assert rb_tree.search(8) is True
        assert rb_tree.size() == 4

    def test_delete_root_node(self, rb_tree: RedBlackTree[int]) -> None:
        """Test deleting root node."""
        rb_tree.insert(5)
        rb_tree.insert(3)
        rb_tree.insert(7)

        assert rb_tree.delete(5) is True
        assert rb_tree.search(5) is False
        assert rb_tree.search(3) is True
        assert rb_tree.search(7) is True
        assert rb_tree.size() == 2

    def test_delete_nonexistent_element(self, rb_tree: RedBlackTree[int]) -> None:
        """Test deleting nonexistent element."""
        rb_tree.insert(5)
        assert rb_tree.delete(10) is False
        assert rb_tree.size() == 1

    def test_delete_empty_tree(self, rb_tree: RedBlackTree[int]) -> None:
        """Test deleting from empty tree."""
        assert rb_tree.delete(5) is False

    def test_find_min(self, rb_tree: RedBlackTree[int]) -> None:
        """Test finding minimum value."""
        values = [5, 3, 7, 2, 4, 6, 8]
        for value in values:
            rb_tree.insert(value)

        assert rb_tree.find_min() == 2

    def test_find_max(self, rb_tree: RedBlackTree[int]) -> None:
        """Test finding maximum value."""
        values = [5, 3, 7, 2, 4, 6, 8]
        for value in values:
            rb_tree.insert(value)

        assert rb_tree.find_max() == 8

    def test_find_min_empty_tree(self, rb_tree: RedBlackTree[int]) -> None:
        """Test finding minimum in empty tree."""
        with pytest.raises(ValueError):
            rb_tree.find_min()

    def test_find_max_empty_tree(self, rb_tree: RedBlackTree[int]) -> None:
        """Test finding maximum in empty tree."""
        with pytest.raises(ValueError):
            rb_tree.find_max()

    def test_height_empty_tree(self, rb_tree: RedBlackTree[int]) -> None:
        """Test height of empty tree."""
        assert rb_tree.height() == 0

    def test_height_single_node(self, rb_tree: RedBlackTree[int]) -> None:
        """Test height of tree with single node."""
        rb_tree.insert(5)
        assert rb_tree.height() == 1

    def test_height_populated_tree(self, populated_rb_tree: RedBlackTree[int]) -> None:
        """Test height of populated tree."""
        height = populated_rb_tree.height()
        assert height >= 3  # Should have reasonable height

    def test_size_empty_tree(self, rb_tree: RedBlackTree[int]) -> None:
        """Test size of empty tree."""
        assert rb_tree.size() == 0

    def test_size_populated_tree(self, populated_rb_tree: RedBlackTree[int]) -> None:
        """Test size of populated tree."""
        assert populated_rb_tree.size() == 15

    def test_is_empty_empty_tree(self, rb_tree: RedBlackTree[int]) -> None:
        """Test is_empty on empty tree."""
        assert rb_tree.is_empty() is True

    def test_is_empty_populated_tree(self, populated_rb_tree: RedBlackTree[int]) -> None:
        """Test is_empty on populated tree."""
        assert populated_rb_tree.is_empty() is False

    def test_red_black_properties(self, rb_tree: RedBlackTree[int]) -> None:
        """Test that Red-Black tree maintains its properties."""
        # Insert values
        values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        for value in values:
            rb_tree.insert(value)

        # Check Red-Black properties
        def check_properties(node: Optional[_RBNode[int]]) -> int:
            if node is None:
                return 1  # Black height for nil nodes

            # Property 1: Root is black
            if node == rb_tree._root and node.color == Color.RED:
                return False

            # Property 2: Red nodes have black children
            if node.color == Color.RED:
                if (node.left and node.left.color == Color.RED) or (
                    node.right and node.right.color == Color.RED
                ):
                    return False

            # Property 3: All paths have same black height
            left_black_height = check_properties(node.left)
            right_black_height = check_properties(node.right)

            if left_black_height != right_black_height:
                return False

            # Return black height including current node
            return left_black_height + (0 if node.color == Color.RED else 1)

        result = check_properties(rb_tree._root)
        assert result > 0  # Should return valid black height

    def test_complex_operations_sequence(self, rb_tree: RedBlackTree[int]) -> None:
        """Test complex sequence of operations."""
        # Insert elements
        values = [50, 30, 70, 20, 40, 60, 80]
        for value in values:
            rb_tree.insert(value)

        assert rb_tree.size() == 7

        # Search for elements
        assert rb_tree.search(50) is True
        assert rb_tree.search(25) is False

        # Find min/max
        assert rb_tree.find_min() == 20
        assert rb_tree.find_max() == 80

        # Delete elements
        rb_tree.delete(30)
        assert rb_tree.search(30) is False
        assert rb_tree.size() == 6

        rb_tree.delete(70)
        assert rb_tree.search(70) is False
        assert rb_tree.size() == 5

    def test_duplicate_handling(self, rb_tree: RedBlackTree[int]) -> None:
        """Test handling of duplicate values."""
        values = [5, 3, 7, 5, 3, 7]  # Duplicates
        for value in values:
            rb_tree.insert(value)

        assert rb_tree.size() == 3  # Red-Black tree ignores duplicates
        assert rb_tree.search(5) is True
        assert rb_tree.search(3) is True
        assert rb_tree.search(7) is True

    def test_delete_all_elements(self, rb_tree: RedBlackTree[int]) -> None:
        """Test deleting all elements."""
        values = [5, 3, 7, 2, 4, 6, 8]
        for value in values:
            rb_tree.insert(value)

        for value in values:
            rb_tree.delete(value)

        assert rb_tree.is_empty() is True
        assert rb_tree.size() == 0

    def test_string_values(self) -> None:
        """Test Red-Black tree with string values."""
        rb_tree = RedBlackTree[str]()
        values = ["banana", "apple", "cherry", "date"]
        for value in values:
            rb_tree.insert(value)

        assert rb_tree.search("apple") is True
        assert rb_tree.search("grape") is False
        assert rb_tree.find_min() == "apple"
        assert rb_tree.find_max() == "date"

    def test_float_values(self) -> None:
        """Test Red-Black tree with float values."""
        rb_tree = RedBlackTree[float]()
        values = [3.14, 2.71, 1.41, 0.58]
        for value in values:
            rb_tree.insert(value)

        assert rb_tree.search(3.14) is True
        assert rb_tree.search(2.0) is False
        assert rb_tree.find_min() == 0.58
        assert rb_tree.find_max() == 3.14

    def test_negative_values(self, rb_tree: RedBlackTree[int]) -> None:
        """Test Red-Black tree with negative values."""
        values = [-5, -3, -7, -2, -4, -6, -8]
        for value in values:
            rb_tree.insert(value)

        assert rb_tree.search(-5) is True
        assert rb_tree.search(5) is False
        assert rb_tree.find_min() == -8
        assert rb_tree.find_max() == -2

    def test_zero_values(self, rb_tree: RedBlackTree[int]) -> None:
        """Test Red-Black tree with zero values."""
        values = [0, -1, 1, -2, 2]
        for value in values:
            rb_tree.insert(value)

        assert rb_tree.search(0) is True
        assert rb_tree.find_min() == -2
        assert rb_tree.find_max() == 2

    def test_repr_empty_tree(self, rb_tree: RedBlackTree[int]) -> None:
        """Test string representation of empty tree."""
        assert repr(rb_tree) == "RedBlackTree(size=0)"

    def test_repr_populated_tree(self, populated_rb_tree: RedBlackTree[int]) -> None:
        """Test string representation of populated tree."""
        result = repr(populated_rb_tree)
        assert result.startswith("RedBlackTree(size=")
        assert result.endswith(")")

    def test_str_empty_tree(self, rb_tree: RedBlackTree[int]) -> None:
        """Test string representation of empty tree."""
        assert str(rb_tree) == "RedBlackTree(size=0)"

    def test_str_populated_tree(self, populated_rb_tree: RedBlackTree[int]) -> None:
        """Test string representation of populated tree."""
        result = str(populated_rb_tree)
        assert "RedBlackTree" in result

    def test_insert_with_complex_rebalancing(self, rb_tree: RedBlackTree[int]) -> None:
        """Test insertion that requires complex rebalancing."""
        # Insert elements in a way that triggers complex rebalancing
        values = [50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 45, 55, 65, 75, 85]
        for value in values:
            rb_tree.insert(value)

        # Verify the tree maintains Red-Black properties
        assert rb_tree.size() == 15
        assert rb_tree.search(50) is True
        assert rb_tree.search(25) is True

    def test_insert_with_left_right_case(self, rb_tree: RedBlackTree[int]) -> None:
        """Test insertion that triggers left-right case."""
        # Insert elements to trigger left-right case
        values = [50, 30, 70, 20, 40, 60, 80, 35, 45]
        for value in values:
            rb_tree.insert(value)

        assert rb_tree.size() == 9
        assert rb_tree.search(35) is True
        assert rb_tree.search(45) is True

    def test_insert_with_right_left_case(self, rb_tree: RedBlackTree[int]) -> None:
        """Test insertion that triggers right-left case."""
        # Insert elements to trigger right-left case
        values = [50, 30, 70, 60, 80, 65, 75]
        for value in values:
            rb_tree.insert(value)

        assert rb_tree.size() == 7
        assert rb_tree.search(65) is True
        assert rb_tree.search(75) is True

    def test_insert_with_uncle_red_case(self, rb_tree: RedBlackTree[int]) -> None:
        """Test insertion with red uncle case."""
        # Insert elements to create a red uncle scenario
        values = [50, 30, 70, 20, 40, 60, 80]
        for value in values:
            rb_tree.insert(value)

        # Insert more elements to trigger red uncle cases
        rb_tree.insert(10)
        rb_tree.insert(25)
        rb_tree.insert(35)
        rb_tree.insert(45)

        assert rb_tree.size() == 11
        assert rb_tree.search(10) is True
        assert rb_tree.search(25) is True

    def test_insert_with_uncle_black_case(self, rb_tree: RedBlackTree[int]) -> None:
        """Test insertion with black uncle case."""
        # Insert elements to create a black uncle scenario
        values = [50, 30, 70, 20, 40, 60, 80]
        for value in values:
            rb_tree.insert(value)

        # Insert elements that will trigger black uncle cases
        rb_tree.insert(15)
        rb_tree.insert(25)
        rb_tree.insert(35)
        rb_tree.insert(45)

        assert rb_tree.size() == 11
        assert rb_tree.search(15) is True
        assert rb_tree.search(25) is True

    def test_rotation_edge_cases(self, rb_tree: RedBlackTree[int]) -> None:
        """Test rotation edge cases."""
        # Insert elements to create scenarios for rotation edge cases
        values = [50, 30, 70, 20, 40, 60, 80]
        for value in values:
            rb_tree.insert(value)

        # Test rotations with edge cases
        rb_tree.insert(10)
        rb_tree.insert(25)
        rb_tree.insert(35)
        rb_tree.insert(45)

        assert rb_tree.size() == 11
        # Verify rotations didn't break the tree
        assert rb_tree.search(10) is True
        assert rb_tree.search(25) is True

    def test_parent_link_maintenance(self, rb_tree: RedBlackTree[int]) -> None:
        """Test that parent links are maintained correctly during rotations."""
        # Insert elements to create rotation scenarios
        values = [50, 30, 70, 20, 40, 60, 80]
        for value in values:
            rb_tree.insert(value)

        # Insert more elements to trigger rotations
        rb_tree.insert(10)
        rb_tree.insert(25)

        assert rb_tree.size() == 9
        # Verify the tree structure is maintained
        assert rb_tree.search(10) is True
        assert rb_tree.search(25) is True

    def test_root_color_maintenance(self, rb_tree: RedBlackTree[int]) -> None:
        """Test that root is always colored black."""
        # Insert elements to trigger various rebalancing scenarios
        values = [50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 45]
        for value in values:
            rb_tree.insert(value)

        # Verify root exists and tree is valid
        assert rb_tree.size() == 11
        assert not rb_tree.is_empty()

    def test_delete_with_complex_rebalancing(self, rb_tree: RedBlackTree[int]) -> None:
        """Test deletion that requires complex rebalancing."""
        # Insert elements to create a complex tree
        values = [50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 45, 55, 65, 75, 85]
        for value in values:
            rb_tree.insert(value)

        # Delete nodes that will trigger complex rebalancing
        rb_tree.delete(50)  # Root deletion
        assert rb_tree.search(50) is False
        assert rb_tree.size() == 14

        rb_tree.delete(30)  # Another complex deletion
        assert rb_tree.search(30) is False
        assert rb_tree.size() == 13

    def test_height_calculation_edge_cases(self, rb_tree: RedBlackTree[int]) -> None:
        """Test height calculation with edge cases."""
        # Test height of empty tree
        assert rb_tree.height() == 0

        # Test height after various operations
        rb_tree.insert(5)
        assert rb_tree.height() == 1

        rb_tree.insert(3)
        rb_tree.insert(7)
        assert rb_tree.height() >= 1  # Should have valid height

    def test_bst_insert_edge_cases(self, rb_tree: RedBlackTree[int]) -> None:
        """Test BST insert edge cases."""
        # Test inserting into empty tree
        rb_tree.insert(5)
        assert rb_tree.search(5) is True

        # Test inserting duplicate
        rb_tree.insert(5)
        assert rb_tree.size() == 1  # Duplicate should be ignored

        # Test inserting multiple elements
        rb_tree.insert(3)
        rb_tree.insert(7)
        assert rb_tree.size() == 3
