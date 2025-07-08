"""The algolib package."""

from .algorithms.graph.traversal.bfs import BFS
from .algorithms.searching.binary import BinarySearcher
from .algorithms.searching.linear import LinearSearcher
from .algorithms.sorting.bubble import BubbleSorter
from .algorithms.sorting.merge import MergeSorter
from .data_structures.disjoint_set import DisjointSet
from .data_structures.graph import Graph
from .data_structures.linked_list import LinkedList
from .data_structures.queue import Queue
from .data_structures.stack import Stack
from .interfaces import Algorithm, GraphSolver, Searcher, Sorter

__all__ = [
    "Algorithm",
    "BFS",
    "BinarySearcher",
    "BubbleSorter",
    "DisjointSet",
    "Graph",
    "GraphSolver",
    "LinkedList",
    "LinearSearcher",
    "MergeSorter",
    "Queue",
    "Searcher",
    "Sorter",
    "Stack",
]
