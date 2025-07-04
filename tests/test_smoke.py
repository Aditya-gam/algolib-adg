from algolib.algorithms.base import BaseAlgorithm


def test_base_abstract() -> None:
    assert issubclass(BaseAlgorithm, object)
