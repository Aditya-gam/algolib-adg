from pathlib import Path

from agent_tools.base import FileWriter


class DocWriter(FileWriter):
    """Writes the algorithm's documentation in .rst format."""

    @property
    def template_path(self) -> str:
        return "doc.rst.jinja"

    @property
    def output_path(self) -> Path:
        file_name = self.spec.name.lower().replace(" ", "_")
        return (
            self.tmp_dir
            / "docs"
            / "source"
            / "algorithms"
            / self.spec.category
            / f"{file_name}.rst"
        )
