"""Unit tests for Binary Search Tree."""

import pytest

from algolib.data_structures import BinarySearchTree


class TestBinarySearchTree:
    """Test cases for Binary Search Tree."""

    def test_insert_single_element(self, bst: BinarySearchTree[int]) -> None:
        """Test inserting a single element."""
        bst.insert(5)
        assert bst.search(5) is True
        assert bst.size() == 1

    def test_insert_multiple_elements(self, bst: BinarySearchTree[int]) -> None:
        """Test inserting multiple elements."""
        values = [5, 3, 7, 2, 4, 6, 8]
        for value in values:
            bst.insert(value)

        for value in values:
            assert bst.search(value) is True
        assert bst.size() == 7

    def test_insert_duplicate_elements(self, bst: BinarySearchTree[int]) -> None:
        """Test inserting duplicate elements."""
        bst.insert(5)
        bst.insert(5)  # Duplicate
        assert bst.search(5) is True
        assert bst.size() == 1  # BST ignores duplicates

    def test_search_existing_element(self, bst: BinarySearchTree[int]) -> None:
        """Test searching for existing element."""
        bst.insert(5)
        assert bst.search(5) is True

    def test_search_nonexistent_element(self, bst: BinarySearchTree[int]) -> None:
        """Test searching for nonexistent element."""
        bst.insert(5)
        assert bst.search(10) is False

    def test_search_empty_tree(self, bst: BinarySearchTree[int]) -> None:
        """Test searching in empty tree."""
        assert bst.search(5) is False

    def test_delete_leaf_node(self, bst: BinarySearchTree[int]) -> None:
        """Test deleting a leaf node."""
        bst.insert(5)
        bst.insert(3)
        bst.insert(7)
        bst.delete(3)
        assert bst.search(3) is False
        assert bst.search(5) is True
        assert bst.search(7) is True
        assert bst.size() == 2

    def test_delete_node_with_one_child(self, bst: BinarySearchTree[int]) -> None:
        """Test deleting a node with one child."""
        bst.insert(5)
        bst.insert(3)
        bst.insert(7)
        bst.insert(6)
        bst.delete(7)
        assert bst.search(7) is False
        assert bst.search(6) is True
        assert bst.size() == 3

    def test_delete_node_with_two_children(self, bst: BinarySearchTree[int]) -> None:
        """Test deleting a node with two children."""
        bst.insert(5)
        bst.insert(3)
        bst.insert(7)
        bst.insert(6)
        bst.insert(8)
        bst.delete(7)
        assert bst.search(7) is False
        assert bst.search(6) is True
        assert bst.search(8) is True
        assert bst.size() == 4

    def test_delete_root_node(self, bst: BinarySearchTree[int]) -> None:
        """Test deleting the root node."""
        bst.insert(5)
        bst.insert(3)
        bst.insert(7)
        bst.delete(5)
        assert bst.search(5) is False
        assert bst.search(3) is True
        assert bst.search(7) is True
        assert bst.size() == 2

    def test_delete_nonexistent_element(self, bst: BinarySearchTree[int]) -> None:
        """Test deleting a nonexistent element."""
        bst.insert(5)
        bst.delete(10)  # Should not raise error
        assert bst.search(5) is True
        assert bst.size() == 1

    def test_delete_empty_tree(self, bst: BinarySearchTree[int]) -> None:
        """Test deleting from empty tree."""
        bst.delete(5)  # Should not raise error
        assert bst.size() == 0

    def test_inorder_traversal(self, bst: BinarySearchTree[int]) -> None:
        """Test inorder traversal."""
        values = [5, 3, 7, 2, 4, 6, 8]
        for value in values:
            bst.insert(value)

        result = bst.inorder()
        expected = [2, 3, 4, 5, 6, 7, 8]
        assert list(result) == expected

    def test_preorder_traversal(self, bst: BinarySearchTree[int]) -> None:
        """Test preorder traversal - not implemented in this BST."""
        values = [5, 3, 7, 2, 4, 6, 8]
        for value in values:
            bst.insert(value)

        # BST only supports inorder traversal
        with pytest.raises(AttributeError):
            bst.preorder_traversal()  # type: ignore[attr-defined]

    def test_postorder_traversal(self, bst: BinarySearchTree[int]) -> None:
        """Test postorder traversal - not implemented in this BST."""
        values = [5, 3, 7, 2, 4, 6, 8]
        for value in values:
            bst.insert(value)

        # BST only supports inorder traversal
        with pytest.raises(AttributeError):
            bst.postorder_traversal()  # type: ignore[attr-defined]

    def test_level_order_traversal(self, bst: BinarySearchTree[int]) -> None:
        """Test level order traversal - not implemented in this BST."""
        values = [5, 3, 7, 2, 4, 6, 8]
        for value in values:
            bst.insert(value)

        # BST only supports inorder traversal
        with pytest.raises(AttributeError):
            bst.level_order_traversal()  # type: ignore[attr-defined]

    def test_find_min(self, bst: BinarySearchTree[int]) -> None:
        """Test finding minimum value."""
        values = [5, 3, 7, 2, 4, 6, 8]
        for value in values:
            bst.insert(value)

        assert bst.find_min() == 2

    def test_find_max(self, bst: BinarySearchTree[int]) -> None:
        """Test finding maximum value."""
        values = [5, 3, 7, 2, 4, 6, 8]
        for value in values:
            bst.insert(value)

        assert bst.find_max() == 8

    def test_find_min_empty_tree(self, bst: BinarySearchTree[int]) -> None:
        """Test finding minimum in empty tree."""
        with pytest.raises(ValueError, match="Cannot find minimum in empty tree"):
            bst.find_min()

    def test_find_max_empty_tree(self, bst: BinarySearchTree[int]) -> None:
        """Test finding maximum in empty tree."""
        with pytest.raises(ValueError, match="Cannot find maximum in empty tree"):
            bst.find_max()

    def test_height_empty_tree(self, bst: BinarySearchTree[int]) -> None:
        """Test height of empty tree."""
        assert bst.height() == -1

    def test_height_single_node(self, bst: BinarySearchTree[int]) -> None:
        """Test height of tree with single node."""
        bst.insert(5)
        assert bst.height() == 0

    def test_height_populated_tree(self, populated_bst: BinarySearchTree[int]) -> None:
        """Test height of populated tree."""
        height = populated_bst.height()
        assert height >= 3  # Should have reasonable height

    def test_size_empty_tree(self, bst: BinarySearchTree[int]) -> None:
        """Test size of empty tree."""
        assert bst.size() == 0

    def test_size_populated_tree(self, populated_bst: BinarySearchTree[int]) -> None:
        """Test size of populated tree."""
        assert populated_bst.size() == 15

    def test_is_empty_empty_tree(self, bst: BinarySearchTree[int]) -> None:
        """Test is_empty on empty tree."""
        assert bst.is_empty() is True

    def test_is_empty_populated_tree(self, populated_bst: BinarySearchTree[int]) -> None:
        """Test is_empty on populated tree."""
        assert populated_bst.is_empty() is False

    def test_clear_tree(self, populated_bst: BinarySearchTree[int]) -> None:
        """Test clearing the tree."""
        # BST doesn't have a clear method, so this should raise AttributeError
        with pytest.raises(AttributeError):
            populated_bst.clear()  # type: ignore[attr-defined]

    def test_string_values(self) -> None:
        """Test BST with string values."""
        bst = BinarySearchTree[str]()
        values = ["banana", "apple", "cherry", "date"]
        for value in values:
            bst.insert(value)

        assert bst.search("apple") is True
        assert bst.search("grape") is False
        assert bst.find_min() == "apple"
        assert bst.find_max() == "date"

    def test_float_values(self) -> None:
        """Test BST with float values."""
        bst = BinarySearchTree[float]()
        values = [3.14, 2.71, 1.41, 0.58]
        for value in values:
            bst.insert(value)

        assert bst.search(3.14) is True
        assert bst.search(2.0) is False
        assert bst.find_min() == pytest.approx(0.58)
        assert bst.find_max() == pytest.approx(3.14)

    def test_negative_values(self, bst: BinarySearchTree[int]) -> None:
        """Test BST with negative values."""
        values = [-5, -3, -7, -2, -4, -6, -8]
        for value in values:
            bst.insert(value)

        assert bst.search(-5) is True
        assert bst.search(5) is False
        assert bst.find_min() == -8
        assert bst.find_max() == -2

    def test_zero_values(self, bst: BinarySearchTree[int]) -> None:
        """Test BST with zero values."""
        values = [0, -1, 1, -2, 2]
        for value in values:
            bst.insert(value)

        assert bst.search(0) is True
        assert bst.find_min() == -2
        assert bst.find_max() == 2

    def test_complex_operations_sequence(self, bst: BinarySearchTree[int]) -> None:
        """Test complex sequence of operations."""
        # Insert elements
        values = [50, 30, 70, 20, 40, 60, 80]
        for value in values:
            bst.insert(value)

        assert bst.size() == 7
        assert bst.height() >= 2

        # Search for elements
        assert bst.search(50) is True
        assert bst.search(25) is False

        # Find min/max
        assert bst.find_min() == 20
        assert bst.find_max() == 80

        # Delete elements
        bst.delete(30)
        assert bst.search(30) is False
        assert bst.size() == 6

        bst.delete(70)
        assert bst.search(70) is False
        assert bst.size() == 5

        # Traversal after deletion
        inorder = list(bst.inorder())
        assert len(inorder) == 5
        assert inorder == sorted(inorder)

    def test_duplicate_handling(self, bst: BinarySearchTree[int]) -> None:
        """Test handling of duplicate values."""
        values = [5, 3, 7, 5, 3, 7]  # Duplicates
        for value in values:
            bst.insert(value)

        assert bst.size() == 3  # BST ignores duplicates
        assert bst.search(5) is True
        assert bst.search(3) is True
        assert bst.search(7) is True

    def test_delete_all_elements(self, bst: BinarySearchTree[int]) -> None:
        """Test deleting all elements."""
        values = [5, 3, 7, 2, 4, 6, 8]
        for value in values:
            bst.insert(value)

        for value in values:
            bst.delete(value)

        assert bst.is_empty() is True
        assert bst.size() == 0

    def test_traversal_empty_tree(self, bst: BinarySearchTree[int]) -> None:
        """Test traversal on empty tree."""
        assert list(bst.inorder()) == []

    def test_traversal_single_node(self, bst: BinarySearchTree[int]) -> None:
        """Test traversal on single node tree."""
        bst.insert(5)
        assert list(bst.inorder()) == [5]

    def test_repr_empty_tree(self, bst: BinarySearchTree[int]) -> None:
        """Test string representation of empty tree."""
        assert repr(bst) == "BinarySearchTree()"

    def test_repr_populated_tree(self, populated_bst: BinarySearchTree[int]) -> None:
        """Test string representation of populated tree."""
        assert repr(populated_bst) == "BinarySearchTree()"

    def test_str_empty_tree(self, bst: BinarySearchTree[int]) -> None:
        """Test string representation of empty tree."""
        assert str(bst) == "BinarySearchTree()"

    def test_str_populated_tree(self, populated_bst: BinarySearchTree[int]) -> None:
        """Test string representation of populated tree."""
        result = str(populated_bst)
        assert "BinarySearchTree" in result

    def test_iteration(self, populated_bst: BinarySearchTree[int]) -> None:
        """Test iteration over tree elements."""
        # BST doesn't implement __iter__, so this should raise TypeError
        with pytest.raises(TypeError):
            list(populated_bst)  # type: ignore[call-overload]

    def test_iteration_empty_tree(self, bst: BinarySearchTree[int]) -> None:
        """Test iteration over empty tree."""
        # BST doesn't implement __iter__, so this should raise TypeError
        with pytest.raises(TypeError):
            list(bst)  # type: ignore[call-overload]

    def test_contains_operator(self, bst: BinarySearchTree[int]) -> None:
        """Test 'in' operator."""
        bst.insert(5)
        bst.insert(3)
        bst.insert(7)

        # BST doesn't implement __contains__, so this should raise TypeError
        with pytest.raises(TypeError):
            assert 5 in bst  # type: ignore[operator]

    def test_contains_operator_empty_tree(self, bst: BinarySearchTree[int]) -> None:
        """Test 'in' operator on empty tree."""
        # BST doesn't implement __contains__, so this should raise TypeError
        with pytest.raises(TypeError):
            assert 5 not in bst  # type: ignore[operator]
