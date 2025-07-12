"""Prim's Minimum Spanning Tree algorithm implementation."""

import heapq
from dataclasses import dataclass
from typing import List, Set, Tuple

from algolib._typing import T
from algolib.data_structures.graph import Graph, Vertex
from algolib.interfaces import GraphAlgo


@dataclass(slots=True, init=False)
class PrimMST(GraphAlgo[T]):
    """Prim's algorithm to generate a Minimum Spanning Tree."""

    def run(self, graph: Graph[T]) -> Tuple[List[Tuple[Vertex[T], Vertex[T], float]], float]:
        if len(graph) == 0:
            raise ValueError("Graph is empty")

        vertices = list(graph._vertices.values())
        start_vertex = vertices[0]

        mst_edges: List[Tuple[Vertex[T], Vertex[T], float]] = []
        total_weight = 0.0
        visited: Set[Vertex[T]] = {start_vertex}

        pq: List[Tuple[float, Vertex[T], Vertex[T]]] = []
        for neighbor, weight in graph.neighbors(start_vertex):
            heapq.heappush(pq, (weight, start_vertex, neighbor))

        while pq and len(visited) < len(graph):
            weight, u, v = heapq.heappop(pq)
            if v in visited:
                continue

            mst_edges.append((u, v, weight))
            total_weight += weight
            visited.add(v)

            for neighbor, edge_weight in graph.neighbors(v):
                if neighbor not in visited:
                    heapq.heappush(pq, (edge_weight, v, neighbor))

        if len(visited) != len(graph):
            raise ValueError("Graph is not connected")

        return mst_edges, total_weight
