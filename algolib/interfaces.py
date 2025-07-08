from typing import Any, MutableSequence, Protocol, Sequence, TypeVar

T = TypeVar("T")


class Algorithm(Protocol):
    """A protocol for a generic algorithm."""

    def run(self, data: Any) -> Any: ...


class Sorter(Algorithm, Protocol):
    """A protocol for sorting algorithms."""

    def sort(self, data: MutableSequence[T]) -> MutableSequence[T]: ...


class Searcher(Algorithm, Protocol):
    """A protocol for searching algorithms."""

    def search(self, data: Sequence[T], target: T) -> int | None: ...


class GraphSolver(Algorithm, Protocol):
    """A protocol for graph algorithms."""

    ...
