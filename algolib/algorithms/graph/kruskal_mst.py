"""Kruskal's Minimum Spanning Tree algorithm implementation."""

from dataclasses import dataclass
from typing import List, Tuple

from algolib._typing import T
from algolib.data_structures.disjoint_set import DisjointSet
from algolib.data_structures.graph import Graph, Vertex
from algolib.interfaces import GraphAlgo


@dataclass(slots=True, init=False)
class KruskalMST(GraphAlgo[T]):
    """Kruskal's algorithm to generate a Minimum Spanning Tree."""

    def run(self, graph: Graph[T]) -> Tuple[List[Tuple[Vertex[T], Vertex[T], float]], float]:
        if len(graph) == 0:
            raise ValueError("Graph is empty")

        edges: List[Tuple[float, Vertex[T], Vertex[T]]] = []
        for vertex in graph._vertices.values():
            for neighbor, weight in graph.neighbors(vertex):
                if not graph.directed:
                    if hash(vertex) < hash(neighbor):
                        edges.append((weight, vertex, neighbor))
                else:
                    edges.append((weight, vertex, neighbor))

        edges.sort()
        union_find = DisjointSet(graph._vertices.values())

        mst_edges: List[Tuple[Vertex[T], Vertex[T], float]] = []
        total_weight = 0.0

        for weight, u, v in edges:
            if union_find.find(u) != union_find.find(v):
                union_find.union(u, v)
                mst_edges.append((u, v, weight))
                total_weight += weight
                if len(mst_edges) == len(graph) - 1:
                    break

        return mst_edges, total_weight
