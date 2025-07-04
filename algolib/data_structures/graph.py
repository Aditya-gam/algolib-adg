from typing import Dict, Generic, Iterator, List, Optional, Tuple

from algolib._typing import T


class Vertex(Generic[T]):
    """A vertex in a graph."""

    def __init__(self, key: T):
        self.key = key

    def __hash__(self) -> int:
        return hash(self.key)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Vertex):
            return NotImplemented
        return bool(self.key == other.key)

    def __repr__(self) -> str:
        return f"Vertex({self.key})"


class Graph(Generic[T]):
    """A graph represented using an adjacency list."""

    def __init__(self, directed: bool = False):
        self._adj: Dict[Vertex[T], List[Tuple[Vertex[T], float]]] = {}
        self._vertices: Dict[T, Vertex[T]] = {}
        self.directed = directed

    def add_vertex(self, key: T) -> Vertex[T]:
        if key in self._vertices:
            return self._vertices[key]
        vertex = Vertex(key)
        self._vertices[key] = vertex
        self._adj[vertex] = []
        return vertex

    def get_vertex(self, key: T) -> Optional[Vertex[T]]:
        return self._vertices.get(key)

    def add_edge(self, u: Vertex[T], v: Vertex[T], weight: float = 1.0) -> None:
        if u not in self._adj or v not in self._adj:
            raise ValueError("Both vertices must be in the graph")
        self._adj[u].append((v, weight))
        if not self.directed:
            self._adj[v].append((u, weight))

    def neighbors(self, v: Vertex[T]) -> Iterator[Tuple[Vertex[T], float]]:
        if v not in self._adj:
            raise ValueError("Vertex not in graph")
        return iter(self._adj[v])

    def __contains__(self, key: T) -> bool:
        return key in self._vertices

    def __len__(self) -> int:
        return len(self._vertices)
