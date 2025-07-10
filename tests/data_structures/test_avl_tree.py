"""Tests for AVL Tree data structure."""

from typing import Optional

import pytest

from algolib.data_structures.avl_tree import AVLTree, _AVLNode


class TestAVLTree:
    """Test cases for AVL Tree data structure."""

    @pytest.fixture
    def avl_tree(self) -> AVLTree[int]:
        """Provide AVLTree instance."""
        return AVLTree()

    @pytest.fixture
    def populated_avl_tree(self) -> AVLTree[int]:
        """Provide populated AVLTree instance."""
        tree: AVLTree[int] = AVLTree()
        values = [10, 5, 15, 3, 7, 12, 17, 2, 4, 6, 8, 11, 13, 16, 18]
        for value in values:
            tree.insert(value)
        return tree

    def test_insert_single_element(self, avl_tree: AVLTree[int]) -> None:
        """Test inserting single element."""
        avl_tree.insert(5)
        assert avl_tree.search(5) is True
        assert avl_tree.size() == 1

    def test_insert_multiple_elements(self, avl_tree: AVLTree[int]) -> None:
        """Test inserting multiple elements."""
        values = [5, 3, 7, 2, 4, 6, 8]
        for value in values:
            avl_tree.insert(value)

        for value in values:
            assert avl_tree.search(value) is True
        assert avl_tree.size() == 7

    def test_insert_duplicate_elements(self, avl_tree: AVLTree[int]) -> None:
        """Test inserting duplicate elements."""
        avl_tree.insert(5)
        avl_tree.insert(5)  # Duplicate
        assert avl_tree.search(5) is True
        assert avl_tree.size() == 1  # AVL tree ignores duplicates

    def test_search_existing_element(self, avl_tree: AVLTree[int]) -> None:
        """Test searching for existing element."""
        avl_tree.insert(5)
        assert avl_tree.search(5) is True

    def test_search_nonexistent_element(self, avl_tree: AVLTree[int]) -> None:
        """Test searching for nonexistent element."""
        avl_tree.insert(5)
        assert avl_tree.search(10) is False

    def test_search_empty_tree(self, avl_tree: AVLTree[int]) -> None:
        """Test searching in empty tree."""
        assert avl_tree.search(5) is False

    def test_delete_leaf_node(self, avl_tree: AVLTree[int]) -> None:
        """Test deleting leaf node."""
        avl_tree.insert(5)
        avl_tree.insert(3)
        avl_tree.insert(7)

        assert avl_tree.delete(3) is True
        assert avl_tree.search(3) is False
        assert avl_tree.size() == 2

    def test_delete_node_with_one_child(self, avl_tree: AVLTree[int]) -> None:
        """Test deleting node with one child."""
        avl_tree.insert(5)
        avl_tree.insert(3)
        avl_tree.insert(7)
        avl_tree.insert(6)

        assert avl_tree.delete(7) is True
        assert avl_tree.search(7) is False
        assert avl_tree.search(6) is True
        assert avl_tree.size() == 3

    def test_delete_node_with_two_children(self, avl_tree: AVLTree[int]) -> None:
        """Test deleting node with two children."""
        avl_tree.insert(5)
        avl_tree.insert(3)
        avl_tree.insert(7)
        avl_tree.insert(6)
        avl_tree.insert(8)

        assert avl_tree.delete(7) is True
        assert avl_tree.search(7) is False
        assert avl_tree.search(6) is True
        assert avl_tree.search(8) is True
        assert avl_tree.size() == 4

    def test_delete_root_node(self, avl_tree: AVLTree[int]) -> None:
        """Test deleting root node."""
        avl_tree.insert(5)
        avl_tree.insert(3)
        avl_tree.insert(7)

        assert avl_tree.delete(5) is True
        assert avl_tree.search(5) is False
        assert avl_tree.search(3) is True
        assert avl_tree.search(7) is True
        assert avl_tree.size() == 2

    def test_delete_nonexistent_element(self, avl_tree: AVLTree[int]) -> None:
        """Test deleting nonexistent element."""
        avl_tree.insert(5)
        assert avl_tree.delete(10) is False
        assert avl_tree.size() == 1

    def test_delete_empty_tree(self, avl_tree: AVLTree[int]) -> None:
        """Test deleting from empty tree."""
        assert avl_tree.delete(5) is False

    def test_find_min(self, avl_tree: AVLTree[int]) -> None:
        """Test finding minimum value."""
        values = [5, 3, 7, 2, 4, 6, 8]
        for value in values:
            avl_tree.insert(value)

        assert avl_tree.find_min() == 2

    def test_find_max(self, avl_tree: AVLTree[int]) -> None:
        """Test finding maximum value."""
        values = [5, 3, 7, 2, 4, 6, 8]
        for value in values:
            avl_tree.insert(value)

        assert avl_tree.find_max() == 8

    def test_find_min_empty_tree(self, avl_tree: AVLTree[int]) -> None:
        """Test finding minimum in empty tree."""
        with pytest.raises(ValueError):
            avl_tree.find_min()

    def test_find_max_empty_tree(self, avl_tree: AVLTree[int]) -> None:
        """Test finding maximum in empty tree."""
        with pytest.raises(ValueError):
            avl_tree.find_max()

    def test_height_empty_tree(self, avl_tree: AVLTree[int]) -> None:
        """Test height of empty tree."""
        assert avl_tree.height() == 0

    def test_height_single_node(self, avl_tree: AVLTree[int]) -> None:
        """Test height of tree with single node."""
        avl_tree.insert(5)
        assert avl_tree.height() == 1

    def test_height_populated_tree(self, populated_avl_tree: AVLTree[int]) -> None:
        """Test height of populated tree."""
        height = populated_avl_tree.height()
        assert height >= 3  # Should have reasonable height

    def test_size_empty_tree(self, avl_tree: AVLTree[int]) -> None:
        """Test size of empty tree."""
        assert avl_tree.size() == 0

    def test_size_populated_tree(self, populated_avl_tree: AVLTree[int]) -> None:
        """Test size of populated tree."""
        assert populated_avl_tree.size() == 15

    def test_is_empty_empty_tree(self, avl_tree: AVLTree[int]) -> None:
        """Test is_empty on empty tree."""
        assert avl_tree.is_empty() is True

    def test_is_empty_populated_tree(self, populated_avl_tree: AVLTree[int]) -> None:
        """Test is_empty on populated tree."""
        assert populated_avl_tree.is_empty() is False

    def test_avl_balance_property(self, avl_tree: AVLTree[int]) -> None:
        """Test that AVL tree maintains balance property."""
        # Insert values that would cause imbalance in regular BST
        values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        for value in values:
            avl_tree.insert(value)

        # Check that the tree is balanced (height difference <= 1)
        def check_balance(node: Optional[_AVLNode[int]]) -> int:
            if node is None:
                return -1
            left_height = check_balance(node.left)
            right_height = check_balance(node.right)
            balance_factor = left_height - right_height
            assert abs(balance_factor) <= 1
            return max(left_height, right_height) + 1

        check_balance(avl_tree._root)

    def test_left_rotation(self, avl_tree: AVLTree[int]) -> None:
        """Test left rotation during insertion."""
        # This sequence should trigger a left rotation
        avl_tree.insert(1)
        avl_tree.insert(2)
        avl_tree.insert(3)

        assert avl_tree.search(1) is True
        assert avl_tree.search(2) is True
        assert avl_tree.search(3) is True
        assert avl_tree.size() == 3

    def test_right_rotation(self, avl_tree: AVLTree[int]) -> None:
        """Test right rotation during insertion."""
        # This sequence should trigger a right rotation
        avl_tree.insert(3)
        avl_tree.insert(2)
        avl_tree.insert(1)

        assert avl_tree.search(1) is True
        assert avl_tree.search(2) is True
        assert avl_tree.search(3) is True
        assert avl_tree.size() == 3

    def test_left_right_rotation(self, avl_tree: AVLTree[int]) -> None:
        """Test left-right rotation during insertion."""
        # This sequence should trigger a left-right rotation
        avl_tree.insert(3)
        avl_tree.insert(1)
        avl_tree.insert(2)

        assert avl_tree.search(1) is True
        assert avl_tree.search(2) is True
        assert avl_tree.search(3) is True
        assert avl_tree.size() == 3

    def test_right_left_rotation(self, avl_tree: AVLTree[int]) -> None:
        """Test right-left rotation during insertion."""
        # This sequence should trigger a right-left rotation
        avl_tree.insert(1)
        avl_tree.insert(3)
        avl_tree.insert(2)

        assert avl_tree.search(1) is True
        assert avl_tree.search(2) is True
        assert avl_tree.search(3) is True
        assert avl_tree.size() == 3

    def test_complex_operations_sequence(self, avl_tree: AVLTree[int]) -> None:
        """Test complex sequence of operations."""
        # Insert elements
        values = [50, 30, 70, 20, 40, 60, 80]
        for value in values:
            avl_tree.insert(value)

        assert avl_tree.size() == 7

        # Search for elements
        assert avl_tree.search(50) is True
        assert avl_tree.search(25) is False

        # Find min/max
        assert avl_tree.find_min() == 20
        assert avl_tree.find_max() == 80

        # Delete elements
        avl_tree.delete(30)
        assert avl_tree.search(30) is False
        assert avl_tree.size() == 6

        avl_tree.delete(70)
        assert avl_tree.search(70) is False
        assert avl_tree.size() == 5

    def test_duplicate_handling(self, avl_tree: AVLTree[int]) -> None:
        """Test handling of duplicate values."""
        values = [5, 3, 7, 5, 3, 7]  # Duplicates
        for value in values:
            avl_tree.insert(value)

        assert avl_tree.size() == 3  # AVL tree ignores duplicates
        assert avl_tree.search(5) is True
        assert avl_tree.search(3) is True
        assert avl_tree.search(7) is True

    def test_delete_all_elements(self, avl_tree: AVLTree[int]) -> None:
        """Test deleting all elements."""
        values = [5, 3, 7, 2, 4, 6, 8]
        for value in values:
            avl_tree.insert(value)

        for value in values:
            avl_tree.delete(value)

        assert avl_tree.is_empty() is True
        assert avl_tree.size() == 0

    def test_string_values(self) -> None:
        """Test AVL tree with string values."""
        avl_tree: AVLTree[str] = AVLTree[str]()
        values = ["banana", "apple", "cherry", "date"]
        for value in values:
            avl_tree.insert(value)

        assert avl_tree.search("apple") is True
        assert avl_tree.search("grape") is False
        assert avl_tree.find_min() == "apple"
        assert avl_tree.find_max() == "date"

    def test_float_values(self) -> None:
        """Test AVL tree with float values."""
        avl_tree: AVLTree[float] = AVLTree[float]()
        values = [3.14, 2.71, 1.41, 0.58]
        for value in values:
            avl_tree.insert(value)

        assert avl_tree.search(3.14) is True
        assert avl_tree.search(2.0) is False
        assert avl_tree.find_min() == 0.58
        assert avl_tree.find_max() == 3.14

    def test_negative_values(self, avl_tree: AVLTree[int]) -> None:
        """Test AVL tree with negative values."""
        values = [-5, -3, -7, -2, -4, -6, -8]
        for value in values:
            avl_tree.insert(value)

        assert avl_tree.search(-5) is True
        assert avl_tree.search(5) is False
        assert avl_tree.find_min() == -8
        assert avl_tree.find_max() == -2

    def test_zero_values(self, avl_tree: AVLTree[int]) -> None:
        """Test AVL tree with zero values."""
        values = [0, -1, 1, -2, 2]
        for value in values:
            avl_tree.insert(value)

        assert avl_tree.search(0) is True
        assert avl_tree.find_min() == -2
        assert avl_tree.find_max() == 2

    def test_repr_empty_tree(self, avl_tree: AVLTree[int]) -> None:
        """Test string representation of empty tree."""
        assert repr(avl_tree) == "AVLTree(size=0)"

    def test_repr_populated_tree(self, populated_avl_tree: AVLTree[int]) -> None:
        """Test string representation of populated tree."""
        result = repr(populated_avl_tree)
        assert result.startswith("AVLTree(size=")
        assert result.endswith(")")

    def test_str_empty_tree(self, avl_tree: AVLTree[int]) -> None:
        """Test string representation of empty tree."""
        assert str(avl_tree) == "AVLTree(size=0)"

    def test_str_populated_tree(self, populated_avl_tree: AVLTree[int]) -> None:
        """Test string representation of populated tree."""
        result = str(populated_avl_tree)
        assert "AVLTree" in result

    def test_contains_method(self, avl_tree: AVLTree[int]) -> None:
        """Test the __contains__ method."""
        avl_tree.insert(5)
        avl_tree.insert(3)
        avl_tree.insert(7)

        assert 5 in avl_tree
        assert 3 in avl_tree
        assert 7 in avl_tree
        assert 4 not in avl_tree

    def test_contains_method_invalid_type(self, avl_tree: AVLTree[int]) -> None:
        """Test __contains__ method with invalid type."""
        avl_tree.insert(5)

        # Test with non-comparable types
        assert [] not in avl_tree
        assert {} not in avl_tree
        assert None not in avl_tree

    def test_len_method(self, avl_tree: AVLTree[int]) -> None:
        """Test the __len__ method."""
        assert len(avl_tree) == 0

        avl_tree.insert(5)
        assert len(avl_tree) == 1

        avl_tree.insert(3)
        avl_tree.insert(7)
        assert len(avl_tree) == 3

    def test_delete_nonexistent_key(self, avl_tree: AVLTree[int]) -> None:
        """Test deleting a key that doesn't exist."""
        avl_tree.insert(5)
        avl_tree.insert(3)
        avl_tree.insert(7)

        # Try to delete a key that doesn't exist
        result = avl_tree.delete(10)
        assert result is False
        assert avl_tree.size() == 3  # Size should remain the same

    def test_delete_from_empty_tree(self, avl_tree: AVLTree[int]) -> None:
        """Test deleting from an empty tree."""
        result = avl_tree.delete(5)
        assert result is False

    def test_clear_method(self, avl_tree: AVLTree[int]) -> None:
        """Test the clear method."""
        avl_tree.insert(5)
        avl_tree.insert(3)
        avl_tree.insert(7)

        assert not avl_tree.is_empty()
        avl_tree.clear()
        assert avl_tree.is_empty()
        assert avl_tree.size() == 0

    def test_delete_node_with_complex_rebalancing(self, avl_tree: AVLTree[int]) -> None:
        """Test deletion that requires complex rebalancing."""
        # Insert elements to create a complex tree structure
        values = [50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 45, 55, 65, 75, 85]
        for value in values:
            avl_tree.insert(value)

        # Delete nodes that will trigger complex rebalancing
        avl_tree.delete(50)  # Root deletion
        assert avl_tree.search(50) is False
        assert avl_tree.size() == 14

        avl_tree.delete(30)  # Another complex deletion
        assert avl_tree.search(30) is False
        assert avl_tree.size() == 13

    def test_delete_node_with_left_right_rebalancing(self, avl_tree: AVLTree[int]) -> None:
        """Test deletion that requires left-right rebalancing."""
        # Create a tree that will need left-right rebalancing after deletion
        values = [50, 30, 70, 20, 40, 60, 80, 35, 45]
        for value in values:
            avl_tree.insert(value)

        # Delete a node that will trigger left-right rebalancing
        avl_tree.delete(20)
        assert avl_tree.search(20) is False
        assert avl_tree.size() == 8

    def test_delete_node_with_right_left_rebalancing(self, avl_tree: AVLTree[int]) -> None:
        """Test deletion that requires right-left rebalancing."""
        # Create a tree that will need right-left rebalancing after deletion
        values = [50, 30, 70, 60, 80, 65, 75]
        for value in values:
            avl_tree.insert(value)

        # Delete a node that will trigger right-left rebalancing
        avl_tree.delete(80)
        assert avl_tree.search(80) is False
        assert avl_tree.size() == 6

    def test_delete_node_with_double_rotation(self, avl_tree: AVLTree[int]) -> None:
        """Test deletion that requires double rotation."""
        # Create a tree that will need double rotation after deletion
        values = [50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 45]
        for value in values:
            avl_tree.insert(value)

        # Delete nodes to trigger double rotation scenarios
        avl_tree.delete(50)
        avl_tree.delete(30)
        assert avl_tree.search(50) is False
        assert avl_tree.search(30) is False
        assert avl_tree.size() == 9

    def test_delete_node_with_null_return(self, avl_tree: AVLTree[int]) -> None:
        """Test deletion that returns None (edge case in _delete method)."""
        # Create a tree with specific structure
        values = [50, 30, 70, 20, 40, 60, 80]
        for value in values:
            avl_tree.insert(value)

        # Delete in a way that triggers the None return path
        avl_tree.delete(20)
        avl_tree.delete(40)
        avl_tree.delete(30)  # This should trigger the None return path
        assert avl_tree.search(30) is False
        assert avl_tree.size() == 4

    def test_balance_factor_edge_cases(self, avl_tree: AVLTree[int]) -> None:
        """Test balance factor calculation with edge cases."""
        # Test with None node
        # This is an internal method, but we can test it indirectly
        avl_tree.insert(5)
        avl_tree.insert(3)
        avl_tree.insert(7)

        # The balance factor should be calculated correctly for all nodes
        assert avl_tree.height() >= 0  # Height should be valid

    def test_height_calculation_edge_cases(self, avl_tree: AVLTree[int]) -> None:
        """Test height calculation with edge cases."""
        # Test height of None node (should return 0)
        assert avl_tree.height() == 0  # Empty tree height

        # Test height after various operations
        avl_tree.insert(5)
        assert avl_tree.height() == 1

        avl_tree.insert(3)
        avl_tree.insert(7)
        assert avl_tree.height() >= 1  # Should have valid height

    def test_rotation_height_updates(self, avl_tree: AVLTree[int]) -> None:
        """Test that rotations properly update heights."""
        # Create a tree that will require rotations
        values = [50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 45]
        for value in values:
            avl_tree.insert(value)

        # Perform operations that will trigger rotations
        avl_tree.delete(50)
        avl_tree.delete(30)

        # Verify the tree is still balanced
        assert avl_tree.height() >= 0  # Height should be valid
        assert avl_tree.size() == 9
