from typing import List, Optional

import pytest
from hypothesis import given
from hypothesis import strategies as st

from algolib.data_structures.linked_list import LinkedList


@given(st.lists(st.integers()))
def test_linked_list_property_preserves_list(items: list[int]) -> None:
    ll = LinkedList[int]()
    for item in items:
        ll.append(item)

    assert list(ll) == items


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
    assert str(ll) == "[]"
    ll.append(1)
    ll.append(2)
    assert str(ll) == "[1, 2]"


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
    # The str representation shows the actual object repr, not the custom str
    assert str(ll) == str([obj2, obj1])


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
    assert str(ll) == "[1]"


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


# Tests for insert_at method


def test_insert_at_beginning() -> None:
    """Test inserting at the beginning of the list."""
    ll = LinkedList[int]()
    ll.append(2)
    ll.append(3)
    ll.insert_at(0, 1)
    assert list(ll) == [1, 2, 3]


def test_insert_at_end() -> None:
    """Test inserting at the end of the list."""
    ll = LinkedList[int]()
    ll.append(1)
    ll.append(2)
    ll.insert_at(2, 3)
    assert list(ll) == [1, 2, 3]


def test_insert_at_middle() -> None:
    """Test inserting in the middle of the list."""
    ll = LinkedList[int]()
    ll.append(1)
    ll.append(3)
    ll.insert_at(1, 2)
    assert list(ll) == [1, 2, 3]


def test_insert_at_empty_list() -> None:
    """Test inserting into an empty list."""
    ll = LinkedList[int]()
    ll.insert_at(0, 1)
    assert list(ll) == [1]


def test_insert_at_multiple_positions() -> None:
    """Test inserting at multiple positions."""
    ll = LinkedList[int]()
    ll.insert_at(0, 1)  # [1]
    ll.insert_at(1, 3)  # [1, 3]
    ll.insert_at(1, 2)  # [1, 2, 3]
    ll.insert_at(3, 5)  # [1, 2, 3, 5]
    ll.insert_at(3, 4)  # [1, 2, 3, 4, 5]
    assert list(ll) == [1, 2, 3, 4, 5]


def test_insert_at_invalid_index_negative() -> None:
    """Test inserting at negative index raises error."""
    ll = LinkedList[int]()
    ll.append(1)
    with pytest.raises(IndexError, match="Index -1 out of bounds"):
        ll.insert_at(-1, 0)


def test_insert_at_invalid_index_too_large() -> None:
    """Test inserting at index beyond list size raises error."""
    ll = LinkedList[int]()
    ll.append(1)
    with pytest.raises(IndexError, match="Index 2 out of bounds"):
        ll.insert_at(2, 3)


def test_insert_at_size_boundary() -> None:
    """Test inserting at the boundary of list size."""
    ll = LinkedList[int]()
    ll.append(1)
    ll.append(2)
    ll.insert_at(2, 3)  # Should work
    assert list(ll) == [1, 2, 3]


# Tests for remove method
def test_remove_first_element() -> None:
    """Test removing the first element."""
    ll = LinkedList[int]()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    assert ll.remove(1) is True
    assert list(ll) == [2, 3]


def test_remove_middle_element() -> None:
    """Test removing an element from the middle."""
    ll = LinkedList[int]()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    assert ll.remove(2) is True
    assert list(ll) == [1, 3]


def test_remove_last_element() -> None:
    """Test removing the last element."""
    ll = LinkedList[int]()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    assert ll.remove(3) is True
    assert list(ll) == [1, 2]


def test_remove_nonexistent_element() -> None:
    """Test removing an element that doesn't exist."""
    ll = LinkedList[int]()
    ll.append(1)
    ll.append(2)
    assert ll.remove(3) is False
    assert list(ll) == [1, 2]


def test_remove_from_empty_list() -> None:
    """Test removing from an empty list."""
    ll = LinkedList[int]()
    assert ll.remove(1) is False


def test_remove_single_element() -> None:
    """Test removing the only element in the list."""
    ll = LinkedList[int]()
    ll.append(1)
    assert ll.remove(1) is True
    assert list(ll) == []
    assert ll.is_empty()


def test_remove_duplicate_elements() -> None:
    """Test removing only the first occurrence of a duplicate element."""
    ll = LinkedList[int]()
    ll.append(1)
    ll.append(2)
    ll.append(1)
    ll.append(3)
    assert ll.remove(1) is True
    assert list(ll) == [2, 1, 3]


def test_remove_all_elements() -> None:
    """Test removing all elements one by one."""
    ll = LinkedList[int]()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    assert ll.remove(1) is True
    assert ll.remove(2) is True
    assert ll.remove(3) is True
    assert list(ll) == []
    assert ll.is_empty()


# Tests for search method
def test_search_first_element() -> None:
    """Test searching for the first element."""
    ll = LinkedList[int]()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    assert ll.search(1) == 0


def test_search_middle_element() -> None:
    """Test searching for an element in the middle."""
    ll = LinkedList[int]()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    assert ll.search(2) == 1


def test_search_last_element() -> None:
    """Test searching for the last element."""
    ll = LinkedList[int]()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    assert ll.search(3) == 2


