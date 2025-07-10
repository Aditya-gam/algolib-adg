"""Unit tests for permutation generation."""

from typing import List, TypeVar, Union

from hypothesis import given
from hypothesis import strategies as st

from algolib.algorithms.backtracking import PermutationFinder

T = TypeVar("T")


class TestPermutationFinder:
    """Test cases for permutation generation."""

    def test_permute_empty_list(self, permutation_finder: PermutationFinder[int]) -> None:
        """Test generating permutations of empty list."""
        result = permutation_finder.permute([])
        assert result == [[]]

    def test_permute_single_element(self, permutation_finder: PermutationFinder[int]) -> None:
        """Test generating permutations of single element."""
        result = permutation_finder.permute([1])
        assert result == [[1]]

    def test_permute_two_elements(self, permutation_finder: PermutationFinder[int]) -> None:
        """Test generating permutations of two elements."""
        result = permutation_finder.permute([1, 2])
        expected = [[1, 2], [2, 1]]
        assert len(result) == 2
        assert all(perm in expected for perm in result)

    def test_permute_three_elements(self, permutation_finder: PermutationFinder[int]) -> None:
        """Test generating permutations of three elements."""
        result = permutation_finder.permute([1, 2, 3])
        expected = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
        assert len(result) == 6
        assert all(perm in expected for perm in result)

    def test_permute_four_elements(self, permutation_finder: PermutationFinder[int]) -> None:
        """Test generating permutations of four elements."""
        result = permutation_finder.permute([1, 2, 3, 4])
        assert len(result) == 24  # 4! = 24
        # Check that all permutations are unique
        unique_perms = {tuple(perm) for perm in result}
        assert len(unique_perms) == 24

    def test_permute_with_duplicates(self, permutation_finder: PermutationFinder[int]) -> None:
        """Test generating permutations with duplicate elements."""
        result = permutation_finder.permute([1, 1, 2])
        expected = [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
        assert len(result) == 3
        assert all(perm in expected for perm in result)

    def test_permute_all_duplicates(self, permutation_finder: PermutationFinder[int]) -> None:
        """Test generating permutations with all duplicate elements."""
        result = permutation_finder.permute([1, 1, 1])
        assert result == [[1, 1, 1]]

    def test_permute_strings(self) -> None:
        """Test generating permutations of strings."""
        permutation_finder = PermutationFinder[str]()
        result = permutation_finder.permute(["a", "b", "c"])
        expected = [
            ["a", "b", "c"],
            ["a", "c", "b"],
            ["b", "a", "c"],
            ["b", "c", "a"],
            ["c", "a", "b"],
            ["c", "b", "a"],
        ]
        assert len(result) == 6
        assert all(perm in expected for perm in result)

    def test_permute_mixed_types(self) -> None:
        """Test generating permutations of mixed types."""
        permutation_finder = PermutationFinder[Union[int, str, float]]()
        result = permutation_finder.permute([1, "a", 2.5])
        assert len(result) == 6
        # Check that all permutations are unique
        unique_perms = {tuple(str(item) for item in perm) for perm in result}
        assert len(unique_perms) == 6

    def test_permute_large_list(self, permutation_finder: PermutationFinder[int]) -> None:
        """Test generating permutations of larger list."""
        result = permutation_finder.permute([1, 2, 3, 4, 5])
        assert len(result) == 120  # 5! = 120
        # Check that all permutations are unique
        unique_perms = {tuple(perm) for perm in result}
        assert len(unique_perms) == 120

    def test_permute_negative_numbers(self, permutation_finder: PermutationFinder[int]) -> None:
        """Test generating permutations with negative numbers."""
        result = permutation_finder.permute([-1, -2, -3])
        expected = [
            [-1, -2, -3],
            [-1, -3, -2],
            [-2, -1, -3],
            [-2, -3, -1],
            [-3, -1, -2],
            [-3, -2, -1],
        ]
        assert len(result) == 6
        assert all(perm in expected for perm in result)

    def test_permute_floats(self) -> None:
        """Test generating permutations of floats."""
        permutation_finder = PermutationFinder[float]()
        result = permutation_finder.permute([1.1, 2.2, 3.3])
        assert len(result) == 6
        # Check that all permutations are unique
        unique_perms = {tuple(perm) for perm in result}
        assert len(unique_perms) == 6

    def test_permute_zeros(self, permutation_finder: PermutationFinder[int]) -> None:
        """Test generating permutations with zeros."""
        result = permutation_finder.permute([0, 0, 0])
        assert result == [[0, 0, 0]]

    def test_permute_single_zero(self, permutation_finder: PermutationFinder[int]) -> None:
        """Test generating permutations with single zero."""
        result = permutation_finder.permute([0])
        assert result == [[0]]

    def test_permute_multiple_zeros(self, permutation_finder: PermutationFinder[int]) -> None:
        """Test generating permutations with multiple zeros."""
        result = permutation_finder.permute([0, 1, 0])
        expected = [[0, 1, 0], [0, 0, 1], [1, 0, 0]]
        assert len(result) == 3
        assert all(perm in expected for perm in result)

    def test_permute_boolean_values(self) -> None:
        """Test generating permutations of boolean values."""
        permutation_finder = PermutationFinder[bool]()
        result = permutation_finder.permute([True, False, True])
        expected = [[True, False, True], [True, True, False], [False, True, True]]
        assert len(result) == 3
        assert all(perm in expected for perm in result)

    def test_permute_none_values(self) -> None:
        """Test generating permutations with None values."""
        permutation_finder = PermutationFinder[Union[int, None]]()
        result = permutation_finder.permute([None, 1, None])
        expected = [[None, 1, None], [None, None, 1], [1, None, None]]
        assert len(result) == 3
        assert all(perm in expected for perm in result)

    def test_permute_complex_numbers(self) -> None:
        """Test generating permutations of complex numbers."""
        permutation_finder = PermutationFinder[complex]()
        result = permutation_finder.permute([1 + 1j, 2 + 2j, 3 + 3j])
        assert len(result) == 6
        # Check that all permutations are unique
        unique_perms = {tuple(str(item) for item in perm) for perm in result}
        assert len(unique_perms) == 6

    def test_permute_empty_strings(self) -> None:
        """Test generating permutations with empty strings."""
        permutation_finder = PermutationFinder[str]()
        result = permutation_finder.permute(["", "a", ""])
        expected = [["", "a", ""], ["", "", "a"], ["a", "", ""]]
        assert len(result) == 3
        assert all(perm in expected for perm in result)

    def test_permute_unicode_strings(self) -> None:
        """Test generating permutations of unicode strings."""
        permutation_finder = PermutationFinder[str]()
        result = permutation_finder.permute(["α", "β", "γ"])
        assert len(result) == 6
        # Check that all permutations are unique
        unique_perms = {tuple(perm) for perm in result}
        assert len(unique_perms) == 6

    def test_permute_lists(self) -> None:
        """Test generating permutations of lists."""
        permutation_finder = PermutationFinder[List[int]]()
        result = permutation_finder.permute([[1], [2], [3]])
        assert len(result) == 6
        # Check that all permutations are unique
        unique_perms: set[tuple[tuple[int, ...], ...]] = {
            tuple(tuple(item) for item in perm) for perm in result
        }
        assert len(unique_perms) == 6

    def test_permute_tuples(self) -> None:
        """Test generating permutations of tuples."""
        permutation_finder = PermutationFinder[tuple[int]]()
        result = permutation_finder.permute([(1,), (2,), (3,)])
        assert len(result) == 6
        # Check that all permutations are unique
        unique_perms = {tuple(perm) for perm in result}
        assert len(unique_perms) == 6

    def test_permute_dictionaries(self) -> None:
        """Test generating permutations of dictionaries."""
        permutation_finder = PermutationFinder[dict[str, int]]()
        result = permutation_finder.permute([{"a": 1}, {"b": 2}, {"c": 3}])
        assert len(result) == 6
        # Check that all permutations are unique
        unique_perms = {tuple(str(item) for item in perm) for perm in result}
        assert len(unique_perms) == 6

    def test_permute_sets(self) -> None:
        """Test generating permutations of sets."""
        permutation_finder = PermutationFinder[set[int]]()
        result = permutation_finder.permute([{1}, {2}, {3}])
        assert len(result) == 6
        # Check that all permutations are unique
        unique_perms = {tuple(str(item) for item in perm) for perm in result}
        assert len(unique_perms) == 6

    def test_permute_nested_structures(self) -> None:
        """Test generating permutations of nested structures."""
        permutation_finder = PermutationFinder[List[int]]()
        result = permutation_finder.permute([[1, 2], [3, 4], [5, 6]])
        assert len(result) == 6
        # Check that all permutations are unique
        unique_perms: set[tuple[tuple[int, ...], ...]] = {
            tuple(tuple(item) for item in perm) for perm in result
        }
        assert len(unique_perms) == 6

    def test_permute_with_custom_objects(self) -> None:
        """Test generating permutations with custom objects."""

        class CustomObject:
            def __init__(self, value: int):
                self.value = value

            def __eq__(self, other: object) -> bool:
                if not isinstance(other, CustomObject):
                    return NotImplemented
                return self.value == other.value

            def __hash__(self) -> int:
                return hash(self.value)

        permutation_finder = PermutationFinder[CustomObject]()
        obj1 = CustomObject(1)
        obj2 = CustomObject(2)
        obj3 = CustomObject(3)
        result = permutation_finder.permute([obj1, obj2, obj3])
        assert len(result) == 6
        # Check that all permutations are unique
        unique_perms = {tuple(perm) for perm in result}
        assert len(unique_perms) == 6

    def test_permute_property_based(self, permutation_finder: PermutationFinder[int]) -> None:
        """Property-based test for permutation generation (unique permutations only)."""

        @given(st.lists(st.integers(), max_size=5))
        def test_permute_properties(data: List[int]) -> None:
            result = permutation_finder.permute(data)

            # Check correct number of unique permutations
            from collections import Counter
            from math import factorial

            def unique_perm_count(lst: List[int]) -> int:
                counts = Counter(lst)
                denom = 1
                for v in counts.values():
                    denom *= factorial(v)
                return factorial(len(lst)) // denom if lst else 1

            expected_count = unique_perm_count(data)
            assert len(result) == expected_count

            # Check all permutations are unique
            assert len({tuple(perm) for perm in result}) == len(result)

            # Check all permutations have correct length
            assert all(len(perm) == len(data) for perm in result)

            # Check all permutations contain all original elements
            for perm in result:
                assert sorted(perm) == sorted(data)

        test_permute_properties()

    def test_permute_multiple_calls_same_instance(
        self, permutation_finder: PermutationFinder[int]
    ) -> None:
        """Test that multiple calls work correctly on the same instance."""
        data = [1, 2, 3]
        result1 = permutation_finder.permute(data)
        result2 = permutation_finder.permute(data)
        assert result1 == result2

    def test_permute_immutability(self, permutation_finder: PermutationFinder[int]) -> None:
        """Test that the original list is not modified."""
        original = [1, 2, 3]
        permutation_finder.permute(original)
        assert original == [1, 2, 3]

    def test_permute_factorial_property(self, permutation_finder: PermutationFinder[int]) -> None:
        """Test that the number of permutations follows factorial property."""
        for n in range(1, 6):  # Test for n = 1 to 5
            data = list(range(n))
            result = permutation_finder.permute(data)
            expected_count = 1
            for i in range(1, n + 1):
                expected_count *= i
            assert len(result) == expected_count
