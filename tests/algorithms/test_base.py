import pytest

from algolib.algorithms.base import Algorithm


def test_algorithm_base_class() -> None:
    class MyAlgorithm(Algorithm[int]):
        def run(self, problem: int) -> None:
            pass

    algo = MyAlgorithm()
    assert isinstance(algo, Algorithm)


def test_algorithm_abstract_method() -> None:
    with pytest.raises(TypeError):
        Algorithm()  # type: ignore
