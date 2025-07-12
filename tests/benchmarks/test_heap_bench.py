import random
from typing import Any, List

import pytest

from algolib.algorithms.sorting.heap_sort import HeapSort


@pytest.mark.benchmark(
    group="sorting",
)
def test_heap_sort_benchmark(benchmark: Any) -> None:
    """Benchmark the heap sort algorithm."""
    data: List[int] = [random.randint(0, 1000) for _ in range(1000)]
    sorter: HeapSort[int] = HeapSort()

    def f() -> None:
        sorter.sort(data)

    benchmark.pedantic(f, rounds=3, warmup_rounds=1, iterations=1)
