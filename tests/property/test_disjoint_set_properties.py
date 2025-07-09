# ruff: noqa: D100,D101,D102,D103,D104,D105,D107
from typing import List, Tuple

import pytest
from hypothesis import given

from algolib.data_structures.disjoint_set import DisjointSet
from tests.property.strategies import union_find_sequences


@pytest.mark.property
@given(ds_and_ops=union_find_sequences())
def test_disjoint_set_properties(
    ds_and_ops: Tuple[DisjointSet[int], List[Tuple[str, int, int]]],
) -> None:
    """
    Tests properties of the DisjointSet data structure:
    1. After a union(u, v), find(u) should equal find(v).
    2. The find operation is idempotent: find(u) == find(find(u)).
    """
    ds, operations = ds_and_ops

    # Re-run operations to verify properties against the final state
    for op_type, u, v in operations:
        if op_type == "union":
            # After a union, the roots of the two elements must be the same.
            assert ds.find(u) == ds.find(v)

        # Test idempotency for every element involved in an operation
        assert ds.find(u) == ds.find(ds.find(u))
        if v != -1:  # v is used in union
            assert ds.find(v) == ds.find(ds.find(v))
