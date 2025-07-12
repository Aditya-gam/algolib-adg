"""Activity Selection greedy algorithm implementation.

Selects the maximum number of non-overlapping activities given their
start and finish times. The greedy strategy is to always pick the
next activity with the earliest finish time.
"""

from dataclasses import dataclass
from typing import List, NamedTuple

from algolib.algorithms.sorting.merge_sort import MergeSort  # Re-use existing sorter


class Activity(NamedTuple):
    """Represents an activity with start and finish times."""

    start: int
    finish: int
    name: str = ""


@dataclass(slots=True, init=False)
class ActivitySelection:
    """Activity Selection algorithm (greedy)."""

    _sorter: MergeSort[Activity]

    def __init__(self) -> None:
        # Sort by finish time ascending
        def get_finish_time(act: Activity) -> int:
            return act.finish

        self._sorter = MergeSort(key=get_finish_time)

    def select(self, activities: List[Activity]) -> List[Activity]:
        """Select the maximum number of non-overlapping activities."""
        if not activities:
            raise ValueError("Activities list cannot be empty")

        sorted_activities = list(activities)
        self._sorter.sort(sorted_activities)

        selected: List[Activity] = []
        last_finish_time = -1
        for activity in sorted_activities:
            if activity.start >= last_finish_time:
                selected.append(activity)
                last_finish_time = activity.finish
        return selected

    def count_activities(self, activities: List[Activity]) -> int:
        """Return the number of non-overlapping activities that can be performed."""
        return len(self.select(activities))

    def total_time(self, activities: List[Activity]) -> int:
        """Total time covered by the selected activities."""
        return sum(act.finish - act.start for act in self.select(activities))
