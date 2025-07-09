# ruff: noqa: D100,D101,D102,D103,D104,D105,D107

from typing import Set

import pytest
from hypothesis import given

from algolib.algorithms.graph.traversal.bfs import BFS
from algolib.data_structures.graph import Graph, Vertex
from tests.property.strategies import small_graph


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
