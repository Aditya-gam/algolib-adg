"""Breadth-First Search algorithm for graph traversal.

BFS explores vertices level by level, visiting all neighbors at the current
depth before moving to vertices at the next depth level.

Time Complexity: O(V + E) - where V is vertices, E is edges
Space Complexity: O(V) - for queue and visited set

Characteristics:
    - Level-by-level: Visits nodes in breadth-first order
    - Queue-based: Uses queue data structure
    - Shortest path: Finds shortest path in unweighted graphs
    - Complete: Explores all reachable vertices

Advantages:
    - Guarantees shortest path in unweighted graphs
    - Memory efficient for sparse graphs
    - Simple to implement and understand
    - Systematic exploration

Disadvantages:
    - Memory intensive for dense graphs
    - Not suitable for very deep graphs
    - Doesn't work with weighted shortest paths

Example:
    >>> graph = Graph()
    >>> # Add vertices and edges...
    >>> bfs = BreadthFirstSearch()
    >>> result = bfs.run(graph, start_vertex)
"""

from collections import deque
from dataclasses import dataclass
from typing import Dict, List, Optional, Set

from algolib._typing import T
from algolib.data_structures.graph import Graph, Vertex
from algolib.interfaces import GraphAlgo


@dataclass(slots=True, init=False)
class BreadthFirstSearch(GraphAlgo[T]):
    """Breadth-First Search algorithm for graph traversal."""

    def traverse(self, graph: Graph[T], start_vertex: Vertex[T]) -> List[Vertex[T]]:
        """Perform BFS traversal starting from a given vertex.

        Args:
            graph: The graph to traverse.
            start_vertex: The vertex from which to start traversal.

        Returns:
            A list of vertices visited in breadth-first order.
        """
        if start_vertex not in graph:
            raise ValueError("Start vertex not in graph")

        visited: Set[Vertex[T]] = {start_vertex}
        queue: deque[Vertex[T]] = deque([start_vertex])
        result: List[Vertex[T]] = []

        while queue:
            current = queue.popleft()
            result.append(current)

            for neighbor, _ in graph.neighbors(current):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return result

    def run(self, graph: Graph[T], start_vertex_key: T) -> List[Vertex[T]]:
        """Run BFS traversal given the key of the starting vertex.

        This keeps backward-compatibility with the original BFS API that
        accepted a vertex key instead of a `Vertex` instance.
        """
        start_vertex = graph.get_vertex(start_vertex_key)
        if start_vertex is None:
            raise ValueError("Start vertex must be in the graph")

        return self.traverse(graph, start_vertex)

    def shortest_path(
        self, graph: Graph[T], start: Vertex[T], end: Vertex[T]
    ) -> Optional[List[Vertex[T]]]:
        """Find shortest path between two vertices in an unweighted graph.

        Args:
            graph: The graph to search
            start: Starting vertex
            end: Target vertex

        Returns:
            Shortest path as list of vertices, or None if no path exists

        Raises:
            ValueError: If start or end vertex is not in graph
        """
        if start not in graph or end not in graph:
            raise ValueError("Start and end vertices must be in graph")

        if start == end:
            return [start]

        visited: Set[Vertex[T]] = set()
        queue: deque[Vertex[T]] = deque([start])
        parent: Dict[Vertex[T], Optional[Vertex[T]]] = {start: None}

        visited.add(start)

        while queue:
            current = queue.popleft()

            for neighbor, _ in graph.neighbors(current):
                if neighbor not in visited:
                    visited.add(neighbor)
                    parent[neighbor] = current
                    queue.append(neighbor)

                    if neighbor == end:
                        # Reconstruct path
                        path: List[Vertex[T]] = []
                        vertex: Optional[Vertex[T]] = end
                        while vertex is not None:
                            path.append(vertex)
                            vertex = parent[vertex]
                        return path[::-1]

        return None  # No path found
