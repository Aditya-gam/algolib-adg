"""The algolib package."""

from . import algorithms, data_structures
from ._typing import T
from .interfaces import GraphAlgo, Searcher, Sorter

__all__ = [
    "T",
    "data_structures",
    "algorithms",
    "Searcher",
    "Sorter",
    "GraphAlgo",
]
