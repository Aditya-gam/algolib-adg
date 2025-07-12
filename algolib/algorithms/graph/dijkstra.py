"""Dijkstra's shortest path algorithm implementation."""

import heapq
from dataclasses import dataclass
from typing import Dict, List, Optional, Set, Tuple

from algolib._typing import T
from algolib.data_structures.graph import Graph, Vertex
from algolib.interfaces import GraphAlgo


@dataclass(slots=True, init=False)
class DijkstraAlgorithm(GraphAlgo[T]):
    """Dijkstra's shortest path algorithm for weighted graphs."""

    def run(
        self, graph: Graph[T], source: Vertex[T]
    ) -> Tuple[Dict[Vertex[T], float], Dict[Vertex[T], Optional[Vertex[T]]]]:
        if source not in graph:
            raise ValueError("Source vertex not in graph")

        distances: Dict[Vertex[T], float] = {v: float("inf") for v in graph._vertices.values()}
        predecessors: Dict[Vertex[T], Optional[Vertex[T]]] = {
            v: None for v in graph._vertices.values()
        }
        distances[source] = 0.0

        pq: List[Tuple[float, Vertex[T]]] = [(0.0, source)]
        visited: Set[Vertex[T]] = set()

        while pq:
            current_dist, current_vertex = heapq.heappop(pq)
            if current_vertex in visited:
                continue
            visited.add(current_vertex)

            for neighbor, weight in graph.neighbors(current_vertex):
                if weight < 0:
                    raise ValueError("Dijkstra's algorithm doesn't work with negative weights")

                if neighbor not in visited and current_dist + weight < distances[neighbor]:
                    new_dist = current_dist + weight
                    distances[neighbor] = new_dist
                    predecessors[neighbor] = current_vertex
                    heapq.heappush(pq, (new_dist, neighbor))

        return distances, predecessors

    def shortest_path(
        self, graph: Graph[T], source: Vertex[T], target: Vertex[T]
    ) -> Optional[List[Vertex[T]]]:
        distances, predecessors = self.run(graph, source)
        if distances[target] == float("inf"):
            return None

        path: List[Vertex[T]] = []
        current: Optional[Vertex[T]] = target
        while current is not None:
            path.append(current)
            current = predecessors[current]
        return path[::-1]
