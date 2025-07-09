from collections import deque
from typing import Any, Deque, List, Set

from algolib._typing import T
from algolib.data_structures.graph import Graph, Vertex
from algolib.interfaces import GraphAlgo


class BFS(GraphAlgo[T]):
    """
    Breadth-First Search (BFS) algorithm implemented for the Graph data structure.
    """

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

    def run(self, graph: Graph[T], start_vertex_key: T) -> List[Vertex[T]]:
        """Runs the BFS algorithm."""
        start_vertex = graph.get_vertex(start_vertex_key)
        if not start_vertex:
            raise ValueError("Start vertex must be in the graph")

        return self.traverse(graph, start_vertex)


# Protocol check to ensure BFS implements GraphAlgo
_bfs_protocol_check: type[GraphAlgo[Any]] = BFS
