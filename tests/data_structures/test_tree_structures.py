"""Unit tests for tree data structures (AVL, Red-Black, and Trie)."""

from typing import Any

import pytest

from algolib.data_structures import AVLTree, Color, RedBlackTree, Trie
from algolib.data_structures.avl_tree import _AVLNode
from algolib.data_structures.red_black_tree import _RBNode


class TestAVLTree:
    """Test cases for AVL Tree self-balancing properties."""

    def is_balanced(self, tree: AVLTree[Any]) -> bool:
        """Check if AVL tree is balanced."""

        def height(node: _AVLNode[Any] | None) -> int:
            if node is None:
                return 0
            return max(height(node.left), height(node.right)) + 1

        for _ in tree.inorder():
            pass  # consume iterator to populate __dict__ maybe

        def check(node: _AVLNode[Any] | None) -> bool:
            if node is None:
                return True
            lh = height(node.left)
            rh = height(node.right)
            if abs(lh - rh) > 1:
                return False
            return check(node.left) and check(node.right)

        return check(tree._root)

    def test_avl_insert_balances(self) -> None:
        """Test that AVL tree maintains balance after insertions."""
        tree = AVLTree[int]()
        for key in [10, 20, 30, 40, 50, 25]:
            tree.insert(key)
        assert list(tree.inorder()) == [10, 20, 25, 30, 40, 50]
        assert self.is_balanced(tree)

    def test_avl_left_rotation(self) -> None:
        """Test AVL tree left rotation."""
        tree = AVLTree[int]()
        for key in [10, 20, 30]:
            tree.insert(key)
        assert list(tree.inorder()) == [10, 20, 30]
        assert self.is_balanced(tree)

    def test_avl_right_rotation(self) -> None:
        """Test AVL tree right rotation."""
        tree = AVLTree[int]()
        for key in [30, 20, 10]:
            tree.insert(key)
        assert list(tree.inorder()) == [10, 20, 30]
        assert self.is_balanced(tree)

    def test_avl_left_right_rotation(self) -> None:
        """Test AVL tree left-right rotation."""
        tree = AVLTree[int]()
        for key in [30, 10, 20]:
            tree.insert(key)
        assert list(tree.inorder()) == [10, 20, 30]
        assert self.is_balanced(tree)

    def test_avl_right_left_rotation(self) -> None:
        """Test AVL tree right-left rotation."""
        tree = AVLTree[int]()
        for key in [10, 30, 20]:
            tree.insert(key)
        assert list(tree.inorder()) == [10, 20, 30]
        assert self.is_balanced(tree)

    def test_avl_complex_insertions(self) -> None:
        """Test AVL tree with complex insertion sequence."""
        tree = AVLTree[int]()
        keys = [50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 45, 55, 65, 75, 85]
        for key in keys:
            tree.insert(key)

        # Check that tree is balanced
        assert self.is_balanced(tree)

        # Check that all keys are present
        for key in keys:
            assert tree.search(key) is True

    def test_avl_delete_maintains_balance(self) -> None:
        """Test that AVL tree maintains balance after deletions."""
        tree = AVLTree[int]()
        keys = [50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 45, 55, 65, 75, 85]
        for key in keys:
            tree.insert(key)

        # Delete some keys and check balance
        for key in [20, 40, 60, 80]:
            tree.delete(key)
            assert self.is_balanced(tree)

    def test_avl_height_property(self) -> None:
        """Test that AVL tree height is logarithmic."""
        tree = AVLTree[int]()
        for i in range(100):
            tree.insert(i)

        # AVL tree height should be O(log n)
        height = tree.height()
        assert height <= 2 * (100**0.5)  # Rough upper bound

    def test_avl_string_keys(self) -> None:
        """Test AVL tree with string keys."""
        tree = AVLTree[str]()
        keys = ["banana", "apple", "cherry", "date", "elderberry"]
        for key in keys:
            tree.insert(key)

        assert self.is_balanced(tree)
        for key in keys:
            assert tree.search(key) is True

    def test_avl_float_keys(self) -> None:
        """Test AVL tree with float keys."""
        tree = AVLTree[float]()
        keys = [3.14, 2.71, 1.41, 0.58, 2.23]
        for key in keys:
            tree.insert(key)

        assert self.is_balanced(tree)
        for key in keys:
            assert tree.search(key) is True

    def test_avl_duplicate_handling(self) -> None:
        """Test AVL tree handling of duplicate keys."""
        tree = AVLTree[int]()
        for key in [5, 3, 7, 5, 3, 7]:
            tree.insert(key)

        assert self.is_balanced(tree)
        assert tree.search(5) is True
        assert tree.search(3) is True
        assert tree.search(7) is True

    def test_avl_empty_tree(self) -> None:
        """Test AVL tree operations on empty tree."""
        tree = AVLTree[int]()
        assert tree.is_empty() is True
        assert tree.height() == 0
        assert tree.search(5) is False
        assert self.is_balanced(tree)

    def test_avl_single_node(self) -> None:
        """Test AVL tree with single node."""
        tree = AVLTree[int]()
        tree.insert(5)
        assert tree.search(5) is True
        assert tree.height() == 1
        assert self.is_balanced(tree)

    def test_avl_inorder_traversal(self) -> None:
        """Test AVL tree inorder traversal."""
        tree = AVLTree[int]()
        keys = [50, 30, 70, 20, 40, 60, 80]
        for key in keys:
            tree.insert(key)

        result = list(tree.inorder())
        expected = sorted(keys)
        assert result == expected

    def test_avl_preorder_traversal(self) -> None:
        """Test AVL tree preorder traversal."""
        tree = AVLTree[int]()
        keys = [50, 30, 70, 20, 40, 60, 80]
        for key in keys:
            tree.insert(key)

        result = list(tree.preorder())
        assert len(result) == len(keys)
        assert all(key in result for key in keys)

    def test_avl_postorder_traversal(self) -> None:
        """Test AVL tree postorder traversal."""
        tree = AVLTree[int]()
        keys = [50, 30, 70, 20, 40, 60, 80]
        for key in keys:
            tree.insert(key)

        result = list(tree.postorder())
        assert len(result) == len(keys)
        assert all(key in result for key in keys)


