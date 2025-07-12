"""Tests for Depth First Search algorithm."""

from typing import Set, Tuple

import pytest
from hypothesis import given
from hypothesis import strategies as st

from algolib.algorithms.graph.traversal.depth_first_search import DepthFirstSearch as DFS
from algolib.data_structures.graph import Graph, Vertex


@st.composite
def random_graph_and_start_vertex(
    draw: st.DrawFn,
) -> Tuple[Graph[int], Vertex[int]]:
    num_vertices = draw(st.integers(min_value=1, max_value=10))
    vertex_keys = list(range(num_vertices))
    graph = Graph[int]()
    vertices = {key: graph.add_vertex(key) for key in vertex_keys}

    # Generate a set of unique edges to avoid parallel edges
    possible_edges = [(v1, v2) for v1 in vertices.values() for v2 in vertices.values() if v1 != v2]
    if possible_edges:
        edges_to_add = draw(st.lists(st.sampled_from(possible_edges), unique=True))
        for u, v in edges_to_add:
            graph.add_edge(u, v)

    start_vertex = draw(st.sampled_from(list(vertices.values())))
    return graph, start_vertex


@given(graph_and_start=random_graph_and_start_vertex())
def test_dfs_property_traversal_properties(graph_and_start: Tuple[Graph[int], Vertex[int]]) -> None:
    graph, start_vertex = graph_and_start
    dfs = DFS[int]()

    traversal_result = dfs.traverse(graph, start_vertex)

    # 1. The first vertex in the traversal is the start vertex.
    assert traversal_result[0] == start_vertex

    # 2. All traversed vertices are unique.
    assert len(traversal_result) == len(set(traversal_result))

    # 3. All traversed vertices must be reachable from the start_vertex.
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

    assert set(traversal_result) == visited


@pytest.fixture
def graph() -> Graph[str]:
    """Fixture for a sample graph."""
    g = Graph[str]()
    vertices = [g.add_vertex(str(i)) for i in range(8)]
    edges = [
        (0, 1),
        (0, 2),
        (1, 3),
        (1, 4),
        (2, 5),
        (2, 6),
        (3, 7),
        (4, 7),
        (5, 7),
        (6, 7),
    ]
    for u, v in edges:
        g.add_edge(vertices[u], vertices[v])
    return g


def test_dfs_traversal(graph: Graph[str]) -> None:
    """Test DFS traversal from a start vertex."""
    dfs = DFS[str]()
    start_vertex = graph.get_vertex("0")
    assert start_vertex is not None

    traversal = dfs.traverse(graph, start_vertex)
    # The exact order depends on neighbor iteration order.
    # We check for correctness of visited nodes and their count.
    expected_reachable_nodes = {"0", "1", "2", "3", "4", "5", "6", "7"}
    traversed_keys = {v.key for v in traversal}
    assert traversed_keys == expected_reachable_nodes
    assert len(traversal) == 8


def test_dfs_traversal_disconnected_component(graph: Graph[str]) -> None:
    """Test DFS on a component disconnected from the start vertex."""
    dfs = DFS[str]()
    # Add a disconnected component
    v8 = graph.add_vertex("8")
    v9 = graph.add_vertex("9")
    graph.add_edge(v8, v9)

    start_vertex = graph.get_vertex("0")
    assert start_vertex is not None

    traversal = dfs.traverse(graph, start_vertex)
    traversed_keys = {v.key for v in traversal}
    assert "8" not in traversed_keys
    assert "9" not in traversed_keys
    assert len(traversal) == 8


def test_dfs_traversal_start_not_in_graph() -> None:
    """Test that ValueError is raised if the start vertex is not in the graph."""
    graph = Graph[int]()
    graph.add_vertex(1)
    start_vertex_not_in_graph = Vertex(99)
    dfs = DFS[int]()
    with pytest.raises(ValueError, match="Start vertex not in graph"):
        dfs.traverse(graph, start_vertex_not_in_graph)


def test_dfs_single_node_graph() -> None:
    """Test DFS on a graph with a single node."""
    graph = Graph[str]()
    start_vertex = graph.add_vertex("A")
    dfs = DFS[str]()
    traversal = dfs.traverse(graph, start_vertex)
    assert traversal == [start_vertex]


