from os import getenv
from typing import cast

from langchain_community.llms import Ollama
from langchain_core.language_models import BaseLLM
from langchain_openai import ChatOpenAI


def get_llm() -> BaseLLM:
    backend = getenv("LLM_BACKEND", "openai")
    if backend == "ollama":
        return cast(
            BaseLLM, Ollama(model=getenv("OLLAMA_MODEL", "openhermes:2.5-mistral"), temperature=0.2)
        )
    return cast(BaseLLM, ChatOpenAI(model="gpt-4o-mini", temperature=0.2))