class TestRedBlackTree:
    """Test cases for Red-Black Tree properties."""

    def test_insertion_ordering(self) -> None:
        """Test Red-Black tree insertion ordering."""
        tree = RedBlackTree[int]()
        for key in [20, 15, 25, 10, 5]:
            tree.insert(key)
        assert list(tree.inorder()) == [5, 10, 15, 20, 25]
        # root should be black
        if tree._root:
            assert tree._root.color == Color.BLACK

    def test_red_black_properties(self) -> None:
        """Test that Red-Black tree maintains its properties."""
        tree = RedBlackTree[int]()
        keys = [50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 45, 55, 65, 75, 85]
        for key in keys:
            tree.insert(key)

        # Check that root is black
        if tree._root:
            assert tree._root.color == Color.BLACK

        # Check that red nodes have black children
        def check_red_black_property(node: _RBNode[int] | None) -> bool:
            if node is None:
                return True
            if node.color == Color.RED:
                if node.left and node.left.color == Color.RED:
                    return False
                if node.right and node.right.color == Color.RED:
                    return False
            return check_red_black_property(node.left) and check_red_black_property(node.right)

        assert check_red_black_property(tree._root)

    def test_black_height_property(self) -> None:
        """Test that all paths have same black height."""
        tree = RedBlackTree[int]()
        keys = [50, 30, 70, 20, 40, 60, 80]
        for key in keys:
            tree.insert(key)

        def get_black_height(node: _RBNode[int] | None) -> int:
            if node is None:
                return 1
            left_height = get_black_height(node.left)
            right_height = get_black_height(node.right)
            if left_height != right_height:
                return -1  # Invalid
            return left_height + (1 if node.color == Color.BLACK else 0)

        assert get_black_height(tree._root) > 0

    def test_red_black_insertion_cases(self) -> None:
        """Test various Red-Black tree insertion cases."""
        tree = RedBlackTree[int]()

        # Case 1: Insert into empty tree
        tree.insert(10)
        assert tree._root is not None
        assert tree._root.color == Color.BLACK

        # Case 2: Insert as red child of black parent
        tree.insert(5)
        tree.insert(15)

        # Case 3: Insert as red child of red parent (requires fixing)
        tree.insert(3)
        tree.insert(7)

        # Verify properties are maintained
        assert tree._root is not None
        assert tree._root.color == Color.BLACK

    def test_red_black_string_keys(self) -> None:
        """Test Red-Black tree with string keys."""
        tree = RedBlackTree[str]()
        keys = ["banana", "apple", "cherry", "date", "elderberry"]
        for key in keys:
            tree.insert(key)

        assert list(tree.inorder()) == sorted(keys)
        assert tree._root is not None
        assert tree._root.color == Color.BLACK

    def test_red_black_float_keys(self) -> None:
        """Test Red-Black tree with float keys."""
        tree = RedBlackTree[float]()
        keys = [3.14, 2.71, 1.41, 0.58, 2.23]
        for key in keys:
            tree.insert(key)

        assert list(tree.inorder()) == sorted(keys)
        assert tree._root is not None
        assert tree._root.color == Color.BLACK

    def test_red_black_duplicate_handling(self) -> None:
        """Test Red-Black tree handling of duplicate keys."""
        tree = RedBlackTree[int]()
        for key in [5, 3, 7, 5, 3, 7]:
            tree.insert(key)

        # Should handle duplicates appropriately
        assert tree.search(5) is True
        assert tree.search(3) is True
        assert tree.search(7) is True

    def test_red_black_empty_tree(self) -> None:
        """Test Red-Black tree operations on empty tree."""
        tree = RedBlackTree[int]()
        assert tree.is_empty() is True
        assert tree.search(5) is False

    def test_red_black_single_node(self) -> None:
        """Test Red-Black tree with single node."""
        tree = RedBlackTree[int]()
        tree.insert(5)
        assert tree.search(5) is True
        assert tree._root is not None
        assert tree._root.color == Color.BLACK

    def test_red_black_inorder_traversal(self) -> None:
        """Test Red-Black tree inorder traversal."""
        tree = RedBlackTree[int]()
        keys = [50, 30, 70, 20, 40, 60, 80]
        for key in keys:
            tree.insert(key)

        result = list(tree.inorder())
        expected = sorted(keys)
        assert result == expected

    def test_red_black_preorder_traversal(self) -> None:
        """Test Red-Black tree preorder traversal."""
        tree = RedBlackTree[int]()
        keys = [50, 30, 70, 20, 40, 60, 80]
        for key in keys:
            tree.insert(key)

        result = list(tree.preorder())
        assert len(result) == len(keys)
        assert all(key in result for key in keys)

    def test_red_black_postorder_traversal(self) -> None:
        """Test Red-Black tree postorder traversal."""
        tree = RedBlackTree[int]()
        keys = [50, 30, 70, 20, 40, 60, 80]
        for key in keys:
            tree.insert(key)

        result = list(tree.postorder())
        assert len(result) == len(keys)
        assert all(key in result for key in keys)

    def test_red_black_complex_operations(self) -> None:
        """Test Red-Black tree with complex operations."""
        tree = RedBlackTree[int]()
        keys = [50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 45, 55, 65, 75, 85]

        # Insert all keys
        for key in keys:
            tree.insert(key)

        # Verify all keys are present
        for key in keys:
            assert tree.search(key) is True

        # Delete some keys
        for key in [20, 40, 60, 80]:
            tree.delete(key)
            assert tree.search(key) is False

        # Verify remaining keys
        remaining_keys = [k for k in keys if k not in [20, 40, 60, 80]]
        for key in remaining_keys:
            assert tree.search(key) is True

    def test_red_black_find_min_max(self) -> None:
        """Test Red-Black tree find_min and find_max methods."""
        tree = RedBlackTree[int]()
        keys = [50, 30, 70, 20, 40, 60, 80]
        for key in keys:
            tree.insert(key)

        assert tree.find_min() == min(keys)
        assert tree.find_max() == max(keys)

    def test_red_black_find_min_max_empty_tree(self) -> None:
        """Test find_min and find_max on empty Red-Black tree."""
        tree = RedBlackTree[int]()
        with pytest.raises(ValueError, match="Tree is empty"):
            tree.find_min()
        with pytest.raises(ValueError, match="Tree is empty"):
            tree.find_max()

    def test_red_black_height(self) -> None:
        """Test Red-Black tree height method."""
        tree = RedBlackTree[int]()
        assert tree.height() == 0  # Empty tree

        tree.insert(5)
        assert tree.height() >= 1  # Single node

        tree.insert(3)
        tree.insert(7)
        assert tree.height() >= 2  # Multiple nodes

    def test_red_black_size(self) -> None:
        """Test Red-Black tree size method."""
        tree = RedBlackTree[int]()
        assert tree.size() == 0

        tree.insert(5)
        assert tree.size() == 1

        tree.insert(3)
        tree.insert(7)
        assert tree.size() == 3

    def test_red_black_clear(self) -> None:
        """Test Red-Black tree clear method."""
        tree = RedBlackTree[int]()
        tree.insert(5)
        tree.insert(3)
        tree.insert(7)

        assert not tree.is_empty()
        tree.clear()
        assert tree.is_empty()
        assert tree.size() == 0

    def test_red_black_len_method(self) -> None:
        """Test Red-Black tree __len__ method."""
        tree = RedBlackTree[int]()
        assert len(tree) == 0

        tree.insert(5)
        assert len(tree) == 1

        tree.insert(3)
        tree.insert(7)
        assert len(tree) == 3

    def test_red_black_repr_method(self) -> None:
        """Test Red-Black tree __repr__ method."""
        tree = RedBlackTree[int]()
        result = repr(tree)
        assert "RedBlackTree" in result

        tree.insert(5)
        result = repr(tree)
        assert "RedBlackTree" in result

    def test_red_black_delete_nonexistent_key(self) -> None:
        """Test deleting a key that doesn't exist in Red-Black tree."""
        tree = RedBlackTree[int]()
        tree.insert(5)
        tree.insert(3)
        tree.insert(7)

        # Try to delete a key that doesn't exist
        result = tree.delete(10)
        assert result is False
        assert tree.size() == 3  # Size should remain the same

    def test_red_black_delete_from_empty_tree(self) -> None:
        """Test deleting from an empty Red-Black tree."""
        tree = RedBlackTree[int]()
        result = tree.delete(5)
        assert result is False