def test_dfs_linear_graph() -> None:
    """Test DFS on a linear graph (a path)."""
    graph = Graph[int]()
    vertices = [graph.add_vertex(i) for i in range(5)]
    for i in range(4):
        graph.add_edge(vertices[i], vertices[i + 1])

    dfs = DFS[int]()
    start_vertex = vertices[0]
    traversal = dfs.traverse(graph, start_vertex)
    # DFS should visit all vertices in the path
    expected_vertices = set(vertices)
    traversed_vertices = set(traversal)
    assert traversed_vertices == expected_vertices
    assert len(traversal) == 5


def test_dfs_with_cycle(graph: Graph[str]) -> None:
    """Test that DFS handles cycles correctly and does not loop infinitely."""
    dfs = DFS[str]()
    # Add a cycle between 3 and 4
    v3 = graph.get_vertex("3")
    v4 = graph.get_vertex("4")
    assert v3 and v4
    graph.add_edge(v3, v4)

    start_vertex = graph.get_vertex("0")
    assert start_vertex
    traversal = dfs.traverse(graph, start_vertex)
    assert len(traversal) == len(graph)  # Should visit every node once
    assert len(set(traversal)) == len(graph)


def test_dfs_run_method(graph: Graph[str]) -> None:
    """Test the run method of the DFS algorithm."""
    dfs = DFS[str]()
    start_vertex = graph.get_vertex("0")
    assert start_vertex is not None

    # Test valid run
    traversal = dfs.run(graph, start_vertex)
    assert traversal is not None
    expected_keys = {"0", "1", "2", "3", "4", "5", "6", "7"}
    traversed_keys = {v.key for v in traversal}
    assert traversed_keys == expected_keys

    # Test with non-existent start vertex
    non_existent_vertex = Vertex("8")
    with pytest.raises(ValueError):
        dfs.run(graph, non_existent_vertex)


def test_dfs_directed_graph() -> None:
    """Test DFS on a directed graph."""
    graph = Graph[int](directed=True)
    vertices = [graph.add_vertex(i) for i in range(4)]

    # Create a directed path: 0 -> 1 -> 2 -> 3
    graph.add_edge(vertices[0], vertices[1])
    graph.add_edge(vertices[1], vertices[2])
    graph.add_edge(vertices[2], vertices[3])

    dfs = DFS[int]()
    start_vertex = vertices[0]
    traversal = dfs.traverse(graph, start_vertex)

    # DFS should visit all vertices in the directed path
    expected_vertices = set(vertices)
    traversed_vertices = set(traversal)
    assert traversed_vertices == expected_vertices
    assert len(traversal) == 4

    # Test reverse direction (should not reach all vertices)
    reverse_traversal = dfs.traverse(graph, vertices[3])
    assert len(reverse_traversal) == 1  # Only vertex 3 should be reachable


def test_dfs_undirected_graph() -> None:
    """Test DFS on an undirected graph."""
    graph = Graph[int](directed=False)
    vertices = [graph.add_vertex(i) for i in range(4)]

    # Create a simple undirected graph: 0 -- 1 -- 2 -- 3
    graph.add_edge(vertices[0], vertices[1])
    graph.add_edge(vertices[1], vertices[2])
    graph.add_edge(vertices[2], vertices[3])

    dfs = DFS[int]()
    start_vertex = vertices[0]
    traversal = dfs.traverse(graph, start_vertex)

    # DFS should visit all vertices in the undirected graph
    expected_vertices = set(vertices)
    traversed_vertices = set(traversal)
    assert traversed_vertices == expected_vertices
    assert len(traversal) == 4

    # Test from any vertex - should reach all vertices
    for vertex in vertices:
        traversal = dfs.traverse(graph, vertex)
        assert len(traversal) == 4


def test_dfs_empty_graph() -> None:
    """Test DFS on an empty graph."""
    graph = Graph[int]()
    start_vertex = Vertex(1)
    dfs = DFS[int]()
    with pytest.raises(ValueError, match="Start vertex not in graph"):
        dfs.traverse(graph, start_vertex)


