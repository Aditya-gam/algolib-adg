"""Tests for Heap data structure."""

import pytest

from algolib.data_structures.heap import MaxHeap


class TestMaxHeap:
    """Test cases for MaxHeap data structure."""

    @pytest.fixture
    def max_heap(self) -> MaxHeap[int]:
        """Provide MaxHeap instance."""
        return MaxHeap()

    @pytest.fixture
    def populated_max_heap(self) -> MaxHeap[int]:
        """Provide populated MaxHeap instance."""
        heap: MaxHeap[int] = MaxHeap()
        values = [10, 5, 15, 3, 7, 12, 17, 2, 4, 6, 8, 11, 13, 16, 18]
        for value in values:
            heap.insert(value)
        return heap

    def test_insert_single_element(self, max_heap: MaxHeap[int]) -> None:
        """Test inserting single element to max heap."""
        max_heap.insert(5)
        assert max_heap.peek() == 5
        assert max_heap.size() == 1

    def test_insert_multiple_elements(self, max_heap: MaxHeap[int]) -> None:
        """Test inserting multiple elements to max heap."""
        values = [5, 3, 7, 2, 4, 6, 8]
        for value in values:
            max_heap.insert(value)

        assert max_heap.peek() == 8  # Max element should be at top
        assert max_heap.size() == 7

    def test_extract_max(self, max_heap: MaxHeap[int]) -> None:
        """Test extracting from max heap."""
        values = [5, 3, 7, 2, 4, 6, 8]
        for value in values:
            max_heap.insert(value)

        # Extract elements in descending order
        expected_order = [8, 7, 6, 5, 4, 3, 2]
        for expected in expected_order:
            assert max_heap.extract_max() == expected

        assert max_heap.is_empty() is True

    def test_extract_max_empty_heap(self, max_heap: MaxHeap[int]) -> None:
        """Test extracting from empty heap."""
        with pytest.raises(IndexError):
            max_heap.extract_max()

    def test_peek_empty_heap(self, max_heap: MaxHeap[int]) -> None:
        """Test peeking at empty heap."""
        with pytest.raises(IndexError):
            max_heap.peek()

    def test_peek_max_heap(self, max_heap: MaxHeap[int]) -> None:
        """Test peeking at max heap."""
        values = [5, 3, 7, 2, 4, 6, 8]
        for value in values:
            max_heap.insert(value)

        assert max_heap.peek() == 8
        assert max_heap.size() == 7  # Size should not change

    def test_size_empty_heap(self, max_heap: MaxHeap[int]) -> None:
        """Test size of empty heap."""
        assert max_heap.size() == 0

    def test_size_populated_heap(self, populated_max_heap: MaxHeap[int]) -> None:
        """Test size of populated heap."""
        assert populated_max_heap.size() == 15

    def test_is_empty_empty_heap(self, max_heap: MaxHeap[int]) -> None:
        """Test is_empty on empty heap."""
        assert max_heap.is_empty() is True

    def test_is_empty_populated_heap(self, populated_max_heap: MaxHeap[int]) -> None:
        """Test is_empty on populated heap."""
        assert populated_max_heap.is_empty() is False

    def test_heap_property_max_heap(self, max_heap: MaxHeap[int]) -> None:
        """Test that max heap maintains heap property."""
        values = [10, 5, 15, 3, 7, 12, 17, 2, 4, 6, 8, 11, 13, 16, 18]
        for value in values:
            max_heap.insert(value)

        # Check heap property: parent >= children
        def check_heap_property(index: int) -> bool:
            if index >= max_heap.size():
                return True

            left_child = 2 * index + 1
            right_child = 2 * index + 2

            if left_child < max_heap.size() and max_heap._heap[index] < max_heap._heap[left_child]:
                return False

            if (
                right_child < max_heap.size()
                and max_heap._heap[index] < max_heap._heap[right_child]
            ):
                return False

            return check_heap_property(left_child) and check_heap_property(right_child)

        assert check_heap_property(0)

    def test_build_heap(self) -> None:
        """Test build_heap operation for max heap."""
        values = [10, 5, 15, 3, 7, 12, 17, 2, 4, 6, 8, 11, 13, 16, 18]
        heap: MaxHeap[int] = MaxHeap()
        heap.build_heap(values)

        assert heap.peek() == 18
        assert heap.size() == 15

    def test_build_heap_empty_list(self) -> None:
        """Test build_heap with empty list."""
        heap: MaxHeap[int] = MaxHeap()
        heap.build_heap([])

        assert heap.is_empty() is True
        assert heap.size() == 0

    def test_complex_operations_sequence(self, max_heap: MaxHeap[int]) -> None:
        """Test complex sequence of operations on max heap."""
        # Insert elements
        values = [50, 30, 70, 20, 40, 60, 80]
        for value in values:
            max_heap.insert(value)

        assert max_heap.size() == 7
        assert max_heap.peek() == 80

        # Extract elements
        assert max_heap.extract_max() == 80
        assert max_heap.extract_max() == 70
        assert max_heap.extract_max() == 60
        assert max_heap.size() == 4

        # Insert more elements
        max_heap.insert(90)
        max_heap.insert(25)
        assert max_heap.peek() == 90
        assert max_heap.size() == 6

    def test_duplicate_elements(self, max_heap: MaxHeap[int]) -> None:
        """Test handling of duplicate elements in max heap."""
        values = [5, 3, 7, 5, 3, 7]  # Duplicates
        for value in values:
            max_heap.insert(value)

        assert max_heap.size() == 6
        assert max_heap.extract_max() == 7
        assert max_heap.extract_max() == 7
        assert max_heap.extract_max() == 5
        assert max_heap.extract_max() == 5
        assert max_heap.extract_max() == 3
        assert max_heap.extract_max() == 3

    def test_string_values(self) -> None:
        """Test max heap with string values."""
        heap: MaxHeap[str] = MaxHeap[str]()
        values = ["banana", "apple", "cherry", "date"]
        for value in values:
            heap.insert(value)

        assert heap.peek() == "date"
        assert heap.extract_max() == "date"
        assert heap.extract_max() == "cherry"

    def test_float_values(self) -> None:
        """Test max heap with float values."""
        heap: MaxHeap[float] = MaxHeap[float]()
        values = [3.14, 2.71, 1.41, 0.58]
        for value in values:
            heap.insert(value)

        assert heap.peek() == 3.14
        assert heap.extract_max() == 3.14
        assert heap.extract_max() == 2.71

    def test_negative_values(self, max_heap: MaxHeap[int]) -> None:
        """Test max heap with negative values."""
        values = [-5, -3, -7, -2, -4, -6, -8]
        for value in values:
            max_heap.insert(value)

        assert max_heap.peek() == -2
        assert max_heap.extract_max() == -2
        assert max_heap.extract_max() == -3

    def test_zero_values(self, max_heap: MaxHeap[int]) -> None:
        """Test max heap with zero values."""
        values = [0, -1, 1, -2, 2]
        for value in values:
            max_heap.insert(value)

        assert max_heap.peek() == 2
        assert max_heap.extract_max() == 2
        assert max_heap.extract_max() == 1

    def test_repr_empty_heap(self, max_heap: MaxHeap[int]) -> None:
        """Test string representation of empty heap."""
        assert repr(max_heap) == "MaxHeap([])"

    def test_repr_populated_heap(self, populated_max_heap: MaxHeap[int]) -> None:
        """Test string representation of populated heap."""
        result = repr(populated_max_heap)
        assert result.startswith("MaxHeap([")
        assert result.endswith("])")

    def test_str_empty_heap(self, max_heap: MaxHeap[int]) -> None:
        """Test string representation of empty heap."""
        assert str(max_heap) == "MaxHeap([])"

    def test_str_populated_heap(self, populated_max_heap: MaxHeap[int]) -> None:
        """Test string representation of populated heap."""
        result = str(populated_max_heap)
        assert result.startswith("MaxHeap([")
        assert result.endswith("])")

    def test_invalid_heap_type(self) -> None:
        """Test creating heap with invalid heap type."""
        # MaxHeap doesn't take heap_type parameter, so this should raise TypeError
        with pytest.raises(TypeError):
            MaxHeap(heap_type="invalid")  # type: ignore[call-arg]

    def test_len_method(self, max_heap: MaxHeap[int]) -> None:
        """Test the __len__ method."""
        assert len(max_heap) == 0

        max_heap.insert(5)
        assert len(max_heap) == 1

        max_heap.insert(3)
        max_heap.insert(7)
        assert len(max_heap) == 3

    def test_bool_method(self, max_heap: MaxHeap[int]) -> None:
        """Test the __bool__ method."""
        assert bool(max_heap) is False  # Empty heap

        max_heap.insert(5)
        assert bool(max_heap) is True  # Non-empty heap

        max_heap.extract_max()
        assert bool(max_heap) is False  # Empty again

    def test_extract_max_single_element(self, max_heap: MaxHeap[int]) -> None:
        """Test extract_max when heap has only one element."""
        max_heap.insert(5)
        result = max_heap.extract_max()
        assert result == 5
        assert max_heap.is_empty()

    def test_heapify_down_edge_cases(self, max_heap: MaxHeap[int]) -> None:
        """Test heapify_down with edge cases."""
        # Create a heap with specific structure to test heapify_down paths
        values = [10, 5, 15, 3, 7, 12, 17]
        max_heap.build_heap(values)

        # Extract max to trigger heapify_down
        result = max_heap.extract_max()
        assert result == 17

        # Verify heap property is maintained
        assert max_heap.peek() == 15

    def test_custom_key_function(self) -> None:
        """Test heap with custom key function."""
        # Create heap that compares by absolute value
        heap: MaxHeap[int] = MaxHeap(key=lambda x: abs(x))

        heap.insert(-5)
        heap.insert(3)
        heap.insert(-7)
        heap.insert(2)

        # Should extract by absolute value (largest first)
        assert heap.extract_max() == -7  # abs(-7) = 7
        assert heap.extract_max() == -5  # abs(-5) = 5
        assert heap.extract_max() == 3  # abs(3) = 3
        assert heap.extract_max() == 2  # abs(2) = 2
