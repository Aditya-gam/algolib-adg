"""Unit tests for graph algorithms."""

from typing import List, cast

import pytest

from algolib.algorithms.graph import DijkstraAlgorithm, KruskalMST, PrimMST, TopologicalSort
from algolib.data_structures import Graph, Vertex


class TestDijkstraAlgorithm:
    """Test cases for Dijkstra's shortest path algorithm."""

    @pytest.fixture
    def dijkstra_solver(self) -> DijkstraAlgorithm[int]:
        """Provide DijkstraAlgorithm instance."""
        return DijkstraAlgorithm[int]()

    @pytest.fixture
    def sample_graph(self) -> Graph[int]:
        """Provide sample graph for testing."""
        graph = Graph[int](directed=True)
        # Add vertices
        for i in range(5):
            graph.add_vertex(i)

        # Add edges with weights
        v0, v1, v2, v3, v4 = (graph.get_vertex(i) for i in range(5))
        assert (
            v0 is not None
            and v1 is not None
            and v2 is not None
            and v3 is not None
            and v4 is not None
        )
        graph.add_edge(v0, v1, 4)
        graph.add_edge(v0, v2, 2)
        graph.add_edge(v1, v2, 1)
        graph.add_edge(v1, v3, 5)
        graph.add_edge(v2, v3, 8)
        graph.add_edge(v2, v4, 10)
        graph.add_edge(v3, v4, 2)

        return graph

    def test_basic_dijkstra(
        self, dijkstra_solver: DijkstraAlgorithm[int], sample_graph: Graph[int]
    ) -> None:
        """Test basic Dijkstra algorithm."""
        start_vertex = sample_graph.get_vertex(0)
        assert start_vertex is not None
        distances, _ = dijkstra_solver.run(sample_graph, start_vertex)

        v1, v2, v3, v4 = (sample_graph.get_vertex(i) for i in range(1, 5))
        assert v1 is not None and v2 is not None and v3 is not None and v4 is not None
        assert distances[start_vertex] == 0  # Distance to self is 0
        assert distances[v1] == 4  # Direct edge to vertex 1
        assert distances[v2] == 2  # Direct edge to vertex 2
        assert distances[v3] == 9  # 0 -> 1 -> 3 = 4 + 5
        # 0 -> 1 -> 3 -> 4 = 4 + 5 + 2
        assert distances[v4] == 11

    def test_dijkstra_empty_graph(self, dijkstra_solver: DijkstraAlgorithm[int]) -> None:
        """Test Dijkstra with empty graph."""
        graph = Graph[int](directed=True)
        start_vertex = Vertex(0)
        with pytest.raises(ValueError, match="Source vertex not in graph"):
            dijkstra_solver.run(graph, start_vertex)

    def test_dijkstra_single_vertex(self, dijkstra_solver: DijkstraAlgorithm[int]) -> None:
        """Test Dijkstra with single vertex."""
        graph = Graph[int](directed=True)
        vertex = graph.add_vertex(0)
        distances, _ = dijkstra_solver.run(graph, vertex)
        assert distances[vertex] == 0

    def test_dijkstra_disconnected_graph(self, dijkstra_solver: DijkstraAlgorithm[int]) -> None:
        """Test Dijkstra with disconnected graph."""
        graph = Graph[int](directed=True)
        graph.add_vertex(0)
        graph.add_vertex(1)
        # No edges between vertices

        start_vertex = graph.get_vertex(0)
        v1 = graph.get_vertex(1)
        assert start_vertex is not None and v1 is not None
        distances, _ = dijkstra_solver.run(graph, start_vertex)
        assert distances[start_vertex] == 0
        assert distances[v1] == float("inf")  # Unreachable

    def test_dijkstra_negative_weights_raises_error(
        self, dijkstra_solver: DijkstraAlgorithm[int]
    ) -> None:
        """Test that negative weights raise error."""
        graph = Graph[int](directed=True)
        v0 = graph.add_vertex(0)
        v1 = graph.add_vertex(1)
        graph.add_edge(v0, v1, -1)  # Negative weight

        start_vertex = graph.get_vertex(0)
        assert start_vertex is not None
        with pytest.raises(
            ValueError, match="Dijkstra's algorithm doesn't work with negative weights"
        ):
            dijkstra_solver.run(graph, start_vertex)

    def test_dijkstra_path_reconstruction(
        self, dijkstra_solver: DijkstraAlgorithm[int], sample_graph: Graph[int]
    ) -> None:
        """Test path reconstruction."""
        start_vertex = sample_graph.get_vertex(0)
        target_vertex = sample_graph.get_vertex(4)
        assert start_vertex is not None and target_vertex is not None
        path = dijkstra_solver.shortest_path(sample_graph, start_vertex, target_vertex)
        assert path is not None
        assert len(path) == 4
        assert path[0] == start_vertex
        assert path[-1] == target_vertex

    def test_dijkstra_multiple_sources(
        self, dijkstra_solver: DijkstraAlgorithm[int], sample_graph: Graph[int]
    ) -> None:
        """Test Dijkstra from different source vertices."""
        # Test from vertex 1
        start_vertex = sample_graph.get_vertex(1)
        v2, v3, v4 = (sample_graph.get_vertex(i) for i in range(2, 5))
        assert start_vertex is not None and v2 is not None and v3 is not None and v4 is not None
        distances, _ = dijkstra_solver.run(sample_graph, start_vertex)
        assert distances[start_vertex] == 0
        assert distances[v2] == 1
        assert distances[v3] == 5
        assert distances[v4] == 7

    def test_dijkstra_undirected_graph(self, dijkstra_solver: DijkstraAlgorithm[int]) -> None:
        """Test Dijkstra with undirected graph."""
        graph = Graph[int](directed=False)
        v0 = graph.add_vertex(0)
        v1 = graph.add_vertex(1)
        v2 = graph.add_vertex(2)

        graph.add_edge(v0, v1, 2)
        graph.add_edge(v1, v2, 3)

        start_vertex = graph.get_vertex(0)
        assert start_vertex is not None
        distances, _ = dijkstra_solver.run(graph, start_vertex)
        assert distances[start_vertex] == 0
        assert distances[v1] == 2
        assert distances[v2] == 5

    def test_dijkstra_self_loops(self, dijkstra_solver: DijkstraAlgorithm[int]) -> None:
        """Test Dijkstra with self-loops."""
        graph = Graph[int](directed=True)
        v0 = graph.add_vertex(0)
        graph.add_edge(v0, v0, 5)  # Self-loop

        start_vertex = graph.get_vertex(0)
        assert start_vertex is not None
        distances, _ = dijkstra_solver.run(graph, start_vertex)
        assert distances[start_vertex] == 0  # Should not use self-loop

    def test_dijkstra_parallel_edges(self, dijkstra_solver: DijkstraAlgorithm[int]) -> None:
        """Test Dijkstra with parallel edges."""
        graph = Graph[int](directed=True)
        v0 = graph.add_vertex(0)
        v1 = graph.add_vertex(1)
        graph.add_edge(v0, v1, 5)
        graph.add_edge(v0, v1, 3)  # Parallel edge with lower weight

        start_vertex = graph.get_vertex(0)
        assert start_vertex is not None
        distances, _ = dijkstra_solver.run(graph, start_vertex)
        assert distances[v1] == 3  # Should use the lower weight edge


