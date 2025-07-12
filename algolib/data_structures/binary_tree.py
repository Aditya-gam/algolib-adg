"""Binary Tree data structure implementation with traversal methods."""

from collections import deque
from dataclasses import dataclass, field
from typing import Deque, Generic, Iterator, Optional, TypeVar

T = TypeVar("T")


@dataclass(slots=True)
class TreeNode(Generic[T]):
    """Node class for binary tree."""

    data: T
    left: Optional["TreeNode[T]"] = field(default=None, repr=False)
    right: Optional["TreeNode[T]"] = field(default=None, repr=False)


@dataclass(slots=True, init=False)
class BinaryTree(Generic[T]):
    """Binary Tree data structure with traversal methods.

    A binary tree is a hierarchical data structure where each node has at most
    two children, referred to as the left child and right child.

    Time Complexities:
        - insert: O(n) - worst case for unbalanced tree
        - search: O(n) - worst case for unbalanced tree
        - traversals: O(n) - visits all nodes once
        - height: O(n) - worst case for unbalanced tree

    Space Complexity: O(n) - where n is the number of nodes

    Traversal Methods:
        - In-order (LNR): Left subtree → Node → Right subtree
        - Pre-order (NLR): Node → Left subtree → Right subtree
        - Post-order (LRN): Left subtree → Right subtree → Node
        - Level-order (BFS): Breadth-first traversal using queue

    Common use cases:
        - Expression trees for parsing mathematical expressions
        - Decision trees in AI/ML
        - File system directories
        - Database indexing
        - Huffman coding trees

    Example:
        >>> tree = BinaryTree[int]()
        >>> tree.insert(5)
        >>> tree.insert(3)
        >>> tree.insert(7)
        >>> tree.insert(1)
        >>> print(list(tree.inorder()))  # Output: [1, 3, 5, 7]
        >>> print(list(tree.preorder())) # Output: [5, 3, 1, 7]
    """

    _root: Optional[TreeNode[T]]

    def __init__(self) -> None:
        """Initialize an empty binary tree."""
        self._root = None

    def insert(self, data: T) -> None:
        """Insert a new node with the given data into the binary tree.

        This implementation uses level-order insertion to maintain a complete tree.

        Args:
            data: The data to insert into the tree

        Example:
            >>> tree = BinaryTree[int]()
            >>> tree.insert(10)
            >>> tree.insert(5)
            >>> tree.insert(15)
            >>> print(tree.size())  # Output: 3
        """
        new_node = TreeNode(data)

        if self._root is None:
            self._root = new_node
            return

        # Level-order insertion to maintain complete tree
        queue: Deque[TreeNode[T]] = deque([self._root])

        while queue:
            current = queue.popleft()

            if current.left is None:
                current.left = new_node
                return
            elif current.right is None:
                current.right = new_node
                return
            else:
                queue.append(current.left)
                queue.append(current.right)

    def search(self, data: T) -> bool:
        """Search for a node with the given data in the binary tree.

        Args:
            data: The data to search for

        Returns:
            True if the data is found, False otherwise

        Example:
            >>> tree = BinaryTree[int]()
            >>> tree.insert(10)
            >>> tree.insert(5)
            >>> print(tree.search(5))   # Output: True
            >>> print(tree.search(15))  # Output: False
        """
        return self._search_recursive(self._root, data)

    def _search_recursive(self, node: Optional[TreeNode[T]], data: T) -> bool:
        """Helper method for recursive search."""
        if node is None:
            return False

        if node.data == data:
            return True

        return self._search_recursive(node.left, data) or self._search_recursive(node.right, data)

    def inorder(self) -> Iterator[T]:
        """In-order traversal: Left → Node → Right.

        For binary search trees, this gives nodes in sorted order.

        Yields:
            Data from nodes in in-order sequence

        Example:
            >>> tree = BinaryTree[str]()
            >>> tree.insert("B")
            >>> tree.insert("A")
            >>> tree.insert("C")
            >>> list(tree.inorder())  # Output: ['A', 'B', 'C']
        """
        yield from self._inorder_recursive(self._root)

    def _inorder_recursive(self, node: Optional[TreeNode[T]]) -> Iterator[T]:
        """Helper method for recursive in-order traversal."""
        if node is not None:
            yield from self._inorder_recursive(node.left)
            yield node.data
            yield from self._inorder_recursive(node.right)

    def preorder(self) -> Iterator[T]:
        """Pre-order traversal: Node → Left → Right.

        Useful for creating a copy of the tree or prefix expressions.

        Yields:
            Data from nodes in pre-order sequence

        Example:
            >>> tree = BinaryTree[int]()
            >>> tree.insert(1)
            >>> tree.insert(2)
            >>> tree.insert(3)
            >>> list(tree.preorder())  # Output: [1, 2, 3]
        """
        yield from self._preorder_recursive(self._root)

    def _preorder_recursive(self, node: Optional[TreeNode[T]]) -> Iterator[T]:
        """Helper method for recursive pre-order traversal."""
        if node is not None:
            yield node.data
            yield from self._preorder_recursive(node.left)
            yield from self._preorder_recursive(node.right)

    def postorder(self) -> Iterator[T]:
        """Post-order traversal: Left → Right → Node.

        Useful for deleting nodes or postfix expressions.

        Yields:
            Data from nodes in post-order sequence

        Example:
            >>> tree = BinaryTree[int]()
            >>> tree.insert(1)
            >>> tree.insert(2)
            >>> tree.insert(3)
            >>> list(tree.postorder())  # Output: [2, 3, 1]
        """
        yield from self._postorder_recursive(self._root)

    def _postorder_recursive(self, node: Optional[TreeNode[T]]) -> Iterator[T]:
        """Helper method for recursive post-order traversal."""
        if node is not None:
            yield from self._postorder_recursive(node.left)
            yield from self._postorder_recursive(node.right)
            yield node.data

    def levelorder(self) -> Iterator[T]:
        """Level-order traversal (BFS): Visit nodes level by level.

        Uses a queue to process nodes in breadth-first order.

        Yields:
            Data from nodes in level-order sequence

        Example:
            >>> tree = BinaryTree[int]()
            >>> tree.insert(1)
            >>> tree.insert(2)
            >>> tree.insert(3)
            >>> tree.insert(4)
            >>> list(tree.levelorder())  # Output: [1, 2, 3, 4]
        """
        if self._root is None:
            return

        queue: Deque[TreeNode[T]] = deque([self._root])

        while queue:
            current = queue.popleft()
            yield current.data

            if current.left is not None:
                queue.append(current.left)
            if current.right is not None:
                queue.append(current.right)

    def height(self) -> int:
        """Calculate the height of the binary tree.

        Returns:
            The height of the tree (number of edges in longest path from root to leaf)
            Returns -1 for an empty tree

        Example:
            >>> tree = BinaryTree[int]()
            >>> print(tree.height())  # Output: -1
            >>> tree.insert(1)
            >>> print(tree.height())  # Output: 0
            >>> tree.insert(2)
            >>> print(tree.height())  # Output: 1
        """
        return self._height_recursive(self._root)

    def _height_recursive(self, node: Optional[TreeNode[T]]) -> int:
        """Helper method for recursive height calculation."""
        if node is None:
            return -1

        left_height = self._height_recursive(node.left)
        right_height = self._height_recursive(node.right)

        return max(left_height, right_height) + 1

    def size(self) -> int:
        """Return the number of nodes in the binary tree.

        Returns:
            The total number of nodes in the tree

        Example:
            >>> tree = BinaryTree[int]()
            >>> print(tree.size())  # Output: 0
            >>> tree.insert(1)
            >>> tree.insert(2)
            >>> print(tree.size())  # Output: 2
        """
        return self._size_recursive(self._root)

    def _size_recursive(self, node: Optional[TreeNode[T]]) -> int:
        """Helper method for recursive size calculation."""
        if node is None:
            return 0

        return 1 + self._size_recursive(node.left) + self._size_recursive(node.right)

    def is_empty(self) -> bool:
        """Check if the binary tree is empty.

        Returns:
            True if the tree contains no nodes, False otherwise

        Example:
            >>> tree = BinaryTree[int]()
            >>> print(tree.is_empty())  # Output: True
            >>> tree.insert(1)
            >>> print(tree.is_empty())  # Output: False
        """
        return self._root is None

    def __len__(self) -> int:
        """Return the number of nodes in the tree (supports len() function)."""
        return self.size()

    def __repr__(self) -> str:
        """Return string representation of the BinaryTree instance."""
        return f"{self.__class__.__name__}()"
