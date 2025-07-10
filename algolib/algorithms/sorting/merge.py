"""Compatibility module: exposes MergeSorter as an alias of the improved MergeSort."""

from .merge_sort import MergeSort as MergeSorter

__all__ = ["MergeSorter"]