class TestKruskalMST:
    """Test cases for Kruskal's Minimum Spanning Tree algorithm."""

    @pytest.fixture
    def kruskal_solver(self) -> KruskalMST[int]:
        """Provide KruskalMST instance."""
        return KruskalMST[int]()

    @pytest.fixture
    def sample_graph(self) -> Graph[int]:
        """Provide sample graph for testing."""
        graph = Graph[int](directed=False)
        for i in range(4):
            graph.add_vertex(i)

        # Add edges with weights
        v0, v1, v2, v3 = (graph.get_vertex(i) for i in range(4))
        assert v0 is not None and v1 is not None and v2 is not None and v3 is not None
        graph.add_edge(v0, v1, 10)
        graph.add_edge(v0, v2, 6)
        graph.add_edge(v0, v3, 5)
        graph.add_edge(v1, v3, 15)
        graph.add_edge(v2, v3, 4)

        return graph

    def test_basic_kruskal(self, kruskal_solver: KruskalMST[int], sample_graph: Graph[int]) -> None:
        """Test basic Kruskal algorithm."""
        edges, total_weight = kruskal_solver.run(sample_graph)

        # MST should have n-1 edges for n vertices
        assert len(edges) == 3  # 4 vertices - 1 = 3 edges

        # Total weight should be minimum
        # The MST selects: (2,3):4, (0,3):5, (0,1):10 = 19
        assert total_weight == 19.0

    def test_kruskal_empty_graph(self, kruskal_solver: KruskalMST[int]) -> None:
        """Test Kruskal with empty graph."""
        graph = Graph[int](directed=False)
        with pytest.raises(ValueError, match="Graph is empty"):
            kruskal_solver.run(graph)

    def test_kruskal_single_vertex(self, kruskal_solver: KruskalMST[int]) -> None:
        """Test Kruskal with single vertex."""
        graph = Graph[int](directed=False)
        graph.add_vertex(0)
        edges, total_weight = kruskal_solver.run(graph)
        assert edges == []
        assert total_weight == 0

    def test_kruskal_disconnected_graph(self, kruskal_solver: KruskalMST[int]) -> None:
        """Test Kruskal with disconnected graph."""
        graph = Graph[int](directed=False)
        graph.add_vertex(0)
        graph.add_vertex(1)
        # No edges between vertices

        edges, total_weight = kruskal_solver.run(graph)
        assert edges == []
        assert total_weight == 0

    def test_kruskal_negative_weights(self, kruskal_solver: KruskalMST[int]) -> None:
        """Test Kruskal with negative weights."""
        graph = Graph[int](directed=False)
        v0 = graph.add_vertex(0)
        v1 = graph.add_vertex(1)
        v2 = graph.add_vertex(2)

        graph.add_edge(v0, v1, -2)
        graph.add_edge(v1, v2, 3)
        graph.add_edge(v0, v2, 1)

        edges, _ = kruskal_solver.run(graph)
        assert len(edges) == 2
        # Should include the negative weight edge if it's part of MST

    def test_kruskal_self_loops(self, kruskal_solver: KruskalMST[int]) -> None:
        """Test Kruskal with self-loops."""
        graph = Graph[int](directed=False)
        v0 = graph.add_vertex(0)
        graph.add_edge(v0, v0, 5)  # Self-loop

        edges, total_weight = kruskal_solver.run(graph)
        assert edges == []
        assert total_weight == 0

    def test_kruskal_parallel_edges(self, kruskal_solver: KruskalMST[int]) -> None:
        """Test Kruskal with parallel edges."""
        graph = Graph[int](directed=False)
        v0 = graph.add_vertex(0)
        v1 = graph.add_vertex(1)

        graph.add_edge(v0, v1, 5)
        graph.add_edge(v0, v1, 3)  # Parallel edge with lower weight

        edges, total_weight = kruskal_solver.run(graph)
        assert len(edges) == 1
        assert total_weight == 3  # Should use the lower weight edge


