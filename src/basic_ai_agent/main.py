from langchain_core.messages import HumanMessage

from src.basic_ai_agent.graph import agent

user_input = input("Enter your message: ")
while user_input != "exit":
    agent.invoke({"messages": [HumanMessage(content=user_input)]})
    user_input = input("Enter your message: ")