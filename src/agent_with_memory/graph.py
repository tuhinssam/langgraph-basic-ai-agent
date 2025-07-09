from langgraph.constants import START, END
from langgraph.graph import StateGraph

from src.agent_with_memory.nodes import process_node
from src.agent_with_memory.schema import AgentState

graph = StateGraph(AgentState)
graph.add_node("process_node", process_node)
graph.add_edge(START, "process_node")
graph.add_edge("process_node", END)

agent = graph.compile()