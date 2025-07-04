from typing import Any

import pytest

from algolib.algorithms.graph.traversal.bfs import BFS
from algolib.data_structures.graph import Graph, Vertex


@pytest.fixture
def sample_graph() -> Graph[str]:
    graph: Graph[str] = Graph()
    vertices = [graph.add_vertex(str(i)) for i in range(6)]
    graph.add_edge(vertices[0], vertices[1])
    graph.add_edge(vertices[0], vertices[2])
    graph.add_edge(vertices[1], vertices[3])
    graph.add_edge(vertices[2], vertices[4])
    graph.add_edge(vertices[3], vertices[5])
    graph.add_edge(vertices[4], vertices[5])
    return graph


def test_bfs_traversal(sample_graph: Graph[str]) -> None:
    bfs = BFS()
    start_vertex: Vertex[str] = Vertex("0")
    traversal_order = bfs.traverse(sample_graph, start_vertex)
    expected_order = [Vertex("0"), Vertex("1"), Vertex("2"), Vertex("3"), Vertex("4"), Vertex("5")]
    assert traversal_order == expected_order


def test_bfs_traversal_disconnected_graph() -> None:
    graph: Graph[str] = Graph()
    vertex_a: Vertex[str] = graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_vertex("C")

    bfs = BFS()
    traversal_order = bfs.traverse(graph, vertex_a)
    assert traversal_order == [Vertex("A")]


def test_bfs_traversal_empty_graph() -> None:
    graph: Graph[str] = Graph()
    bfs = BFS()
    with pytest.raises(ValueError):
        # Assuming that starting BFS on a non-existent vertex in an empty graph should raise an error
        # Or, we could test a scenario where the start vertex is not in the graph.
        # For now, let's assume the graph must contain the start vertex.
        bfs.traverse(graph, Vertex("Start"))


def test_bfs_traversal_graph_with_cycle(sample_graph: Graph[str]) -> None:
    # Adding a cycle: 3 -> 0
    # Ensure that these vertices are in the graph.
    v3 = sample_graph.get_vertex("3")
    v0 = sample_graph.get_vertex("0")
    assert v3 is not None
    assert v0 is not None
    sample_graph.add_edge(v3, v0)

    bfs = BFS()
    start_vertex: Vertex[str] = Vertex("0")
    traversal_order = bfs.traverse(sample_graph, start_vertex)
    # The order depends on the order of neighbors in the adjacency list.
    # Given the current sample_graph edge additions: (0,1), (0,2), (1,3), (2,4), (3,5), (4,5)
    # When 3->0 is added, for vertex 3, it will visit 5 then 0 (if 0 wasn't visited).
    # Since 0 is already visited from the start, this cycle should not cause an infinite loop
    # or re-add 0 to result. The order remains deterministic.
    expected_order = [Vertex("0"), Vertex("1"), Vertex("2"), Vertex("3"), Vertex("4"), Vertex("5")]
    assert traversal_order == expected_order


def test_bfs_traversal_larger_graph() -> None:
    graph: Graph[str] = Graph()
    vertices = {str(i): graph.add_vertex(str(i)) for i in range(10)}
    graph.add_edge(vertices["0"], vertices["1"])
    graph.add_edge(vertices["0"], vertices["2"])
    graph.add_edge(vertices["1"], vertices["3"])
    graph.add_edge(vertices["1"], vertices["4"])
    graph.add_edge(vertices["2"], vertices["5"])
    graph.add_edge(vertices["2"], vertices["6"])
    graph.add_edge(vertices["3"], vertices["7"])
    graph.add_edge(vertices["4"], vertices["7"])
    graph.add_edge(vertices["5"], vertices["8"])
    graph.add_edge(vertices["6"], vertices["8"])
    graph.add_edge(vertices["7"], vertices["9"])
    graph.add_edge(vertices["8"], vertices["9"])

    bfs = BFS()
    start_vertex: Vertex[str] = vertices["0"]
    traversal_order = bfs.traverse(graph, start_vertex)
    expected_order = [
        Vertex("0"),
        Vertex("1"),
        Vertex("2"),
        Vertex("3"),
        Vertex("4"),
        Vertex("5"),
        Vertex("6"),
        Vertex("7"),
        Vertex("8"),
        Vertex("9"),
    ]
    assert traversal_order == expected_order


def test_bfs_traversal_single_node_graph() -> None:
    graph: Graph[str] = Graph()
    vertex_a: Vertex[str] = graph.add_vertex("A")
    bfs = BFS()
    traversal_order = bfs.traverse(graph, vertex_a)
    assert traversal_order == [Vertex("A")]


def test_bfs_traversal_graph_no_edges() -> None:
    graph: Graph[str] = Graph()
    vertices = [graph.add_vertex(str(i)) for i in range(5)]
    bfs = BFS()
    traversal_order = bfs.traverse(graph, vertices[0])
    assert traversal_order == [Vertex("0")]


