"""
Main agent class that orchestrates the code generation process.
"""

from pathlib import Path
from typing import Any, List, Type

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
SYSTEM_PROMPT = """You are Algo-Agent.
Generate minimal, idiomatic Python implementing the supplied spec.
Never modify existing library code.

You must generate all four artifacts: code, tests, documentation, and a benchmark.
To do this, you must call all four available tools in order: `write_code`, `write_tests`, `write_docs`, and `write_bench`.
"""


class BaseWriterTool(BaseTool):
    """Base class for tools that write files using a FileWriter."""

    spec: AlgorithmSpec
    writer_class: Type[FileWriter]

    def _run(self, *args: Any, **kwargs: Any) -> str:
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
