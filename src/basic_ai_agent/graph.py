from langgraph.constants import START, END
from langgraph.graph import StateGraph

from src.basic_ai_agent.nodes import process_node
from src.basic_ai_agent.schema import AgentState

graph = StateGraph(AgentState)
graph.add_node("process_node", process_node)
graph.add_edge(START, "process_node")
graph.add_edge("process_node", END)

agent = graph.compile()