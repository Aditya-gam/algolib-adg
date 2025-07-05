from os import getenv
from typing import cast

from langchain_core.language_models import BaseLLM
from langchain_ollama import OllamaLLM


def get_llm() -> BaseLLM:
    return cast(
        BaseLLM, OllamaLLM(model=getenv("OLLAMA_MODEL", "openhermes:2.5-mistral"), temperature=0.2)
    )
