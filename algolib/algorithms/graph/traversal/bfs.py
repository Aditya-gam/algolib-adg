from collections import deque
from typing import Deque, Generic, List, Set, TypeVar

from algolib.data_structures.graph import Graph, Vertex

T = TypeVar("T")


class BFS(Generic[T]):
    def traverse(self, graph: Graph[T], start_vertex: Vertex[T]) -> List[Vertex[T]]:
        if start_vertex not in graph:
            raise ValueError("Start vertex must be in the graph")

        queue: Deque[Vertex[T]] = deque([start_vertex])
        visited: Set[Vertex[T]] = {start_vertex}
        traversal_order: List[Vertex[T]] = []

        while queue:
            current_vertex = queue.popleft()
            traversal_order.append(current_vertex)

            for neighbor, _ in graph.neighbors(current_vertex):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return traversal_order
