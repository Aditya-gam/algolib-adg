"""Tests for core interfaces."""

from typing import Any, List, Optional

from algolib.interfaces import GraphAlgo, Searcher, Sorter


class MockSearcher:
    """Mock implementation of Searcher protocol."""

    def search(self, seq: List[Any], target: Any) -> Optional[int]:
        """Mock search implementation."""
        try:
            return seq.index(target)
        except ValueError:
            return None


class MockSorter:
    """Mock implementation of Sorter protocol."""

    def sort(self, seq: List[Any]) -> List[Any]:
        """Mock sort implementation."""
        seq.sort()
        return seq


class MockGraph:
    """Mock graph for testing GraphAlgo protocol."""

    def __init__(self) -> None:
        self.vertices: List[Any] = []
        self.edges: List[Any] = []


class MockGraphAlgo:
    """Mock implementation of GraphAlgo protocol."""

    def run(self, graph: MockGraph, *args: Any, **kwargs: Any) -> int:
        """Mock graph algorithm implementation."""
        return len(graph.vertices)


class TestInterfaces:
    """Test the core interfaces."""

    def test_searcher_protocol(self) -> None:
        """Test Searcher protocol implementation."""
        searcher = MockSearcher()
        assert isinstance(searcher, Searcher)

        # Test search functionality
        data = [1, 2, 3, 4, 5]
        assert searcher.search(data, 3) == 2
        assert searcher.search(data, 6) is None

    def test_sorter_protocol(self) -> None:
        """Test Sorter protocol implementation."""
        sorter = MockSorter()
        assert isinstance(sorter, Sorter)

        # Test sort functionality
        data = [3, 1, 4, 1, 5]
        result = sorter.sort(data)
        assert result == [1, 1, 3, 4, 5]
        assert data == [1, 1, 3, 4, 5]  # Should be modified in place

    def test_graph_algo_protocol(self) -> None:
        """Test GraphAlgo protocol implementation."""
        algo = MockGraphAlgo()
        assert isinstance(algo, GraphAlgo)

        # Test run functionality
        graph = MockGraph()
        graph.vertices = [1, 2, 3]
        result = algo.run(graph)
        assert result == 3

    def test_graph_algo_with_args_and_kwargs(self) -> None:
        """Test GraphAlgo protocol with additional arguments."""
        algo = MockGraphAlgo()
        graph = MockGraph()
        graph.vertices = [1, 2, 3]

        # Test with positional and keyword arguments
        result = algo.run(graph, "arg1", "arg2", kwarg1="value1", kwarg2="value2")
        assert result == 3

    def test_graph_algo_with_empty_graph(self) -> None:
        """Test GraphAlgo protocol with empty graph."""
        algo = MockGraphAlgo()
        graph = MockGraph()
        graph.vertices = []

        result = algo.run(graph)
        assert result == 0

    def test_graph_algo_with_single_vertex(self) -> None:
        """Test GraphAlgo protocol with single vertex."""
        algo = MockGraphAlgo()
        graph = MockGraph()
        graph.vertices = [42]

        result = algo.run(graph)
        assert result == 1
