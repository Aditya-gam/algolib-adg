from typing import cast

from langchain_core.language_models import BaseChatModel
from langchain_ollama import ChatOllama


def get_llm() -> BaseChatModel:
    """Returns a ChatOllama model instance."""
    return cast(
        BaseChatModel,
        ChatOllama(model="llama3.1", temperature=0.2),
    )
