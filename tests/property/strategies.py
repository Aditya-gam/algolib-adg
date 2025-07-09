# ruff: noqa: D100,D101,D102,D103,D104,D105,D107
from typing import List, Tuple

from hypothesis import strategies as st
from hypothesis.strategies import SearchStrategy

from algolib.data_structures.disjoint_set import DisjointSet
from algolib.data_structures.graph import Graph

# Basic Strategies
random_int_list: SearchStrategy[List[int]] = st.lists(st.integers())


@st.composite
def small_graph(draw: st.DrawFn) -> Graph[int]:
    """Generates a small, undirected graph with integer vertices."""
    graph = Graph[int](directed=False)
    # Generate up to 10 vertices
    vertices = draw(
        st.lists(st.integers(min_value=0, max_value=9), min_size=0, max_size=10, unique=True)
    )
    for v_key in vertices:
        graph.add_vertex(v_key)

    if not vertices:
        return graph

    # Generate edges between existing vertices
    edge_tuples = draw(
        st.lists(
            st.tuples(st.sampled_from(vertices), st.sampled_from(vertices)).filter(
                lambda e: e[0] != e[1]
            ),
            max_size=20,
        )
    )

    for u_key, v_key in edge_tuples:
        u = graph.get_vertex(u_key)
        v = graph.get_vertex(v_key)
        if u and v:
            # Avoid adding parallel edges for simplicity in this strategy
            # A more complex strategy could handle this, but it's not needed for now
            is_neighbor = any(neighbor == v for neighbor, _ in graph.neighbors(u))
            if not is_neighbor:
                graph.add_edge(u, v)

    return graph


@st.composite
def union_find_sequences(draw: st.DrawFn) -> Tuple[DisjointSet[int], List[Tuple[str, int, int]]]:
    """Generates a sequence of union/find operations for a DisjointSet."""
    # Generate a set of elements (0 to 19)
    elements = list(range(draw(st.integers(min_value=1, max_value=20))))
    ds = DisjointSet[int](elements)

    # Generate a sequence of operations
    operations: List[Tuple[str, int, int]] = []
    if not elements:
        return ds, operations

    for _ in range(draw(st.integers(min_value=0, max_value=50))):
        op_type = draw(st.sampled_from(["union", "find"]))
        if op_type == "union":
            u = draw(st.sampled_from(elements))
            v = draw(st.sampled_from(elements))
            operations.append(("union", u, v))
            ds.union(u, v)
        else:  # find
            u = draw(st.sampled_from(elements))
            # The 'v' is just a placeholder for the find operation tuple
            operations.append(("find", u, -1))

    return ds, operations
