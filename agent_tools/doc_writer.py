from pathlib import Path

from agent_tools.base import FileWriter
from algolib.specs.schema import AlgorithmSpec


class DocWriter(FileWriter):
    def __init__(self, spec: AlgorithmSpec):
        super().__init__(spec, "doc.rst.jinja")

    def write(self) -> Path:
        """
        Renders the algorithm's documentation from a Jinja2 template
        and writes it to a .rst file in the temporary directory.
        """
        content = self.render_template()
        file_path = self.tmp_dir / f"{self.slug}.rst"
        file_path.write_text(content)
        return file_path
