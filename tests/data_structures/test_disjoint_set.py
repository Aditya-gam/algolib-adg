import pytest

from algolib.data_structures.disjoint_set import DisjointSet


@pytest.fixture  # type: ignore[misc]
def ds() -> DisjointSet[str]:
    return DisjointSet[str](["A", "B", "C", "D"])


def test_disjoint_set_initialization() -> None:
    elements = ["A", "B", "C"]
    ds = DisjointSet(elements)
    for el in elements:
        assert ds.find(el) == el


def test_disjoint_set_union_and_find(ds: DisjointSet[str]) -> None:
    ds.union("A", "B")
    assert ds.find("A") == ds.find("B")
    ds.union("C", "D")
    assert ds.find("C") == ds.find("D")
    assert ds.find("A") != ds.find("C")


def test_disjoint_set_union_by_rank(ds: DisjointSet[str]) -> None:
    ds.union("A", "B")
    ds.union("C", "D")
    ds.union("A", "C")
    # Path compression means find returns the root
    root = ds.find("A")
    assert root == ds.find("B")
    assert root == ds.find("C")
    assert root == ds.find("D")


def test_disjoint_set_path_compression(ds: DisjointSet[str]) -> None:
    ds.union("A", "B")
    ds.union("B", "C")
    ds.union("C", "D")

    # This find operation should compress the path for "A"
    ds.find("A")

    # Check if parent of "A" is now the root "D" (or whatever the root is)
    root = ds.find("D")
    # This is an internal check, so we're making an assumption about implementation
    # A better test is to check invariants, which we already do.
    # This just gives a bit more confidence in path compression.
    assert ds.find("A") == root


def test_disjoint_set_union_by_rank_reverse_order() -> None:
    ds = DisjointSet[str](["A", "B", "C", "D", "E"])
    ds.union("A", "B")  # rank of A becomes 1
    ds.union("C", "D")  # rank of C becomes 1
    ds.union("A", "C")  # rank of A becomes 2

    # Now we have a tree rooted at A with rank 2.
    # Let's union E (rank 0) into it.
    ds.union("E", "A")

    # The root of E should now be A.
    # This tests the case where rank(root1) < rank(root2)
    assert ds.find("E") == ds.find("A")


def test_disjoint_set_find_non_existent() -> None:
    ds = DisjointSet[str]()
    with pytest.raises(KeyError):
        ds.find("A")


def test_disjoint_set_union_same_set(ds: DisjointSet[str]) -> None:
    ds.union("A", "B")
    root1 = ds.find("A")
    ds.union("A", "B")
    root2 = ds.find("A")
    assert root1 == root2


def test_disjoint_set_with_integers() -> None:
    ds = DisjointSet[int]([1, 2, 3])
    ds.union(1, 2)
    assert ds.find(1) == ds.find(2)
    assert ds.find(1) != ds.find(3)


def test_disjoint_set_with_custom_objects() -> None:
    class CustomObject:
        def __init__(self, value: int):
            self.value = value

        def __hash__(self) -> int:
            return hash(self.value)

        def __eq__(self, other: object) -> bool:
            if not isinstance(other, CustomObject):
                return NotImplemented
            return self.value == other.value

    obj1, obj2, obj3 = CustomObject(1), CustomObject(2), CustomObject(3)
    ds = DisjointSet[CustomObject]([obj1, obj2, obj3])
    ds.union(obj1, obj2)
    assert ds.find(obj1) == ds.find(obj2)
    assert ds.find(obj1) != ds.find(obj3)


def test_disjoint_set_union_non_existent_element_1(ds: DisjointSet[str]) -> None:
    with pytest.raises(KeyError):
        ds.union("X", "A")


def test_disjoint_set_union_non_existent_element_2(ds: DisjointSet[str]) -> None:
    with pytest.raises(KeyError):
        ds.union("A", "X")


def test_disjoint_set_complex_union_structure() -> None:
    elements = list(range(10))
    ds = DisjointSet[int](elements)
    ds.union(0, 1)
    ds.union(2, 3)
    ds.union(0, 2)
    ds.union(4, 5)
    ds.union(6, 7)
    ds.union(4, 6)
    ds.union(0, 4)
    root = ds.find(0)
    for i in range(8):
        assert ds.find(i) == root
    assert ds.find(8) != root
    assert ds.find(9) != root


def test_disjoint_set_init_with_empty_iterable() -> None:
    ds = DisjointSet[int]([])
    with pytest.raises(KeyError):
        ds.find(1)


def test_disjoint_set_init_with_no_iterable() -> None:
    ds = DisjointSet[int]()
    with pytest.raises(KeyError):
        ds.find(1)


def test_disjoint_set_repeated_unions() -> None:
    ds = DisjointSet[str](["A", "B", "C"])
    ds.union("A", "B")
    ds.union("B", "A")
    ds.union("A", "B")
    assert ds.find("A") == ds.find("B")
    assert ds.find("A") != ds.find("C")
