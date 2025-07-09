from collections import deque
from typing import Any, Deque, Generic, List, Set, cast

from algolib._typing import T
from algolib.data_structures.graph import Graph, Vertex
from algolib.interfaces import GraphSolver


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

    def run(self, data: Any) -> Any:
        """Runs the BFS algorithm."""
        if not isinstance(data, tuple) or len(data) != 2:
            raise TypeError("Expected a tuple (graph, start_vertex) for BFS.")

        graph, start_vertex = data
        if not isinstance(graph, Graph):
            raise TypeError("First element of the tuple must be a Graph.")
        if not isinstance(start_vertex, Vertex):
            raise TypeError("Second element of the tuple must be a Vertex.")

        return self.traverse(cast(Graph[T], graph), cast(Vertex[T], start_vertex))


_bfs_protocol_check: type[GraphSolver] = BFS
