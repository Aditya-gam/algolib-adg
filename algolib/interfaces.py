"""
This module defines the core interfaces for algorithms in the library.
"""

from typing import (
    TYPE_CHECKING,
    Any,
    MutableSequence,
    Protocol,
    Sequence,
    TypeVar,
    runtime_checkable,
)

if TYPE_CHECKING:
    from algolib.data_structures.graph import Graph


T_contra = TypeVar("T_contra", contravariant=True)
T = TypeVar("T")
T_vertex = TypeVar("T_vertex")

__all__ = ["Searcher", "Sorter", "GraphAlgo"]


@runtime_checkable
class Searcher(Protocol[T_contra]):
    """A protocol for searching algorithms."""

    def search(self, seq: Sequence[T_contra], target: T_contra) -> int | None: ...


@runtime_checkable
class Sorter(Protocol[T]):
    """A protocol for sorting algorithms."""

    def sort(self, seq: MutableSequence[T]) -> MutableSequence[T]: ...


@runtime_checkable
class GraphAlgo(Protocol[T_vertex]):
    """A protocol for graph algorithms."""

    def run(self, graph: "Graph[T_vertex]", *args: Any, **kwds: Any) -> Any: ...
