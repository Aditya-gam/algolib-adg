from typing import List, Set, Tuple

import pytest
from hypothesis import given
from hypothesis import strategies as st

from algolib.algorithms.graph.traversal.breadth_first_search import BreadthFirstSearch as BFS
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
def test_bfs_property_traversal_properties(graph_and_start: Tuple[Graph[int], Vertex[int]]) -> None:
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
    with pytest.raises(ValueError, match="Start vertex not in graph"):
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


def test_bfs_run_method(graph: Graph[str]) -> None:
    """Test the run method of the BFS algorithm."""
    bfs = BFS[str]()
    start_vertex = graph.get_vertex("0")
    assert start_vertex is not None

    # Test valid run
    traversal = bfs.run(graph, start_vertex.key)
    assert traversal is not None
    assert [v.key for v in traversal] == ["0", "1", "2", "3", "4", "5", "6", "7"]

    # Test with non-existent start vertex
    with pytest.raises(ValueError):
        bfs.run(graph, "8")


# Tests for shortest_path method
def test_shortest_path_same_vertex(graph: Graph[str]) -> None:
    """Test shortest path when start and end are the same vertex."""
    bfs = BFS[str]()
    start_vertex = graph.get_vertex("0")
    assert start_vertex is not None

    path = bfs.shortest_path(graph, start_vertex, start_vertex)
    assert path == [start_vertex]


def test_shortest_path_adjacent_vertices(graph: Graph[str]) -> None:
    """Test shortest path between adjacent vertices."""
    bfs = BFS[str]()
    start_vertex = graph.get_vertex("0")
    end_vertex = graph.get_vertex("1")
    assert start_vertex is not None and end_vertex is not None

    path = bfs.shortest_path(graph, start_vertex, end_vertex)
    assert path == [start_vertex, end_vertex]


def test_shortest_path_distant_vertices(graph: Graph[str]) -> None:
    """Test shortest path between distant vertices."""
    bfs = BFS[str]()
    start_vertex = graph.get_vertex("0")
    end_vertex = graph.get_vertex("7")
    assert start_vertex is not None and end_vertex is not None

    path = bfs.shortest_path(graph, start_vertex, end_vertex)
    assert path is not None
    assert path[0] == start_vertex
    assert path[-1] == end_vertex
    assert len(path) == 4  # Shortest path: 0 -> 1 -> 3 -> 7


def test_shortest_path_no_path() -> None:
    """Test shortest path when no path exists."""
    graph = Graph[int]()
    v1 = graph.add_vertex(1)
    v2 = graph.add_vertex(2)
    # No edge between v1 and v2

    bfs = BFS[int]()
    path = bfs.shortest_path(graph, v1, v2)
    assert path is None


def test_shortest_path_start_not_in_graph(graph: Graph[str]) -> None:
    """Test shortest path when start vertex is not in graph."""
    bfs = BFS[str]()
    end_vertex = graph.get_vertex("0")
    start_vertex_not_in_graph = Vertex("99")
    assert end_vertex is not None

    with pytest.raises(ValueError, match="Start and end vertices must be in graph"):
        bfs.shortest_path(graph, start_vertex_not_in_graph, end_vertex)


def test_shortest_path_end_not_in_graph(graph: Graph[str]) -> None:
    """Test shortest path when end vertex is not in graph."""
    bfs = BFS[str]()
    start_vertex = graph.get_vertex("0")
    end_vertex_not_in_graph = Vertex("99")
    assert start_vertex is not None

    with pytest.raises(ValueError, match="Start and end vertices must be in graph"):
        bfs.shortest_path(graph, start_vertex, end_vertex_not_in_graph)


def test_shortest_path_linear_graph() -> None:
    """Test shortest path in a linear graph."""
    graph = Graph[int]()
    vertices = [graph.add_vertex(i) for i in range(5)]
    for i in range(4):
        graph.add_edge(vertices[i], vertices[i + 1])

    bfs = BFS[int]()
    path = bfs.shortest_path(graph, vertices[0], vertices[4])
    assert path == vertices


