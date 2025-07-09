from langchain_core.messages import HumanMessage, AIMessage

from src.agent_with_memory.graph import agent

conversation_history = []
counter = 0

user_input = input("Enter:")
while user_input != "exit":
    conversation_history.append(HumanMessage(content=user_input))
    result = agent.invoke({"messages": conversation_history})
    #print(result["messages"])
    conversation_history = result["messages"]
    user_input = input("Enter:")

with open("conversation_history.txt", "w") as file:
    file.write("Your Conversation Log: \n")
    for message in conversation_history:
        if isinstance(message, HumanMessage):
            file.write(f"You: {message.content}\n")
        elif isinstance(message, AIMessage):
            file.write(f"AI: {message.content}\n")
    file.write("End of Conversation\n")

print("Conversation saved to logging.txt")

