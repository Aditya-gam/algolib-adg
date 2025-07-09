from dataclasses import dataclass
from typing import Dict, Generic, Iterable, Optional

from algolib._typing import T


@dataclass(slots=True, init=False)
class DisjointSet(Generic[T]):
    """A disjoint set data structure with path compression and union-by-rank."""

    _parent: Dict[T, T]
    _rank: Dict[T, int]

    def __init__(self, elements: Optional[Iterable[T]] = None) -> None:
        """Initializes the DisjointSet, optionally with an initial set of elements.

        Args:
            elements: An iterable of initial elements to add to the disjoint set.
                      Each element will be in its own set.
        """
        self._parent = {}
        self._rank = {}
        if elements:
            for el in elements:
                self._parent[el] = el
                self._rank[el] = 0

    def find(self, item: T) -> T:
        """Finds the representative of the set containing the item.

        This method uses path compression for optimization.

        Args:
            item: The item to find.

        Returns:
            The representative of the set containing the item.

        Raises:
            KeyError: If the item is not in the disjoint set.
        """
        if item not in self._parent:
            raise KeyError(f"Item {item} not in DisjointSet")
        if self._parent[item] == item:
            return item
        # Path compression
        self._parent[item] = self.find(self._parent[item])
        return self._parent[item]

    def union(self, item1: T, item2: T) -> None:
        """Merges the sets containing item1 and item2.

        This method uses union by rank (or size) for optimization.

        Args:
            item1: An item in the first set.
            item2: An item in the second set.
        """
        root1 = self.find(item1)
        root2 = self.find(item2)

        if root1 != root2:
            # Union by rank
            if self._rank[root1] > self._rank[root2]:
                self._parent[root2] = root1
            elif self._rank[root1] < self._rank[root2]:
                self._parent[root1] = root2
            else:
                self._parent[root2] = root1
                self._rank[root1] += 1