class TestPrimMST:
    """Test cases for Prim's Minimum Spanning Tree algorithm."""

    @pytest.fixture
    def prim_solver(self) -> PrimMST[int]:
        """Provide PrimMST instance."""
        return PrimMST[int]()

    @pytest.fixture
    def sample_graph(self) -> Graph[int]:
        """Provide sample graph for testing."""
        graph = Graph[int](directed=False)
        for i in range(4):
            graph.add_vertex(i)

        # Add edges with weights
        v0, v1, v2, v3 = (graph.get_vertex(i) for i in range(4))
        assert v0 is not None and v1 is not None and v2 is not None and v3 is not None
        graph.add_edge(v0, v1, 10)
        graph.add_edge(v0, v2, 6)
        graph.add_edge(v0, v3, 5)
        graph.add_edge(v1, v3, 15)
        graph.add_edge(v2, v3, 4)

        return graph

    def test_basic_prim(self, prim_solver: PrimMST[int], sample_graph: Graph[int]) -> None:
        """Test basic Prim algorithm."""
        edges, total_weight = prim_solver.run(sample_graph)

        # MST should have n-1 edges for n vertices
        assert len(edges) == 3  # 4 vertices - 1 = 3 edges

        # Total weight should be minimum
        # The MST selects: (2,3):4, (0,3):5, (0,1):10 = 19
        assert total_weight == 19.0

    def test_prim_empty_graph(self, prim_solver: PrimMST[int]) -> None:
        """Test Prim with empty graph."""
        graph = Graph[int](directed=False)
        with pytest.raises(ValueError, match="Graph is empty"):
            prim_solver.run(graph)

    def test_prim_single_vertex(self, prim_solver: PrimMST[int]) -> None:
        """Test Prim with single vertex."""
        graph = Graph[int](directed=False)
        graph.add_vertex(0)
        edges, total_weight = prim_solver.run(graph)
        assert edges == []
        assert total_weight == 0

    def test_prim_disconnected_graph(self, prim_solver: PrimMST[int]) -> None:
        """Test Prim with disconnected graph."""
        graph = Graph[int](directed=False)
        graph.add_vertex(0)
        graph.add_vertex(1)
        # No edges between vertices

        with pytest.raises(ValueError, match="Graph is not connected"):
            prim_solver.run(graph)

    def test_prim_different_start_vertices(
        self, prim_solver: PrimMST[int], sample_graph: Graph[int]
    ) -> None:
        """Test Prim with different start vertices."""
        # Prim always starts from the first vertex in the graph
        edges, total_weight = prim_solver.run(sample_graph)

        # Should still get MST with same total weight
        assert len(edges) == 3
        assert total_weight == 19.0

    def test_prim_negative_weights(self, prim_solver: PrimMST[int]) -> None:
        """Test Prim with negative weights."""
        graph = Graph[int](directed=False)
        v0 = graph.add_vertex(0)
        v1 = graph.add_vertex(1)
        v2 = graph.add_vertex(2)

        graph.add_edge(v0, v1, -2)
        graph.add_edge(v1, v2, 3)
        graph.add_edge(v0, v2, 1)

        edges, _ = prim_solver.run(graph)
        assert len(edges) == 2

    def test_prim_self_loops(self, prim_solver: PrimMST[int]) -> None:
        """Test Prim with self-loops."""
        graph = Graph[int](directed=False)
        v0 = graph.add_vertex(0)
        graph.add_edge(v0, v0, 5)  # Self-loop

        edges, total_weight = prim_solver.run(graph)
        assert edges == []
        assert total_weight == 0

    def test_prim_parallel_edges(self, prim_solver: PrimMST[int]) -> None:
        """Test Prim with parallel edges."""
        graph = Graph[int](directed=False)
        v0 = graph.add_vertex(0)
        v1 = graph.add_vertex(1)

        graph.add_edge(v0, v1, 5)
        graph.add_edge(v0, v1, 3)  # Parallel edge with lower weight

        edges, total_weight = prim_solver.run(graph)
        assert len(edges) == 1
        assert total_weight == 3  # Should use the lower weight edge


