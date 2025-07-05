from pathlib import Path

from agent_tools.base import FileWriter


class CodeWriter(FileWriter):
    """Writes the algorithm's implementation source code."""

    @property
    def template_path(self) -> str:
        return "code.py.jinja"

    @property
    def output_path(self) -> Path:
        # e.g., algolib/algorithms/sorting/bubble.py
        # For now, all output is in .agent-tmp
        file_name = self.spec.name.lower().replace(" ", "_")
        return self.tmp_dir / "algolib" / "algorithms" / self.spec.category / f"{file_name}.py"
