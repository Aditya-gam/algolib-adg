from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar("T")


class BaseAlgorithm(ABC, Generic[T]):
    """Common interface for every algorithm in **algolib**."""

    @abstractmethod
    def run(self, data: T) -> T:  # pragma: no cover
        """Execute the algorithm and return the result."""
        raise NotImplementedError
