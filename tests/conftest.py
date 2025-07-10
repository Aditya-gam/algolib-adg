"""Shared test fixtures for the algolib test suite."""

from typing import Dict, List, Tuple

import pytest

from algolib.algorithms.backtracking import (
    NQueensSolver,
    PermutationFinder,
    SubsetGeneration,
    SudokuSolver,
)
from algolib.algorithms.dynamic_programming import (
    LCS,
    LIS,
    KnapsackDP,
)
from algolib.algorithms.graph import (
    DijkstraAlgorithm,
    KruskalMST,
    PrimMST,
    TopologicalSort,
)
from algolib.algorithms.graph.traversal import (
    BreadthFirstSearch,
    DepthFirstSearch,
)
from algolib.algorithms.greedy import (
    ActivitySelection,
    FractionalKnapsack,
    HuffmanCoding,
)
from algolib.algorithms.math import Fibonacci
from algolib.algorithms.searching import BinarySearcher, LinearSearcher
from algolib.algorithms.sorting import (
    BubbleSorter,
    CountingSort,
    HeapSort,
    InsertionSort,
    MergeSort,
    QuickSort,
    RadixSort,
    SelectionSort,
)
from algolib.data_structures import (
    AVLTree,
    BinarySearchTree,
    BinaryTree,
    DisjointSet,
    Graph,
    LinkedList,
    MaxHeap,
    Queue,
    RedBlackTree,
    Stack,
    Trie,
    Vertex,
)

# =============================================================================
# Algorithm Fixtures
# =============================================================================


@pytest.fixture
def n_queens_solver() -> NQueensSolver:
    """Provide N-Queens solver instance."""
    return NQueensSolver()


@pytest.fixture
def permutation_finder() -> PermutationFinder[int]:
    """Provide permutation finder instance."""
    return PermutationFinder[int]()


@pytest.fixture
def subset_generator() -> SubsetGeneration[int]:
    """Provide subset generator instance."""
    return SubsetGeneration[int]()


@pytest.fixture
def sudoku_solver() -> SudokuSolver:
    """Provide Sudoku solver instance."""
    return SudokuSolver()


@pytest.fixture
def knapsack_dp() -> KnapsackDP:
    """Provide knapsack DP solver instance."""
    return KnapsackDP()


@pytest.fixture
def lcs_solver() -> LCS:
    """Provide LCS solver instance."""
    return LCS()


@pytest.fixture
def lis_solver() -> LIS[int]:
    """Provide LIS solver instance."""
    return LIS[int]()


@pytest.fixture
def dijkstra_solver() -> DijkstraAlgorithm[int]:
    """Provide Dijkstra solver instance."""
    return DijkstraAlgorithm[int]()


@pytest.fixture
def kruskal_mst() -> KruskalMST[int]:
    """Provide Kruskal MST solver instance."""
    return KruskalMST[int]()


@pytest.fixture
def prim_mst() -> PrimMST[int]:
    """Provide Prim MST solver instance."""
    return PrimMST[int]()


@pytest.fixture
def topological_sorter() -> TopologicalSort[int]:
    """Provide topological sort solver instance."""
    return TopologicalSort[int]()


@pytest.fixture
def bfs_traversal() -> BreadthFirstSearch[int]:
    """Provide BFS traversal instance."""
    return BreadthFirstSearch[int]()


@pytest.fixture
def dfs_traversal() -> DepthFirstSearch[int]:
    """Provide DFS traversal instance."""
    return DepthFirstSearch[int]()


@pytest.fixture
def activity_selector() -> ActivitySelection:
    """Provide activity selection solver instance."""
    return ActivitySelection()


@pytest.fixture
def fractional_knapsack_solver() -> FractionalKnapsack:
    """Provide fractional knapsack solver instance."""
    return FractionalKnapsack()


@pytest.fixture
def huffman_coder() -> HuffmanCoding:
    """Provide Huffman coding solver instance."""
    return HuffmanCoding()


@pytest.fixture
def fibonacci_calculator() -> Fibonacci:
    """Provide Fibonacci calculator instance."""
    return Fibonacci()


@pytest.fixture
def binary_searcher() -> BinarySearcher[int]:
    """Provide binary search instance."""
    return BinarySearcher[int]()


@pytest.fixture
def linear_searcher() -> LinearSearcher[int]:
    """Provide linear search instance."""
    return LinearSearcher[int]()


@pytest.fixture
def bubble_sorter() -> BubbleSorter[int]:
    """Provide bubble sort instance."""
    return BubbleSorter[int]()


@pytest.fixture
def counting_sorter() -> CountingSort:
    """Provide counting sort instance."""
    return CountingSort()


