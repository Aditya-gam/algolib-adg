import ast
import subprocess
from abc import ABC, abstractmethod
from pathlib import Path
from typing import final

from jinja2 import Environment, FileSystemLoader

from algolib.specs.schema import AlgorithmSpec


class FileWriter(ABC):
    def __init__(self, spec: AlgorithmSpec):
        self.spec = spec
        self.slug = spec.name.lower().replace(" ", "_")
        self.tmp_dir = Path(".agent-tmp") / self.slug
        self.tmp_dir.mkdir(parents=True, exist_ok=True)
        self.env = Environment(
            loader=FileSystemLoader("agent_tools/templates"),
            autoescape=True,
            trim_blocks=True,
            lstrip_blocks=True,
        )

    @property
    @abstractmethod
    def template_path(self) -> str:
        raise NotImplementedError

    @property
    @abstractmethod
    def output_path(self) -> Path:
        raise NotImplementedError

    @property
    def is_python_code(self) -> bool:
        return self.output_path.suffix == ".py"

    def _render(self) -> str:
        template = self.env.get_template(self.template_path)
        return template.render(spec=self.spec)

    def _format_and_validate(self, content: str) -> str:
        if not self.is_python_code:
            return content

        try:
            ast.parse(content)
            # Format with ruff
            process = subprocess.run(
                ["ruff", "format", "-"],
                input=content,
                text=True,
                capture_output=True,
                check=True,
            )
            return process.stdout
        except SyntaxError as e:
            # Add more context to the error
            raise SyntaxError(
                f"Generated code in {self.output_path} is not valid Python.\n{e}"
            ) from e
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"Ruff formatting failed for {self.output_path}.\n{e.stderr}") from e

    @final
    def write(self, append: bool = False) -> Path:
        content = self._render()
        content = self._format_and_validate(content)

        self.output_path.parent.mkdir(parents=True, exist_ok=True)

        mode = "a" if append else "w"
        with self.output_path.open(mode) as f:
            f.write(content)

        return self.output_path
