import random
from typing import Any, List

import pytest

from algolib.algorithms.sorting.quick_sort import QuickSort


@pytest.mark.benchmark(
    group="sorting",
)
def test_quick_sort_benchmark(benchmark: Any) -> None:
    """Benchmark the quick sort algorithm."""
    # Use a smaller dataset to avoid recursion issues
    data: List[int] = [random.randint(0, 100) for _ in range(100)]
    sorter: QuickSort[int] = QuickSort()

    def f() -> None:
        sorter.sort(data.copy())  # Use copy to avoid modifying original data

    benchmark.pedantic(f, rounds=3, warmup_rounds=1, iterations=1)
