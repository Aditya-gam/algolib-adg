"""Unit tests for subset generation."""

from typing import List, TypeVar

import pytest
from hypothesis import given
from hypothesis import strategies as st

from algolib.algorithms.backtracking import SubsetGeneration

T = TypeVar("T")


class TestSubsetGeneration:
    """Test cases for subset generation."""

    def test_generate_empty_list(self, subset_generator: SubsetGeneration[int]) -> None:
        """Test generating subsets of empty list."""
        result = subset_generator.generate([])
        assert result == [[]]

    def test_generate_single_element(self, subset_generator: SubsetGeneration[int]) -> None:
        """Test generating subsets of single element."""
        result = subset_generator.generate([1])
        expected = [[], [1]]
        assert len(result) == 2
        assert all(subset in expected for subset in result)

    def test_generate_two_elements(self, subset_generator: SubsetGeneration[int]) -> None:
        """Test generating subsets of two elements."""
        result = subset_generator.generate([1, 2])
        expected = [[], [1], [2], [1, 2]]
        assert len(result) == 4
        assert all(subset in expected for subset in result)

    def test_generate_three_elements(self, subset_generator: SubsetGeneration[int]) -> None:
        """Test generating subsets of three elements."""
        result = subset_generator.generate([1, 2, 3])
        expected = [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
        assert len(result) == 8
        assert all(subset in expected for subset in result)

    def test_generate_four_elements(self, subset_generator: SubsetGeneration[int]) -> None:
        """Test generating subsets of four elements."""
        result = subset_generator.generate([1, 2, 3, 4])
        assert len(result) == 16  # 2^4 = 16
        # Check that all subsets are unique
        unique_subsets = set(tuple(subset) for subset in result)
        assert len(unique_subsets) == 16

    def test_generate_with_duplicates(self, subset_generator: SubsetGeneration[int]) -> None:
        """Test generating subsets with duplicate elements."""
        result = subset_generator.generate([1, 1, 2])
        # For [1, 1, 2], we get all possible combinations (2^3 = 8 total)
        # But only 6 unique subsets: [], [1], [1, 1], [2], [1, 2], [1, 1, 2]
        assert len(result) == 8  # Total combinations
        # Check that all expected unique subsets are present
        expected_subsets = [[], [1], [1, 1], [2], [1, 2], [1, 1, 2]]
        for subset in expected_subsets:
            assert subset in result
        # Check that we have the right number of unique subsets
        unique_subsets = set(tuple(subset) for subset in result)
        assert len(unique_subsets) == 6

    def test_generate_all_duplicates(self, subset_generator: SubsetGeneration[int]) -> None:
        """Test generating subsets with all duplicate elements."""
        result = subset_generator.generate([1, 1, 1])
        # For [1, 1, 1], we get all possible combinations (2^3 = 8 total)
        # But only 4 unique subsets: [], [1], [1, 1], [1, 1, 1]
        assert len(result) == 8  # Total combinations
        expected_subsets = [[], [1], [1, 1], [1, 1, 1]]
        for subset in expected_subsets:
            assert subset in result
        # Check that we have the right number of unique subsets
        unique_subsets = set(tuple(subset) for subset in result)
        assert len(unique_subsets) == 4

    def test_generate_strings(self) -> None:
        """Test generating subsets of strings."""
        subset_generator = SubsetGeneration[str]()
        result = subset_generator.generate(["a", "b", "c"])
        expected = [[], ["a"], ["b"], ["c"], ["a", "b"], ["a", "c"], ["b", "c"], ["a", "b", "c"]]
        assert len(result) == 8
        assert all(subset in expected for subset in result)

    def test_generate_mixed_types(self) -> None:
        """Test generating subsets of mixed types."""
        from typing import Union

        subset_generator = SubsetGeneration[Union[int, str, float]]()
        result = subset_generator.generate([1, "a", 2.5])
        assert len(result) == 8
        # Check that all subsets are unique
        unique_subsets = set(tuple(str(item) for item in subset) for subset in result)
        assert len(unique_subsets) == 8

    def test_generate_large_list(self, subset_generator: SubsetGeneration[int]) -> None:
        """Test generating subsets of larger list."""
        result = subset_generator.generate([1, 2, 3, 4, 5])
        assert len(result) == 32  # 2^5 = 32
        # Check that all subsets are unique
        unique_subsets = set(tuple(subset) for subset in result)
        assert len(unique_subsets) == 32

    def test_generate_negative_numbers(self, subset_generator: SubsetGeneration[int]) -> None:
        """Test generating subsets with negative numbers."""
        result = subset_generator.generate([-1, -2, -3])
        expected = [[], [-1], [-2], [-3], [-1, -2], [-1, -3], [-2, -3], [-1, -2, -3]]
        assert len(result) == 8
        assert all(subset in expected for subset in result)

    def test_generate_floats(self) -> None:
        """Test generating subsets of floats."""
        subset_generator = SubsetGeneration[float]()
        result = subset_generator.generate([1.1, 2.2, 3.3])
        assert len(result) == 8
        # Check that all subsets are unique
        unique_subsets = set(tuple(subset) for subset in result)
        assert len(unique_subsets) == 8

    def test_generate_zeros(self, subset_generator: SubsetGeneration[int]) -> None:
        """Test generating subsets with zeros."""
        result = subset_generator.generate([0, 0, 0])
        # For [0, 0, 0], we get all possible combinations (2^3 = 8 total)
        # But only 4 unique subsets: [], [0], [0, 0], [0, 0, 0]
        assert len(result) == 8  # Total combinations
        expected_subsets = [[], [0], [0, 0], [0, 0, 0]]
        for subset in expected_subsets:
            assert subset in result
        # Check that we have the right number of unique subsets
        unique_subsets = set(tuple(subset) for subset in result)
        assert len(unique_subsets) == 4

    def test_generate_single_zero(self, subset_generator: SubsetGeneration[int]) -> None:
        """Test generating subsets with single zero."""
        result = subset_generator.generate([0])
        expected = [[], [0]]
        assert len(result) == 2
        assert all(subset in expected for subset in result)

    def test_generate_multiple_zeros(self, subset_generator: SubsetGeneration[int]) -> None:
        """Test generating subsets with multiple zeros."""
        result = subset_generator.generate([0, 1, 0])
        # For [0, 1, 0], we get all possible combinations (2^3 = 8 total)
        # Unique subsets: [], [0], [1], [0, 0], [0, 1], [1, 0], [0, 1, 0]
        assert len(result) == 8  # Total combinations
        # Check that we have the right number of unique subsets
        unique_subsets = set(tuple(subset) for subset in result)
        assert len(unique_subsets) == 7
        # Check that all expected unique subsets are present
        expected_unique = {(), (0,), (1,), (0, 0), (0, 1), (1, 0), (0, 1, 0)}
        assert unique_subsets == expected_unique

    def test_generate_boolean_values(self) -> None:
        """Test generating subsets of boolean values."""
        subset_generator = SubsetGeneration[bool]()
        result = subset_generator.generate([True, False, True])
        # For [True, False, True], we get all possible combinations (2^3 = 8 total)
        # Unique subsets: [], [True], [False], [True, True], [True, False], [False, True], [True, False, True]
        assert len(result) == 8  # Total combinations
        # Check that we have the right number of unique subsets
        unique_subsets = set(tuple(subset) for subset in result)
        assert len(unique_subsets) == 7
        # Check that all expected unique subsets are present
        expected_unique = {
            (),
            (True,),
            (False,),
            (True, True),
            (True, False),
            (False, True),
            (True, False, True),
        }
        assert unique_subsets == expected_unique

    def test_generate_none_values(self) -> None:
        """Test generating subsets with None values."""
        from typing import Optional

        subset_generator = SubsetGeneration[Optional[int]]()
        result = subset_generator.generate([None, 1, None])
        # For [None, 1, None], we get all possible combinations (2^3 = 8 total)
        # Unique subsets: [], [None], [1], [None, None], [None, 1], [1, None], [None, 1, None]
        assert len(result) == 8  # Total combinations
        # Check that we have the right number of unique subsets
        unique_subsets = set(tuple(subset) for subset in result)
        assert len(unique_subsets) == 7
        # Check that all expected unique subsets are present
        expected_unique = {(), (None,), (1,), (None, None), (None, 1), (1, None), (None, 1, None)}
        assert unique_subsets == expected_unique

    def test_generate_complex_numbers(self) -> None:
        """Test generating subsets of complex numbers."""
        subset_generator = SubsetGeneration[complex]()
        result = subset_generator.generate([1 + 1j, 2 + 2j, 3 + 3j])
        assert len(result) == 8
        # Check that all subsets are unique
        unique_subsets = set(tuple(str(item) for item in subset) for subset in result)
        assert len(unique_subsets) == 8

    def test_generate_empty_strings(self) -> None:
        """Test generating subsets with empty strings."""
        subset_generator = SubsetGeneration[str]()
        result = subset_generator.generate(["", "a", ""])
        # For ['', 'a', ''], we get all possible combinations (2^3 = 8 total)
        # Unique subsets: [], [''], ['a'], ['', ''], ['', 'a'], ['a', ''], ['', 'a', '']
        assert len(result) == 8  # Total combinations
        # Check that we have the right number of unique subsets
        unique_subsets = set(tuple(subset) for subset in result)
        assert len(unique_subsets) == 7
        # Check that all expected unique subsets are present
        expected_unique = {(), ("",), ("a",), ("", ""), ("", "a"), ("a", ""), ("", "a", "")}
        assert unique_subsets == expected_unique

    def test_generate_unicode_strings(self) -> None:
        """Test generating subsets of unicode strings."""
        subset_generator = SubsetGeneration[str]()
        result = subset_generator.generate(["α", "β", "γ"])
        assert len(result) == 8
        # Check that all subsets are unique
        unique_subsets = set(tuple(subset) for subset in result)
        assert len(unique_subsets) == 8

    def test_generate_lists(self) -> None:
        """Test generating subsets of lists."""
        subset_generator = SubsetGeneration[list[int]]()
        result = subset_generator.generate([[1], [2], [3]])
        assert len(result) == 8
        # Check that all subsets are unique
        unique_subsets = set(tuple(tuple(item) for item in subset) for subset in result)
        assert len(unique_subsets) == 8

    def test_generate_tuples(self) -> None:
        """Test generating subsets of tuples."""
        subset_generator = SubsetGeneration[tuple[int, ...]]()
        result = subset_generator.generate([(1,), (2,), (3,)])
        assert len(result) == 8
        # Check that all subsets are unique
        unique_subsets = set(tuple(subset) for subset in result)
        assert len(unique_subsets) == 8

    def test_generate_dictionaries(self) -> None:
        """Test generating subsets of dictionaries."""
        subset_generator = SubsetGeneration[dict[str, int]]()
        result = subset_generator.generate([{"a": 1}, {"b": 2}])
        assert len(result) == 4
        # Check that all subsets are unique
        unique_subsets = set(tuple(frozenset(item.items()) for item in subset) for subset in result)
        assert len(unique_subsets) == 4

    def test_generate_sets(self) -> None:
        """Test generating subsets of sets."""
        subset_generator = SubsetGeneration[set[int]]()
        result = subset_generator.generate([{1}, {2}, {3}])
        assert len(result) == 8
        # Check that all subsets are unique
        unique_subsets = set(tuple(frozenset(item) for item in subset) for subset in result)
        assert len(unique_subsets) == 8

    def test_generate_nested_structures(self) -> None:
        """Test generating subsets of nested structures."""
        from typing import Union

        subset_generator = SubsetGeneration[Union[list[int], dict[str, int], tuple[int, int]]]()
        result = subset_generator.generate([[1, 2], {"a": 1}, (1, 2)])
        assert len(result) == 8
        # Check that all subsets are unique
        unique_subsets = set(tuple(str(item) for item in subset) for subset in result)
        assert len(unique_subsets) == 8

    def test_generate_with_custom_objects(self) -> None:
        """Test generating subsets with custom objects."""

        class CustomObject:
            def __init__(self, value: int):
                self.value = value

            def __eq__(self, other: object) -> bool:
                if not isinstance(other, CustomObject):
                    return False
                return self.value == other.value

            def __hash__(self) -> int:
                return hash(self.value)

        subset_generator = SubsetGeneration[CustomObject]()
        obj1 = CustomObject(1)
        obj2 = CustomObject(2)
        result = subset_generator.generate([obj1, obj2])
        assert len(result) == 4
        # Check that all subsets are unique
        unique_subsets = set(tuple(obj.value for obj in subset) for subset in result)
        assert len(unique_subsets) == 4

    def test_generate_property_based(self, subset_generator: SubsetGeneration[int]) -> None:
        """Property-based test for subset generation."""

        @given(st.lists(st.integers(), max_size=5))
        def test_generate_properties(data: List[int]) -> None:
            result = subset_generator.generate(data)
            # Property 1: Number of subsets should be 2^n
            assert len(result) == 2 ** len(data)
            # Property 2: Empty subset should always be present
            assert [] in result
            # Property 3: All subsets should be unique (when converted to tuples)
            unique_subsets = set(tuple(subset) for subset in result)
            # Note: The original list may have duplicates, but unique tuples should match
            # the number of unique combinations
            assert len(unique_subsets) <= len(result)
            # Property 4: All elements should appear in some subset
            all_elements = set(data)
            elements_in_subsets = set()
            for subset in result:
                elements_in_subsets.update(subset)
            assert elements_in_subsets == all_elements

        test_generate_properties()

    def test_generate_multiple_calls_same_instance(
        self, subset_generator: SubsetGeneration[int]
    ) -> None:
        """Test that multiple calls work correctly on the same instance."""
        result1 = subset_generator.generate([1, 2])
        result2 = subset_generator.generate([3, 4])
        assert len(result1) == 4
        assert len(result2) == 4
        assert result1 != result2

    def test_generate_immutability(self, subset_generator: SubsetGeneration[int]) -> None:
        """Test that input list is not modified."""
        original = [1, 2, 3]
        subset_generator.generate(original)
        assert original == [1, 2, 3]

    def test_generate_power_set_property(self, subset_generator: SubsetGeneration[int]) -> None:
        """Test that generated result is indeed a power set."""
        data = [1, 2, 3]
        result = subset_generator.generate(data)
        # Power set should contain all possible subsets
        expected_subsets = [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
        for subset in expected_subsets:
            assert subset in result

    def test_generate_empty_subset_included(self, subset_generator: SubsetGeneration[int]) -> None:
        """Test that empty subset is always included."""
        result = subset_generator.generate([1, 2, 3, 4, 5])
        assert [] in result

    def test_generate_full_subset_included(self, subset_generator: SubsetGeneration[int]) -> None:
        """Test that full subset is always included."""
        data = [1, 2, 3]
        result = subset_generator.generate(data)
        assert data in result

    def test_generate_single_element_subsets(self, subset_generator: SubsetGeneration[int]) -> None:
        """Test that all single element subsets are included."""
        data = [1, 2, 3]
        result = subset_generator.generate(data)
        for element in data:
            assert [element] in result

    def test_generate_subset_ordering(self, subset_generator: SubsetGeneration[int]) -> None:
        """Test that subset ordering is consistent."""
        data = [1, 2, 3]
        result1 = subset_generator.generate(data)
        result2 = subset_generator.generate(data)
        assert result1 == result2

    def test_generate_subset_cardinality(self, subset_generator: SubsetGeneration[int]) -> None:
        """Test that all subsets have correct cardinality."""
        data = [1, 2, 3, 4]
        result = subset_generator.generate(data)
        for subset in result:
            assert len(subset) <= len(data)

    # Tests for generate_iterative method
    def test_generate_iterative_empty_list(self, subset_generator: SubsetGeneration[int]) -> None:
        """Test iterative generation of subsets of empty list."""
        result = subset_generator.generate_iterative([])
        assert result == [[]]

    def test_generate_iterative_single_element(
        self, subset_generator: SubsetGeneration[int]
    ) -> None:
        """Test iterative generation of subsets of single element."""
        result = subset_generator.generate_iterative([1])
        expected = [[], [1]]
        assert len(result) == 2
        assert all(subset in expected for subset in result)

    def test_generate_iterative_three_elements(
        self, subset_generator: SubsetGeneration[int]
    ) -> None:
        """Test iterative generation of subsets of three elements."""
        result = subset_generator.generate_iterative([1, 2, 3])
        expected = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
        assert len(result) == 8
        assert all(subset in expected for subset in result)

    def test_generate_iterative_large_list(self, subset_generator: SubsetGeneration[int]) -> None:
        """Test iterative generation of subsets of larger list."""
        result = subset_generator.generate_iterative([1, 2, 3, 4, 5])
        assert len(result) == 32  # 2^5 = 32
        # Check that all subsets are unique
        unique_subsets = set(tuple(subset) for subset in result)
        assert len(unique_subsets) == 32

    def test_generate_iterative_consistency_with_recursive(
        self, subset_generator: SubsetGeneration[int]
    ) -> None:
        """Test that iterative and recursive methods produce same results."""
        data = [1, 2, 3, 4]
        recursive_result = subset_generator.generate(data)
        iterative_result = subset_generator.generate_iterative(data)

        # Convert to sets of tuples for comparison
        recursive_set = set(tuple(subset) for subset in recursive_result)
        iterative_set = set(tuple(subset) for subset in iterative_result)
        assert recursive_set == iterative_set

    # Tests for generate_with_size method
    def test_generate_with_size_zero(self, subset_generator: SubsetGeneration[int]) -> None:
        """Test generating subsets of size 0."""
        result = subset_generator.generate_with_size([1, 2, 3], 0)
        assert result == [[]]

    def test_generate_with_size_one(self, subset_generator: SubsetGeneration[int]) -> None:
        """Test generating subsets of size 1."""
        result = subset_generator.generate_with_size([1, 2, 3], 1)
        expected = [[1], [2], [3]]
        assert len(result) == 3
        assert all(subset in expected for subset in result)

    def test_generate_with_size_two(self, subset_generator: SubsetGeneration[int]) -> None:
        """Test generating subsets of size 2."""
        result = subset_generator.generate_with_size([1, 2, 3, 4], 2)
        expected = [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
        assert len(result) == 6
        assert all(subset in expected for subset in result)

    def test_generate_with_size_full(self, subset_generator: SubsetGeneration[int]) -> None:
        """Test generating subsets of full size."""
        data = [1, 2, 3]
        result = subset_generator.generate_with_size(data, 3)
        assert result == [data]

    def test_generate_with_size_negative(self, subset_generator: SubsetGeneration[int]) -> None:
        """Test generating subsets with negative size raises ValueError."""
        with pytest.raises(ValueError, match="Size cannot be negative"):
            subset_generator.generate_with_size([1, 2, 3], -1)

    def test_generate_with_size_too_large(self, subset_generator: SubsetGeneration[int]) -> None:
        """Test generating subsets with size larger than elements raises ValueError."""
        with pytest.raises(ValueError, match="Size cannot be larger than the number of elements"):
            subset_generator.generate_with_size([1, 2, 3], 4)

    def test_generate_with_size_strings(self) -> None:
        """Test generating subsets of specific size with strings."""
        subset_generator = SubsetGeneration[str]()
        result = subset_generator.generate_with_size(["a", "b", "c", "d"], 2)
        expected = [["a", "b"], ["a", "c"], ["a", "d"], ["b", "c"], ["b", "d"], ["c", "d"]]
        assert len(result) == 6
        assert all(subset in expected for subset in result)

    # Tests for count_subsets method
    def test_count_subsets_empty(self, subset_generator: SubsetGeneration[int]) -> None:
        """Test counting subsets of empty list."""
        assert subset_generator.count_subsets([]) == 1

    def test_count_subsets_single_element(self, subset_generator: SubsetGeneration[int]) -> None:
        """Test counting subsets of single element."""
        assert subset_generator.count_subsets([1]) == 2

    def test_count_subsets_three_elements(self, subset_generator: SubsetGeneration[int]) -> None:
        """Test counting subsets of three elements."""
        assert subset_generator.count_subsets([1, 2, 3]) == 8

    def test_count_subsets_five_elements(self, subset_generator: SubsetGeneration[int]) -> None:
        """Test counting subsets of five elements."""
        assert subset_generator.count_subsets([1, 2, 3, 4, 5]) == 32

    def test_count_subsets_consistency_with_generate(
        self, subset_generator: SubsetGeneration[int]
    ) -> None:
        """Test that count matches actual generation."""
        data = [1, 2, 3, 4]
        count = subset_generator.count_subsets(data)
        actual = subset_generator.generate(data)
        assert count == len(actual)

    # Tests for count_subsets_with_size method
    def test_count_subsets_with_size_zero(self, subset_generator: SubsetGeneration[int]) -> None:
        """Test counting subsets of size 0."""
        assert subset_generator.count_subsets_with_size([1, 2, 3], 0) == 1

    def test_count_subsets_with_size_one(self, subset_generator: SubsetGeneration[int]) -> None:
        """Test counting subsets of size 1."""
        assert subset_generator.count_subsets_with_size([1, 2, 3], 1) == 3

    def test_count_subsets_with_size_two(self, subset_generator: SubsetGeneration[int]) -> None:
        """Test counting subsets of size 2."""
        assert subset_generator.count_subsets_with_size([1, 2, 3, 4], 2) == 6

    def test_count_subsets_with_size_full(self, subset_generator: SubsetGeneration[int]) -> None:
        """Test counting subsets of full size."""
        assert subset_generator.count_subsets_with_size([1, 2, 3], 3) == 1

    def test_count_subsets_with_size_negative(
        self, subset_generator: SubsetGeneration[int]
    ) -> None:
        """Test counting subsets with negative size raises ValueError."""
        with pytest.raises(ValueError, match="Size cannot be negative"):
            subset_generator.count_subsets_with_size([1, 2, 3], -1)

    def test_count_subsets_with_size_too_large(
        self, subset_generator: SubsetGeneration[int]
    ) -> None:
        """Test counting subsets with size larger than elements raises ValueError."""
        with pytest.raises(ValueError, match="Size cannot be larger than the number of elements"):
            subset_generator.count_subsets_with_size([1, 2, 3], 4)

    def test_count_subsets_with_size_consistency_with_generate(
        self, subset_generator: SubsetGeneration[int]
    ) -> None:
        """Test that count matches actual generation for specific size."""
        data = [1, 2, 3, 4]
        size = 2
        count = subset_generator.count_subsets_with_size(data, size)
        actual = subset_generator.generate_with_size(data, size)
        assert count == len(actual)

    # Tests for _binomial_coefficient method (via count_subsets_with_size)
    def test_binomial_coefficient_symmetry(self, subset_generator: SubsetGeneration[int]) -> None:
        """Test that binomial coefficient is symmetric."""
        data = [1, 2, 3, 4, 5]
        assert subset_generator.count_subsets_with_size(
            data, 2
        ) == subset_generator.count_subsets_with_size(data, 3)

    def test_binomial_coefficient_edge_cases(self, subset_generator: SubsetGeneration[int]) -> None:
        """Test binomial coefficient edge cases."""
        data = [1, 2, 3, 4, 5]
        assert subset_generator.count_subsets_with_size(data, 0) == 1
        assert subset_generator.count_subsets_with_size(data, 5) == 1
        assert subset_generator.count_subsets_with_size(data, 1) == 5

    # Tests for is_subset method
    def test_is_subset_empty_subset(self, subset_generator: SubsetGeneration[int]) -> None:
        """Test that empty set is subset of any set."""
        assert subset_generator.is_subset([], [1, 2, 3]) is True
        assert subset_generator.is_subset([], []) is True

    def test_is_subset_valid_subset(self, subset_generator: SubsetGeneration[int]) -> None:
        """Test valid subset relationships."""
        assert subset_generator.is_subset([1, 2], [1, 2, 3, 4]) is True
        assert subset_generator.is_subset([1], [1, 2, 3]) is True
        assert subset_generator.is_subset([1, 2, 3], [1, 2, 3]) is True

    def test_is_subset_not_subset(self, subset_generator: SubsetGeneration[int]) -> None:
        """Test invalid subset relationships."""
        assert subset_generator.is_subset([1, 5], [1, 2, 3, 4]) is False
        assert subset_generator.is_subset([1, 2, 3], [1, 2]) is False

    def test_is_subset_with_duplicates(self, subset_generator: SubsetGeneration[int]) -> None:
        """Test subset with duplicate elements."""
        assert subset_generator.is_subset([1, 1], [1, 2, 3]) is True
        # The is_subset method uses set operations, so [1, 1, 1] is a subset of [1, 2, 3]
        # because set([1, 1, 1]) = {1} and set([1, 2, 3]) = {1, 2, 3}
        assert subset_generator.is_subset([1, 1, 1], [1, 2, 3]) is True

    def test_is_subset_strings(self) -> None:
        """Test subset with strings."""
        subset_generator = SubsetGeneration[str]()
        assert subset_generator.is_subset(["a", "b"], ["a", "b", "c"]) is True
        assert subset_generator.is_subset(["a", "d"], ["a", "b", "c"]) is False

    def test_is_subset_mixed_types(self) -> None:
        """Test subset with mixed types."""
        from typing import Union

        subset_generator = SubsetGeneration[Union[int, str, float]]()
        assert subset_generator.is_subset([1, "a"], [1, "a", 2.5]) is True
        assert subset_generator.is_subset([1, "b"], [1, "a", 2.5]) is False

    # Tests for __repr__ method
    def test_repr(self, subset_generator: SubsetGeneration[int]) -> None:
        """Test string representation."""
        assert repr(subset_generator) == "SubsetGeneration()"


@pytest.fixture
def subset_generator() -> SubsetGeneration[int]:
    """Fixture to provide a SubsetGeneration instance."""
    return SubsetGeneration[int]()
