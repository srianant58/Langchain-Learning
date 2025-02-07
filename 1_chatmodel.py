from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import AIMessage,HumanMessage,SystemMessage

load_dotenv()

model  = ChatGroq(temperature = 0,model="llama-3.3-70b-versatile")

# result = model.invoke('What is 81 divide by 3?')
messages =[
    SystemMessage(content="Solve the following math problems and explain it step by step"),
    HumanMessage(content="What is 81 divided by 9?")
]

# print(result.content)
result = model.invoke(messages)
print(f"Answer from AI: {result.content}")