@pytest.fixture
def heap_sorter() -> HeapSort[int]:
    """Provide heap sort instance."""
    return HeapSort()


@pytest.fixture
def insertion_sorter() -> InsertionSort:
    """Provide insertion sort instance."""
    return InsertionSort()


@pytest.fixture
def merge_sorter() -> MergeSort[int]:
    """Provide merge sort instance."""
    return MergeSort[int]()


@pytest.fixture
def quick_sorter() -> QuickSort[int]:
    """Provide quick sort instance."""
    return QuickSort()


@pytest.fixture
def radix_sorter() -> RadixSort:
    """Provide radix sort instance."""
    return RadixSort()


@pytest.fixture
def selection_sorter() -> SelectionSort:
    """Provide selection sort instance."""
    return SelectionSort()


# =============================================================================
# Data Structure Fixtures
# =============================================================================


@pytest.fixture
def avl_tree() -> AVLTree[int]:
    """Provide empty AVL tree instance."""
    return AVLTree[int]()


@pytest.fixture
def bst() -> BinarySearchTree[int]:
    """Provide empty binary search tree instance."""
    return BinarySearchTree[int]()


@pytest.fixture
def binary_tree() -> BinaryTree[int]:
    """Provide empty binary tree instance."""
    return BinaryTree[int]()


@pytest.fixture
def disjoint_set() -> DisjointSet[int]:
    """Provide empty disjoint set instance."""
    return DisjointSet[int]()


@pytest.fixture
def graph() -> Graph[int]:
    """Provide empty graph instance."""
    return Graph[int]()


@pytest.fixture
def heap() -> MaxHeap[int]:
    """Provide empty heap instance."""
    return MaxHeap[int]()


@pytest.fixture
def linked_list() -> LinkedList[int]:
    """Provide empty linked list instance."""
    return LinkedList[int]()


@pytest.fixture
def queue() -> Queue[int]:
    """Provide empty queue instance."""
    return Queue[int]()


@pytest.fixture
def red_black_tree() -> RedBlackTree[int]:
    """Provide empty red-black tree instance."""
    return RedBlackTree[int]()


@pytest.fixture
def stack() -> Stack[int]:
    """Provide empty stack instance."""
    return Stack[int]()


@pytest.fixture
def trie() -> Trie:
    """Provide empty trie instance."""
    return Trie()


# =============================================================================
# Test Data Fixtures
# =============================================================================


@pytest.fixture
def sorted_list() -> List[int]:
    """Provide a sorted list of integers."""
    return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


@pytest.fixture
def unsorted_list() -> List[int]:
    """Provide an unsorted list of integers."""
    return [5, 2, 8, 1, 9, 3, 7, 4, 6, 0]


@pytest.fixture
def duplicate_list() -> List[int]:
    """Provide a list with duplicate elements."""
    return [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]


@pytest.fixture
def empty_list() -> List[int]:
    """Provide an empty list."""
    return []


@pytest.fixture
def single_element_list() -> List[int]:
    """Provide a list with single element."""
    return [42]


@pytest.fixture
def large_list() -> List[int]:
    """Provide a large list for performance testing."""
    return list(range(1000))


@pytest.fixture
def negative_list() -> List[int]:
    """Provide a list with negative numbers."""
    return [-5, -2, -8, -1, -9, -3, -7, -4, -6]


@pytest.fixture
def float_list() -> List[float]:
    """Provide a list of floats."""
    return [3.14, 2.71, 1.41, 0.58, 2.23]


@pytest.fixture
def string_list() -> List[str]:
    """Provide a list of strings."""
    return ["apple", "banana", "cherry", "date", "elderberry"]


@pytest.fixture
def graph_data() -> Dict[int, List[int]]:
    """Provide graph adjacency data."""
    return {
        0: [1, 2],
        1: [0, 3, 4],
        2: [0, 5, 6],
        3: [1],
        4: [1],
        5: [2],
        6: [2],
    }


@pytest.fixture
def weighted_graph_data() -> Dict[int, List[Tuple[int, float]]]:
    """Provide weighted graph data."""
    return {
        0: [(1, 4), (2, 2)],
        1: [(0, 4), (2, 1), (3, 5)],
        2: [(0, 2), (1, 1), (3, 8)],
        3: [(1, 5), (2, 8)],
    }


@pytest.fixture
def bst_values() -> List[int]:
    """Provide values for building a BST."""
    return [50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 45, 55, 65, 75, 85]


@pytest.fixture
def populated_bst(bst: BinarySearchTree[int], bst_values: List[int]) -> BinarySearchTree[int]:
    """Provide a populated binary search tree."""
    for value in bst_values:
        bst.insert(value)
    return bst


