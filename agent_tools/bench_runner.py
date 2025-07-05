from pathlib import Path

from agent_tools.base import FileWriter


class BenchRunner(FileWriter):
    """Writes a pytest-benchmark fixture."""

    @property
    def template_path(self) -> str:
        return "benchmark.py.jinja"

    @property
    def output_path(self) -> Path:
        file_name = self.spec.name.lower().replace(" ", "_")
        return (
            self.tmp_dir
            / "tests"
            / "benchmarks"
            / self.spec.category
            / f"test_bench_{file_name}.py"
        )