def test_search_nonexistent_element() -> None:
    """Test searching for an element that doesn't exist."""
    ll = LinkedList[int]()
    ll.append(1)
    ll.append(2)
    assert ll.search(3) is None


def test_search_empty_list() -> None:
    """Test searching in an empty list."""
    ll = LinkedList[int]()
    assert ll.search(1) is None


def test_search_duplicate_elements() -> None:
    """Test searching returns the first occurrence."""
    ll = LinkedList[int]()
    ll.append(1)
    ll.append(2)
    ll.append(1)
    ll.append(3)
    assert ll.search(1) == 0  # First occurrence


def test_search_single_element() -> None:
    """Test searching in a list with one element."""
    ll = LinkedList[int]()
    ll.append(1)
    assert ll.search(1) == 0
    assert ll.search(2) is None


# Tests for size method
def test_size_empty_list() -> None:
    """Test size of empty list."""
    ll = LinkedList[int]()
    assert ll.size() == 0


def test_size_single_element() -> None:
    """Test size of list with one element."""
    ll = LinkedList[int]()
    ll.append(1)
    assert ll.size() == 1


def test_size_multiple_elements() -> None:
    """Test size of list with multiple elements."""
    ll = LinkedList[int]()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    assert ll.size() == 3


def test_size_after_operations() -> None:
    """Test size changes after various operations."""
    ll = LinkedList[int]()
    assert ll.size() == 0

    ll.append(1)
    assert ll.size() == 1

    ll.prepend(2)
    assert ll.size() == 2

    ll.insert_at(1, 3)
    assert ll.size() == 3

    ll.remove(2)
    assert ll.size() == 2

    ll.remove(1)
    assert ll.size() == 1

    ll.remove(3)
    assert ll.size() == 0


def test_size_consistency_with_len() -> None:
    """Test that size() and len() return the same value."""
    ll = LinkedList[int]()
    assert ll.size() == len(ll)

    ll.append(1)
    assert ll.size() == len(ll)

    ll.append(2)
    assert ll.size() == len(ll)


# Tests for __repr__ method
def test_repr() -> None:
    """Test string representation."""
    ll = LinkedList[int]()
    assert repr(ll) == "LinkedList()"


def test_repr_consistency() -> None:
    """Test that repr is consistent."""
    ll = LinkedList[int]()
    repr1 = repr(ll)
    repr2 = repr(ll)
    assert repr1 == repr2


def test_repr_after_operations() -> None:
    """Test that repr doesn't change after operations."""
    ll = LinkedList[int]()
    repr_before = repr(ll)

    ll.append(1)
    ll.append(2)
    ll.remove(1)

    repr_after = repr(ll)
    assert repr_before == repr_after


# Tests for edge cases and error conditions
def test_insert_at_zero_empty_list() -> None:
    """Test inserting at index 0 in empty list."""
    ll = LinkedList[int]()
    ll.insert_at(0, 1)
    assert list(ll) == [1]
    assert ll.size() == 1


def test_remove_head_tail_consistency() -> None:
    """Test that head and tail are properly updated when removing elements."""
    ll = LinkedList[int]()
    ll.append(1)
    ll.append(2)
    ll.append(3)

    # Remove head
    ll.remove(1)
    assert list(ll) == [2, 3]

    # Remove tail
    ll.remove(3)
    assert list(ll) == [2]

    # Remove last element
    ll.remove(2)
    assert list(ll) == []
    assert ll.is_empty()


def test_multiple_operations_consistency() -> None:
    """Test consistency of multiple operations."""
    ll = LinkedList[int]()

    # Build list: [1, 2, 3, 4, 5]
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    assert list(ll) == [1, 2, 3, 4, 5]
    assert ll.size() == 5

    # Remove middle element
    ll.remove(3)
    assert list(ll) == [1, 2, 4, 5]
    assert ll.size() == 4

    # Insert at middle
    ll.insert_at(2, 3)
    assert list(ll) == [1, 2, 3, 4, 5]
    assert ll.size() == 5

    # Remove first and last
    ll.remove(1)
    ll.remove(5)
    assert list(ll) == [2, 3, 4]
    assert ll.size() == 3


def test_search_with_none_values() -> None:
    """Test searching with None values."""
    ll = LinkedList[Optional[int]]()
    ll.append(1)
    ll.append(None)
    ll.append(3)

    assert ll.search(1) == 0
    assert ll.search(None) == 1
    assert ll.search(3) == 2
    assert ll.search(2) is None


def test_remove_with_none_values() -> None:
    """Test removing None values."""
    ll = LinkedList[Optional[int]]()
    ll.append(1)
    ll.append(None)
    ll.append(3)

    assert ll.remove(None) is True
    assert list(ll) == [1, 3]
    assert ll.size() == 2


def test_insert_at_with_none_values() -> None:
    """Test inserting None values."""
    ll = LinkedList[Optional[int]]()
    ll.append(1)
    ll.append(3)
    ll.insert_at(1, None)
    assert list(ll) == [1, None, 3]
    assert ll.size() == 3
