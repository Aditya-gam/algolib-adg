from typing import Any, Protocol, TypeVar, runtime_checkable

T = TypeVar("T")
T_contra = TypeVar("T_contra", contravariant=True)


@runtime_checkable
class SupportsLessThan(Protocol[T_contra]):
    def __lt__(self, other: T_contra) -> bool: ...  # pragma: no cover


ComparableT = TypeVar("ComparableT", bound=SupportsLessThan[Any])
