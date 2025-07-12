"""Binary Search Tree (BST) data structure implementation."""

from dataclasses import dataclass, field
from typing import Generic, Iterator, Optional

from algolib._typing import ComparableT


@dataclass(slots=True)
class BSTNode(Generic[ComparableT]):
    """Node class for binary search tree."""

    data: ComparableT
    left: Optional["BSTNode[ComparableT]"] = field(default=None, repr=False)
    right: Optional["BSTNode[ComparableT]"] = field(default=None, repr=False)


@dataclass(slots=True, init=False)
class BinarySearchTree(Generic[ComparableT]):
    """Binary Search Tree (BST) data structure.

    A binary search tree is a binary tree where for each node:
    - All nodes in the left subtree have values less than the node's value
    - All nodes in the right subtree have values greater than the node's value
    - Both subtrees are also binary search trees

    Time Complexities (average case for balanced tree):
        - insert: O(log n) - logarithmic insertion
        - search: O(log n) - logarithmic search
        - delete: O(log n) - logarithmic deletion
        - find_min/find_max: O(log n) - logarithmic extrema finding

    Time Complexities (worst case for unbalanced tree):
        - All operations: O(n) - degenerates to linear search

    Space Complexity: O(n) - where n is the number of nodes

    Advantages:
        - Efficient searching, insertion, and deletion
        - In-order traversal gives sorted sequence
        - No duplicate values (by design)
        - Dynamic size

    Disadvantages:
        - Can become unbalanced, leading to poor performance
        - No guaranteed O(log n) performance without balancing
        - More complex than simple arrays or lists

    Common use cases:
        - Database indexing
        - Expression parsing
        - Priority queues
        - Autocomplete systems
        - File system organization

    Example:
        >>> bst = BinarySearchTree[int]()
        >>> bst.insert(5)
        >>> bst.insert(3)
        >>> bst.insert(7)
        >>> bst.insert(1)
        >>> print(list(bst.inorder()))  # Output: [1, 3, 5, 7]
        >>> print(bst.search(3))        # Output: True
        >>> print(bst.find_min())       # Output: 1
    """

    _root: Optional[BSTNode[ComparableT]]

    def __init__(self) -> None:
        """Initialize an empty binary search tree."""
        self._root = None

    def insert(self, data: ComparableT) -> None:
        """Insert a new node with the given data into the BST.

        Maintains the BST property by inserting in the correct position.
        Duplicates are ignored (no insertion occurs).

        Args:
            data: The data to insert into the tree

        Example:
            >>> bst = BinarySearchTree[int]()
            >>> bst.insert(10)
            >>> bst.insert(5)
            >>> bst.insert(15)
            >>> print(bst.size())  # Output: 3
        """
        self._root = self._insert_recursive(self._root, data)

    def _insert_recursive(
        self, node: Optional[BSTNode[ComparableT]], data: ComparableT
    ) -> BSTNode[ComparableT]:
        """Helper method for recursive insertion."""
        if node is None:
            return BSTNode(data)

        if data < node.data:
            node.left = self._insert_recursive(node.left, data)
        elif data > node.data:
            node.right = self._insert_recursive(node.right, data)
        # If data == node.data, we ignore duplicates

        return node

    def search(self, data: ComparableT) -> bool:
        """Search for a node with the given data in the BST.

        Args:
            data: The data to search for

        Returns:
            True if the data is found, False otherwise

        Example:
            >>> bst = BinarySearchTree[int]()
            >>> bst.insert(10)
            >>> bst.insert(5)
            >>> print(bst.search(5))   # Output: True
            >>> print(bst.search(15))  # Output: False
        """
        return self._search_recursive(self._root, data)

    def _search_recursive(self, node: Optional[BSTNode[ComparableT]], data: ComparableT) -> bool:
        """Helper method for recursive search."""
        if node is None:
            return False

        if data == node.data:
            return True
        elif data < node.data:
            return self._search_recursive(node.left, data)
        else:
            return self._search_recursive(node.right, data)

    def delete(self, data: ComparableT) -> bool:
        """Delete a node with the given data from the BST.

        Args:
            data: The data to delete from the tree

        Returns:
            True if the node was found and deleted, False otherwise

        Example:
            >>> bst = BinarySearchTree[int]()
            >>> bst.insert(10)
            >>> bst.insert(5)
            >>> bst.insert(15)
            >>> success = bst.delete(5)
            >>> print(success)  # Output: True
            >>> print(bst.search(5))  # Output: False
        """
        if not self.search(data):
            return False

        self._root = self._delete_recursive(self._root, data)
        return True

    def _delete_recursive(
        self, node: Optional[BSTNode[ComparableT]], data: ComparableT
    ) -> Optional[BSTNode[ComparableT]]:
        """Helper method for recursive deletion."""
        if node is None:
            return None

        if data < node.data:
            node.left = self._delete_recursive(node.left, data)
        elif data > node.data:
            node.right = self._delete_recursive(node.right, data)
        else:
            # Node to be deleted found
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                # Node has two children
                successor = self._find_min_node(node.right)
                node.data = successor.data
                node.right = self._delete_recursive(node.right, successor.data)

        return node

    def find_min(self) -> ComparableT:
        """Find the minimum value in the BST.

        Returns:
            The minimum value in the tree

        Raises:
            ValueError: If the tree is empty

        Example:
            >>> bst = BinarySearchTree[int]()
            >>> bst.insert(10)
            >>> bst.insert(5)
            >>> bst.insert(15)
            >>> print(bst.find_min())  # Output: 5
        """
        if self._root is None:
            raise ValueError("Cannot find minimum in empty tree")

        return self._find_min_node(self._root).data

    def _find_min_node(self, node: BSTNode[ComparableT]) -> BSTNode[ComparableT]:
        """Helper method to find the node with minimum value."""
        while node.left is not None:
            node = node.left
        return node

    def find_max(self) -> ComparableT:
        """Find the maximum value in the BST.

        Returns:
            The maximum value in the tree

        Raises:
            ValueError: If the tree is empty

        Example:
            >>> bst = BinarySearchTree[int]()
            >>> bst.insert(10)
            >>> bst.insert(5)
            >>> bst.insert(15)
            >>> print(bst.find_max())  # Output: 15
        """
        if self._root is None:
            raise ValueError("Cannot find maximum in empty tree")

        return self._find_max_node(self._root).data

    def _find_max_node(self, node: BSTNode[ComparableT]) -> BSTNode[ComparableT]:
        """Helper method to find the node with maximum value."""
        while node.right is not None:
            node = node.right
        return node

    def inorder(self) -> Iterator[ComparableT]:
        """In-order traversal of the BST (returns values in sorted order).

        Yields:
            Data from nodes in sorted order

        Example:
            >>> bst = BinarySearchTree[int]()
            >>> bst.insert(5)
            >>> bst.insert(3)
            >>> bst.insert(7)
            >>> bst.insert(1)
            >>> list(bst.inorder())  # Output: [1, 3, 5, 7]
        """
        yield from self._inorder_recursive(self._root)

    def _inorder_recursive(self, node: Optional[BSTNode[ComparableT]]) -> Iterator[ComparableT]:
        """Helper method for recursive in-order traversal."""
        if node is not None:
            yield from self._inorder_recursive(node.left)
            yield node.data
            yield from self._inorder_recursive(node.right)

    def height(self) -> int:
        """Calculate the height of the BST.

        Returns:
            The height of the tree (number of edges in longest path from root to leaf)
            Returns -1 for an empty tree

        Example:
            >>> bst = BinarySearchTree[int]()
            >>> print(bst.height())  # Output: -1
            >>> bst.insert(10)
            >>> print(bst.height())  # Output: 0
            >>> bst.insert(5)
            >>> print(bst.height())  # Output: 1
        """
        return self._height_recursive(self._root)

    def _height_recursive(self, node: Optional[BSTNode[ComparableT]]) -> int:
        """Helper method for recursive height calculation."""
        if node is None:
            return -1

        left_height = self._height_recursive(node.left)
        right_height = self._height_recursive(node.right)

        return max(left_height, right_height) + 1

    def size(self) -> int:
        """Return the number of nodes in the BST.

        Returns:
            The total number of nodes in the tree

        Example:
            >>> bst = BinarySearchTree[int]()
            >>> print(bst.size())  # Output: 0
            >>> bst.insert(10)
            >>> bst.insert(5)
            >>> print(bst.size())  # Output: 2
        """
        return self._size_recursive(self._root)

    def _size_recursive(self, node: Optional[BSTNode[ComparableT]]) -> int:
        """Helper method for recursive size calculation."""
        if node is None:
            return 0

        return 1 + self._size_recursive(node.left) + self._size_recursive(node.right)

    def is_empty(self) -> bool:
        """Check if the BST is empty.

        Returns:
            True if the tree contains no nodes, False otherwise

        Example:
            >>> bst = BinarySearchTree[int]()
            >>> print(bst.is_empty())  # Output: True
            >>> bst.insert(10)
            >>> print(bst.is_empty())  # Output: False
        """
        return self._root is None

    def __len__(self) -> int:
        """Return the number of nodes in the tree (supports len() function)."""
        return self.size()

    def __repr__(self) -> str:
        """Return string representation of the BinarySearchTree instance."""
        return f"{self.__class__.__name__}()"