@pytest.fixture
def knapsack_items() -> List[Tuple[int, int]]:
    """Provide knapsack items (weight, value)."""
    return [(2, 3), (3, 4), (4, 5), (5, 6)]


@pytest.fixture
def activity_data() -> List[Tuple[int, int]]:
    """Provide activity data (start_time, end_time)."""
    return [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11)]


@pytest.fixture
def valid_sudoku_board() -> List[List[int]]:
    """Provide a valid Sudoku board."""
    return [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9],
    ]


@pytest.fixture
def solved_sudoku_board() -> List[List[int]]:
    """Provide a solved Sudoku board."""
    return [
        [5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, 6, 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 3, 7, 2, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 4, 5, 2, 8, 6, 1, 7, 9],
    ]


@pytest.fixture
def unsolvable_sudoku_board() -> List[List[int]]:
    """Provide an unsolvable Sudoku board."""
    return [
        [5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, 6, 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 3, 7, 2, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 4, 5, 2, 8, 6, 1, 7, 1],  # Invalid: two 1s in last row
    ]


@pytest.fixture
def lcs_strings() -> Tuple[str, str]:
    """Provide strings for LCS testing."""
    return "ABCDGH", "AEDFHR"


@pytest.fixture
def lis_sequence() -> List[int]:
    """Provide sequence for LIS testing."""
    return [10, 22, 9, 33, 21, 50, 41, 60, 80]


@pytest.fixture
def huffman_text() -> str:
    """Provide text for Huffman coding testing."""
    return "hello world"


@pytest.fixture
def vertices() -> List[Vertex[int]]:
    """Provide vertices for graph testing."""
    return [Vertex(i) for i in range(5)]


@pytest.fixture
def populated_graph(graph: Graph[int], graph_data: Dict[int, List[int]]) -> Graph[int]:
    """Provide a populated graph."""
    for vertex_id, neighbors in graph_data.items():
        u = graph.add_vertex(vertex_id)
        for neighbor in neighbors:
            v = graph.add_vertex(neighbor)
            graph.add_edge(u, v)
    return graph


@pytest.fixture
def populated_linked_list(linked_list: LinkedList[int], sorted_list: List[int]) -> LinkedList[int]:
    """Provide a populated linked list."""
    for value in sorted_list:
        linked_list.append(value)
    return linked_list


@pytest.fixture
def populated_stack(stack: Stack[int], sorted_list: List[int]) -> Stack[int]:
    """Provide a populated stack."""
    for value in sorted_list:
        stack.push(value)
    return stack


@pytest.fixture
def populated_queue(queue: Queue[int], sorted_list: List[int]) -> Queue[int]:
    """Provide a populated queue."""
    for value in sorted_list:
        queue.enqueue(value)
    return queue


@pytest.fixture
def populated_heap(heap: MaxHeap[int], unsorted_list: List[int]) -> MaxHeap[int]:
    """Provide a populated heap."""
    for value in unsorted_list:
        heap.insert(value)
    return heap


@pytest.fixture
def populated_trie(trie: Trie) -> Trie:
    """Provide a populated trie."""
    words = ["apple", "app", "application", "banana", "band", "bandana"]
    for word in words:
        trie.insert(word)
    return trie


@pytest.fixture
def populated_disjoint_set() -> DisjointSet[int]:
    """Provide a populated disjoint set."""
    return DisjointSet[int](range(10))


# =============================================================================
# Performance Testing Fixtures
# =============================================================================


@pytest.fixture
def performance_list() -> List[int]:
    """Provide a large list for performance testing."""
    return list(range(10000))


@pytest.fixture
def performance_graph() -> Graph[int]:
    """Provide a large graph for performance testing."""
    graph = Graph[int]()
    for i in range(100):
        u = graph.add_vertex(i)
        for j in range(i + 1, min(i + 10, 100)):
            v = graph.add_vertex(j)
            graph.add_edge(u, v)
    return graph


# =============================================================================
# Edge Case Fixtures
# =============================================================================


@pytest.fixture
def single_element_graph() -> Graph[int]:
    """Provide a graph with single vertex."""
    graph = Graph[int]()
    graph.add_vertex(1)
    return graph


@pytest.fixture
def empty_graph() -> Graph[int]:
    """Provide an empty graph."""
    return Graph[int]()


@pytest.fixture
def self_loop_graph() -> Graph[int]:
    """Provide a graph with self-loops."""
    graph = Graph[int]()
    v = graph.add_vertex(1)
    graph.add_edge(v, v)  # Self-loop
    return graph


@pytest.fixture
def disconnected_graph() -> Graph[int]:
    """Provide a disconnected graph."""
    graph = Graph[int]()
    graph.add_vertex(1)
    graph.add_vertex(2)
    # No edges between vertices
    return graph
