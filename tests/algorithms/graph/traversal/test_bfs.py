from typing import List, Set, Tuple

import pytest
from hypothesis import given
from hypothesis import strategies as st

from algolib.algorithms.graph.traversal.bfs import BFS
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
    possible_edges = [
        (v1, v2)
        for v1 in vertices.values()
        for v2 in vertices.values()
        if v1 != v2
    ]
    if possible_edges:
        edges_to_add = draw(
            st.lists(st.sampled_from(possible_edges), unique=True))
        for u, v in edges_to_add:
            graph.add_edge(u, v)

    start_vertex = draw(st.sampled_from(list(vertices.values())))
    return graph, start_vertex


@given(graph_and_start=random_graph_and_start_vertex())
def test_bfs_property_traversal_properties(
    graph_and_start: Tuple[Graph[int], Vertex[int]]
) -> None:
    graph, start_vertex = graph_and_start
    bfs = BFS[int]()

    traversal_result = bfs.traverse(graph, start_vertex)

    # 1. The first vertex in the traversal is the start vertex.
    assert traversal_result[0] == start_vertex

    # 2. All traversed vertices are unique.
    assert len(traversal_result) == len(set(traversal_result))

    # 3. All traversed vertices must be reachable from the start_vertex.
    q: List[Vertex[int]] = [start_vertex]
    reachable: Set[Vertex[int]] = {start_vertex}
    head = 0
    while head < len(q):
        curr = q[head]
        head += 1
        for neighbor, _ in graph.neighbors(curr):
            if neighbor not in reachable:
                reachable.add(neighbor)
                q.append(neighbor)

    assert set(traversal_result) == reachable


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


def test_bfs_traversal(graph: Graph[str]) -> None:
    """Test BFS traversal from a start vertex."""
    bfs = BFS[str]()
    start_vertex = graph.get_vertex("0")
    assert start_vertex is not None

    traversal = bfs.traverse(graph, start_vertex)
    # The exact order depends on neighbor iteration order.
    # We check for correctness of visited nodes and their count.
    expected_reachable_nodes = {"0", "1", "2", "3", "4", "5", "6", "7"}
    traversed_keys = {v.key for v in traversal}
    assert traversed_keys == expected_reachable_nodes
    assert len(traversal) == 8


def test_bfs_traversal_disconnected_component(graph: Graph[str]) -> None:
    """Test BFS on a component disconnected from the start vertex."""
    bfs = BFS[str]()
    # Add a disconnected component
    v8 = graph.add_vertex("8")
    v9 = graph.add_vertex("9")
    graph.add_edge(v8, v9)

    start_vertex = graph.get_vertex("0")
    assert start_vertex is not None

    traversal = bfs.traverse(graph, start_vertex)
    traversed_keys = {v.key for v in traversal}
    assert "8" not in traversed_keys
    assert "9" not in traversed_keys
    assert len(traversal) == 8


def test_bfs_traversal_start_not_in_graph() -> None:
    """Test that ValueError is raised if the start vertex is not in the graph."""
    graph = Graph[int]()
    graph.add_vertex(1)
    start_vertex_not_in_graph = Vertex(99)
    bfs = BFS[int]()
    with pytest.raises(
        ValueError, match="Start vertex must be in the graph"
    ):
        bfs.traverse(graph, start_vertex_not_in_graph)


def test_bfs_single_node_graph() -> None:
    """Test BFS on a graph with a single node."""
    graph = Graph[str]()
    start_vertex = graph.add_vertex("A")
    bfs = BFS[str]()
    traversal = bfs.traverse(graph, start_vertex)
    assert traversal == [start_vertex]


def test_bfs_linear_graph() -> None:
    """Test BFS on a linear graph (a path)."""
    graph = Graph[int]()
    vertices = [graph.add_vertex(i) for i in range(5)]
    for i in range(4):
        graph.add_edge(vertices[i], vertices[i + 1])

    bfs = BFS[int]()
    start_vertex = vertices[0]
    traversal = bfs.traverse(graph, start_vertex)
    expected_order = [vertices[i] for i in range(5)]
    assert traversal == expected_order


def test_bfs_with_cycle(graph: Graph[str]) -> None:
    """Test that BFS handles cycles correctly and does not loop infinitely."""
    bfs = BFS[str]()
    # Add a cycle between 3 and 4
    v3 = graph.get_vertex("3")
    v4 = graph.get_vertex("4")
    assert v3 and v4
    graph.add_edge(v3, v4)

    start_vertex = graph.get_vertex("0")
    assert start_vertex
    traversal = bfs.traverse(graph, start_vertex)
    assert len(traversal) == len(graph)  # Should visit every node once
    assert len(set(traversal)) == len(graph)
