from typing import TypedDict, List, Union

from langchain_core.messages import HumanMessage, AIMessage


class AgentState(TypedDict):
    messages: List[Union[HumanMessage,AIMessage]]