def test_shortest_path_multiple_paths() -> None:
    """Test shortest path when multiple paths exist."""
    graph = Graph[str]()
    vertices = [graph.add_vertex(str(i)) for i in range(4)]
    # Create a diamond shape: 0 -> 1, 0 -> 2, 1 -> 3, 2 -> 3
    graph.add_edge(vertices[0], vertices[1])
    graph.add_edge(vertices[0], vertices[2])
    graph.add_edge(vertices[1], vertices[3])
    graph.add_edge(vertices[2], vertices[3])

    bfs = BFS[str]()
    path = bfs.shortest_path(graph, vertices[0], vertices[3])
    assert path is not None
    assert path[0] == vertices[0]
    assert path[-1] == vertices[3]
    assert len(path) == 3  # Shortest path length should be 3


def test_shortest_path_cycle() -> None:
    """Test shortest path in a graph with cycles."""
    graph = Graph[int]()
    vertices = [graph.add_vertex(i) for i in range(4)]
    # Create a cycle: 0 -> 1 -> 2 -> 3 -> 0
    for i in range(4):
        graph.add_edge(vertices[i], vertices[(i + 1) % 4])

    bfs = BFS[int]()
    path = bfs.shortest_path(graph, vertices[0], vertices[2])
    assert path is not None
    assert path[0] == vertices[0]
    assert path[-1] == vertices[2]
    assert len(path) == 3  # Shortest path: 0 -> 1 -> 2


def test_shortest_path_disconnected_graph() -> None:
    """Test shortest path in a disconnected graph."""
    graph = Graph[int]()
    # Component 1: 0 -> 1 -> 2
    v0 = graph.add_vertex(0)
    v1 = graph.add_vertex(1)
    v2 = graph.add_vertex(2)
    graph.add_edge(v0, v1)
    graph.add_edge(v1, v2)

    # Component 2: 3 -> 4
    v3 = graph.add_vertex(3)
    v4 = graph.add_vertex(4)
    graph.add_edge(v3, v4)

    bfs = BFS[int]()
    # Path within same component
    path1 = bfs.shortest_path(graph, v0, v2)
    assert path1 == [v0, v1, v2]

    # Path between different components
    path2 = bfs.shortest_path(graph, v0, v4)
    assert path2 is None


def test_shortest_path_single_vertex_graph() -> None:
    """Test shortest path in a graph with single vertex."""
    graph = Graph[str]()
    vertex = graph.add_vertex("A")

    bfs = BFS[str]()
    path = bfs.shortest_path(graph, vertex, vertex)
    assert path == [vertex]


def test_shortest_path_empty_graph() -> None:
    """Test shortest path in an empty graph."""
    graph = Graph[int]()
    v1 = Vertex(1)
    v2 = Vertex(2)

    bfs = BFS[int]()
    with pytest.raises(ValueError, match="Start and end vertices must be in graph"):
        bfs.shortest_path(graph, v1, v2)


def test_shortest_path_optimality() -> None:
    """Test that shortest path returns the optimal (shortest) path."""
    graph = Graph[int]()
    vertices = [graph.add_vertex(i) for i in range(6)]
    # Create a graph with multiple paths from 0 to 5
    # Path 1: 0 -> 1 -> 5 (length 3)
    # Path 2: 0 -> 2 -> 3 -> 4 -> 5 (length 5)
    # Path 3: 0 -> 2 -> 5 (length 3)
    graph.add_edge(vertices[0], vertices[1])
    graph.add_edge(vertices[1], vertices[5])
    graph.add_edge(vertices[0], vertices[2])
    graph.add_edge(vertices[2], vertices[3])
    graph.add_edge(vertices[3], vertices[4])
    graph.add_edge(vertices[4], vertices[5])
    graph.add_edge(vertices[2], vertices[5])

    bfs = BFS[int]()
    path = bfs.shortest_path(graph, vertices[0], vertices[5])
    assert path is not None
    assert len(path) == 3  # Should find the shortest path of length 3
