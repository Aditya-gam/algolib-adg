from typing import Optional

import pytest
from hypothesis import given
from hypothesis import strategies as st

from algolib.data_structures.stack import Stack


@given(st.lists(st.integers()))
def test_stack_property_reversal(initial_list: list[int]) -> None:
    stack = Stack[int]()
    for item in initial_list:
        stack.push(item)

    popped_list = []
    while not stack.is_empty():
        popped_list.append(stack.pop())

    assert popped_list == initial_list[::-1]


def test_stack_push_and_peek() -> None:
    stack = Stack[int]()
    stack.push(10)
    assert stack.peek() == 10
    stack.push(20)
    assert stack.peek() == 20


def test_stack_pop() -> None:
    stack = Stack[int]()
    stack.push(1)
    stack.push(2)
    assert stack.pop() == 2
    assert stack.pop() == 1


def test_stack_is_empty() -> None:
    stack = Stack[int]()
    assert stack.is_empty() is True
    stack.push(1)
    assert stack.is_empty() is False
    stack.pop()
    assert stack.is_empty() is True


def test_stack_pop_on_empty() -> None:
    stack = Stack[int]()
    with pytest.raises(IndexError):
        stack.pop()


def test_stack_peek_on_empty() -> None:
    stack = Stack[int]()
    with pytest.raises(IndexError):
        stack.peek()


def test_stack_with_different_types() -> None:
    stack = Stack[str]()
    stack.push("hello")
    stack.push("world")
    assert stack.pop() == "world"
    assert stack.peek() == "hello"


def test_stack_len() -> None:
    stack = Stack[int]()
    assert len(stack) == 0
    stack.push(1)
    assert len(stack) == 1
    stack.pop()
    assert len(stack) == 0


def test_stack_repr() -> None:
    stack = Stack[int]()
    assert repr(stack) == "Stack([])"
    stack.push(1)
    stack.push(2)
    assert repr(stack) == "Stack([1, 2])"


def test_stack_push_pop_interleaved() -> None:
    stack = Stack[int]()
    stack.push(1)
    stack.push(2)
    assert stack.pop() == 2
    stack.push(3)
    assert stack.pop() == 3
    assert stack.peek() == 1


def test_stack_peek_after_pop() -> None:
    stack = Stack[str]()
    stack.push("a")
    stack.push("b")
    stack.pop()
    assert stack.peek() == "a"


def test_stack_emptying_and_refilling() -> None:
    stack = Stack[int]()
    for i in range(5):
        stack.push(i)
    for _ in range(5):
        stack.pop()
    assert stack.is_empty()
    stack.push(100)
    assert not stack.is_empty()
    assert stack.peek() == 100


def test_stack_with_none() -> None:
    stack = Stack[Optional[int]]()
    stack.push(1)
    stack.push(None)
    assert stack.pop() is None
    assert stack.pop() == 1


def test_stack_with_custom_objects() -> None:
    class CustomObject:
        def __init__(self, value: int):
            self.value = value

        def __eq__(self, other: object) -> bool:
            if not isinstance(other, CustomObject):
                return NotImplemented
            return self.value == other.value

    obj1 = CustomObject(1)
    obj2 = CustomObject(2)
    stack = Stack[CustomObject]()
    stack.push(obj1)
    stack.push(obj2)
    assert stack.pop() == obj2
    assert stack.peek() == obj1


def test_stack_large_number_of_items() -> None:
    stack = Stack[int]()
    for i in range(1000):
        stack.push(i)
    assert len(stack) == 1000
    for i in range(999, -1, -1):
        assert stack.pop() == i
    assert stack.is_empty()


def test_stack_pop_to_empty_and_peek() -> None:
    stack = Stack[int]()
    stack.push(1)
    stack.pop()
    assert stack.is_empty()
    with pytest.raises(IndexError):
        stack.peek()
