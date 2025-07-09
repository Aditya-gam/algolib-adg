# ruff: noqa: D100,D101,D102,D103,D104,D105,D107
from typing import List, Tuple, Type

import pytest
from hypothesis import given
from hypothesis import strategies as st

from algolib.algorithms.searching.base import Searcher
from algolib.algorithms.searching.binary import BinarySearcher
from algolib.algorithms.searching.linear import LinearSearcher

# A strategy for a sorted list and an element to search for
sorted_list_and_element = st.lists(st.integers(), min_size=1).flatmap(
    lambda lst: st.tuples(
        st.just(sorted(list(set(lst)))), st.one_of(st.sampled_from(lst), st.integers())
    )
)

ALL_SEARCHERS: List[Type[Searcher[int]]] = [LinearSearcher, BinarySearcher]


@pytest.mark.property
@pytest.mark.parametrize("searcher_class", ALL_SEARCHERS)
@given(data_and_target=sorted_list_and_element)
def test_search_properties(
    searcher_class: Type[Searcher[int]], data_and_target: Tuple[List[int], int]
) -> None:
    """
    Tests that search algorithms correctly find an element or return None.
    - If the element is in the list, the searcher should return a valid index.
    - If the element is not in the list, the searcher should return None.
    """
    data, target = data_and_target
    searcher = searcher_class()

    result = searcher.search(data, target)

    if target in data:
        assert result is not None
        assert 0 <= result < len(data)
        assert data[result] == target
    else:
        assert result is None
