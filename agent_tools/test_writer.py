from pathlib import Path

from agent_tools.base import FileWriter


class TestWriter(FileWriter):
    """Writes the algorithm's unit and property-based tests."""

    @property
    def template_path(self) -> str:
        return "test.py.jinja"

    @property
    def output_path(self) -> Path:
        file_name = self.spec.name.lower().replace(" ", "_")
        return self.tmp_dir / "tests" / "algorithms" / self.spec.category / f"test_{file_name}.py"
