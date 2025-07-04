from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar("T")


class Algorithm(ABC, Generic[T]):
    """Common interface for every algorithm in **algolib**."""

    @abstractmethod
    def run(self, problem: T) -> None:
        """Execute the algorithm and return the result."""
        raise NotImplementedError
