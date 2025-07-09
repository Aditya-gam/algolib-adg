from dataclasses import dataclass
from typing import Dict, Generic, Iterator, List, Optional, Tuple, cast

from algolib._typing import T


@dataclass(slots=True, frozen=True)
class Vertex(Generic[T]):
    """A vertex in a graph."""

    key: T

    def __hash__(self) -> int:
        """Computes the hash of the vertex key."""
        return hash(self.key)

    def __eq__(self, other: object) -> bool:
        """Checks if two vertices are equal."""
        if not isinstance(other, Vertex):
            return NotImplemented
        return cast(bool, self.key == other.key)

    def __repr__(self) -> str:
        """Returns a string representation of the vertex."""
        return f"Vertex({self.key})"


@dataclass(slots=True, init=False)
class Graph(Generic[T]):
    """A graph represented using an adjacency list.

    Attributes:
        directed: Whether the graph is directed.
    """

    _adj: Dict[Vertex[T], List[Tuple[Vertex[T], float]]]
    _vertices: Dict[T, Vertex[T]]
    directed: bool

    def __init__(self, directed: bool = False) -> None:
        """Initializes a new Graph.

        Args:
            directed: If True, the graph is directed. Defaults to False.
        """
        self._adj = {}
        self._vertices = {}
        self.directed = directed

    def add_vertex(self, key: T) -> Vertex[T]:
        """Adds a vertex to the graph or returns it if it already exists.

        Args:
            key: The key of the vertex to add.

        Returns:
            The Vertex object.
        """
        if key in self._vertices:
            return self._vertices[key]
        vertex = Vertex(key)
        self._vertices[key] = vertex
        self._adj[vertex] = []
        return vertex

    def get_vertex(self, key: T) -> Optional[Vertex[T]]:
        """Gets a vertex by its key.

        Args:
            key: The key of the vertex to get.

        Returns:
            The Vertex object if found, otherwise None.
        """
        return self._vertices.get(key)

    def add_edge(self, u: Vertex[T], v: Vertex[T], weight: float = 1.0) -> None:
        """Adds an edge between two vertices.

        Args:
            u: The source vertex.
            v: The destination vertex.
            weight: The weight of the edge. Defaults to 1.0.

        Raises:
            ValueError: If either vertex is not in the graph.
        """
        if u not in self._adj or v not in self._adj:
            raise ValueError("Both vertices must be in the graph")
        self._adj[u].append((v, weight))
        if not self.directed:
            self._adj[v].append((u, weight))

    def neighbors(self, v: Vertex[T]) -> Iterator[Tuple[Vertex[T], float]]:
        """Returns an iterator over the neighbors of a vertex and edge weights.

        Args:
            v: The vertex whose neighbors to get.

        Yields:
            A tuple containing the neighbor vertex and the edge weight.

        Raises:
            ValueError: If the vertex is not in the graph.
        """
        if v not in self._adj:
            raise ValueError("Vertex not in graph")
        return iter(self._adj[v])

    def __contains__(self, item: object) -> bool:
        """Checks if a vertex or key is in the graph.

        Args:
            item: The vertex or key to check.

        Returns:
            True if the item is in the graph, otherwise False.
        """
        if isinstance(item, Vertex):
            return item in self._adj
        return item in self._vertices

    def __len__(self) -> int:
        """Returns the number of vertices in the graph."""
        return len(self._vertices)

    def get_neighbors(self, v: Vertex[T]) -> List[Vertex[T]]:
        """Gets all neighbor vertices of a given vertex.

        Args:
            v: The vertex whose neighbors to retrieve.

        Returns:
            A list of neighbor vertices.
        """
        return [neighbor for neighbor, _ in self.neighbors(v)]