class TestTopologicalSort:
    """Test cases for Topological Sort algorithm."""

    @pytest.fixture
    def topological_sorter(self) -> TopologicalSort[int]:
        """Provide TopologicalSort instance."""
        return TopologicalSort[int]()

    @pytest.fixture
    def sample_dag(self) -> Graph[int]:
        """Provide sample directed acyclic graph for testing."""
        graph = Graph[int](directed=True)
        for i in range(6):
            graph.add_vertex(i)

        # Add edges to create a DAG
        v0, v1, v2, v3, v4, v5 = (graph.get_vertex(i) for i in range(6))
        assert (
            v0 is not None
            and v1 is not None
            and v2 is not None
            and v3 is not None
            and v4 is not None
            and v5 is not None
        )
        graph.add_edge(v5, v2)
        graph.add_edge(v5, v0)
        graph.add_edge(v4, v0)
        graph.add_edge(v4, v1)
        graph.add_edge(v2, v3)
        graph.add_edge(v3, v1)

        return graph

    def test_basic_topological_sort(
        self, topological_sorter: TopologicalSort[int], sample_dag: Graph[int]
    ) -> None:
        """Test basic topological sort."""
        result = topological_sorter.sort(sample_dag)

        # Should have all vertices
        assert len(result) == 6

        # Should be a valid topological order
        assert self._is_valid_topological_order(sample_dag, result)

    def test_topological_sort_empty_graph(self, topological_sorter: TopologicalSort[int]) -> None:
        """Test topological sort with empty graph."""
        graph = Graph[int](directed=True)
        result = topological_sorter.sort(graph)
        assert result == []

    def test_topological_sort_single_vertex(self, topological_sorter: TopologicalSort[int]) -> None:
        """Test topological sort with single vertex."""
        graph = Graph[int](directed=True)
        graph.add_vertex(0)
        result = topological_sorter.sort(graph)
        assert len(result) == 1
        assert result[0].key == 0

    def test_topological_sort_linear_dag(self, topological_sorter: TopologicalSort[int]) -> None:
        """Test topological sort with linear DAG."""
        graph = Graph[int](directed=True)
        for i in range(4):
            graph.add_vertex(i)

        v0, v1, v2, v3 = (graph.get_vertex(i) for i in range(4))
        assert v0 is not None and v1 is not None and v2 is not None and v3 is not None
        graph.add_edge(v0, v1)
        graph.add_edge(v1, v2)
        graph.add_edge(v2, v3)

        result = topological_sorter.sort(graph)
        assert len(result) == 4
        assert [v.key for v in result] == [0, 1, 2, 3]

    def test_topological_sort_cycle_raises_error(
        self, topological_sorter: TopologicalSort[int]
    ) -> None:
        """Test that cycle raises error."""
        graph = Graph[int](directed=True)
        for i in range(3):
            graph.add_vertex(i)

        v0, v1, v2 = (graph.get_vertex(i) for i in range(3))
        assert v0 is not None and v1 is not None and v2 is not None
        graph.add_edge(v0, v1)
        graph.add_edge(v1, v2)
        graph.add_edge(v2, v0)  # Creates cycle

        with pytest.raises(ValueError, match="Graph contains cycle"):
            topological_sorter.sort(graph)

    def test_topological_sort_self_loop_raises_error(
        self, topological_sorter: TopologicalSort[int]
    ) -> None:
        """Test that self-loop raises error."""
        graph = Graph[int](directed=True)
        graph.add_vertex(0)
        v0 = graph.get_vertex(0)
        assert v0 is not None
        graph.add_edge(v0, v0)  # Self-loop

        with pytest.raises(ValueError, match="Graph contains cycle"):
            topological_sorter.sort(graph)

    def test_topological_sort_disconnected_components(
        self, topological_sorter: TopologicalSort[int]
    ) -> None:
        """Test topological sort with disconnected components."""
        graph = Graph[int](directed=True)
        for i in range(4):
            graph.add_vertex(i)

        # Component 1: 0 -> 1
        v0, v1, v2, v3 = (graph.get_vertex(i) for i in range(4))
        assert v0 is not None and v1 is not None and v2 is not None and v3 is not None
        graph.add_edge(v0, v1)
        # Component 2: 2 -> 3
        graph.add_edge(v2, v3)

        result = topological_sorter.sort(graph)
        assert len(result) == 4
        assert self._is_valid_topological_order(graph, result)

    def test_topological_sort_multiple_valid_orders(
        self, topological_sorter: TopologicalSort[int]
    ) -> None:
        """Test that multiple valid topological orders are possible."""
        graph = Graph[int](directed=True)
        for i in range(4):
            graph.add_vertex(i)

        v0, v1, v2, v3 = (graph.get_vertex(i) for i in range(4))
        assert v0 is not None and v1 is not None and v2 is not None and v3 is not None
        graph.add_edge(v0, v2)
        graph.add_edge(v1, v2)
        graph.add_edge(v2, v3)

        result = topological_sorter.sort(graph)
        assert len(result) == 4
        assert self._is_valid_topological_order(graph, result)
        # Both [0, 1, 2, 3] and [1, 0, 2, 3] are valid

    def test_topological_sort_complex_dag(self, topological_sorter: TopologicalSort[int]) -> None:
        """Test topological sort with complex DAG."""
        graph = Graph[int](directed=True)
        for i in range(8):
            graph.add_vertex(i)

        # Create a more complex DAG
        vertices_raw = [graph.get_vertex(i) for i in range(8)]
        assert all(v is not None for v in vertices_raw)
        vertices = cast(List[Vertex[int]], [v for v in vertices_raw if v is not None])
        edges = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 4), (2, 5), (3, 6), (4, 6), (5, 7), (6, 7)]
        for u, v in edges:
            graph.add_edge(vertices[u], vertices[v])

        result = topological_sorter.sort(graph)
        assert len(result) == 8
        assert self._is_valid_topological_order(graph, result)

    def test_topological_sort_undirected_graph_raises_error(
        self, topological_sorter: TopologicalSort[int]
    ) -> None:
        """Test that undirected graph raises error."""
        graph = Graph[int](directed=False)
        graph.add_vertex(0)
        graph.add_vertex(1)
        v0, v1 = graph.get_vertex(0), graph.get_vertex(1)
        assert v0 is not None and v1 is not None
        graph.add_edge(v0, v1)

        with pytest.raises(ValueError, match="Topological sort requires a directed graph"):
            topological_sorter.sort(graph)

    def _is_valid_topological_order(self, graph: Graph[int], order: List[Vertex[int]]) -> bool:
        """Check if the order is a valid topological order."""
        # Create a mapping from vertex to its position in the order
        position = {vertex: i for i, vertex in enumerate(order)}

        # Check that for every edge (u, v), u comes before v in the order
        for vertex in graph.vertices():
            for neighbor, _ in graph.neighbors(vertex):
                if position[vertex] >= position[neighbor]:
                    return False

        return True
