from typing import Any, cast

import pytest

from algolib._typing import SupportsLessThan


def test_supports_less_than_protocol() -> None:
    class LessThanComparable:
        def __lt__(self, other: "LessThanComparable") -> bool:
            return True

    class NotLessThanComparable:
        pass

    assert isinstance(LessThanComparable(), SupportsLessThan)

    with pytest.raises(TypeError):
        # Cast to Any to bypass mypy type checking for this intentional error test
        _ = cast(Any, NotLessThanComparable()) < cast(Any, NotLessThanComparable())
