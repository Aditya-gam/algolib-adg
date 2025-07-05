import ast
from abc import ABC, abstractmethod
from pathlib import Path
from typing import final

import astor
from jinja2 import Environment, FileSystemLoader

from algolib.specs.schema import AlgorithmSpec


class FileWriter(ABC):
    def __init__(self, spec: AlgorithmSpec, template_path: str):
        self.spec = spec
        self.template_path = template_path
        self.slug = spec.name.lower().replace(" ", "_")
        self.tmp_dir = Path(".agent-tmp") / self.slug
        self.tmp_dir.mkdir(parents=True, exist_ok=True)
        self.env = Environment(loader=FileSystemLoader("agent_tools/templates"), autoescape=True)

    @final
    def render_template(self) -> str:
        template = self.env.get_template(self.template_path)
        return template.render(spec=self.spec)

    @final
    def write_output(self, file_path: Path, content: str) -> None:
        try:
            # Ensure the generated code is syntactically valid
            parsed_ast = ast.parse(content)
            source = astor.to_source(parsed_ast)
            file_path.write_text(source)
        except SyntaxError as e:
            print(f"Error: Generated code for {file_path} is not valid Python.")
            raise e

    @abstractmethod
    def write(self) -> Path:
        """Renders the template and writes the output to a file."""
        raise NotImplementedError
