"""Tests for Binary Tree data structure."""

import pytest

from algolib.data_structures.binary_tree import BinaryTree


class TestBinaryTree:
    """Test cases for Binary Tree data structure."""

    @pytest.fixture
    def binary_tree(self) -> BinaryTree[int]:
        """Provide BinaryTree instance."""
        return BinaryTree()

    @pytest.fixture
    def populated_binary_tree(self) -> BinaryTree[int]:
        """Provide populated BinaryTree instance."""
        tree: BinaryTree[int] = BinaryTree()
        values = [10, 5, 15, 3, 7, 12, 17, 2, 4, 6, 8, 11, 13, 16, 18]
        for value in values:
            tree.insert(value)
        return tree

    def test_insert_single_element(self, binary_tree: BinaryTree[int]) -> None:
        """Test inserting single element."""
        binary_tree.insert(5)
        assert binary_tree.search(5) is True
        assert binary_tree.size() == 1

    def test_insert_multiple_elements(self, binary_tree: BinaryTree[int]) -> None:
        """Test inserting multiple elements."""
        values = [5, 3, 7, 2, 4, 6, 8]
        for value in values:
            binary_tree.insert(value)

        for value in values:
            assert binary_tree.search(value) is True
        assert binary_tree.size() == 7

    def test_insert_duplicate_elements(self, binary_tree: BinaryTree[int]) -> None:
        """Test inserting duplicate elements."""
        binary_tree.insert(5)
        binary_tree.insert(5)  # Duplicate
        assert binary_tree.search(5) is True
        assert binary_tree.size() == 2  # Binary tree allows duplicates

    def test_search_existing_element(self, binary_tree: BinaryTree[int]) -> None:
        """Test searching for existing element."""
        binary_tree.insert(5)
        assert binary_tree.search(5) is True

    def test_search_nonexistent_element(self, binary_tree: BinaryTree[int]) -> None:
        """Test searching for non-existent element."""
        values = [5, 3, 7, 2, 4, 6, 8]
        for value in values:
            binary_tree.insert(value)

        assert binary_tree.search(10) is False
        assert binary_tree.search(-1) is False
        assert binary_tree.search(100) is False

    def test_search_empty_tree(self, binary_tree: BinaryTree[int]) -> None:
        """Test searching in empty tree."""
        assert binary_tree.search(5) is False
        assert binary_tree.search(0) is False

    def test_height_empty_tree(self, binary_tree: BinaryTree[int]) -> None:
        """Test height of empty tree."""
        assert binary_tree.height() == -1

    def test_height_single_node(self, binary_tree: BinaryTree[int]) -> None:
        """Test height of tree with single node."""
        binary_tree.insert(5)
        assert binary_tree.height() == 0

    def test_height_multiple_nodes(self, binary_tree: BinaryTree[int]) -> None:
        """Test height of tree with multiple nodes."""
        values = [5, 3, 7, 2, 4, 6, 8]
        for value in values:
            binary_tree.insert(value)

        # Height should be at least 2 for this tree structure
        assert binary_tree.height() >= 2

    def test_size_empty_tree(self, binary_tree: BinaryTree[int]) -> None:
        """Test size of empty tree."""
        assert binary_tree.size() == 0

    def test_size_populated_tree(self, populated_binary_tree: BinaryTree[int]) -> None:
        """Test size of populated tree."""
        assert populated_binary_tree.size() == 15

    def test_is_empty_empty_tree(self, binary_tree: BinaryTree[int]) -> None:
        """Test is_empty on empty tree."""
        assert binary_tree.is_empty() is True

    def test_is_empty_populated_tree(self, populated_binary_tree: BinaryTree[int]) -> None:
        """Test is_empty on populated tree."""
        assert populated_binary_tree.is_empty() is False

    def test_len_function(self, binary_tree: BinaryTree[int]) -> None:
        """Test len() function on binary tree."""
        assert len(binary_tree) == 0
        binary_tree.insert(5)
        assert len(binary_tree) == 1
        binary_tree.insert(3)
        binary_tree.insert(7)
        assert len(binary_tree) == 3

    def test_duplicate_handling(self, binary_tree: BinaryTree[int]) -> None:
        """Test handling of duplicate values."""
        values = [5, 3, 7, 5, 3, 7]  # Duplicates
        for value in values:
            binary_tree.insert(value)

        assert binary_tree.size() == 6  # Binary tree allows duplicates
        assert binary_tree.search(5) is True
        assert binary_tree.search(3) is True
        assert binary_tree.search(7) is True

    def test_tree_properties(self, binary_tree: BinaryTree[int]) -> None:
        """Test basic tree properties."""
        # Test empty tree
        assert binary_tree.is_empty() is True
        assert binary_tree.size() == 0
        assert binary_tree.height() == -1

        # Test single node
        binary_tree.insert(5)
        assert binary_tree.is_empty() is False
        assert binary_tree.size() == 1
        assert binary_tree.height() == 0

        # Test multiple nodes
        binary_tree.insert(3)
        binary_tree.insert(7)
        assert binary_tree.size() == 3
        assert binary_tree.height() == 1

    def test_inorder_traversal(self, binary_tree: BinaryTree[int]) -> None:
        """Test inorder traversal."""
        values = [5, 3, 7, 2, 4, 6, 8]
        for value in values:
            binary_tree.insert(value)

        result = binary_tree.inorder()
        expected = [2, 3, 4, 5, 6, 7, 8]
        assert list(result) == expected

    def test_preorder_traversal(self, binary_tree: BinaryTree[int]) -> None:
        """Test preorder traversal."""
        values = [5, 3, 7, 2, 4, 6, 8]
        for value in values:
            binary_tree.insert(value)

        result = binary_tree.preorder()
        expected = [5, 3, 2, 4, 7, 6, 8]
        assert list(result) == expected

    def test_postorder_traversal(self, binary_tree: BinaryTree[int]) -> None:
        """Test postorder traversal."""
        values = [5, 3, 7, 2, 4, 6, 8]
        for value in values:
            binary_tree.insert(value)

        result = binary_tree.postorder()
        expected = [2, 4, 3, 6, 8, 7, 5]
        assert list(result) == expected

    def test_level_order_traversal(self, binary_tree: BinaryTree[int]) -> None:
        """Test level-order traversal of binary tree."""
        values = [5, 3, 7, 2, 4, 6, 8]
        for value in values:
            binary_tree.insert(value)

        level_order = list(binary_tree.levelorder())
        # Level-order should visit nodes level by level
        assert level_order == [5, 3, 7, 2, 4, 6, 8]

    def test_traversal_empty_tree(self, binary_tree: BinaryTree[int]) -> None:
        """Test traversals on empty tree."""
        assert list(binary_tree.inorder()) == []
        assert list(binary_tree.preorder()) == []
        assert list(binary_tree.postorder()) == []
        assert list(binary_tree.levelorder()) == []

    def test_traversal_single_node(self, binary_tree: BinaryTree[int]) -> None:
        """Test traversals on tree with single node."""
        binary_tree.insert(5)
        assert list(binary_tree.inorder()) == [5]
        assert list(binary_tree.preorder()) == [5]
        assert list(binary_tree.postorder()) == [5]
        assert list(binary_tree.levelorder()) == [5]

    def test_complex_operations_sequence(self, binary_tree: BinaryTree[int]) -> None:
        """Test complex sequence of operations on binary tree."""
        # Insert elements
        values = [50, 30, 70, 20, 40, 60, 80]
        for value in values:
            binary_tree.insert(value)

        assert binary_tree.size() == 7
        assert binary_tree.search(50) is True
        assert binary_tree.search(90) is False

        # Test traversals
        inorder = list(binary_tree.inorder())
        assert len(inorder) == 7

        preorder = list(binary_tree.preorder())
        assert len(preorder) == 7

        postorder = list(binary_tree.postorder())
        assert len(postorder) == 7

        levelorder = list(binary_tree.levelorder())
        assert len(levelorder) == 7

    def test_string_values(self, binary_tree: BinaryTree[str]) -> None:
        """Test binary tree with string values."""
        values = ["banana", "apple", "cherry", "date"]
        for value in values:
            binary_tree.insert(value)

        assert binary_tree.search("apple") is True
        assert binary_tree.search("grape") is False

        inorder = list(binary_tree.inorder())
        assert len(inorder) == 4

    def test_float_values(self, binary_tree: BinaryTree[float]) -> None:
        """Test binary tree with float values."""
        values = [3.14, 2.71, 1.41, 0.58]
        for value in values:
            binary_tree.insert(value)

        assert binary_tree.search(3.14) is True
        assert binary_tree.search(2.0) is False

        inorder = list(binary_tree.inorder())
        assert len(inorder) == 4

    def test_negative_values(self, binary_tree: BinaryTree[int]) -> None:
        """Test binary tree with negative values."""
        values = [-5, -3, -7, -2, -4, -6, -8]
        for value in values:
            binary_tree.insert(value)

        assert binary_tree.search(-5) is True
        assert binary_tree.search(5) is False

        inorder = list(binary_tree.inorder())
        assert len(inorder) == 7

    def test_zero_values(self, binary_tree: BinaryTree[int]) -> None:
        """Test binary tree with zero values."""
        values = [0, -1, 1, -2, 2]
        for value in values:
            binary_tree.insert(value)

        assert binary_tree.search(0) is True
        assert binary_tree.search(3) is False

        inorder = list(binary_tree.inorder())
        assert len(inorder) == 5

    def test_traversal_consistency(self, binary_tree: BinaryTree[int]) -> None:
        """Test that traversals are consistent."""
        values = [5, 3, 7, 2, 4, 6, 8]
        for value in values:
            binary_tree.insert(value)

        # Inorder should give sorted order
        inorder = list(binary_tree.inorder())
        assert inorder == sorted(values)

        # Preorder should start with root
        preorder = list(binary_tree.preorder())
        assert preorder[0] == 5

        # Postorder should end with root
        postorder = list(binary_tree.postorder())
        assert postorder[-1] == 5

        # Level order should have root first
        level_order = list(binary_tree.levelorder())
        assert level_order[0] == 5