class TestTrie:
    """Test cases for Trie data structure."""

    @pytest.fixture
    def trie(self) -> Trie:
        """Provide empty Trie instance."""
        return Trie()

    def test_basic_operations(self, trie: Trie) -> None:
        """Test basic Trie operations."""
        words = ["apple", "app", "application", "banana"]
        for w in words:
            trie.insert(w)

        assert trie.search("apple") is True
        assert trie.search("app") is True
        assert trie.search("apples") is False
        assert trie.starts_with("appl") is True
        assert trie.starts_with("ban") is True
        assert trie.starts_with("cat") is False

    def test_empty_trie(self, trie: Trie) -> None:
        """Test operations on empty Trie."""
        assert trie.search("") is False
        assert trie.search("any") is False
        # Empty string is prefix of everything
        assert trie.starts_with("") is True
        assert trie.starts_with("any") is False

    def test_insert_empty_string(self, trie: Trie) -> None:
        """Test inserting empty string."""
        trie.insert("")
        assert trie.search("") is True
        assert trie.starts_with("") is True

    def test_insert_single_character(self, trie: Trie) -> None:
        """Test inserting single character."""
        trie.insert("a")
        assert trie.search("a") is True
        assert trie.search("b") is False
        assert trie.starts_with("a") is True
        assert trie.starts_with("b") is False

    def test_insert_duplicate_words(self, trie: Trie) -> None:
        """Test inserting duplicate words."""
        trie.insert("apple")
        trie.insert("apple")
        assert trie.search("apple") is True
        assert trie.search("app") is False

    def test_prefix_search(self, trie: Trie) -> None:
        """Test prefix search functionality."""
        words = ["apple", "app", "application", "banana", "band", "bandana"]
        for word in words:
            trie.insert(word)

        # Test various prefixes
        assert trie.starts_with("app") is True
        assert trie.starts_with("ban") is True
        assert trie.starts_with("cat") is False
        # Empty string is prefix of everything
        assert trie.starts_with("") is True

    def test_case_sensitivity(self, trie: Trie) -> None:
        """Test case sensitivity."""
        trie.insert("Apple")
        assert trie.search("Apple") is True
        assert trie.search("apple") is False
        assert trie.starts_with("App") is True
        assert trie.starts_with("app") is False

    def test_numbers_as_strings(self, trie: Trie) -> None:
        """Test Trie with numbers as strings."""
        numbers = ["123", "12", "1234", "456", "45"]
        for num in numbers:
            trie.insert(num)

        assert trie.search("123") is True
        assert trie.search("12") is True
        assert trie.search("1234") is True
        assert trie.search("456") is True
        assert trie.search("789") is False

    def test_special_characters(self, trie: Trie) -> None:
        """Test Trie with special characters."""
        words = ["hello-world", "hello_world", "hello.world", "hello world"]
        for word in words:
            trie.insert(word)

        assert trie.search("hello-world") is True
        assert trie.search("hello_world") is True
        assert trie.search("hello.world") is True
        assert trie.search("hello world") is True
        assert trie.search("hello") is False

    def test_unicode_strings(self, trie: Trie) -> None:
        """Test Trie with unicode strings."""
        words = ["αβγ", "αβ", "αβγδε", "δεζ", "δεζη"]
        for word in words:
            trie.insert(word)

        assert trie.search("αβγ") is True
        assert trie.search("αβ") is True
        assert trie.search("δεζ") is True
        assert trie.search("αβγδε") is True
        assert trie.search("xyz") is False

    def test_large_number_of_words(self, trie: Trie) -> None:
        """Test Trie with large number of words."""
        words = [f"word{i}" for i in range(1000)]
        for word in words:
            trie.insert(word)

        # Test some random words
        assert trie.search("word0") is True
        assert trie.search("word999") is True
        assert trie.search("word1000") is False
        assert trie.starts_with("word") is True
        assert trie.starts_with("xyz") is False

    def test_nested_prefixes(self, trie: Trie) -> None:
        """Test Trie with nested prefixes."""
        words = ["a", "ab", "abc", "abcd", "abcde"]
        for word in words:
            trie.insert(word)

        # Test that all prefixes work
        assert trie.starts_with("a") is True
        assert trie.starts_with("ab") is True
        assert trie.starts_with("abc") is True
        assert trie.starts_with("abcd") is True
        assert trie.starts_with("abcde") is True
        assert trie.starts_with("abcdef") is False

    def test_word_boundaries(self, trie: Trie) -> None:
        """Test Trie word boundaries."""
        trie.insert("cat")
        trie.insert("cats")
        trie.insert("catnip")

        assert trie.search("cat") is True
        assert trie.search("cats") is True
        assert trie.search("catnip") is True
        assert trie.search("c") is False
        assert trie.search("ca") is False

    def test_prefix_with_exact_match(self, trie: Trie) -> None:
        """Test that exact matches also work as prefixes."""
        trie.insert("hello")
        trie.insert("world")

        assert trie.search("hello") is True
        assert trie.starts_with("hello") is True
        assert trie.search("world") is True
        assert trie.starts_with("world") is True

    def test_empty_string_handling(self, trie: Trie) -> None:
        """Test handling of empty strings."""
        trie.insert("")
        trie.insert("hello")

        assert trie.search("") is True
        assert trie.search("hello") is True
        assert trie.starts_with("") is True
        assert trie.starts_with("h") is True

    def test_single_character_words(self, trie: Trie) -> None:
        """Test Trie with single character words."""
        chars = ["a", "b", "c", "d", "e"]
        for char in chars:
            trie.insert(char)

        for char in chars:
            assert trie.search(char) is True
            assert trie.starts_with(char) is True

        assert trie.search("f") is False
        assert trie.starts_with("f") is False

    def test_very_long_words(self, trie: Trie) -> None:
        """Test Trie with very long words."""
        long_word = "a" * 1000
        trie.insert(long_word)

        assert trie.search(long_word) is True
        assert trie.starts_with("a" * 500) is True
        assert trie.search("a" * 999) is False
        assert trie.search("a" * 1001) is False
