# This file will contain the LangChain agent that orchestrates the
# different writer tools to generate the algorithm's code, tests,
# documentation, and benchmarks.

from agent_tools.bench_runner import BenchRunner
from agent_tools.code_writer import CodeWriter
from agent_tools.doc_writer import DocWriter
from agent_tools.llm_router import get_llm
from agent_tools.test_writer import TestWriter
from algolib.specs.schema import AlgorithmSpec


class Agent:
    def __init__(self, spec: AlgorithmSpec):
        self.spec = spec
        self.llm = get_llm()

    def run(self) -> None:
        # 1. Generate code
        code_writer = CodeWriter(self.spec)
        code_path = code_writer.write()
        print(f"Generated code at: {code_path}")

        # 2. Generate tests
        test_writer = TestWriter(self.spec)
        test_path = test_writer.write()
        print(f"Generated tests at: {test_path}")

        # 3. Generate docs
        doc_writer = DocWriter(self.spec)
        doc_path = doc_writer.write()
        print(f"Generated docs at: {doc_path}")

        # 4. Generate benchmarks
        bench_runner = BenchRunner(self.spec)
        bench_path = bench_runner.write()
        print(f"Generated benchmarks at: {bench_path}")

        # TODO: Add LangChain orchestration logic here.
        # This will involve creating a chain or agent that can
        # intelligently use the writer tools.
        pass
