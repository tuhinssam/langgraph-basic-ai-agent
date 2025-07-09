from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

from src.basic_ai_agent.schema import AgentState

load_dotenv()

llm = ChatOpenAI(model="gpt-4o")

def process_node(state: AgentState) -> AgentState:
    response = llm.invoke(state["messages"])
    print(f"\nAI response: {response.content}")
    return state
