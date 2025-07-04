from typing import List, Optional

import pytest

from algolib.data_structures.linked_list import LinkedList


def test_linked_list_append() -> None:
    ll = LinkedList[int]()
    ll.append(1)
    ll.append(2)
    assert list(ll) == [1, 2]


def test_linked_list_prepend() -> None:
    ll = LinkedList[int]()
    ll.prepend(1)
    ll.prepend(2)
    assert list(ll) == [2, 1]


def test_linked_list_len() -> None:
    ll = LinkedList[int]()
    assert len(ll) == 0
    ll.append(1)
    assert len(ll) == 1
    ll.prepend(2)
    assert len(ll) == 2


def test_linked_list_iter() -> None:
    ll = LinkedList[int]()
    items = [10, 20, 30]
    for item in items:
        ll.append(item)

    # Test round-trip
    iterated_items: List[int] = list(ll)
    assert iterated_items == items


def test_linked_list_is_empty() -> None:
    ll = LinkedList[int]()
    assert ll.is_empty()
    ll.append(1)
    assert not ll.is_empty()


def test_linked_list_str() -> None:
    ll = LinkedList[int]()
    assert str(ll) == "LinkedList()"
    ll.append(1)
    ll.append(2)
    assert str(ll) == "LinkedList(1 -> 2)"


def test_linked_list_append_and_prepend() -> None:
    ll = LinkedList[int]()
    ll.append(1)
    ll.prepend(2)
    ll.append(3)
    ll.prepend(4)
    assert list(ll) == [4, 2, 1, 3]


def test_linked_list_empty_list_iteration() -> None:
    ll = LinkedList[int]()
    for _ in ll:
        pytest.fail("Should not iterate over an empty list")


def test_linked_list_with_none() -> None:
    ll = LinkedList[Optional[int]]()
    ll.append(1)
    ll.append(None)
    ll.prepend(2)
    assert list(ll) == [2, 1, None]


def test_linked_list_with_custom_objects() -> None:
    class CustomObject:
        def __init__(self, value: int):
            self.value = value

        def __eq__(self, other: object) -> bool:
            if not isinstance(other, CustomObject):
                return NotImplemented
            return self.value == other.value

        def __str__(self) -> str:
            return f"Obj({self.value})"

    obj1 = CustomObject(1)
    obj2 = CustomObject(2)
    ll = LinkedList[CustomObject]()
    ll.append(obj1)
    ll.prepend(obj2)
    assert list(ll) == [obj2, obj1]
    assert str(ll) == "LinkedList(Obj(2) -> Obj(1))"


def test_linked_list_large_number_of_items_append() -> None:
    ll = LinkedList[int]()
    items = list(range(1000))
    for item in items:
        ll.append(item)
    assert list(ll) == items


def test_linked_list_large_number_of_items_prepend() -> None:
    ll = LinkedList[int]()
    items = list(range(1000))
    for item in items:
        ll.prepend(item)
    assert list(ll) == list(reversed(items))


def test_linked_list_iterator_multiple_times() -> None:
    ll = LinkedList[int]()
    items = [1, 2, 3]
    for item in items:
        ll.append(item)

    assert list(ll) == items
    # Iterate a second time
    assert list(ll) == items


def test_linked_list_str_single_item() -> None:
    ll = LinkedList[int]()
    ll.append(1)
    assert str(ll) == "LinkedList(1)"


def test_emptying_and_refilling() -> None:
    ll = LinkedList[int]()
    for i in range(5):
        ll.append(i)

    # Not a public method, but we can re-initialize
    ll = LinkedList[int]()
    assert ll.is_empty()
    assert len(ll) == 0

    ll.append(100)
    assert list(ll) == [100]
    assert len(ll) == 1
