from collections import deque
from typing import Deque, Generic, List, Set

from algolib._typing import T
from algolib.data_structures.graph import Graph, Vertex


class BFS(Generic[T]):
    """Breadth-First Search (BFS) graph traversal algorithm."""

    def traverse(self, graph: Graph[T], start_vertex: Vertex[T]) -> List[Vertex[T]]:
        """Performs a breadth-first traversal on a graph.

        Args:
            graph: The graph to traverse.
            start_vertex: The vertex from which to start the traversal.

        Returns:
            A list of vertices in the order they were visited.

        Raises:
            ValueError: If the start vertex is not in the graph.
        """
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
