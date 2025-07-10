"""Depth-First Search algorithm for graph traversal.

DFS explores as far as possible along each branch before backtracking, using
either recursion or an explicit stack.
"""

from dataclasses import dataclass
from typing import List, Set

from algolib._typing import T
from algolib.data_structures.graph import Graph, Vertex
from algolib.interfaces import GraphAlgo


@dataclass(slots=True, init=False)
class DepthFirstSearch(GraphAlgo[T]):
    """Depth-First Search algorithm for graph traversal."""

    def traverse(self, graph: Graph[T], start_vertex: Vertex[T]) -> List[Vertex[T]]:
        """Traverse the graph using DFS (alias for run method)."""
        return self.run(graph, start_vertex)

    def run(self, graph: Graph[T], start: Vertex[T]) -> List[Vertex[T]]:
        """Run DFS traversal starting from a vertex."""
        if start not in graph:
            raise ValueError("Start vertex not in graph")

        visited: Set[Vertex[T]] = set()
        result: List[Vertex[T]] = []

        self._dfs_recursive(graph, start, visited, result)
        return result

    def _dfs_recursive(
        self,
        graph: Graph[T],
        vertex: Vertex[T],
        visited: Set[Vertex[T]],
        result: List[Vertex[T]],
    ) -> None:
        visited.add(vertex)
        result.append(vertex)

        for neighbor, _ in graph.neighbors(vertex):
            if neighbor not in visited:
                self._dfs_recursive(graph, neighbor, visited, result)

    def run_iterative(self, graph: Graph[T], start: Vertex[T]) -> List[Vertex[T]]:
        """Run DFS traversal using an explicit stack."""
        if start not in graph:
            raise ValueError("Start vertex not in graph")

        visited: Set[Vertex[T]] = set()
        stack: List[Vertex[T]] = [start]
        result: List[Vertex[T]] = []

        while stack:
            current = stack.pop()

            if current not in visited:
                visited.add(current)
                result.append(current)

                # Add neighbors to stack in reverse order for consistent traversal
                neighbors = list(graph.neighbors(current))
                for neighbor, _ in reversed(neighbors):
                    if neighbor not in visited:
                        stack.append(neighbor)

        return result
