from dotenv import load_dotenv
from langchain_core.messages import AIMessage
from langchain_openai import ChatOpenAI

from src.agent_with_memory.schema import AgentState

load_dotenv()

llm = ChatOpenAI(model='gpt-4o')

def process_node(state: AgentState) -> AgentState:
    """
    This node will provide response for user input
    """
    response = llm.invoke(state['messages'])
    state['messages'].append(AIMessage(content=response.content))
    print(f"\nAI Response: {response.content}")
    print(f"CURRENT STATE: {state['messages']}")
    return state