"""
Main agent class that orchestrates the code generation process.
"""

import sys
from pathlib import Path
from typing import List, Type

import yaml
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.tools import BaseTool

from agent_tools.base import FileWriter
from agent_tools.bench_runner import BenchRunner
from agent_tools.code_writer import CodeWriter
from agent_tools.doc_writer import DocWriter
from agent_tools.llm_router import get_llm
from agent_tools.test_writer import TestWriter
from algolib.specs.schema import AlgorithmSpec

# System prompt to guide the LLM's behavior
SYSTEM_PROMPT = """You are Algo-Agent, a world-class Python programmer specializing in algorithms and data structures. Your task is to generate a complete, production-ready implementation of a given algorithm based on a specification.

**Your output MUST adhere to the following strict standards:**
1.  **Code Style (PEP 8)**: All code must be formatted with Ruff.
2.  **Typing (Strict Mypy)**:
    - All functions and methods must have explicit type hints for all arguments and return values.
    - Use types from Python's `typing` module (e.g., `List`, `Dict`, `Tuple`).
    - For custom generic types, import `ComparableT` from `algolib._typing`.
    - **Crucially, do not use `Any` or `object`**.
3.  **Object-Oriented Design (SOLID)**:
    - The generated class must inherit from the correct base class (e.g., `Sorter`).
    - The implementation should be contained within the class methods.
4.  **Clarity and Readability (Clean Code)**:
    - Use clear and descriptive variable names.
    - Add comments to explain complex or non-obvious parts of the algorithm.
5.  **Testing (TDD)**:
    - Generated tests must be thorough, covering edge cases (empty lists, single-element lists), sorted lists, and typical unsorted cases.
    - Use the `unittest` framework.

**Your process is to call all four available tools in order: `write_code`, `write_tests`, `write_docs`, and `write_bench` to generate a complete set of artifacts.**
"""


class BaseWriterTool(BaseTool):
    """Base class for tools that write files using a FileWriter."""

    spec: AlgorithmSpec
    writer_class: Type[FileWriter]

    def _run(self) -> str:
        writer = self.writer_class(self.spec)
        # Handle append mode for documentation
        append_mode = self.name == "write_docs"
        output_path = writer.write(append=append_mode)
        return f"Successfully wrote {self.name} to {output_path}"


class CodeWriterTool(BaseWriterTool):
    name: str = "write_code"
    description: str = "Writes the algorithm's implementation source code."
    writer_class: Type[FileWriter] = CodeWriter


class TestWriterTool(BaseWriterTool):
    name: str = "write_tests"
    description: str = "Writes unit and property-based tests for the algorithm."
    writer_class: Type[FileWriter] = TestWriter


class DocWriterTool(BaseWriterTool):
    name: str = "write_docs"
    description: str = "Writes the algorithm's documentation in .rst format."
    writer_class: Type[FileWriter] = DocWriter


class BenchRunnerTool(BaseWriterTool):
    name: str = "write_bench"
    description: str = "Writes a pytest-benchmark fixture for the algorithm."
    writer_class: Type[FileWriter] = BenchRunner


class Agent:
    """
    Orchestrates the different writer tools to generate the algorithm's
    code, tests, documentation, and benchmarks using a LangChain agent.
    """

    def __init__(self, spec: AlgorithmSpec):
        self.spec = spec
        self.llm = get_llm()
        self.tools: List[BaseTool] = [
            CodeWriterTool(spec=spec),
            TestWriterTool(spec=spec),
            DocWriterTool(spec=spec),
            BenchRunnerTool(spec=spec),
        ]

        prompt = ChatPromptTemplate.from_messages([
            ("system", SYSTEM_PROMPT),
            ("human", "{input}"),
            ("placeholder", "{agent_scratchpad}"),
        ])

        agent = create_tool_calling_agent(self.llm, self.tools, prompt)
        self.agent_executor = AgentExecutor(agent=agent, tools=self.tools, verbose=True)

    def fix_code(self, file_path: Path, errors: str) -> None:
        """
        Reads the content of a file with errors, asks the LLM to fix it,
        and overwrites the file with the corrected code.
        """
        print(f"Attempting to fix errors in: {file_path}")
        file_content = file_path.read_text()

        prompt = f"""The following file has validation errors:

File: {file_path.name}
Content:
```python
{file_content}
```

Errors:
```
{errors}
```

Please fix the code to resolve these errors and provide the full, corrected file content.
"""

        response = self.llm.invoke(prompt)
        corrected_code = response.content

        # Ensure corrected_code is a string
        if not isinstance(corrected_code, str):
            # Fallback or error handling if the content is not a string
            print(
                f"Warning: LLM response content is not a string: {corrected_code}", file=sys.stderr
            )
            corrected_code = ""  # Or handle as appropriate

        # The response might contain markdown code blocks, so we need to extract the code.
        if "```" in corrected_code:
            corrected_code = corrected_code.split("```")[1]
            if corrected_code.startswith("python"):
                corrected_code = corrected_code[6:]

        file_path.write_text(corrected_code)
        print(f"File {file_path.name} updated with corrections.")

    def run(self) -> dict[str, Path]:
        """
        Runs the agent to generate all the necessary files.

        Returns:
            A dictionary mapping the file type to the generated file path.
        """
        print(f"Running agent for spec: {self.spec.name}")

        # Serialize the spec to pass as input to the agent
        spec_str = yaml.dump(self.spec.model_dump())
        response = self.agent_executor.invoke({
            "input": f"Generate all artifacts for the following algorithm spec:\n\n{spec_str}"
        })

        print(f"Agent finished. Output:\n{response.get('output')}")

        # The files are written by the tools; return their expected paths
        return {
            "code": CodeWriter(self.spec).output_path,
            "tests": TestWriter(self.spec).output_path,
            "docs": DocWriter(self.spec).output_path,
            "benchmarks": BenchRunner(self.spec).output_path,
        }
