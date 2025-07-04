import pytest

from algolib.data_structures.graph import Graph, Vertex


@pytest.fixture()
def graph() -> Graph[str]:
    return Graph[str]()


def test_add_vertex(graph: Graph[str]) -> None:
    vertex = graph.add_vertex("A")
    assert isinstance(vertex, Vertex)
    assert vertex.key == "A"
    assert "A" in graph


def test_add_edge_undirected(graph: Graph[str]) -> None:
    v1 = graph.add_vertex("A")
    v2 = graph.add_vertex("B")
    graph.add_edge(v1, v2, weight=10)

    neighbors_v1 = list(graph.neighbors(v1))
    neighbors_v2 = list(graph.neighbors(v2))

    assert len(neighbors_v1) == 1
    assert neighbors_v1[0] == (v2, 10)
    assert len(neighbors_v2) == 1
    assert neighbors_v2[0] == (v1, 10)


def test_add_edge_directed(graph: Graph[str]) -> None:
    graph_directed = Graph[str](directed=True)
    v1 = graph_directed.add_vertex("A")
    v2 = graph_directed.add_vertex("B")
    graph_directed.add_edge(v1, v2, weight=10)

    neighbors_v1 = list(graph_directed.neighbors(v1))
    neighbors_v2 = list(graph_directed.neighbors(v2))

    assert len(neighbors_v1) == 1
    assert neighbors_v1[0] == (v2, 10)
    assert len(neighbors_v2) == 0


def test_neighbors(graph: Graph[str]) -> None:
    vA = graph.add_vertex("A")
    vB = graph.add_vertex("B")
    vC = graph.add_vertex("C")
    graph.add_edge(vA, vB, 5)
    graph.add_edge(vA, vC, 3)

    neighbors_A = dict(graph.neighbors(vA))
    assert neighbors_A == {vB: 5, vC: 3}
    assert dict(graph.neighbors(vB)) == {vA: 5}


def test_get_vertex(graph: Graph[str]) -> None:
    graph.add_vertex("A")
    vertex = graph.get_vertex("A")
    assert vertex is not None
    assert vertex.key == "A"
    assert graph.get_vertex("B") is None


def test_graph_len(graph: Graph[str]) -> None:
    assert len(graph) == 0
    graph.add_vertex("A")
    assert len(graph) == 1
    graph.add_vertex("B")
    assert len(graph) == 2


def test_vertex_repr() -> None:
    vertex = Vertex("A")
    assert repr(vertex) == "Vertex(A)"


def test_add_edge_with_nonexistent_vertex(graph: Graph[str]) -> None:
    vA = Vertex("A")
    vB = graph.add_vertex("B")
    with pytest.raises(ValueError, match="Both vertices must be in the graph"):
        graph.add_edge(vA, vB)


def test_neighbors_of_nonexistent_vertex(graph: Graph[str]) -> None:
    vA = Vertex("A")
    with pytest.raises(ValueError, match="Vertex not in graph"):
        list(graph.neighbors(vA))


def test_vertex_equality() -> None:
    v1 = Vertex("A")
    v2 = Vertex("A")
    v3 = Vertex("B")
    assert v1 == v2
    assert v1 != v3
    assert v1 != "A"


def test_add_existing_vertex(graph: Graph[str]) -> None:
    v1 = graph.add_vertex("A")
    v2 = graph.add_vertex("A")
    assert v1 is v2
    assert len(graph) == 1


def test_graph_with_self_loops_directed() -> None:
    graph = Graph[str](directed=True)
    v1 = graph.add_vertex("A")
    graph.add_edge(v1, v1)
    neighbors = list(graph.neighbors(v1))
    assert len(neighbors) == 1
    assert neighbors[0] == (v1, 1.0)


def test_graph_with_self_loops_undirected(graph: Graph[str]) -> None:
    v1 = graph.add_vertex("A")
    graph.add_edge(v1, v1)
    neighbors = list(graph.neighbors(v1))
    assert len(neighbors) == 2  # Edge to self is added twice
    assert neighbors[0] == (v1, 1.0)
    assert neighbors[1] == (v1, 1.0)


def test_graph_multiple_edges_between_vertices(graph: Graph[str]) -> None:
    v1 = graph.add_vertex("A")
    v2 = graph.add_vertex("B")
    graph.add_edge(v1, v2, weight=5)
    graph.add_edge(v1, v2, weight=10)
    neighbors = list(graph.neighbors(v1))
    assert len(neighbors) == 2
    assert (v2, 5) in neighbors
    assert (v2, 10) in neighbors


def test_graph_neighbors_of_isolated_vertex(graph: Graph[str]) -> None:
    v1 = graph.add_vertex("A")
    assert len(list(graph.neighbors(v1))) == 0


def test_edge_weights(graph: Graph[str]) -> None:
    v1 = graph.add_vertex("A")
    v2 = graph.add_vertex("B")
    graph.add_edge(v1, v2, weight=3.14)
    neighbors = list(graph.neighbors(v1))
    assert neighbors[0] == (v2, 3.14)
