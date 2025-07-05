import unittest
from pathlib import Path

import yaml
from pydantic import ValidationError

from algolib.specs.schema import AlgorithmSpec


class TestAlgorithmSpec(unittest.TestCase):
    def setUp(self) -> None:
        self.valid_spec_data = {
            "name": "Test Algorithm",
            "description": "A test algorithm.",
            "category": "Testing",
            "complexity": {
                "time_worst": "O(n^2)",
                "time_average": "O(n^2)",
                "time_best": "O(n)",
                "space_worst": "O(1)",
            },
            "parameters": [
                {"name": "data", "type": "List[int]", "description": "A list of integers."}
            ],
            "returns": {"type": "List[int]", "description": "A sorted list of integers."},
            "dependencies": [],
        }
        self.spec_file = Path("test_spec.yml")
        with open(self.spec_file, "w") as f:
            yaml.dump(self.valid_spec_data, f)

    def tearDown(self) -> None:
        if self.spec_file.exists():
            self.spec_file.unlink()

    def test_from_file_valid(self) -> None:
        spec = AlgorithmSpec.from_file(self.spec_file)
        self.assertEqual(spec.name, "Test Algorithm")
        self.assertEqual(spec.complexity.time_worst, "O(n^2)")

    def test_from_file_invalid_missing_field(self) -> None:
        del self.valid_spec_data["name"]
        with open(self.spec_file, "w") as f:
            yaml.dump(self.valid_spec_data, f)

        with self.assertRaises(ValidationError):
            AlgorithmSpec.from_file(self.spec_file)

    def test_from_file_invalid_wrong_type(self) -> None:
        self.valid_spec_data["complexity"] = "should_be_a_dict"
        with open(self.spec_file, "w") as f:
            yaml.dump(self.valid_spec_data, f)

        with self.assertRaises(ValidationError):
            AlgorithmSpec.from_file(self.spec_file)
