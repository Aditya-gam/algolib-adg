# ruff: noqa: D100,D101,D102,D103,D104,D105,D107
import collections
from typing import List, Set, Tuple, Type

import pytest
from hypothesis import given
from hypothesis import strategies as st

from algolib.algorithms.graph.traversal.breadth_first_search import (
    BreadthFirstSearch as BFS,
)
from algolib.algorithms.graph.traversal.depth_first_search import (
    DepthFirstSearch as DFS,
)
from algolib.algorithms.searching.base import Searcher
from algolib.algorithms.searching.binary import BinarySearcher
from algolib.algorithms.searching.linear import LinearSearcher
from algolib.algorithms.sorting import (
    BubbleSorter,
    CountingSort,
    HeapSort,
    InsertionSort,
    MergeSorter,
    QuickSort,
    RadixSort,
    SelectionSort,
)
from algolib.algorithms.sorting.base import Sorter
from algolib.data_structures.avl_tree import AVLTree
from algolib.data_structures.disjoint_set import DisjointSet
from algolib.data_structures.graph import Graph, Vertex
from algolib.data_structures.red_black_tree import (
    Color,
    RedBlackTree,
    _RBNode,
)
from tests.property.strategies import (
    build_avl_tree,
    build_rbt,
    random_int_list,
    small_graph,
    union_find_sequences,
)


def reference_dfs(graph: Graph[int], start_vertex: Vertex[int]) -> Set[Vertex[int]]:
    """A reference implementation of DFS to find all reachable vertices."""
    visited: Set[Vertex[int]] = set()
    stack = [start_vertex]

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            # Get neighbors and add to stack
            for neighbor, _ in reversed(list(graph.neighbors(vertex))):
                if neighbor not in visited:
                    stack.append(neighbor)
    return visited


# A strategy for a sorted list and an element to search for
sorted_list_and_element = st.lists(st.integers(), min_size=1).flatmap(
    lambda lst: st.tuples(
        st.just(sorted(list(set(lst)))), st.one_of(st.sampled_from(lst), st.integers())
    )
)

ALL_SEARCHERS: List[Type[Searcher[int]]] = [LinearSearcher, BinarySearcher]
ALL_SORTERS: List[Type[Sorter[int]]] = [
    BubbleSorter,
    MergeSorter,
    InsertionSort,
    SelectionSort,
    QuickSort,
    HeapSort,
]


@pytest.mark.property
@given(ds_and_ops=union_find_sequences())
def test_disjoint_set_properties(
    ds_and_ops: Tuple[DisjointSet[int], List[Tuple[str, int, int]]],
) -> None:
    """
    Tests properties of the DisjointSet data structure:
    1. After a union(u, v), find(u) should equal find(v).
    2. The find operation is idempotent: find(u) == find(find(u)).
    """
    ds, operations = ds_and_ops

    # Re-run operations to verify properties against the final state
    for op_type, u, v in operations:
        if op_type == "union":
            # After a union, the roots of the two elements must be the same.
            assert ds.find(u) == ds.find(v)

        # Test idempotency for every element involved in an operation
        assert ds.find(u) == ds.find(ds.find(u))
        if v != -1:  # v is used in union
            assert ds.find(v) == ds.find(ds.find(v))


@pytest.mark.property
@pytest.mark.parametrize("searcher_class", ALL_SEARCHERS)
@given(data_and_target=sorted_list_and_element)
def test_search_properties(
    searcher_class: Type[Searcher[int]], data_and_target: Tuple[List[int], int]
) -> None:
    """
    Tests that search algorithms correctly find an element or return None.
    - If the element is in the list, the searcher should return a valid index.
    - If the element is not in the list, the searcher should return None.
    """
    data, target = data_and_target
    searcher = searcher_class()

    result = searcher.search(data, target)

    if target in data:
        assert result is not None
        assert 0 <= result < len(data)
        assert data[result] == target
    else:
        assert result is None


@pytest.mark.property
@pytest.mark.parametrize("sorter_class", ALL_SORTERS)
@given(data=random_int_list)
def test_generic_sort_property(sorter_class: Type[Sorter[int]], data: List[int]) -> None:
    """Tests that a generic sorting algorithm correctly sorts a list."""
    sorter = sorter_class()
    sorted_data = sorter.sort(data.copy())
    assert sorted_data == sorted(data)


@pytest.mark.property
@given(data=st.lists(st.integers(min_value=0, max_value=1000)))
def test_counting_sort_property(data: list[int]) -> None:
    """Tests that counting sort correctly sorts a list of non-negative integers."""
    sorter = CountingSort(min_val=0, max_val=1000)
    sorted_data = sorter.sort(data.copy())
    assert sorted_data == sorted(data)


