from typing import TypedDict, List

from langchain_core.messages import HumanMessage


class AgentState(TypedDict):
    messages: List[HumanMessage]