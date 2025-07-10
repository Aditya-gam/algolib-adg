import random
from typing import Any

import pytest

from algolib.algorithms.graph.dijkstra import DijkstraAlgorithm
from algolib.data_structures.graph import Graph


def _create_graph(num_vertices: int, num_edges: int) -> Graph[int]:
    graph = Graph[int](directed=True)
    vertices = [graph.add_vertex(i) for i in range(num_vertices)]

    # Ensure the graph is connected
    for i in range(num_vertices - 1):
        graph.add_edge(vertices[i], vertices[i + 1], weight=random.uniform(1, 10))

    # Add random edges
    for _ in range(num_edges - (num_vertices - 1)):
        u = random.choice(vertices)
        v = random.choice(vertices)
        if u != v and not any(neighbor == v for neighbor, _ in graph.neighbors(u)):
            graph.add_edge(u, v, weight=random.uniform(1, 10))

    return graph


@pytest.mark.benchmark(
    group="graph",
)
def test_dijkstra_benchmark(benchmark: Any) -> None:
    """Benchmark the Dijkstra's algorithm."""
    num_vertices = 100
    num_edges = 300
    graph = _create_graph(num_vertices, num_edges)
    source = graph.get_vertex(0)
    assert source is not None
    algo: DijkstraAlgorithm[int] = DijkstraAlgorithm()

    def f() -> None:
        algo.run(graph, source)

    benchmark.pedantic(f, rounds=3, warmup_rounds=1, iterations=1)