def test_bfs_traversal_multiple_disconnected_components() -> None:
    graph: Graph[str] = Graph()
    v0: Vertex[str] = graph.add_vertex("0")
    v1: Vertex[str] = graph.add_vertex("1")
    v2: Vertex[str] = graph.add_vertex("2")
    v3: Vertex[str] = graph.add_vertex("3")
    v4: Vertex[str] = graph.add_vertex("4")

    # Component 1
    graph.add_edge(v0, v1)
    graph.add_edge(v1, v2)

    # Component 2
    graph.add_edge(v3, v4)

    bfs = BFS()
    traversal_order = bfs.traverse(graph, v0)
    assert traversal_order == [v0, v1, v2]

    traversal_order_2 = bfs.traverse(graph, v3)
    assert traversal_order_2 == [v3, v4]


def test_bfs_traversal_different_start_vertices(sample_graph: Graph[str]) -> None:
    bfs = BFS()
    # Test from vertex "1"
    start_vertex_1 = sample_graph.get_vertex("1")
    assert start_vertex_1 is not None
    traversal_order_1 = bfs.traverse(sample_graph, start_vertex_1)
    expected_order_1 = [
        sample_graph.get_vertex("1"),
        sample_graph.get_vertex("0"),
        sample_graph.get_vertex("3"),
        sample_graph.get_vertex("2"),
        sample_graph.get_vertex("5"),
        sample_graph.get_vertex("4"),
    ]
    assert traversal_order_1 == expected_order_1

    # Test from vertex "2"
    start_vertex_2 = sample_graph.get_vertex("2")
    assert start_vertex_2 is not None
    traversal_order_2 = bfs.traverse(sample_graph, start_vertex_2)
    expected_order_2 = [
        sample_graph.get_vertex("2"),
        sample_graph.get_vertex("0"),
        sample_graph.get_vertex("4"),
        sample_graph.get_vertex("1"),
        sample_graph.get_vertex("5"),
        sample_graph.get_vertex("3"),
    ]
    assert traversal_order_2 == expected_order_2


def test_bfs_traversal_complete_graph() -> None:
    graph: Graph[str] = Graph()
    vertices = [graph.add_vertex(str(i)) for i in range(4)]
    # Connect every vertex to every other vertex
    for i in range(4):
        for j in range(i + 1, 4):
            graph.add_edge(vertices[i], vertices[j])

    bfs = BFS()
    traversal_order = bfs.traverse(graph, vertices[0])
    # The order of neighbors might vary based on internal Dict order, but the set of visited nodes should be all.
    # For deterministic test, we can sort the next level neighbors or define a fixed order.
    # Given how Python dicts work, insertion order is preserved from 3.7+
    expected_order = [Vertex("0"), Vertex("1"), Vertex("2"), Vertex("3")]
    assert set(traversal_order) == set(expected_order)  # Order can vary for same depth


def test_bfs_traversal_line_graph() -> None:
    graph: Graph[str] = Graph()
    v0: Vertex[str] = graph.add_vertex("0")
    v1: Vertex[str] = graph.add_vertex("1")
    v2: Vertex[str] = graph.add_vertex("2")
    v3: Vertex[str] = graph.add_vertex("3")
    graph.add_edge(v0, v1)
    graph.add_edge(v1, v2)
    graph.add_edge(v2, v3)

    bfs = BFS()
    traversal_order = bfs.traverse(graph, v0)
    assert traversal_order == [v0, v1, v2, v3]


def test_bfs_traversal_star_graph() -> None:
    graph: Graph[str] = Graph()
    center: Vertex[str] = graph.add_vertex("Center")
    leaf1: Vertex[str] = graph.add_vertex("Leaf1")
    leaf2: Vertex[str] = graph.add_vertex("Leaf2")
    leaf3: Vertex[str] = graph.add_vertex("Leaf3")
    graph.add_edge(center, leaf1)
    graph.add_edge(center, leaf2)
    graph.add_edge(center, leaf3)

    bfs = BFS()
    traversal_order = bfs.traverse(graph, center)
    # Order of leaves can vary based on adjacency list. So check set equality for second level.
    assert traversal_order[0] == center
    assert set(traversal_order[1:]) == {leaf1, leaf2, leaf3}


def test_bfs_traversal_directed_graph() -> None:
    graph: Graph[str] = Graph(directed=True)
    vA: Vertex[str] = graph.add_vertex("A")
    vB: Vertex[str] = graph.add_vertex("B")
    vC: Vertex[str] = graph.add_vertex("C")
    vD: Vertex[str] = graph.add_vertex("D")

    graph.add_edge(vA, vB)
    graph.add_edge(vA, vC)
    graph.add_edge(vB, vD)

    bfs = BFS()
    traversal_order = bfs.traverse(graph, vA)
    assert traversal_order == [vA, vB, vC, vD]