def test_dfs_self_loop() -> None:
    """Test DFS on a graph with self-loops."""
    graph = Graph[int]()
    vertex = graph.add_vertex(1)
    graph.add_edge(vertex, vertex)  # Self-loop

    dfs = DFS[int]()
    traversal = dfs.traverse(graph, vertex)
    assert traversal == [vertex]  # Should visit vertex once


def test_dfs_multiple_edges() -> None:
    """Test DFS on a graph with multiple edges between the same vertices."""
    graph = Graph[int]()
    v1 = graph.add_vertex(1)
    v2 = graph.add_vertex(2)
    graph.add_edge(v1, v2)
    graph.add_edge(v2, v1)  # Multiple edges

    dfs = DFS[int]()
    traversal = dfs.traverse(graph, v1)
    expected_vertices = {v1, v2}
    traversed_vertices = set(traversal)
    assert traversed_vertices == expected_vertices
    assert len(traversal) == 2


# Tests for run_iterative method
def test_run_iterative_basic(graph: Graph[str]) -> None:
    """Test iterative DFS traversal."""
    dfs = DFS[str]()
    start_vertex = graph.get_vertex("0")
    assert start_vertex is not None

    traversal = dfs.run_iterative(graph, start_vertex)
    expected_reachable_nodes = {"0", "1", "2", "3", "4", "5", "6", "7"}
    traversed_keys = {v.key for v in traversal}
    assert traversed_keys == expected_reachable_nodes
    assert len(traversal) == 8


def test_run_iterative_single_node() -> None:
    """Test iterative DFS on a graph with a single node."""
    graph = Graph[str]()
    start_vertex = graph.add_vertex("A")
    dfs = DFS[str]()
    traversal = dfs.run_iterative(graph, start_vertex)
    assert traversal == [start_vertex]


def test_run_iterative_linear_graph() -> None:
    """Test iterative DFS on a linear graph."""
    graph = Graph[int]()
    vertices = [graph.add_vertex(i) for i in range(5)]
    for i in range(4):
        graph.add_edge(vertices[i], vertices[i + 1])

    dfs = DFS[int]()
    start_vertex = vertices[0]
    traversal = dfs.run_iterative(graph, start_vertex)
    expected_vertices = set(vertices)
    traversed_vertices = set(traversal)
    assert traversed_vertices == expected_vertices
    assert len(traversal) == 5


def test_run_iterative_with_cycle(graph: Graph[str]) -> None:
    """Test iterative DFS with cycles."""
    dfs = DFS[str]()
    # Add a cycle between 3 and 4
    v3 = graph.get_vertex("3")
    v4 = graph.get_vertex("4")
    assert v3 and v4
    graph.add_edge(v3, v4)

    start_vertex = graph.get_vertex("0")
    assert start_vertex
    traversal = dfs.run_iterative(graph, start_vertex)
    assert len(traversal) == len(graph)  # Should visit every node once
    assert len(set(traversal)) == len(graph)


def test_run_iterative_disconnected_component(graph: Graph[str]) -> None:
    """Test iterative DFS on a component disconnected from the start vertex."""
    dfs = DFS[str]()
    # Add a disconnected component
    v8 = graph.add_vertex("8")
    v9 = graph.add_vertex("9")
    graph.add_edge(v8, v9)

    start_vertex = graph.get_vertex("0")
    assert start_vertex is not None

    traversal = dfs.run_iterative(graph, start_vertex)
    traversed_keys = {v.key for v in traversal}
    assert "8" not in traversed_keys
    assert "9" not in traversed_keys
    assert len(traversal) == 8


def test_run_iterative_start_not_in_graph() -> None:
    """Test iterative DFS when start vertex is not in graph."""
    graph = Graph[int]()
    graph.add_vertex(1)
    start_vertex_not_in_graph = Vertex(99)
    dfs = DFS[int]()
    with pytest.raises(ValueError, match="Start vertex not in graph"):
        dfs.run_iterative(graph, start_vertex_not_in_graph)


