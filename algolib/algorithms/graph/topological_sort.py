"""Topological Sort algorithm for directed acyclic graphs."""

from dataclasses import dataclass
from typing import List, Set

from algolib._typing import T
from algolib.data_structures.graph import Graph, Vertex
from algolib.interfaces import GraphAlgo


@dataclass(slots=True, init=False)
class TopologicalSort(GraphAlgo[T]):
    """Topological Sort algorithm for DAGs."""

    def sort(self, graph: Graph[T]) -> List[Vertex[T]]:
        """Sort the graph topologically (alias for run method)."""
        return self.run(graph)

    def run(self, graph: Graph[T]) -> List[Vertex[T]]:
        if not graph.directed:
            raise ValueError("Topological sort requires a directed graph")

        visited: Set[Vertex[T]] = set()
        rec_stack: Set[Vertex[T]] = set()
        result: List[Vertex[T]] = []

        # Detect cycles
        for vertex in graph._vertices.values():
            if vertex not in visited:
                if self._has_cycle_dfs(graph, vertex, visited, rec_stack):
                    raise ValueError("Graph contains cycles - topological sort impossible")

        # Reset visited for actual sort
        visited.clear()
        for vertex in graph._vertices.values():
            if vertex not in visited:
                self._topological_dfs(graph, vertex, visited, result)

        return result[::-1]

    def _has_cycle_dfs(
        self,
        graph: Graph[T],
        vertex: Vertex[T],
        visited: Set[Vertex[T]],
        rec_stack: Set[Vertex[T]],
    ) -> bool:
        visited.add(vertex)
        rec_stack.add(vertex)

        for neighbor, _ in graph.neighbors(vertex):
            if neighbor not in visited:
                if self._has_cycle_dfs(graph, neighbor, visited, rec_stack):
                    return True
            elif neighbor in rec_stack:
                return True

        rec_stack.remove(vertex)
        return False

    def _topological_dfs(
        self,
        graph: Graph[T],
        vertex: Vertex[T],
        visited: Set[Vertex[T]],
        result: List[Vertex[T]],
    ) -> None:
        visited.add(vertex)
        for neighbor, _ in graph.neighbors(vertex):
            if neighbor not in visited:
                self._topological_dfs(graph, neighbor, visited, result)
        result.append(vertex)
