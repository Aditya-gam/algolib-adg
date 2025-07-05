from os import getenv
from typing import Union

from langchain_community.llms import Ollama
from langchain_openai import ChatOpenAI


def get_llm() -> Union[Ollama, ChatOpenAI]:
    backend = getenv("LLM_BACKEND", "openai")
    if backend == "ollama":
        return Ollama(model=getenv("OLLAMA_MODEL", "openhermes:2.5-mistral"), temperature=0.2)
    return ChatOpenAI(model="gpt-4o-mini", temperature=0.2)
