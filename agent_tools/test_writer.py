from pathlib import Path

from agent_tools.base import FileWriter
from algolib.specs.schema import AlgorithmSpec


class TestWriter(FileWriter):
    def __init__(self, spec: AlgorithmSpec):
        super().__init__(spec, "test.py.jinja")

    def write(self) -> Path:
        """
        Renders the algorithm's unit and property-based tests from a
        Jinja2 template and writes them to a file in the temporary directory.
        The generated source code is passed through Ruff for formatting.
        """
        content = self.render_template()
        file_path = self.tmp_dir / f"test_{self.slug}.py"
        self.write_output(file_path, content)
        # TODO: Pass through Ruff for formatting
        return file_path