@pytest.mark.property
@given(data=st.lists(st.integers(min_value=0)))
def test_radix_sort_property(data: list[int]) -> None:
    """Tests that radix sort correctly sorts a list of non-negative integers."""
    sorter = RadixSort()
    sorted_data = sorter.sort(data.copy())
    assert sorted_data == sorted(data)


@pytest.mark.property
@given(graph_and_start=small_graph())
def test_bfs_and_dfs_visit_all_reachable_nodes(
    graph_and_start: Tuple[Graph[int], Vertex[int]],
) -> None:
    """
    Tests that BFS and DFS visit exactly the set of nodes reachable
    from a start node. It uses a reference DFS to determine the set
    of all reachable nodes.
    """
    graph, start_vertex = graph_and_start

    # Get the set of visited nodes from BFS and DFS
    bfs_algo = BFS[int]()
    bfs_visited_vertices = set(bfs_algo.traverse(graph, start_vertex))

    dfs_algo = DFS[int]()
    dfs_visited_vertices = set(dfs_algo.traverse(graph, start_vertex))

    # Get the set of reachable nodes from the reference DFS
    reachable_vertices = reference_dfs(graph, start_vertex)

    assert bfs_visited_vertices == reachable_vertices
    assert dfs_visited_vertices == reachable_vertices


@pytest.mark.property
@given(graph_and_start=small_graph())
def test_bfs_depth_is_non_decreasing(graph_and_start: Tuple[Graph[int], Vertex[int]]) -> None:
    """
    Tests that the depth of nodes in a BFS traversal is non-decreasing.
    """
    graph, start_vertex = graph_and_start

    # 1. Get the traversal order from the BFS algorithm under test
    bfs_algo = BFS[int]()
    traversal_order = bfs_algo.traverse(graph, start_vertex)

    # 2. Get the ground-truth depth of each node using a simple BFS
    depths = {start_vertex: 0}
    queue = collections.deque([start_vertex])
    visited_for_depth = {start_vertex}

    while queue:
        vertex = queue.popleft()
        for neighbor, _ in graph.neighbors(vertex):
            if neighbor not in visited_for_depth:
                visited_for_depth.add(neighbor)
                depths[neighbor] = depths[vertex] + 1
                queue.append(neighbor)

    # 3. Check that depths are non-decreasing in the traversal order
    if not traversal_order:
        return

    # Get depths for traversed nodes, handling disconnected components
    traversed_depths = [depths.get(v, -1) for v in traversal_order]

    for i in range(len(traversed_depths) - 1):
        assert traversed_depths[i] <= traversed_depths[i + 1]


@pytest.mark.property
@given(tree=build_avl_tree())
def test_avl_tree_properties(tree: AVLTree[int]) -> None:
    """
    Tests the core properties of an AVL tree:
    1. It maintains the Binary Search Tree (BST) property.
    2. The balance factor of every node is in {-1, 0, 1}.
    """
    # 1. Verify BST property (in-order traversal is sorted)
    inorder_nodes = list(tree.inorder())
    assert inorder_nodes == sorted(inorder_nodes)

    # 2. Verify AVL balance property
    if tree.is_empty():
        return

    nodes_to_check = [tree._root]
    while nodes_to_check:
        current_node = nodes_to_check.pop()
        if current_node:
            balance_factor = tree._balance_factor(current_node)
            assert balance_factor in {-1, 0, 1}
            nodes_to_check.append(current_node.left)
            nodes_to_check.append(current_node.right)


@pytest.mark.property
@given(tree=build_rbt())
def test_rbt_properties(tree: RedBlackTree[int]) -> None:
    """Tests the core properties of a Red-Black Tree."""
    if tree.is_empty():
        return

    # Property 1: Root is black
    assert tree._root is not None
    assert tree._root.color == Color.BLACK

    # Properties 2 & 4: No double reds, and all paths have same black-height
    # We can check these with a single traversal.
    # Property 2: No red node has a red child.
    # Property 4: Equal black-height paths.
    black_heights = set()

    def check_node(node: _RBNode[int] | None, current_bh: int) -> None:
        if node is None:
            black_heights.add(current_bh)
            return

        if node.color == Color.BLACK:
            current_bh += 1
        else:  # Node is Red
            # Property 2: Red node cannot have red children
            if node.left:
                assert node.left.color == Color.BLACK
            if node.right:
                assert node.right.color == Color.BLACK

        check_node(node.left, current_bh)
        check_node(node.right, current_bh)

    check_node(tree._root, 0)
    # If all paths have the same black height, the set will have one element.
    assert len(black_heights) == 1
