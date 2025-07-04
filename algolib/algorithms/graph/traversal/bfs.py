from collections import deque
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from algolib.data_structures.graph import Graph, Vertex


class BFS:
    def traverse(self, graph: "Graph[Any]", start: "Vertex[Any]") -> list["Vertex[Any]"]:
        visited: set["Vertex[Any]"] = set()
        queue: deque["Vertex[Any]"] = deque()
        result: list["Vertex[Any]"] = []

        queue.append(start)
        visited.add(start)

        while queue:
            current_vertex = queue.popleft()
            result.append(current_vertex)

            for neighbor in graph.get_neighbors(current_vertex):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return result
