from typing import Optional

import pytest

from algolib.data_structures.queue import Queue


def test_queue_enqueue_and_peek() -> None:
    queue = Queue[int]()
    queue.enqueue(10)
    assert queue.peek() == 10
    queue.enqueue(20)
    assert queue.peek() == 10


def test_queue_dequeue() -> None:
    queue = Queue[int]()
    queue.enqueue(1)
    queue.enqueue(2)
    assert queue.dequeue() == 1
    assert queue.dequeue() == 2


def test_queue_is_empty() -> None:
    queue = Queue[int]()
    assert queue.is_empty() is True
    queue.enqueue(1)
    assert queue.is_empty() is False
    queue.dequeue()
    assert queue.is_empty() is True


def test_queue_dequeue_on_empty() -> None:
    queue = Queue[int]()
    with pytest.raises(IndexError):
        queue.dequeue()


def test_queue_peek_on_empty() -> None:
    queue = Queue[int]()
    with pytest.raises(IndexError):
        queue.peek()


def test_queue_with_different_types() -> None:
    queue = Queue[str]()
    queue.enqueue("hello")
    queue.enqueue("world")
    assert queue.dequeue() == "hello"
    assert queue.peek() == "world"


def test_queue_len() -> None:
    queue = Queue[int]()
    assert len(queue) == 0
    queue.enqueue(1)
    assert len(queue) == 1
    queue.dequeue()
    assert len(queue) == 0


def test_queue_repr() -> None:
    queue = Queue[int]()
    assert repr(queue) == "Queue([])"
    queue.enqueue(1)
    queue.enqueue(2)
    assert repr(queue) == "Queue([1, 2])"


def test_queue_enqueue_dequeue_interleaved() -> None:
    queue = Queue[int]()
    queue.enqueue(1)
    queue.enqueue(2)
    assert queue.dequeue() == 1
    queue.enqueue(3)
    assert queue.peek() == 2
    assert queue.dequeue() == 2
    assert queue.dequeue() == 3


def test_queue_peek_after_dequeue() -> None:
    queue = Queue[str]()
    queue.enqueue("a")
    queue.enqueue("b")
    queue.enqueue("c")
    queue.dequeue()
    assert queue.peek() == "b"


def test_queue_emptying_and_refilling() -> None:
    queue = Queue[int]()
    for i in range(5):
        queue.enqueue(i)
    for _ in range(5):
        queue.dequeue()
    assert queue.is_empty()
    queue.enqueue(100)
    assert not queue.is_empty()
    assert queue.peek() == 100


def test_queue_with_none() -> None:
    queue = Queue[Optional[int]]()
    queue.enqueue(1)
    queue.enqueue(None)
    assert queue.dequeue() == 1
    assert queue.dequeue() is None


def test_queue_with_custom_objects() -> None:
    class CustomObject:
        def __init__(self, value: int):
            self.value = value

        def __eq__(self, other: object) -> bool:
            if not isinstance(other, CustomObject):
                return NotImplemented
            return self.value == other.value

    obj1 = CustomObject(1)
    obj2 = CustomObject(2)
    queue = Queue[CustomObject]()
    queue.enqueue(obj1)
    queue.enqueue(obj2)
    assert queue.dequeue() == obj1
    assert queue.peek() == obj2


def test_queue_large_number_of_items() -> None:
    queue = Queue[int]()
    for i in range(1000):
        queue.enqueue(i)
    assert len(queue) == 1000
    for i in range(1000):
        assert queue.dequeue() == i
    assert queue.is_empty()


def test_queue_dequeue_to_empty_and_peek() -> None:
    queue = Queue[int]()
    queue.enqueue(1)
    queue.dequeue()
    assert queue.is_empty()
    with pytest.raises(IndexError):
        queue.peek()