def test_run_iterative_directed_graph() -> None:
    """Test iterative DFS on a directed graph."""
    graph = Graph[int](directed=True)
    vertices = [graph.add_vertex(i) for i in range(4)]

    # Create a directed path: 0 -> 1 -> 2 -> 3
    graph.add_edge(vertices[0], vertices[1])
    graph.add_edge(vertices[1], vertices[2])
    graph.add_edge(vertices[2], vertices[3])

    dfs = DFS[int]()
    start_vertex = vertices[0]
    traversal = dfs.run_iterative(graph, start_vertex)

    # Should visit all vertices in the directed path
    expected_vertices = set(vertices)
    traversed_vertices = set(traversal)
    assert traversed_vertices == expected_vertices
    assert len(traversal) == 4


def test_run_iterative_undirected_graph() -> None:
    """Test iterative DFS on an undirected graph."""
    graph = Graph[int](directed=False)
    vertices = [graph.add_vertex(i) for i in range(4)]

    # Create a simple undirected graph: 0 -- 1 -- 2 -- 3
    graph.add_edge(vertices[0], vertices[1])
    graph.add_edge(vertices[1], vertices[2])
    graph.add_edge(vertices[2], vertices[3])

    dfs = DFS[int]()
    start_vertex = vertices[0]
    traversal = dfs.run_iterative(graph, start_vertex)

    # Should visit all vertices in the undirected graph
    expected_vertices = set(vertices)
    traversed_vertices = set(traversal)
    assert traversed_vertices == expected_vertices
    assert len(traversal) == 4


def test_run_iterative_self_loop() -> None:
    """Test iterative DFS on a graph with self-loops."""
    graph = Graph[int]()
    vertex = graph.add_vertex(1)
    graph.add_edge(vertex, vertex)  # Self-loop

    dfs = DFS[int]()
    traversal = dfs.run_iterative(graph, vertex)
    assert traversal == [vertex]  # Should visit vertex once


def test_run_iterative_multiple_edges() -> None:
    """Test iterative DFS on a graph with multiple edges."""
    graph = Graph[int]()
    v1 = graph.add_vertex(1)
    v2 = graph.add_vertex(2)
    graph.add_edge(v1, v2)
    graph.add_edge(v2, v1)  # Multiple edges

    dfs = DFS[int]()
    traversal = dfs.run_iterative(graph, v1)
    expected_vertices = {v1, v2}
    traversed_vertices = set(traversal)
    assert traversed_vertices == expected_vertices
    assert len(traversal) == 2


def test_run_iterative_consistency_with_recursive(graph: Graph[str]) -> None:
    """Test that iterative and recursive DFS produce same results."""
    dfs = DFS[str]()
    start_vertex = graph.get_vertex("0")
    assert start_vertex is not None

    recursive_traversal = dfs.run(graph, start_vertex)
    iterative_traversal = dfs.run_iterative(graph, start_vertex)

    # Both should visit the same set of vertices
    recursive_vertices = set(recursive_traversal)
    iterative_vertices = set(iterative_traversal)
    assert recursive_vertices == iterative_vertices
    assert len(recursive_traversal) == len(iterative_traversal)


def test_run_iterative_empty_graph() -> None:
    """Test iterative DFS on an empty graph."""
    graph = Graph[int]()
    start_vertex = Vertex(1)
    dfs = DFS[int]()
    with pytest.raises(ValueError, match="Start vertex not in graph"):
        dfs.run_iterative(graph, start_vertex)


def test_run_iterative_complex_graph() -> None:
    """Test iterative DFS on a more complex graph."""
    graph = Graph[int]()
    vertices = [graph.add_vertex(i) for i in range(6)]

    # Create a complex graph with multiple paths
    edges = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 4), (2, 5), (3, 5), (4, 5)]
    for u, v in edges:
        graph.add_edge(vertices[u], vertices[v])

    dfs = DFS[int]()
    start_vertex = vertices[0]
    traversal = dfs.run_iterative(graph, start_vertex)

    # Should visit all vertices
    expected_vertices = set(vertices)
    traversed_vertices = set(traversal)
    assert traversed_vertices == expected_vertices
    assert len(traversal) == 6

    # First vertex should be start vertex
    assert traversal[0] == start_vertex

    # All vertices should be unique
    assert len(traversal) == len(set(traversal))
