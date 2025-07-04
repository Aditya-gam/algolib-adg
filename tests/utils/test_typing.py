from algolib._typing import SupportsLessThan


def test_supports_less_than_protocol() -> None:
    class LessThanComparable:
        def __lt__(self, other: "LessThanComparable") -> bool:
            return True

    class NotLessThanComparable:
        pass

    assert isinstance(LessThanComparable(), SupportsLessThan)
    assert not isinstance(NotLessThanComparable(), SupportsLessThan)
