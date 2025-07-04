from algolib.algorithms.base import Algorithm


def test_base_abstract() -> None:
    assert issubclass(Algorithm, object)


def test_smoke() -> None:
    pass