def test_bfs_traversal_directed_graph_with_multiple_paths() -> None:
    graph: Graph[str] = Graph(directed=True)
    vA: Vertex[str] = graph.add_vertex("A")
    vB: Vertex[str] = graph.add_vertex("B")
    vC: Vertex[str] = graph.add_vertex("C")
    vD: Vertex[str] = graph.add_vertex("D")

    graph.add_edge(vA, vB)
    graph.add_edge(vA, vC)
    graph.add_edge(vB, vD)
    graph.add_edge(vC, vD)  # Both B and C can reach D

    bfs = BFS()
    traversal_order = bfs.traverse(graph, vA)
    # The order should be A, B, C, D (D is visited when B is processed first).
    assert traversal_order == [vA, vB, vC, vD]


def test_bfs_traversal_directed_graph_with_cycle() -> None:
    graph: Graph[str] = Graph(directed=True)
    vA: Vertex[str] = graph.add_vertex("A")
    vB: Vertex[str] = graph.add_vertex("B")
    vC: Vertex[str] = graph.add_vertex("C")

    graph.add_edge(vA, vB)
    graph.add_edge(vB, vC)
    graph.add_edge(vC, vA)  # Cycle A -> B -> C -> A

    bfs = BFS()
    traversal_order = bfs.traverse(graph, vA)
    # A is visited first, then B, then C. A is not revisited.
    assert traversal_order == [vA, vB, vC]


def test_bfs_traversal_string_keys() -> None:
    graph: Graph[str] = Graph[str]()
    start_vertex = graph.add_vertex("Start")
    middle_vertex = graph.add_vertex("Middle")
    end_vertex = graph.add_vertex("End")
    graph.add_edge(start_vertex, middle_vertex)
    graph.add_edge(middle_vertex, end_vertex)

    bfs = BFS()
    traversal_order = bfs.traverse(graph, start_vertex)
    assert [v.key for v in traversal_order] == ["Start", "Middle", "End"]


def test_bfs_traversal_integer_keys() -> None:
    graph: Graph[int] = Graph[int]()
    v1 = graph.add_vertex(1)
    v2 = graph.add_vertex(2)
    v3 = graph.add_vertex(3)
    graph.add_edge(v1, v2)
    graph.add_edge(v2, v3)

    bfs = BFS()
    traversal_order = bfs.traverse(graph, v1)
    assert [v.key for v in traversal_order] == [1, 2, 3]


def test_bfs_traversal_mixed_type_keys() -> None:
    # Although not generally recommended for graph keys, testing for robustness
    graph: Graph[Any] = Graph[Any]()  # Use Any for mixed types
    v1: Vertex[int] = graph.add_vertex(1)
    vA: Vertex[str] = graph.add_vertex("A")
    vFloat: Vertex[float] = graph.add_vertex(3.14)

    graph.add_edge(v1, vA)
    graph.add_edge(vA, vFloat)

    bfs = BFS()
    traversal_order = bfs.traverse(graph, v1)
    assert traversal_order == [v1, vA, vFloat]


def test_bfs_traversal_self_loop() -> None:
    graph: Graph[str] = Graph()
    vA: Vertex[str] = graph.add_vertex("A")
    vB: Vertex[str] = graph.add_vertex("B")
    graph.add_edge(vA, vA)  # Self-loop
    graph.add_edge(vA, vB)

    bfs = BFS()
    traversal_order = bfs.traverse(graph, vA)
    # Self-loop shouldn't change traversal order (A visited once)
    assert traversal_order == [vA, vB]


def test_bfs_traversal_parallel_edges() -> None:
    graph: Graph[str] = Graph()
    vA: Vertex[str] = graph.add_vertex("A")
    vB: Vertex[str] = graph.add_vertex("B")
    graph.add_edge(vA, vB)
    graph.add_edge(vA, vB, weight=2.0)  # Parallel edge

    bfs = BFS()
    traversal_order = bfs.traverse(graph, vA)
    # Parallel edges shouldn't affect BFS unique path.
    assert traversal_order == [vA, vB]


def test_bfs_traversal_start_node_no_neighbors() -> None:
    graph: Graph[str] = Graph()
    vA: Vertex[str] = graph.add_vertex("A")
    graph.add_vertex("B")  # Isolated
    bfs = BFS()
    traversal_order = bfs.traverse(graph, vA)
    assert traversal_order == [vA]


def test_bfs_traversal_unreachable_target_node() -> None:
    graph: Graph[str] = Graph()
    vA: Vertex[str] = graph.add_vertex("A")
    vB: Vertex[str] = graph.add_vertex("B")
    vC: Vertex[str] = graph.add_vertex("C")
    graph.add_edge(vA, vB)

    bfs = BFS()
    traversal_order = bfs.traverse(graph, vA)
    assert traversal_order == [vA, vB]
    assert vC not in traversal_order  # C is unreachable from A
