# ruff: noqa: D100,D101,D102,D103,D104,D105,D107
import collections
from typing import List, Set, Tuple, Type

import pytest
from hypothesis import given
from hypothesis import strategies as st

from algolib.algorithms.graph.traversal.breadth_first_search import BreadthFirstSearch as BFS
from algolib.algorithms.searching.base import Searcher
from algolib.algorithms.searching.binary import BinarySearcher
from algolib.algorithms.searching.linear import LinearSearcher
from algolib.algorithms.sorting.base import Sorter
from algolib.algorithms.sorting.bubble import BubbleSorter
from algolib.algorithms.sorting.merge import MergeSorter
from algolib.data_structures.disjoint_set import DisjointSet
from algolib.data_structures.graph import Graph, Vertex
from tests.property.strategies import random_int_list, small_graph, union_find_sequences


def is_sorted(data: List[int]) -> bool:
    """Checks if a list is sorted in non-decreasing order."""
    return all(data[i] <= data[i + 1] for i in range(len(data) - 1))


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
ALL_SORTERS: List[Type[Sorter[int]]] = [BubbleSorter, MergeSorter]


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
def test_sort_properties(sorter_class: Type[Sorter[int]], data: List[int]) -> None:
    """
    Tests two properties of sorting algorithms:
    1. Idempotency: Applying the sort twice has the same result as applying it once.
    2. Correctness: The output is sorted and is a permutation of the input.
    """
    sorter = sorter_class()

    # Property 1: The output is sorted
    sorted_data = sorter.sort(data.copy())
    assert is_sorted(list(sorted_data))

    # Property 2: The output is a permutation of the input
    assert collections.Counter(data) == collections.Counter(sorted_data)


@pytest.mark.property
@pytest.mark.parametrize("sorter_class", ALL_SORTERS)
@given(data=st.lists(st.integers(), min_size=1, max_size=100))
def test_sort_idempotency(sorter_class: Type[Sorter[int]], data: List[int]) -> None:
    """Tests that sorting an already sorted list does not change it."""
    sorter = sorter_class()

    # First sort
    sorted_once = sorter.sort(data.copy())
    assert is_sorted(list(sorted_once))

    # Sorting again should not change the list
    sorted_twice = sorter.sort(sorted_once[:])
    assert sorted_once == sorted_twice


@pytest.mark.property
@given(graph=small_graph())
def test_bfs_visits_all_reachable_nodes(graph: Graph[int]) -> None:
    """
    Tests that BFS visits exactly the set of nodes reachable from a start node.
    It uses a reference DFS to determine the set of all reachable nodes.
    """
    if len(graph) == 0:
        return  # Nothing to test in an empty graph

    # Pick a starting vertex
    start_key = list(graph._vertices.keys())[0]
    start_vertex = graph.get_vertex(start_key)

    if start_vertex is None:
        return

    # Get the set of visited nodes from BFS
    bfs_algo = BFS[int]()
    bfs_visited_vertices = set(bfs_algo.traverse(graph, start_vertex))

    # Get the set of reachable nodes from the reference DFS
    reachable_vertices = reference_dfs(graph, start_vertex)

    assert bfs_visited_vertices == reachable_vertices
